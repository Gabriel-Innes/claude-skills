#!/usr/bin/env python3
"""Compile SAP's own Database Tables Reference (REFDB.chm) into the skill's dictionary (maintenance only).

Source: REFDB.chm, "SAP Business One SDK 10.0 - Database Tables Reference", shipped with the SDK
(<SDK folder>\\Help\\REFDB.chm). Decompile it first (Windows, to a path without spaces):

    hh.exe -decompile <extractdir> REFDB.chm

The result is one folder per module (Administration, Banking, ... Marketing_Documents) holding one <TABLE>.htm per
table, plus refdb.hhc. Each page has three tables: a logo header, the field table (Field, Description, Type, Size,
Related, Default Value, Constraints - enum values continue on following rows with the first cells empty) and the keys
table (Key, Unique, Field - the columns of a multi-column key continue on following rows).

    python build_refdb_schema.py <extractdir> --out references/dictionary/10.0 \
        --objects references/objects/object-types.md --verified YYYY-MM-DD [--label "SAP Business One 10.0"]

Writes, in the same format as build_schema_dict.py (so SKILL.md's workflow is identical for both versions):
  dict/<TABLE>.md   module, column count, ObjType, indexes, then one line per column
  table-index.md    one line per table

Checks: every page named in refdb.hhc is read, every page has the expected headers and 8-cell rows, table names match
file names, and each table's columns/keys are non-empty. Anything else stops the build with the table named.
"""
import argparse, collections, html, os, re, sys

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("extract")
ap.add_argument("--out", required=True)
ap.add_argument("--objects")
ap.add_argument("--verified", required=True)
ap.add_argument("--label", default="SAP Business One 10.0")
ap.add_argument("--source", default="REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference)")
A = ap.parse_args()


def clean(c):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", c))).replace("\xa0", " ").strip()


def cells(tr):
    return [clean(c) for c in re.findall(r"<t[dh].*?</t[dh]>", tr, re.S)]


def rows(tbl):
    return [cells(x) for x in re.findall(r"<tr.*?</tr>", tbl, re.S)]


objs = collections.defaultdict(list)
if A.objects:
    for line in open(A.objects, encoding="utf-8"):
        m = re.match(r"\| (\d+) \| (\w+) \|", line)
        if m:
            objs[m.group(2)].append(m.group(1))

modules = sorted(d for d in os.listdir(A.extract)
                 if os.path.isdir(os.path.join(A.extract, d)) and not d.startswith("!"))
if not modules:
    sys.exit("no module folders found; is this the decompiled REFDB.chm?")

# pages named by the table of contents must all be present
hhc = [f for f in os.listdir(A.extract) if f.lower().endswith(".hhc")]
toc_pages = set()
if hhc:
    s = open(os.path.join(A.extract, hhc[0]), encoding="utf-8", errors="replace").read()
    for loc in re.findall(r'<param name="Local" value="([^"]+)"', s):
        loc = loc.replace("\\", "/")
        if loc.split("/")[0] in modules and loc.lower().endswith(".htm"):
            toc_pages.add(loc)

os.makedirs(os.path.join(A.out, "dict"), exist_ok=True)
head = f"<!-- source: {A.source} | version: {A.label} | verified: {A.verified} -->"
index_lines, ncols, nkeys, seen = [], 0, 0, set()
no_primary, issues = [], collections.Counter()

for mod in modules:
    modname = mod.replace("_", " ")
    for fn in sorted(os.listdir(os.path.join(A.extract, mod))):
        if not fn.lower().endswith(".htm"):
            continue
        rel_path = f"{mod}/{fn}"
        seen.add(rel_path)
        name = fn[:-4]
        s = open(os.path.join(A.extract, mod, fn), encoding="utf-8", errors="replace").read()
        tn = re.search(r"Table Name:\s*([^<]+)", s)
        td = re.search(r"Table Description:\s*([^<]*)", s)
        if not tn or tn.group(1).strip() != name:
            sys.exit(f"{rel_path}: 'Table Name' ({tn.group(1).strip() if tn else None}) doesn't match the file name")
        desc = clean(td.group(1)) if td else ""
        tabs = re.findall(r"<table.*?</table>", s, re.S)
        if len(tabs) != 3:
            sys.exit(f"{rel_path}: expected 3 tables, found {len(tabs)}")
        frows, krows = rows(tabs[1]), rows(tabs[2])
        if frows[0][:7] != ["Field", "Description", "Type", "Size", "Related", "Default Value", "Constraints"]:
            sys.exit(f"{rel_path}: unexpected field-table header {frows[0]}")
        if krows[0][:3] != ["Key", "Unique", "Field"]:
            sys.exit(f"{rel_path}: unexpected key-table header {krows[0]}")

        fields = []  # [name, desc, type, size, related, default, [(value, label)]]
        for r in frows[1:]:
            if len(r) != 8:
                sys.exit(f"{rel_path}: field row with {len(r)} cells: {r}")
            if r[0]:
                fields.append([r[0], r[1], r[2], r[3], r[4], r[5], [] if not r[6] and not r[7] else [(r[6], r[7])]])
            elif r[6] or r[7]:
                if not fields:
                    sys.exit(f"{rel_path}: constraint row before any field")
                fields[-1][6].append((r[6], r[7]))
        keys = []  # [name, unique, [columns]]
        for r in krows[1:]:
            if len(r) < 3:
                sys.exit(f"{rel_path}: key row {r}")
            if r[0]:
                keys.append([r[0], r[1], [r[2]] if r[2] else []])
            elif keys and r[2]:
                keys[-1][2].append(r[2])
        if not fields:
            sys.exit(f"{rel_path}: no fields")
        if not keys:
            issues["table with no keys"] += 1
        elif keys[0][0] != "PRIMARY":
            no_primary.append(name)

        ot = objs.get(name)
        out = [head, f"# {name} - {desc}",
               f"Module: {modname} | {len(fields)} columns" + (f" | ObjType: {','.join(ot)}" if ot else ""),
               "Indexes (name: columns; first = primary key; U = unique):"]
        for k in keys:
            out.append(f"  {k[0]}{' U' if k[1] == 'Yes' else ''}: {', '.join(k[2])}")
        out.append("Fields (name type(len) description [values] ->parent table):")
        for f_ in fields:
            fname, fdesc, ftype, fsize, frel, fdef, cons = f_
            if ftype == "Num" and re.fullmatch(r"\d+\.\d+", fsize):
                t = f"Num({fsize.replace('.', ',')})"
            else:
                t = f"{ftype}({fsize})" if fsize else ftype
            parts = [f"  {fname} {t}"]
            if fdesc:
                parts.append(fdesc)
            if fdef:
                parts.append(f"default={fdef}")
            if cons:
                parts.append("[" + ", ".join(f"{v}={l}" for v, l in cons) + "]")
            if frel and frel != "-":
                parts.append(f"->{frel}")
            out.append(" ".join(parts))
        ncols += len(fields)
        nkeys += len(keys)
        with open(os.path.join(A.out, "dict", f"{name}.md"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(out) + "\n")
        index_lines.append(f"| {name} | {desc.replace('|', '/')} | {modname} | {len(fields)} | {len(keys)} | "
                           f"{','.join(ot) if ot else ''} |")

missing = sorted(toc_pages - seen)
if missing:
    sys.exit(f"{len(missing)} pages named in the table of contents were not read (first: {missing[:5]})")

index_lines.sort(key=lambda l: l.split("|")[1].strip())
with open(os.path.join(A.out, "table-index.md"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write(f"<!-- source: {A.source}; ObjType from references/objects/object-types.md | version: {A.label} | "
             f"verified: {A.verified} -->\n\n# {A.label} table index\n\n")
    fh.write(f"{len(index_lines)} tables, one line each, sorted by name. Open `dict/<TABLE>.md` for columns, indexes, "
             "valid values and parent-table links. Grep by description or module for topic search.\n\n")
    fh.write("| Table | Description | Module | Cols | Idx | ObjType |\n|---|---|---|---|---|---|\n")
    fh.write("\n".join(index_lines) + "\n")
print(f"{len(index_lines)} tables, {ncols} columns, {nkeys} keys written to {A.out}"
      f" | TOC pages checked: {len(toc_pages)}"
      f" | first key not PRIMARY: {no_primary[:10] or 'none'}" + (f" | {dict(issues)}" if issues else ""))
