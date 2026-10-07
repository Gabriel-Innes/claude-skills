#!/usr/bin/env python3
"""Build references/core-api/groups/, endpoints.md and enums.md from the Cin7 Core API Blueprint (maintenance only).

    python scripts/build_core_api_reference.py --apib <dearinventory.apib> --out references/core-api \
        --verified YYYY-MM-DD [--source-url https://dearinventory.docs.apiary.io/]

The input is the API Blueprint (`.apib`, FORMAT 1A) export of the Cin7 Core developer portal
(https://dearinventory.docs.apiary.io/, "Cin7 Core Developer Portal", API v2 at
https://inventory.dearsystems.com/ExternalApi/v2/). The raw file stays outside the repository.

What is written (every file fully regenerated):
  groups/<slug>.md   one file per `# Group`: the group's own notes, every "Available Fields" table, every enum
                     table, every action as `### METHOD /path` with its parameters, request body and response
                     body (JSON re-serialised at two-space indent when it parses, otherwise kept as written).
                     The sample request headers (`api-auth-accountid`, `api-auth-applicationkey`) are dropped:
                     the header names are documented once in api-basics.md and the sample values are never
                     written.
  endpoints.md       one row per action: method, path with query template, group, resource, title, file anchor
  enums.md           every table that is not a field table (status, type and value lists), with its anchor and
                     the group and heading it sits under
It prints the counts for references/core-api/INDEX.md and refuses to write if a sample header value survives.
"""
import argparse
import json
import os
import re
import sys
from collections import OrderedDict

GROUP_RE = re.compile(r"^# Group\s+(.+?)\s*$")
RESOURCE_RE = re.compile(r"^## (.+?)\s*\[(/[^\]]*)\]\s*$")
ACTION_RE = re.compile(r"^### (.*?)\s*\[(GET|POST|PUT|DELETE|PATCH)(?:\s+([^\]]+))?\]\s*$")
ANCHOR_RE = re.compile(r'<a name="([^"]+)"\s*/?>')
HEADER_VALUE_RE = re.compile(r"api-auth-(?:accountid|applicationkey)\s*:\s*(\S+)", re.I)
TOP_RE = re.compile(r"^\s{0,3}\+ (Request|Response|Parameters)(?![A-Za-z])")
NEXT_TOP_RE = re.compile(r"^\s{0,3}(\+ |#)")
FIELD_HEADER_RE = re.compile(r"^\|\s*property(?![A-Za-z])", re.I)
PARAM_RE = re.compile(r"^\s+\+ (\w+)\s*\(([^)]*)\)\s*(?:\.\.\.\s*(.*))?$")


def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s or "group"


def anchor_id(method, path):
    return slugify(method + " " + re.sub(r"\?.*$", "", path))


def dedent_block(lines):
    """Strip the common leading indentation of a body block (blank lines ignored)."""
    body = [l.rstrip() for l in lines]
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    if not body:
        return []
    indent = min(len(l) - len(l.lstrip()) for l in body if l.strip())
    return [l[indent:] for l in body]


def render_body(lines):
    text = "\n".join(dedent_block(lines))
    if not text.strip():
        return ["```json", "(empty)", "```"]
    try:
        parsed = json.loads(text)
        text = json.dumps(parsed, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        pass  # keep as written: the portal has a few hand-typed, non-JSON bodies
    return ["```json"] + text.split("\n") + ["```"]


class Action:
    def __init__(self, title, method, path, resource):
        self.title, self.method, self.path, self.resource = title, method, path, resource
        self.params = []     # (name, spec, description)
        self.request = []    # raw body lines
        self.response = []   # raw body lines
        self.response_code = None
        self.notes = []      # prose lines inside the action block that are not part of a list item


class Resource:
    def __init__(self, title, path):
        self.title, self.path = title, path


def parse_groups(text):
    """Split the file into (title, lines) groups; everything before the first group is the preamble."""
    groups = []
    current, buf = None, []
    for line in text.split("\n"):
        m = GROUP_RE.match(line)
        if m:
            if current is not None:
                groups.append((current, buf))
            elif buf:
                groups.append(("__preamble__", buf))
            current, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if current is not None:
        groups.append((current, buf))
    return groups


def convert_group(title, lines, slug):
    """Return (markdown lines, actions, enum tables) for one group.

    The group is rewritten line by line: resource and action headings are normalised, request/response blocks are
    turned into fenced bodies, sample headers are dropped, everything else (tables, prose, anchors) is kept.
    """
    out = []
    actions = []
    enums = []
    resource = None
    action = None
    i, n = 0, len(lines)
    last_heading = title
    last_anchor = None
    while i < n:
        line = lines[i]
        rm = RESOURCE_RE.match(line)
        am = ACTION_RE.match(line)
        if rm:
            resource = Resource(rm.group(1).strip(), rm.group(2).strip())
            action = None
            last_heading = resource.title
            out.append("")
            out.append(f"## {resource.title}")
            out.append("")
            out.append(f"Path: `{resource.path}`")
            i += 1
            continue
        if am:
            atitle, method, apath = am.group(1).strip(), am.group(2), (am.group(3) or "").strip()
            if not apath:
                apath = resource.path if resource else "(path not stated)"
            action = Action(atitle, method, apath, resource)
            actions.append(action)
            aid = anchor_id(method, apath)
            shown = f"### {method} {apath}"
            if atitle and atitle.upper() not in (method, "GET", "POST", "PUT", "DELETE"):
                shown = f"### {atitle}: {method} {apath}"
            out.append("")
            out.append(f'<a id="{aid}"></a>')
            out.append(shown)
            i += 1
            continue
        top = TOP_RE.match(line)
        if top and top.group(1) == "Parameters" and action is not None:
            out.append("")
            out.append("Parameters:")
            i += 1
            while i < n and not NEXT_TOP_RE.match(lines[i]) and (lines[i].startswith("    ") or not lines[i].strip()):
                l = lines[i]
                if not l.strip():
                    i += 1
                    if i < n and (NEXT_TOP_RE.match(lines[i]) or not lines[i].startswith("    ")):
                        break
                    continue
                pm = PARAM_RE.match(l)
                if pm:
                    name, spec, desc = pm.group(1), pm.group(2).strip(), (pm.group(3) or "").strip()
                    action.params.append((name, spec, desc))
                    out.append(f"- `{name}` ({spec}): {desc}".rstrip(": "))
                elif l.strip().startswith("+ Default:"):
                    out.append(f"  - default: {l.split(':', 1)[1].strip()}")
                elif l.strip().startswith("+ "):
                    out.append(f"  - {l.strip()[2:]}")
                else:
                    out.append("  " + l.strip())
                i += 1
            continue
        if top and top.group(1) == "Request" and action is not None:
            i += 1
            body = []
            while i < n and not NEXT_TOP_RE.match(lines[i]):
                l = lines[i]
                s = l.strip()
                if s.startswith("+ Headers") or HEADER_VALUE_RE.search(l):
                    i += 1
                    continue
                if s.startswith("+ Body"):
                    i += 1
                    while i < n and not NEXT_TOP_RE.match(lines[i]) and not lines[i].strip().startswith("+ "):
                        body.append(lines[i])
                        i += 1
                    continue
                i += 1
            action.request = body
            if dedent_block(body):
                out.append("")
                out.append("Request body:")
                out.append("")
                out.extend(render_body(body))
            continue
        if top and top.group(1) == "Response" and action is not None:
            code = re.search(r"\+ Response\s+(\d+)", line)
            action.response_code = code.group(1) if code else "200"
            i += 1
            body = []
            while i < n and not NEXT_TOP_RE.match(lines[i]):
                s = lines[i].strip()
                if s.startswith("+ Body"):
                    i += 1
                    while i < n and not NEXT_TOP_RE.match(lines[i]):
                        body.append(lines[i])
                        i += 1
                    continue
                i += 1
            action.response = body
            out.append("")
            out.append(f"Response {action.response_code}:")
            out.append("")
            out.extend(render_body(body) if dedent_block(body) else ["```json", "(no body)", "```"])
            continue
        # Any other line: headings, tables, prose, anchors. Never a sample header.
        if HEADER_VALUE_RE.search(line) or line.strip().startswith("+ Headers"):
            i += 1
            continue
        hm = re.match(r"^(#{2,4}) (.+?)\s*$", line)
        if hm:
            heading = ANCHOR_RE.sub("", hm.group(2)).strip()
            last_heading = heading
            a = ANCHOR_RE.search(hm.group(2))
            last_anchor = a.group(1) if a else None
            out.append("")
            out.append(f"{hm.group(1)} {heading}" + (f' <a id="{last_anchor}"></a>' if last_anchor else ""))
            i += 1
            continue
        a = ANCHOR_RE.search(line)
        if a and not line.strip().startswith("|"):
            last_anchor = a.group(1)
            out.append(f'<a id="{last_anchor}"></a>')
            i += 1
            continue
        if line.startswith("|") and (i == 0 or not lines[i - 1].startswith("|")):
            # start of a table: collect it whole to classify
            tbl = []
            while i < n and lines[i].startswith("|"):
                tbl.append(lines[i].rstrip())
                i += 1
            header = tbl[0].lower()
            is_field_table = bool(FIELD_HEADER_RE.match(tbl[0]))
            if not is_field_table and len(tbl) > 2:
                enums.append((slug, last_heading, last_anchor, tbl))
            out.extend(tbl)
            continue
        out.append(line.rstrip())
        i += 1
    # collapse runs of blank lines
    collapsed = []
    for l in out:
        if l == "" and collapsed and collapsed[-1] == "":
            continue
        collapsed.append(l)
    return collapsed, actions, enums


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apib", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--verified", required=True)
    ap.add_argument("--source-url", default="https://dearinventory.docs.apiary.io/")
    args = ap.parse_args()

    text = open(args.apib, encoding="utf-8").read()
    host = re.search(r"^HOST:\s*(\S+)", text, re.M)
    base_url = host.group(1) if host else "(HOST not stated)"
    sample_values = set(HEADER_VALUE_RE.findall(text))
    provenance = (f"<!-- source: {args.source_url} (API Blueprint export, Cin7 Core Developer Portal) | "
                  f"version: Cin7 Core API v2 ({base_url}), generated by scripts/build_core_api_reference.py | "
                  f"verified: {args.verified} -->")

    groups = parse_groups(text)
    groups_dir = os.path.join(args.out, "groups")
    os.makedirs(groups_dir, exist_ok=True)
    for old in os.listdir(groups_dir):
        if old.endswith(".md"):
            os.remove(os.path.join(groups_dir, old))

    catalogue = []
    all_enums = []
    group_rows = []
    counts = OrderedDict(groups=0, resources=0, actions=0, field_tables=0, enum_tables=0)
    written = {}
    for title, lines in groups:
        if title == "__preamble__":
            continue
        slug = slugify(title)
        md, actions, enums = convert_group(title, lines, slug)
        field_tables = sum(1 for l in md if FIELD_HEADER_RE.match(l))
        resources = sorted({a.resource.path for a in actions if a.resource})
        header = [provenance, "", f"# {title} (Cin7 Core API v2)", "",
                  f"Group `{title}` of the Cin7 Core API reference. Base URL `{base_url}`; every request carries the "
                  f"`api-auth-accountid` and `api-auth-applicationkey` headers (see `../api-basics.md`). "
                  f"{len(actions)} actions on {len(resources)} resources, {field_tables} field tables.", ""]
        if actions:
            header.append("| Action | Path |")
            header.append("|---|---|")
            for a in actions:
                shown = a.title if a.title and a.title.upper() not in ("GET", "POST", "PUT", "DELETE") else a.method
                header.append(f"| [{shown}](#{anchor_id(a.method, a.path)}) | `{a.method} {a.path}` |")
            header.append("")
        content = "\n".join(header + md).rstrip() + "\n"
        path = os.path.join(groups_dir, slug + ".md")
        written[path] = content
        counts["groups"] += 1
        counts["resources"] += len(resources)
        counts["actions"] += len(actions)
        counts["field_tables"] += field_tables
        counts["enum_tables"] += len(enums)
        group_rows.append((title, slug, len(resources), len(actions), field_tables, len(enums)))
        for a in actions:
            catalogue.append((title, slug, a))
        all_enums.extend((title, slug, h, anc, tbl) for (_, h, anc, tbl) in enums)

    # endpoints.md
    ep = [provenance, "", "# Cin7 Core API v2: endpoint catalogue", "",
          f"One row per documented action ({counts['actions']} actions, {counts['resources']} resources, "
          f"{counts['groups']} groups). Grep by path (`/sale/invoice`), method (`^\\| DELETE`) or group. The link "
          f"opens the group file at the action: parameters, request body and response body. Paths are relative to "
          f"`{base_url}`; `{{Name}}` marks a query parameter, listed in the Parameters column (`*` = required).", "",
          "| Method | Path | Group | Resource | Action | Parameters | File |", "|---|---|---|---|---|---|---|"]
    for title, slug, a in catalogue:
        params = ", ".join((p[0] + ("*" if "required" in p[1] else "")) for p in a.params)
        shown = a.title if a.title and a.title.upper() not in ("GET", "POST", "PUT", "DELETE") else ""
        bare = re.sub(r"\?.*$", "", a.path)
        res = a.resource.title if a.resource else ""
        ep.append(f"| {a.method} | `{bare}` | {title} | {res} | {shown} | {params} | "
                  f"[{slug}.md](groups/{slug}.md#{anchor_id(a.method, a.path)}) |")
    written[os.path.join(args.out, "endpoints.md")] = "\n".join(ep) + "\n"

    # enums.md
    en = [provenance, "", "# Cin7 Core API v2: status, type and value lists", "",
          f"Every list table in the reference that is not a field table ({len(all_enums)} tables), with the group and "
          "heading it sits under. Grep the value (`BACKORDERED`) or the anchor name the field tables link to "
          "(`SaleStatesList`). Each table is also in its group file.", ""]
    for title, slug, heading, anc, tbl in all_enums:
        en.append(f"## {title}: {heading}" + (f" (`{anc}`)" if anc else ""))
        en.append("")
        en.append(f"Source file: `groups/{slug}.md`")
        en.append("")
        en.extend(tbl)
        en.append("")
    written[os.path.join(args.out, "enums.md")] = "\n".join(en).rstrip() + "\n"

    # safety: no sample header value may survive
    leaked = []
    for path, content in written.items():
        for v in sample_values:
            if v in content:
                leaked.append((os.path.basename(path), v))
    if leaked:
        sys.exit("not written: sample header values survive in " + ", ".join(f"{p} ({v[:8]}...)" for p, v in leaked))
    for path, content in written.items():
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)

    print(f"base URL: {base_url}")
    print("counts: " + ", ".join(f"{k}={v}" for k, v in counts.items()))
    print(f"sample header values dropped: {len(sample_values)}")
    print()
    print("| Group | File | Resources | Actions | Field tables | Enum tables |")
    print("|---|---|---|---|---|---|")
    for title, slug, r, a, ft, et in group_rows:
        print(f"| {title} | `groups/{slug}.md` | {r} | {a} | {ft} | {et} |")


if __name__ == "__main__":
    main()
