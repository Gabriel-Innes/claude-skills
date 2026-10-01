#!/usr/bin/env python3
"""Compile the erpref.com cache (see fetch_erpref_schema.py) into the skill's dictionary (maintenance only).

Writes, under <out>:
  dict/<TABLE>.md   one file per table: module, ObjType, indexes, then one line per column
  table-index.md    one line per table (description, module, column/index counts, ObjType)

    python build_schema_dict.py --cache <dir> --out references/dictionary/9.3 \
        --objects references/objects/object-types.md --verified YYYY-MM-DD [--label "SAP Business One 9.3"]

Every table in the cached listing must have both cache files, with column and index counts matching the
listing; otherwise it stops and names the table, so a half-finished crawl can't produce a half dictionary.
Add --allow-partial to build only what is cached (testing).
"""
import argparse, collections, html, json, os, re, sys

strip = lambda s: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()


def load_objtypes(path):
    objs = collections.defaultdict(list)
    if path:
        for line in open(path, encoding="utf-8"):
            m = re.match(r"\| (\d+) \| (\w+) \|", line)
            if m:
                objs[m.group(2)].append(m.group(1))
    return objs


def parse_indexes(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for tb in re.findall(r"<table[^>]*erpindicies.*?</table>", s, re.S):
        for tr in re.findall(r"<tr.*?</tr>", tb, re.S)[1:]:
            out.append([strip(x) for x in re.findall(r"<td.*?</td>", tr, re.S)])
    return out


def col_type(d):
    t, length, dec = d["sqlType"], d["length"], d["decimals"]
    if length in (None, ""):
        return t
    return f"{t}({length},{dec})" if dec not in (0, None) else f"{t}({length})"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--objects", help="object-types.md, to add an ObjType column")
    ap.add_argument("--verified", required=True, help="YYYY-MM-DD for the provenance headers")
    ap.add_argument("--label", default="SAP Business One 9.3")
    ap.add_argument("--allow-partial", action="store_true")
    ap.add_argument("--index-note", default="", help="warning added to each file's Indexes line and to the index header")
    a = ap.parse_args()

    listing = os.path.join(a.cache, "tables.json")
    if not os.path.exists(listing):
        sys.exit(f"{listing} not found; run fetch_erpref_schema.py first")
    tables = json.load(open(listing, encoding="utf-8"))
    objs = load_objtypes(a.objects)
    os.makedirs(os.path.join(a.out, "dict"), exist_ok=True)
    head = f"<!-- source: erpref.com (schema IP: SAP) | version: {a.label} | verified: {a.verified} -->"

    index_lines, ncols, skipped = [], 0, []
    for t in sorted(tables, key=lambda x: x["table"]):
        name = t["table"]
        cp, ip = os.path.join(a.cache, "cols", f"{name}.json"), os.path.join(a.cache, "idx", f"{name}.html")
        if not (os.path.exists(cp) and os.path.exists(ip)):
            skipped.append(name)
            continue
        cols = json.load(open(cp, encoding="utf-8"))["data"]
        idx = parse_indexes(ip)
        if len(cols) != t["cols"] or len(idx) != t["indicies"]:
            sys.exit(f"{name}: {len(cols)} cols / {len(idx)} indexes, listing says {t['cols']} / {t['indicies']}")
        cols.sort(key=lambda d: d["column"])
        ot = objs.get(name)
        out = [head, f"# {name} - {t['description']}",
               f"Module: {t['module']} | {len(cols)} columns" + (f" | ObjType: {','.join(ot)}" if ot else ""),
               "Indexes (name: columns; first = primary key; U = unique)" + (f" - {a.index_note}" if a.index_note else "") + ":"]
        for c in idx:
            nm, _primary, uniq, _type, cl = (c + [""] * 5)[:5]
            out.append(f"  {nm}{' U' if uniq == 'Yes' else ''}: {cl}")
        out.append("Fields (name type(len) description [values] ->parent table):")
        for d in cols:
            parts = [f"  {strip(d['field'])} {col_type(d)}"]
            if (d["description"] or "").strip():
                parts.append(d["description"].strip())
            if d["defaultValue"]:
                parts.append(f"default={d['defaultValue']}")
            if d["constraints"]:
                parts.append(f"[{d['constraints']}]")
            if d["relation"]:
                parts.append("->" + "/".join(re.findall(r">([^<]+)</a>", d["relation"])))
            out.append(" ".join(parts))
            ncols += 1
        with open(os.path.join(a.out, "dict", f"{name}.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(out) + "\n")
        index_lines.append(f"| {name} | {t['description'].replace('|', '/')} | {t['module']} | {len(cols)} | "
                           f"{len(idx)} | {','.join(ot) if ot else ''} |")

    if skipped and not a.allow_partial:
        sys.exit(f"{len(skipped)} tables not cached (first: {skipped[:5]}); finish the fetch or pass --allow-partial")
    with open(os.path.join(a.out, "table-index.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"<!-- source: erpref.com (schema IP: SAP); ObjType from references/objects/object-types.md | "
                f"version: {a.label} | verified: {a.verified} -->\n\n# {a.label} table index\n\n")
        f.write(f"> **Version disclaimer:** this is the {a.label} schema only. Later releases can differ, and a client's own "
                "user-defined tables and fields are not included. Confirm columns on the client's database."
                + (f" **{a.index_note}**" if a.index_note else "") + "\n\n"
                f"{len(index_lines)} tables, one line each, sorted by name. Open `dict/<TABLE>.md` for columns, indexes, "
                "valid values and parent-table links. Grep by description or module for topic search.\n\n")
        f.write("| Table | Description | Module | Cols | Idx | ObjType |\n|---|---|---|---|---|---|\n")
        f.write("\n".join(index_lines) + "\n")
    print(f"{len(index_lines)} tables, {ncols} columns written to {a.out}" + (f" ({len(skipped)} skipped)" if skipped else ""))


if __name__ == "__main__":
    main()
