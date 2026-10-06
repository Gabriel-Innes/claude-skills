#!/usr/bin/env python3
"""Compile an Acumatica DAC-based OData v4 `$metadata` document into grep-friendly Markdown references (maintenance only).

    python scripts/build_odata_metadata_ref.py <metadata.xml> references/odata/metadata \\
        --verified YYYY-MM-DD --label "Acumatica ERP 2026 R2"

Fetch the metadata outside this script from a **clean** instance (never a customer's):
    GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata
The document carries no instance-specific member, so a gzipped copy is committed under
sources/acumatica-assistant/ (the script reads .gz directly) for anyone to regenerate the snapshot. The script writes:

    INDEX.md            provenance, counts, how the files are meant to be read
    entity-sets.md      one row per DAC: every entity-set name (URL alias) that reaches it, the key, the fields the
                        metadata marks non-filterable / non-selectable, and singletons
    api/INDEX.md        one row per EntityType / ComplexType: key, counts, base type, entity sets, and the bundle
                        file + line range of its entry
    api/members-NN.md   the entries, bundled: a heading per type, then one line per field
                        (`Type.Field : Edm.Type [key] [required] "Display name"`) and per navigation property
                        (`Type.Nav -> Target (LocalField=TargetField)`), so a grep for `^PX.Objects.SO.SOOrder.` returns
                        the whole DAC and a grep for `\\.OrderNbr ` finds every DAC with that field
    enums.md            EnumType members (the DAC metadata has very few)

Use --exclude-regex to drop types whose fully qualified name matches (for example customization-project namespaces)
when the source instance is not clean; the generated INDEX.md records every filter used.
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bundle_util  # noqa: E402  (shared with the other skills' builders: bundles + File/Line/Lines ranges)

EDM = "http://docs.oasis-open.org/odata/ns/edm"
EDMX = "http://docs.oasis-open.org/odata/ns/edmx"
DESCRIPTION = "Org.OData.Core.V1.Description"
MAX_BYTES = 1_000_000  # bundle size, the repo standard (a skill must stay under 200 files)


def q(ns: str, name: str) -> str:
    return f"{{{ns}}}{name}"


def truth(value: str | None) -> bool:
    return value is not None and value.lower() == "true"


def description(el: ET.Element) -> str:
    for ann in el.findall(q(EDM, "Annotation")):
        if ann.attrib.get("Term") == DESCRIPTION and ann.attrib.get("String"):
            return ann.attrib["String"].replace('"', "'").strip()
    return ""


def filter_restrictions(es: ET.Element) -> tuple[list[str], bool]:
    """Return (NonFilterableProperties, Filterable=false) from a Cap.FilterRestrictions annotation on an entity set.

    The guide (DAC-Based OData: General Information) says every field in NonFilterableProperties is treated as
    non-filterable *and* non-selectable, and Filterable=false means no field declared in the DAC itself may be used
    in $filter or $select (inherited fields may). Both forms are kept."""
    non_filterable: list[str] = []
    not_filterable = False
    for ann in es.findall(q(EDM, "Annotation")):
        term = ann.attrib.get("Term", "")
        if not term.endswith("FilterRestrictions"):
            continue
        for pv in ann.iter(q(EDM, "PropertyValue")):
            prop = pv.attrib.get("Property")
            if prop == "NonFilterableProperties":
                non_filterable += [p.text.strip() for p in pv.iter(q(EDM, "PropertyPath")) if p.text]
            elif prop == "Filterable" and pv.attrib.get("Bool", "").lower() == "false":
                not_filterable = True
    return non_filterable, not_filterable


def parse(path: Path):
    # The committed copy under sources/acumatica-assistant/ is gzipped (20 MB raw, 1 MB compressed).
    if path.suffix == ".gz":
        import gzip
        with gzip.open(path, "rb") as f:
            root = ET.parse(f).getroot()
    else:
        root = ET.parse(path).getroot()
    if root.tag != q(EDMX, "Edmx"):
        raise SystemExit("Expected OData v4 edmx:Edmx in the OASIS namespace.")
    if root.attrib.get("Version") not in (None, "4.0"):
        raise SystemExit(f"Expected OData v4 metadata, got Edmx Version={root.attrib.get('Version')!r}.")
    schemas = root.findall(".//" + q(EDM, "Schema"))
    if not schemas:
        raise SystemExit("No OData v4 Schema elements found.")
    return schemas


def build(metadata: Path, out: Path, verified: str, label: str, source: str, excludes: list[re.Pattern[str]],
          max_bytes: int = MAX_BYTES) -> dict:
    schemas = parse(metadata)
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"Output directory is not empty: {out}. Build into an empty scratch directory.")
    excluded: set[str] = set()

    def blocked(name: str) -> bool:
        if any(rx.search(name) for rx in excludes):
            excluded.add(name)
            return True
        return False

    # ---- pass 1: containers (entity sets and singletons), so type entries can list their URL names ------------
    sets_by_type: dict[str, list[str]] = {}
    singletons_by_type: dict[str, list[str]] = {}
    restrictions_by_type: dict[str, tuple[list[str], bool]] = {}
    restriction_conflicts: list[str] = []
    for schema in schemas:
        for container in schema.findall(q(EDM, "EntityContainer")):
            for es in container.findall(q(EDM, "EntitySet")):
                t = es.attrib.get("EntityType", "")
                if blocked(t):
                    continue
                sets_by_type.setdefault(t, []).append(es.attrib["Name"])
                r = filter_restrictions(es)
                if t in restrictions_by_type and restrictions_by_type[t] != r:
                    restriction_conflicts.append(f"{t}: {es.attrib['Name']}")
                restrictions_by_type.setdefault(t, r)
            for sg in container.findall(q(EDM, "Singleton")):
                t = sg.attrib.get("Type", "")
                if blocked(t):
                    continue
                singletons_by_type.setdefault(t, []).append(sg.attrib["Name"])

    def url_names(t: str) -> list[str]:
        # The generated `PX_Namespace_Class` name first, then the display-name and class-name aliases as listed.
        names = sets_by_type.get(t, [])
        return sorted(names, key=lambda n: (not n.startswith("PX_") and "_" not in n, names.index(n)))

    # ---- pass 2a: keys per type, so a derived DAC (Customer : BAccount) can show the key it inherits ------------
    own_keys: dict[str, list[str]] = {}
    base_of: dict[str, str] = {}
    for schema in schemas:
        ns = schema.attrib.get("Namespace", "")
        for kind in ("EntityType", "ComplexType"):
            for el in schema.findall(q(EDM, kind)):
                full = f"{ns}.{el.attrib['Name']}" if ns else el.attrib["Name"]
                own_keys[full] = [x.attrib.get("Name", "") for x in el.findall(f"{q(EDM,'Key')}/{q(EDM,'PropertyRef')}")]
                if el.attrib.get("BaseType"):
                    base_of[full] = el.attrib["BaseType"]

    def resolved_keys(full: str) -> tuple[list[str], str]:
        """(key fields, type that declares them): the type's own key, else the nearest base type's."""
        seen, t = set(), full
        while t and t not in seen:
            seen.add(t)
            if own_keys.get(t):
                return own_keys[t], t
            t = base_of.get(t, "")
        return [], ""

    # ---- pass 2b: types -----------------------------------------------------------------------------------------
    type_entries: list[tuple[str, str]] = []
    type_rows: list[dict] = []
    enum_lines: list[str] = []
    n_props = n_navs = n_labelled = 0
    edm_types: dict[str, int] = {}

    for schema in schemas:
        ns = schema.attrib.get("Namespace", "")
        for kind in ("EntityType", "ComplexType"):
            for el in schema.findall(q(EDM, kind)):
                full = f"{ns}.{el.attrib['Name']}" if ns else el.attrib["Name"]
                if blocked(full):
                    continue
                keys, key_owner = resolved_keys(full)
                props = el.findall(q(EDM, "Property"))
                navs = el.findall(q(EDM, "NavigationProperty"))
                label_text = description(el)
                base = el.attrib.get("BaseType", "")
                names = url_names(full)
                non_filterable, not_filterable = restrictions_by_type.get(full, ([], False))

                lines = [f"# {full} ({kind})", ""]
                if label_text:
                    lines.append(f'Label: "{label_text}"')
                if base:
                    lines.append(f"BaseType: {base}")
                if truth(el.attrib.get("Abstract")):
                    lines.append("Abstract: true")
                if truth(el.attrib.get("OpenType")):
                    lines.append("OpenType: true")
                if keys:
                    lines.append("Key: " + ", ".join(keys) + (f" (inherited from {key_owner})" if key_owner != full else ""))
                if names:
                    lines.append("Entity sets: " + ", ".join(names))
                if singletons_by_type.get(full):
                    lines.append("Singletons: " + ", ".join(singletons_by_type[full]))
                if not_filterable:
                    lines.append("Filterable: false (fields declared in this DAC cannot be used in $filter or $select; inherited ones can)")
                if non_filterable:
                    lines.append("Non-filterable, non-selectable: " + ", ".join(non_filterable))
                lines.append("")
                for p in props:
                    name, etype = p.attrib.get("Name", ""), p.attrib.get("Type", "")
                    edm_types[etype] = edm_types.get(etype, 0) + 1
                    tags = []
                    if name in keys and key_owner == full:
                        tags.append("key")
                    if p.attrib.get("Nullable") == "false":
                        tags.append("required")
                    lab = description(p)
                    n_labelled += bool(lab)
                    lines.append(f"{full}.{name} : {etype}" + (" [" + " ".join(tags) + "]" if tags else "") + (f' "{lab}"' if lab else ""))
                n_props += len(props)
                for nv in navs:
                    name, target = nv.attrib.get("Name", ""), nv.attrib.get("Type", "")
                    rc = [(c.attrib.get("Property", ""), c.attrib.get("ReferencedProperty", "")) for c in nv.findall(q(EDM, "ReferentialConstraint"))]
                    via = " (" + ", ".join(f"{a}={b}" for a, b in rc) + ")" if rc else ""
                    lines.append(f"{full}.{name} -> {target}{via}")
                n_navs += len(navs)
                type_entries.append((full, "\n".join(lines).rstrip() + "\n"))
                type_rows.append(dict(name=full, kind=kind, label=label_text, keys=", ".join(keys), props=len(props),
                                      navs=len(navs), base=base, sets=names, singletons=singletons_by_type.get(full, []),
                                      non_filterable=non_filterable, not_filterable=not_filterable))

        for el in schema.findall(q(EDM, "EnumType")):
            full = f"{ns}.{el.attrib['Name']}" if ns else el.attrib["Name"]
            if blocked(full):
                continue
            for m in el.findall(q(EDM, "Member")):
                enum_lines.append(f"{full}.{m.attrib.get('Name','')} = {m.attrib.get('Value','')}")

    type_entries.sort(key=lambda x: x[0].lower())
    type_rows.sort(key=lambda r: r["name"].lower())
    enum_lines.sort(key=str.lower)

    # ---- write ------------------------------------------------------------------------------------------------------
    out.mkdir(parents=True, exist_ok=True)
    provenance = f"<!-- source: {source} | version: {label} | verified: {verified} -->"
    locs = bundle_util.write_bundles([("members", type_entries)], str(out / "api"), provenance, max_bytes, numbered_prefix="members")

    lines = [provenance, "", "# DAC-based OData metadata: type index", "",
             "One row per EntityType / ComplexType. Open the entry with the `File`, `Line` and `Lines` columns "
             "(a line-range read of `api/<File>`), or grep `api/members-*.md` for `^<Type>\\.`. A type with a BaseType "
             "lists only the fields it adds; its key and the rest of its fields are those of the base type (the entry "
             "says which type declares the key).", "",
             "| Type | Kind | Label | Key | Fields | Navigation | BaseType | Entity sets | File | Line | Lines |",
             "|---|---|---|---|---:|---:|---|---|---|---:|---:|"]
    for r in type_rows:
        f, ln, n = locs[r["name"]]
        lines.append(f"| {r['name']} | {r['kind']} | {r['label']} | {r['keys']} | {r['props']} | {r['navs']} | {r['base']} | {', '.join(r['sets'])} | {f} | {ln} | {n} |")
    (out / "api" / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    lines = [provenance, "", "# DAC-based OData entity sets", "",
             "One row per DAC that the container exposes. **Entity sets** are the names accepted after `/api/odata/dac/` "
             "(the generated `PX_Namespace_Class` name, the display-name alias and the class-name alias; a digit suffix "
             "means the alias collided with another DAC). **Non-filterable** fields are the `Cap.FilterRestrictions` "
             "`NonFilterableProperties` of the entity set, which the DAC-based OData interface refuses in both `$filter` "
             "and `$select`; **Filterable=false** means no field declared in the DAC itself may be used in `$filter` or "
             "`$select`.", "",
             "| DAC | Label | Entity sets | Key | Non-filterable fields | Filterable=false |", "|---|---|---|---|---|---|"]
    n_sets = 0
    for r in type_rows:
        if not r["sets"]:
            continue
        n_sets += len(r["sets"])
        lines.append(f"| {r['name']} | {r['label']} | {', '.join(r['sets'])} | {r['keys']} | {', '.join(r['non_filterable'])} | {'yes' if r['not_filterable'] else ''} |")
    singles = [(r["name"], r["singletons"], r["label"]) for r in type_rows if r["singletons"]]
    if singles:
        lines += ["", "## Singletons", "", "Setup-style DACs exposed as a single record (`GET .../api/odata/dac/<Name>` returns one object, not a `value` array).", "",
                  "| DAC | Label | Singleton names |", "|---|---|---|"]
        lines += [f"| {t} | {lab} | {', '.join(names)} |" for t, names, lab in singles]
    (out / "entity-sets.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    (out / "enums.md").write_text(provenance + "\n\n# DAC-based OData enum members\n\n" + ("\n".join(enum_lines) + "\n" if enum_lines else "(none)\n"), encoding="utf-8", newline="\n")

    counts = {
        "schemas": len(schemas),
        "entity_types": sum(r["kind"] == "EntityType" for r in type_rows),
        "complex_types": sum(r["kind"] == "ComplexType" for r in type_rows),
        "fields": n_props, "fields_with_display_name": n_labelled, "navigation_properties": n_navs,
        "entity_sets": n_sets, "dacs_with_entity_sets": sum(bool(r["sets"]) for r in type_rows),
        "singletons": sum(len(v) for v in singletons_by_type.values()),
        "dacs_with_non_filterable_fields": sum(bool(r["non_filterable"]) for r in type_rows),
        "dacs_filterable_false": sum(r["not_filterable"] for r in type_rows),
        "enum_members": len(enum_lines), "excluded_types": len(excluded),
        "member_bundles": len({v[0] for v in locs.values()}),
    }
    namespaces = sorted({s.attrib.get("Namespace", "") for s in schemas if s.attrib.get("Namespace")})
    lines = [provenance, "", "# DAC-based OData metadata snapshot", "",
             f"Compiled from `GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata` of a clean **{label}** instance by "
             "`scripts/build_odata_metadata_ref.py`. It is the OData v4 CSDL of the DAC-based interface, not a tenant's "
             "generic-inquiry (`/api/odata/gi`) metadata and not the contract-based REST API's `swagger.json`.", "",
             "| Path | Covers |", "|---|---|",
             "| `entity-sets.md` | One row per DAC: the entity-set names accepted in the URL, key fields, non-filterable fields, `Filterable=false`; plus singletons |",
             "| `api/INDEX.md` | One row per EntityType / ComplexType: label, key, counts, base type, entity sets, and the bundle file + line range of its entry |",
             "| `api/members-NN.md` | The entries: a heading per type, then `Type.Field : Edm.Type [key] [required] \"Display name\"` and `Type.Nav -> Target (LocalField=TargetField)` lines |",
             "| `enums.md` | `Enum.Member = Value` lines |", "",
             "## How to read it", "",
             "- **Which DAC / which URL name?** grep `entity-sets.md` for the class name, the display name (`| Sales Order |`) or the URL alias.",
             "- **Fields of a DAC**: grep `api/members-*.md` for `^PX\\.Objects\\.SO\\.SOOrder\\.` (one line per field and navigation property), or take `File` / `Line` / `Lines` from `api/INDEX.md` and read that range. A DAC with a `BaseType` (for example `PX.Objects.AR.Customer : PX.Objects.CR.BAccount`) lists only the fields it adds; read the base type's entry for the rest, including the key.",
             "- **Which DACs have a field named X?** grep `api/members-*.md` for `\\.X : `.",
             "- **Joins**: a navigation line `A.BAccountByCustomerID -> PX.Objects.CR.BAccount (CustomerID=BAccountID)` means `$expand=BAccountByCustomerID` and that `A.CustomerID` equals `BAccount.BAccountID`; `A.SOLineCollection -> Collection(PX.Objects.SO.SOLine)` is a detail collection.",
             "- Field lines carry the field's UI display name in quotes when the metadata has one (the `Org.OData.Core.V1.Description` annotation), which is how a user's wording (\"Customer Order Nbr.\") maps to a field (`CustomerOrderNbr`).", "",
             "## Counts", ""]
    lines += [f"- {k}: {v}" for k, v in counts.items()]
    lines += ["", "## Edm types used", "", ", ".join(f"`{t}` ({n})" for t, n in sorted(edm_types.items(), key=lambda x: -x[1])), "",
              "## Scope and limits", "",
              "- One clean instance, one release. A customer's instance adds customization and user-defined fields, extension DACs and "
              "custom namespaces, and may lack modules (Manufacturing, Payroll, Field Service, Construction ...) whose DACs are listed here. "
              "Absence here is not proof of absence there, and presence here is not proof of presence there: confirm on the "
              "client's `/api/odata/dac/$metadata`.",
              "- The DAC-based interface exposes DACs, not forms. A DAC's fields are the database-backed and unbound fields the "
              "server publishes; the metadata does not say which fields are populated for a given record type.",
              "- Navigation property names are generated (`<Target>By<LocalField>` for lookups, `<Detail>Collection` for details); "
              "the referential constraint in parentheses is the join the server uses.",
              "- `Edm.Decimal` fields are declared with `Scale=\"Variable\"`; `Edm.Binary` is used for `tstamp`; no `MaxLength` "
              "or `Precision` facets are published.",
              "- The `px.GetDeletedRecords()` function documented for removed-record tracking is not declared in this metadata; "
              "its result shape is the `PX.Api.OData.DAC.DeletedRecordResult` complex type (`RefNoteID`, `DeleteDate`).",
              "- Namespaces: " + ", ".join(namespaces) + "."]
    if restriction_conflicts:
        lines += ["", "## Restriction conflicts", "",
                  "Entity sets of the same DAC with different `Cap.FilterRestrictions` (the first one seen was kept):", ""]
        lines += [f"- {c}" for c in restriction_conflicts]
    if excludes:
        lines += ["", "## Exclusion filters", ""] + [f"- type name: `{rx.pattern}`" for rx in excludes]
    (out / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return counts


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("metadata", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--verified", required=True, help="YYYY-MM-DD")
    ap.add_argument("--label", required=True, help='e.g. "Acumatica ERP 2026 R2"')
    ap.add_argument("--source", default="DAC-based OData $metadata of a clean Acumatica ERP instance (GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata)",
                    help="provenance text; never include an instance URL with credentials")
    ap.add_argument("--exclude-regex", action="append", default=[], help="repeatable regex matched against fully qualified type names")
    ap.add_argument("--max-bytes", type=int, default=MAX_BYTES, help="bundle size before a bundle file is split")
    args = ap.parse_args()
    counts = build(args.metadata, args.out, args.verified, args.label, args.source,
                   [re.compile(p) for p in args.exclude_regex], args.max_bytes)
    for k, v in counts.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
