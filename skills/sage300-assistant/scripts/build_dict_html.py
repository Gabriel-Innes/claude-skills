"""Compile a Sage 300 AOM *HTML* export (SDK 7.0A+ format, e.g. Sage 300 2023) into the same
compact per-module reference files and table index that build_dict.py / build_index.py produce
from the older XML export.

Usage:
    python scripts/build_dict_html.py <aom-html-folder> references/dictionary/<version>

Writes <out>/dict/<MODULE>.md and <out>/table-index.md.
"""
import argparse, html, os, re, sys
from collections import defaultdict

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("src", help="folder of AOM HTML pages (<TABLE>.html, <ROTOID>.html, Advantage.html); "
                            "some zips nest it one level down (e.g. AOM/ or AOM.2025.1/)")
ap.add_argument("out", help="output folder, normally references/dictionary/<AOM version>, e.g. 7.3A")
args = ap.parse_args()
SRC, OUT = args.src, args.out
if not os.path.isfile(os.path.join(SRC, "Advantage.html")):
    sys.exit(f"error: {SRC} has no Advantage.html - point at the folder that directly contains the "
             f"<TABLE>.html pages (the zip may nest it one level down). For an XML export use build_dict.py.")
os.makedirs(os.path.join(OUT, "dict"), exist_ok=True)

TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")
def text(s):
    return WS.sub(" ", html.unescape(TAG.sub(" ", s))).strip()

h1_re = re.compile(r"<h1>Table: ([^<]*)</h1>")
tbl_re = re.compile(r"<b>Table: </b>([A-Z0-9]+)<br>")
view_re = re.compile(r'<b>View: </b><a href="([A-Z]{2}\d{4})\.html"')
row_re = re.compile(r"<tr valign=\"top\" align=\"left\">(.*?)</tr>", re.S)
cell_re = re.compile(r"<td[^>]*>(.*?)</td>", re.S)
enum_re = re.compile(r'<td align="right">(-?\d+)</td>\s*<td>=</td>\s*<td[^>]*>([^<]*)</td>')
anchor_re = re.compile(r'<a name="([A-Z0-9]+)">')
phys_re = re.compile(r"<b>Tables: </b>(.*?)<br>", re.S)

# view page -> physical table list (split tables)
phys_cache = {}
def phys_tables(rotoid):
    if rotoid not in phys_cache:
        p = os.path.join(SRC, rotoid + ".html")
        phys_cache[rotoid] = []
        if os.path.exists(p):
            m = phys_re.search(open(p, encoding="utf-8", errors="replace").read())
            if m:
                phys_cache[rotoid] = re.findall(r'href="([A-Z0-9]+)\.html"', m.group(1))
    return phys_cache[rotoid]

ROW_START = '<tr valign="top" align="left">'
def parse_rows(section):
    """Yield the list of cells (raw html) per data row. Rows are split on the row-start marker
    rather than </tr>, because enum lists are nested <table>s inside the 4th cell."""
    for chunk in section.split(ROW_START)[1:]:
        cells = cell_re.findall(chunk)          # first three cells are flat
        if cells:
            yield cells[:3] + [chunk]           # 4th element: whole chunk (holds enum table if any)

modules, index = defaultdict(list), defaultdict(list)
count = 0
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".html"):
        continue
    x = open(os.path.join(SRC, fn), encoding="utf-8", errors="replace").read()
    tm = tbl_re.search(x)
    if not tm or "<h1>Table:" not in x or tm.group(1) != fn[:-5]:
        continue
    tname = tm.group(1)
    tdesc = text(h1_re.search(x).group(1)) if h1_re.search(x) else ""
    vm = view_re.search(x)
    rotoid = vm.group(1) if vm else ""
    phys = phys_tables(rotoid) if rotoid else []

    lines = [f"## {tname} - {tdesc}" + (f" (view {rotoid})" if rotoid else "")]
    if len(phys) > 1:
        lines.append(f"Physical tables of this view: {', '.join(phys)} (join 1:1 on the primary key)")

    # split page into Keys section and Fields section
    ki, fi = x.find("<h3>Keys"), x.find("<h3>Fields")
    keys_html = x[ki:fi] if ki >= 0 and fi > ki else ""
    fields_html = x[fi:] if fi >= 0 else ""

    keys = []
    for cells in parse_rows(keys_html):
        if len(cells) < 3:
            continue
        flags = sorted(set(re.findall(r'title="(?:Duplicates|Modifiable)">([DM])</a>', cells[1])))
        kf = "+".join(re.findall(r'href="#([A-Z0-9]+)"', cells[2]))
        if kf:
            keys.append(kf + (f" [{','.join(flags)}]" if flags else ""))
    if keys:
        lines.append("Keys (first = PK; D=dups allowed, M=modifiable): " + "; ".join(keys))

    lines.append("Fields (NAME type description [values]):")
    for cells in parse_rows(fields_html):
        if len(cells) < 3:
            continue
        am = anchor_re.search(cells[0])
        if not am:
            continue
        fname, ftype, fdesc = am.group(1), text(cells[1]), text(cells[2])
        line = f"  {fname} {ftype} {fdesc}".rstrip()
        if len(cells) > 3:
            vals = enum_re.findall(cells[3])
            if vals:
                line += " [" + ",".join(f"{i}={html.unescape(v).strip()}" for i, v in vals) + "]"
        lines.append(line)

    modules[tname[:2]].append("\n".join(lines))
    index[tname[:2]].append(f"- `{tname}` - {tdesc}" + (f" ({rotoid})" if rotoid else ""))
    count += 1

# module titles from the module landing pages (AP.html etc.), fall back to code
def module_title(mod):
    p = os.path.join(SRC, mod + ".html")
    if os.path.exists(p):
        m = re.search(r"<title>([^<]*)</title>", open(p, encoding="utf-8", errors="replace").read())
        if m:
            return text(m.group(1))
    return mod

for mod, blocks in modules.items():
    with open(os.path.join(OUT, "dict", mod + ".md"), "w", encoding="utf-8") as f:
        f.write(f"# {mod} module - compiled AOM dictionary\n\n")
        f.write("\n\n".join(blocks) + "\n")

with open(os.path.join(OUT, "table-index.md"), "w", encoding="utf-8") as f:
    f.write("# Sage 300 AOM table index\n\n")
    f.write("Format: `TABLE` - description (view rotoid). Field details, keys and enum values: read the "
            "table's entry in `dict/<MODULE>.md` (module = first two letters of the table name).\n\n")
    for mod in sorted(index):
        f.write(f"## {mod} - {module_title(mod)}\n\n" + "\n".join(index[mod]) + "\n\n")

print(f"{count} tables across {len(modules)} modules -> {OUT}")
