"""Compile a Sage 300 AOM *XML* export (pre-2023 SDKs, e.g. AOM60) into compact per-module
reference files: <out>/<MODULE>.md, one block per table with keys, fields and inline enum values.

Usage:
    python scripts/build_dict.py <aom-xml-folder> references/dictionary/<version>/dict

Pair with build_index.py for the table index. For 2023+ HTML exports use build_dict_html.py instead.
Maintenance tool only - never needed to answer a user request. No dependencies beyond the stdlib.
"""
import argparse, re, os, sys
from collections import defaultdict

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("src", help="folder of AOM XML pages (<TABLE>.xml, <ROTOID>.xml)")
ap.add_argument("out", help="output folder, normally references/dictionary/<version>/dict")
args = ap.parse_args()
SRC, OUT = args.src, args.out
if not os.path.isdir(SRC):
    sys.exit(f"error: {SRC} is not a folder. Expected the unzipped AOM XML export (contains e.g. OEORDH.xml).")
if not any(f.endswith(".xml") for f in os.listdir(SRC)):
    sys.exit(f"error: no .xml files in {SRC}. For an HTML export (2023+) use scripts/build_dict_html.py.")
os.makedirs(OUT, exist_ok=True)

table_re = re.compile(r'<table name="([A-Z0-9]+)" desc="([^"]*)">')
view_re = re.compile(r'<view name="([A-Z]{2}\d{4})"')
field_re = re.compile(
    r"<field>\s*<fieldname>([A-Z0-9]+)</fieldname>\s*"
    r"(?:<fieldindex>\d+</fieldindex>\s*)?"
    r"<fieldtype>([^<]*)</fieldtype>\s*<fielddesc>([^<]*)</fielddesc>", re.S)
key_re = re.compile(r"<key>\s*<keytitle>([^<]*)</keytitle>.*?<keyfieldlist>\s*(.*?)</keyfieldlist>", re.S)
keyfield_re = re.compile(r"<keyfield>([A-Z0-9]+)</keyfield>")
keyflag_re = re.compile(r'keyflag type="Key" value="([A-Z])"')
present_block_re = re.compile(
    r"<fieldname>([A-Z0-9]+)</fieldname>.*?(?:<fieldpresentlist>(.*?)</fieldpresentlist>|</field>)", re.S)
present_re = re.compile(r'index="(-?\d+)" value="([^"]*)"')
tablelist_re = re.compile(r"<tablelist>(.*?)</tablelist>", re.S)

# cache rotoid pages: rotoid -> {fieldname: "1=Active,2=Future"}
roto_cache = {}
def roto_enums(rotoid):
    if rotoid in roto_cache:
        return roto_cache[rotoid]
    enums, phys = {}, []
    p = os.path.join(SRC, rotoid + ".xml")
    if os.path.exists(p):
        x = open(p, encoding="utf-8", errors="replace").read()
        tl = tablelist_re.search(x)
        if tl:
            phys = re.findall(r'<table name="([A-Z0-9]+)"', tl.group(1))
        for m in present_block_re.finditer(x):
            if m.group(2):
                vals = present_re.findall(m.group(2))
                if vals:
                    enums[m.group(1)] = ",".join(f"{i}={v}" for i, v in vals)
    roto_cache[rotoid] = (enums, phys)
    return roto_cache[rotoid]

modules = defaultdict(list)
count = 0
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".xml"):
        continue
    base = fn[:-4]
    x = open(os.path.join(SRC, fn), encoding="utf-8", errors="replace").read()
    if "<recordlength>" not in x:
        continue
    tm = table_re.search(x)
    if not tm or tm.group(1) != base:
        continue
    tname, tdesc = tm.groups()
    vm = view_re.search(x)
    rotoid = vm.group(1) if vm else ""
    enums, phys = roto_enums(rotoid) if rotoid else ({}, [])

    lines = [f"## {tname} - {tdesc}" + (f" (view {rotoid})" if rotoid else "")]
    if len(phys) > 1:
        lines.append(f"Physical tables of this view: {', '.join(phys)} (join 1:1 on the primary key)")
    keys = []
    for km in key_re.finditer(x):
        flags = set(keyflag_re.findall(km.group(0)))
        kf = "+".join(keyfield_re.findall(km.group(2)))
        suffix = "" if not flags else " [" + ",".join(sorted(flags)) + "]"
        keys.append(kf + suffix)
    if keys:
        lines.append("Keys (first = PK; D=dups allowed, M=modifiable): " + "; ".join(keys))
    lines.append("Fields (NAME type description [values]):")
    for fname, ftype, fdesc in field_re.findall(x):
        e = enums.get(fname)
        lines.append(f"  {fname} {ftype} {fdesc}".rstrip() + (f" [{e}]" if e else ""))
    modules[base[:2]].append("\n".join(lines))
    count += 1

for mod, blocks in modules.items():
    with open(os.path.join(OUT, mod + ".md"), "w", encoding="utf-8") as f:
        f.write(f"# {mod} module - compiled AOM dictionary\n\n")
        f.write("Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; "
                "Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.\n\n")
        f.write("\n\n".join(blocks) + "\n")
print(f"Compiled {count} tables into {len(modules)} module files in {OUT}")
