"""Build the one-line-per-table index (table-index.md) from a Sage 300 AOM *XML* export.

Usage:
    python scripts/build_index.py <aom-xml-folder> references/dictionary/<version>/table-index.md

Companion to build_dict.py (XML exports only; build_dict_html.py writes both files for HTML exports).
Maintenance tool only. Stdlib only.
"""
import argparse, re, os, sys
from collections import defaultdict

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("src", help="folder of AOM XML pages")
ap.add_argument("out", help="output file, normally references/dictionary/<version>/table-index.md")
args = ap.parse_args()
SRC, OUT = args.src, args.out
if not os.path.isdir(SRC):
    sys.exit(f"error: {SRC} is not a folder. Expected the unzipped AOM XML export.")
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)

MODULE_NAMES = {}
tables = defaultdict(list)  # module -> [(table, desc, view)]

table_re = re.compile(r'<table name="([A-Z0-9]+)" desc="([^"]*)">')
view_re = re.compile(r'<view name="([A-Z]{2}\d{4})"')
app_re = re.compile(r'<application name="([^"]+)"')

for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".xml"):
        continue
    base = fn[:-4]
    path = os.path.join(SRC, fn)
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            head = f.read(4000)
    except OSError:
        continue
    # module index page
    m = app_re.search(head)
    if m and re.fullmatch(r"[A-Z]{2}", base):
        MODULE_NAMES[base] = m.group(1)
        continue
    # table page: has <recordlength> and a <table name=...> element
    if "<recordlength>" not in head:
        continue
    tm = table_re.search(head)
    if not tm:
        continue
    tname, tdesc = tm.groups()
    if tname != base:  # only index the canonical table page
        continue
    vm = view_re.search(head)
    view = vm.group(1) if vm else ""
    module = base[:2]
    tables[module].append((tname, tdesc, view))

with open(OUT, "w", encoding="utf-8") as f:
    f.write("# Sage 300 AOM table index\n\n")
    f.write("Format: `TABLE` - description (view rotoid). ")
    f.write("Field details: read `<TABLE>.xml`; enum values & compositions: read `<rotoid>.xml`.\n")
    for module in sorted(tables):
        name = MODULE_NAMES.get(module, module)
        f.write(f"\n## {module} - {name}\n\n")
        for tname, tdesc, view in tables[module]:
            v = f" ({view})" if view else ""
            f.write(f"- `{tname}` - {tdesc}{v}\n")

count = sum(len(v) for v in tables.values())
print(f"Indexed {count} tables across {len(tables)} modules -> {OUT}")
print("Modules:", ", ".join(f"{m}={MODULE_NAMES.get(m,'?')}" for m in sorted(tables)))
