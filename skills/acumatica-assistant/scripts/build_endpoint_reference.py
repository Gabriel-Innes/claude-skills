#!/usr/bin/env python3
"""Build references/endpoints/<Endpoint>-<Version>/ from an endpoint's swagger.json (maintenance only).

    python scripts/build_endpoint_reference.py --swagger <swagger.json> --out references/endpoints \
        --release "2025 R2" --build 25.201.0213 --verified YYYY-MM-DD [--source-note "..."] \
        [--scrub-to ../../sources/acumatica-assistant/<Endpoint>-<Version>.swagger.json]

The input is the OpenAPI 3.0 document of ONE endpoint (`GET <Base endpoint URL>/swagger.json`, or More > OpenAPI
3.0 on the Web Service Endpoints (SM207060) form). Use a system endpoint (`Default`): its contract is fixed by
Acumatica, so it is the same on every instance of that release. Never feed a custom endpoint or an endpoint
extension, which carry a customer's own entities and fields. The raw swagger stays outside the repository;
`--scrub-to` writes a copy with `servers` removed (the only instance-specific member), which is committed under
`sources/acumatica-assistant/` so the snapshot can be regenerated from it later.

Only names and types are extracted, into four fully regenerated files under <out>/<Endpoint>-<Version>/:
  entities.md      top-level entities with form ID, screen title and counts
  fields.md        one line per field of every entity schema: `Schema.Field : Type`
  expand-paths.md  one line per linked/detail path of every top-level entity: `Entity: Path -> Schema`
  actions.md       one line per action: `Entity.Action(Parameter: Type, ...)`
The instance URL in `servers` is never written, and nothing is written if any part of its host name (generic words
such as `erp` or `sandbox` excepted) shows up in the output.
It prints the counts for references/endpoints/INDEX.md and every `Usr`-prefixed name, which a maintainer must
confirm is Acumatica's own (the guide's Comparison of System Endpoints lists them) before committing.
"""
import argparse
import json
import os
import re
import sys
from functools import lru_cache
from urllib.parse import urlparse

BASE_ENTITY = "Entity"
SKIP_FIELDS = {"_workflowActions"}  # on every entity (workflow actions outside the contract); named once in entities.md
# Host-name labels that name a role or a vendor, not a customer, and so need not be absent from the output.
GENERIC_LABELS = {"www", "erp", "sandbox", "demo", "test", "uat", "dev", "stage", "staging", "prod", "api", "app",
                  "apps", "cloud", "portal", "acumatica", "com", "net", "org", "local", "localhost"}


def ref_name(node):
    return node["$ref"].rsplit("/", 1)[-1] if "$ref" in node else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--swagger", required=True)
    ap.add_argument("--out", required=True, help="references/endpoints (the snapshot folder is created inside)")
    ap.add_argument("--release", required=True, help='Acumatica release of the instance, e.g. "2025 R2"')
    ap.add_argument("--build", required=True, help="build of the instance, e.g. 25.201.0213")
    ap.add_argument("--verified", required=True)
    ap.add_argument("--source-note", default="", help="where the swagger came from, without naming the instance")
    ap.add_argument("--scrub-to", default="", help="also write the swagger with `servers` removed to this path")
    a = ap.parse_args()

    doc = json.load(open(a.swagger, encoding="utf-8-sig"))
    endpoint = doc["info"]["title"]  # "Default/25.200.001"
    contract = doc["info"]["version"]
    schemas = doc["components"]["schemas"]
    paths = doc["paths"]

    def parts(name):
        return schemas[name].get("allOf", [schemas[name]])

    entities = sorted(n for n, s in schemas.items() if "allOf" in s and ref_name(s["allOf"][0]) == BASE_ENTITY)
    entity_set = set(entities)
    odd = set()

    @lru_cache(maxsize=None)
    def fields(name):
        """[(field, type text, nested schema or None, is array)] sorted by field name."""
        out = []
        for part in parts(name):
            for fname, node in part.get("properties", {}).items():
                if fname in SKIP_FIELDS:
                    continue
                is_array = node.get("type") == "array"
                target = ref_name(node.get("items", {}) if is_array else node)
                if target is None:
                    odd.add(f"{name}.{fname}")
                    target = node.get("items", {}).get("type", "?") if is_array else node.get("type", "?")
                out.append((fname, target + ("[]" if is_array else ""), target if target in entity_set else None, is_array))
        return tuple(sorted(out))

    top = []  # (entity, form, title)
    for t in doc.get("tags", []):
        m = re.match(r"^(.*?)\s*\(([A-Za-z0-9.]+)\)\s*$", t.get("description", ""))
        top.append((t["name"], m.group(2) if m else "", m.group(1) if m else t.get("description", "")))
    top.sort()
    top_names = [t[0] for t in top]
    missing = [n for n in top_names if n not in entity_set]
    if missing:
        sys.exit(f"tags without an entity schema: {missing}")

    actions = {}  # entity -> [(action, body entity, [(param, type)])]
    for p, item in paths.items():
        seg = p.strip("/").split("/")
        if len(seg) != 2 or seg[1].startswith(("{", "$")) or "post" not in item:
            continue
        body = schemas[ref_name(item["post"]["requestBody"]["content"]["application/json"]["schema"])]
        params = body["properties"].get("parameters", {}).get("properties", {})
        actions.setdefault(seg[0], []).append((
            seg[1],
            ref_name(body["properties"]["entity"]),
            [(k, ref_name(v) or v.get("type", "?")) for k, v in params.items()],
        ))

    expand = {}  # entity -> [(path, schema, is array)]
    reached = set()

    def walk(name, prefix, stack, out):
        for fname, _, nested, is_array in fields(name):
            if nested is None or nested in stack:
                continue
            reached.add(nested)
            out.append((prefix + fname, nested, is_array))
            walk(nested, prefix + fname + "/", stack + [nested], out)

    for name in top_names:
        expand[name] = []
        walk(name, "", [name], expand[name])
    orphans = [n for n in entities if n not in reached and n not in top_names]

    folder = os.path.join(a.out, endpoint.replace("/", "-"))
    note = f" ({a.source_note})" if a.source_note else ""
    header = (
        f"<!-- source: swagger.json (OpenAPI {doc.get('openapi', '3.0')}) of the {endpoint} system endpoint{note} | "
        f"version: Acumatica ERP {a.release}, build {a.build}, Contract Version {contract} | verified: {a.verified} | "
        "generated by scripts/build_endpoint_reference.py -->"
    )
    n_fields = sum(len(fields(n)) for n in entities)
    n_nested = sum(1 for n in entities for f in fields(n) if f[2])
    n_actions = sum(len(v) for v in actions.values())
    n_paths = sum(len(v) for v in expand.values())
    value_types = sorted(n for n, s in schemas.items() if "allOf" not in s and n.endswith("Value"))
    files = {}

    lines = [
        header,
        "",
        f"# {endpoint}: top-level entities",
        "",
        f"The {len(top)} entities that `{endpoint}` exposes at `/entity/{endpoint}/<Entity>`, with the form each is",
        "mapped to. `Fields` counts the value fields, `Nested` the linked and detail entities (each needs `$expand`),",
        "`Actions` the actions the contract names. Details: `fields.md`, `expand-paths.md`, `actions.md` in this folder.",
        "",
        f"Counts: {len(top)} top-level entities, {len(entities) - len(top)} nested entity schemas, {n_fields} fields "
        f"({n_fields - n_nested} value fields, {n_nested} linked/detail), {n_paths} expand paths, {n_actions} actions on "
        f"{len(actions)} entities ({sum(1 for v in actions.values() for x in v if x[2])} with parameters).",
        "",
        "Every entity also carries the system members `id`, `rowNumber`, `note`, `custom`, `error`, `files`, `_links` and",
        "`_workflowActions` (the form's workflow actions outside the contract, listed by `$adHocSchema`,",
        "`../../rest/rest-api-guide.md` § 2); they are not repeated per entity. Every top-level entity accepts the same",
        "requests (list, by keys, by ID, PUT,",
        "PATCH, DELETE, `files`, `$adHocSchema`) and `POST <Entity>/<action name>` for workflow actions that are not in",
        "the contract. The swagger does not name the key fields (`ids` is one slash-delimited path value): they are the",
        "form's keys, in the order the form defines them (`../../rest/rest-api-guide.md` § 5).",
        "",
        "| Entity | Form | Screen title | Fields | Nested | Actions |",
        "|---|---|---|---:|---:|---:|",
    ]
    for name, form, title in top:
        fs = fields(name)
        nested = sum(1 for f in fs if f[2])
        lines.append(f"| {name} | {form} | {title} | {len(fs) - nested} | {nested} | {len(actions.get(name, []))} |")
    if orphans:
        lines += ["", "Entity schemas in the swagger that no top-level entity references (listed in `fields.md` only): "
                  + ", ".join(f"`{n}`" for n in orphans) + "."]
    files["entities.md"] = lines

    lines = [
        header,
        "",
        f"# {endpoint}: fields",
        "",
        "One line per field of every entity schema (top-level and nested): `Schema.Field : Type`. Grep",
        "`^SalesOrder\\.` for an entity's fields or `\\.InventoryID ` for a field name across entities.",
        "",
        f"- A `...Value` type is a value field, sent and returned as `{{\"value\": ...}}`: {', '.join(value_types)}.",
        "  Contract Version 4 has no drop-down types: a drop-down is a `StringValue` and the swagger does not list its",
        "  allowed values.",
        "- Any other type is another schema in this file: a **linked entity** (`Address`) or, with `[]`, a **detail",
        "  entity** (`SalesOrderDetail[]`). Neither is returned unless named in `$expand` (`expand-paths.md`).",
        "",
        "```text",
    ]
    for name in entities:
        lines += [f"{name}.{fname} : {ftype}" for fname, ftype, _, _ in fields(name)]
    lines.append("```")
    files["fields.md"] = lines

    lines = [
        header,
        "",
        f"# {endpoint}: expand paths",
        "",
        "One line per linked or detail entity reachable from a top-level entity: `Entity: Path -> Schema`, `[]` for a",
        "detail (array). Grep `^SalesOrder: ` for everything `SalesOrder` can expand, or `-> Address` for where a",
        "schema is used. The path is the Contract Version 4 `$expand` value; a nested path needs its parent listed too",
        "(`$expand=Details,Details/Allocations`). Look the schema's fields up in `fields.md`.",
        "",
        "```text",
    ]
    for name in top_names:
        lines += [f"{name}: {path} -> {schema}{'[]' if is_array else ''}" for path, schema, is_array in expand[name]]
    lines.append("```")
    files["expand-paths.md"] = lines

    lines = [
        header,
        "",
        f"# {endpoint}: actions",
        "",
        "One line per action in the contract: `Entity.Action(Parameter: Type, ...)`. Invoke with",
        f"`POST /entity/{endpoint}/<Entity>/<Action>` and the body `{{\"entity\": {{...}}, \"parameters\": {{...}}}}`; the",
        "entity part identifies the record (its fields are in `fields.md`). Grep `^Shipment\\.` for an entity's actions.",
        "Workflow actions outside the contract are discovered with `<Entity>/$adHocSchema`.",
        "",
        "```text",
    ]
    for name in sorted(actions):
        for action, body_entity, params in sorted(actions[name]):
            sig = ", ".join(f"{k}: {v}" for k, v in params)
            other = f"  [entity body: {body_entity}]" if body_entity != name else ""
            lines.append(f"{name}.{action}({sig}){other}")
    lines.append("```")
    files["actions.md"] = lines

    # The instance must stay anonymous: every label of the host name, and every hyphen-separated part of a label,
    # must be absent from the output unless it is a generic word. A short label must be absent as a whole word
    # (`SalesOrder` is the words `sales` and `order`); a label of six or more characters as a substring too, so a
    # customer's name glued into an identifier (`ContosoOrder`) is caught. All files are checked before any is written.
    host = urlparse((doc.get("servers") or [{}])[0].get("url", "")).hostname or ""
    tokens = {t.lower() for label in host.split(".") for t in (label, *label.split("-"))}
    banned = {t for t in tokens if len(t) > 2 and t not in GENERIC_LABELS}
    texts = {fname: "\n".join(body) + "\n" for fname, body in files.items()}
    checks = dict(texts)
    if a.scrub_to:
        scrubbed = {k: v for k, v in doc.items() if k != "servers"}
        checks[a.scrub_to] = json.dumps(scrubbed, indent=1, ensure_ascii=False) + "\n"
    for fname, text in checks.items():
        lowered = text.lower()
        words = set(re.findall(r"[a-z0-9]+", re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text).lower()))
        hit = sorted(b for b in banned if b in words or (len(b) >= 6 and b in lowered))
        if host and host.lower() in lowered:
            hit.append(host)
        if hit:
            sys.exit(f"{fname} would contain the instance name {hit}; nothing written")
    os.makedirs(folder, exist_ok=True)
    for fname, text in texts.items():
        with open(os.path.join(folder, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    if a.scrub_to:
        os.makedirs(os.path.dirname(os.path.abspath(a.scrub_to)), exist_ok=True)
        with open(a.scrub_to, "w", encoding="utf-8", newline="\n") as f:
            f.write(checks[a.scrub_to])
        print(f"scrubbed swagger (servers removed) -> {a.scrub_to}")

    print(f"{endpoint} (Contract Version {contract}) -> {folder}")
    print(f"  {len(top)} top-level entities, {len(entities) - len(top)} nested entity schemas, {n_fields} fields, "
          f"{n_paths} expand paths, {n_actions} actions on {len(actions)} entities")
    usr = [f"{n}.{f[0]}" for n in entities for f in fields(n) if f[0].startswith("Usr")] + [n for n in entities if n.startswith("Usr")]
    print(f"  Usr-prefixed names to confirm as Acumatica's own: {usr or 'none'}")
    if odd:
        print(f"  fields with an inline type (no $ref): {sorted(odd)}")
    if orphans:
        print(f"  entity schemas not referenced by a top-level entity: {orphans}")


if __name__ == "__main__":
    main()
