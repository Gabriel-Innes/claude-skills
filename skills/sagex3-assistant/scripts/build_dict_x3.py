"""Compile the Sage X3 table dictionary from Sage's online help into compact, grep-friendly reference
files (maintenance only - never needed at runtime).

Usage:
    python scripts/build_dict_x3.py references/dictionary/V11 --cache <folder outside the repo>
    python scripts/build_dict_x3.py references/dictionary/V11 --cache ... --base https://online-help.sagex3.com/erp/12/en-US/MCD/

Source: the "Table dictionary" pages of the Sage X3 online help (default: V11,
https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm). Four page families are read:
  ATB_0.htm       alphabetical table index: table, V9/V10 change flags, abbreviation, description, module
  <TABLE>.htm     per table: header, keys (name, column expression, duplicates), columns (name, title,
                  dimension, data type, length, local menu, link expression, cancellation, activity code)
  MEN00nnn.htm    local menu nnn: title and its numbered values (the enum behind a type-M column)
  ATY_<code>.htm  data type: internal type and the table it links to (e.g. BPR -> BPARTNER)

Writes <out>/table-index.md, <out>/dict/<Module>.md, <out>/local-menus.md, <out>/data-types.md and a
build-report.json next to the cache. Every fetched page is cached as a file under --cache so re-runs
(and parser fixes) cost no network; keep the cache OUTSIDE the skill folder - the raw vendor pages are
never redistributed, only the facts extracted here.
"""
import argparse, html, json, os, re, sys, time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("out", help="output folder, normally references/dictionary/<version>, e.g. V11")
ap.add_argument("--cache", required=True, help="folder for the raw HTML pages (outside the skill folder)")
ap.add_argument("--base", default="https://online-help.sagex3.com/erp/11/en-US/MCD/",
                help="MCD folder of the online help to read (default: V11 en-US)")
ap.add_argument("--version", default="V11", help="version label written into provenance headers")
ap.add_argument("--workers", type=int, default=8, help="parallel fetches (default 8)")
ap.add_argument("--limit", type=int, default=0, help="only the first N tables (parser testing)")
ap.add_argument("--offline", action="store_true", help="never fetch; use the cache only")
args = ap.parse_args()
OUT, CACHE, BASE = args.out, args.cache, args.base.rstrip("/") + "/"
os.makedirs(os.path.join(OUT, "dict"), exist_ok=True)
os.makedirs(CACHE, exist_ok=True)
TODAY = time.strftime("%Y-%m-%d")

# ----------------------------------------------------------------------------------------------- fetch
UA = "Mozilla/5.0 (compatible; claude-skills dictionary builder; +https://github.com/fdtaljaard/claude-skills)"
failed = {}

def fetch(page):
    """Return the page's HTML (from cache or the web); '' and a note in `failed` when it can't be had."""
    path = os.path.join(CACHE, page)
    if os.path.exists(path):
        return open(path, encoding="utf-8", errors="replace").read()
    if args.offline:
        failed[page] = "not in cache (offline)"
        return ""
    for attempt in range(4):
        try:
            with urlopen(Request(BASE + page, headers={"User-Agent": UA}), timeout=60) as r:
                data = r.read().decode("utf-8", errors="replace")
            with open(path, "w", encoding="utf-8") as f:
                f.write(data)
            return data
        except HTTPError as e:
            if e.code == 404:
                failed[page] = "404"
                return ""
            err = f"HTTP {e.code}"
        except (URLError, TimeoutError, OSError) as e:
            err = str(e)
        time.sleep(1.5 * (attempt + 1))
    failed[page] = err
    return ""

def fetch_all(pages, label):
    pages = [p for p in pages if not os.path.exists(os.path.join(CACHE, p))]
    if not pages or args.offline:
        return
    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for _ in as_completed([ex.submit(fetch, p) for p in pages]):
            done += 1
            if done % 100 == 0 or done == len(pages):
                print(f"  {label}: {done}/{len(pages)} fetched", flush=True)

# ----------------------------------------------------------------------------------------------- parse
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")
TABLE_RE = re.compile(r"<table\b[^>]*>(.*?)</table>", re.S | re.I)
TR_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.S | re.I)
TD_RE = re.compile(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", re.S | re.I)
TH_RE = re.compile(r"<th\b[^>]*>(.*?)</th>", re.S | re.I)
HREF_RE = re.compile(r'href="(?:\.\./MCD/)?([A-Za-z0-9_]+)\.htm"', re.I)
H1_RE = re.compile(r"<h1[^>]*>\s*<span>(.*?)</span>", re.S | re.I)

def text(s):
    s = re.sub(r"</a\s*$", "", s.strip())      # link-expression cells end in an unterminated "</a"
    return WS.sub(" ", html.unescape(TAG.sub(" ", s)).replace("\xa0", " ")).strip()

def tables_by_header(page_html):
    """Yield (list of <th> texts, list of rows, each a list of raw cell html) for each <table> on the page."""
    for t in TABLE_RE.findall(page_html):
        rows = TR_RE.findall(t)
        ths = [text(h) for h in TH_RE.findall(rows[0])] if rows else []
        if not ths:
            continue
        data = [TD_RE.findall(r) for r in rows[1:]]
        yield ths, [r for r in data if r]

# -- index -------------------------------------------------------------------------------------------
print("index ...", flush=True)
idx = fetch("ATB_0.htm")
if not idx:
    sys.exit(f"error: cannot read {BASE}ATB_0.htm ({failed.get('ATB_0.htm')})")
tables = []                     # dicts: name, abbr, desc, module, v9, v10
for ths, rows in tables_by_header(idx):
    if not ths or not ths[0].startswith("Table"):   # header is "Table V11" (the version varies)
        continue
    for cells in rows:
        if len(cells) < 6:
            continue
        m = HREF_RE.search(cells[0])
        name = text(cells[0])
        if not m or m.group(1) != name:
            continue
        # V9 / V10 cells hold a "Modification" link (table changed) or a "New table" image (absent there)
        tables.append(dict(name=name, v9=bool(HREF_RE.search(cells[1])), v10=bool(HREF_RE.search(cells[2])),
                           new9="New table" in cells[1], new10="New table" in cells[2],
                           abbr=text(cells[3]), desc=text(cells[4]), module=text(cells[5]),
                           act=text(cells[6]) if len(cells) > 6 else ""))
seen = set()
tables = [t for t in tables if not (t["name"] in seen or seen.add(t["name"]))]
if args.limit:
    tables = tables[:args.limit]
print(f"  {len(tables)} tables in the index", flush=True)

# -- table pages --------------------------------------------------------------------------------------
fetch_all([t["name"] + ".htm" for t in tables], "tables")

def parse_table(t):
    """Fill t with header (module, activity), keys [(name, expr, dups, act)] and fields [dict]."""
    x = fetch(t["name"] + ".htm")
    t["keys"], t["fields"], t["read"] = [], [], bool(x)
    if not x:
        return
    for ths, rows in tables_by_header(x):
        if ths[:2] == ["Table", "Abbreviation"] and rows:
            c = [text(v) for v in rows[0]]
            if len(c) >= 5:
                # the table page is authoritative: index rows for new tables carry a "New table" image in
                # place of the V9 link and their cells shift, so the index abbreviation can be wrong
                t["abbr"] = c[1] or t["abbr"]
                t["desc"] = c[2] or t["desc"]
                t["module"] = c[3] or t["module"]
                t["act"] = c[4] or t["act"]
        elif ths[:2] == ["Key", "Description"]:
            for cells in rows:
                c = [text(v) for v in cells]
                if len(c) >= 3 and c[0]:
                    t["keys"].append((c[0], c[1], c[2].lower().startswith("y"), c[3] if len(c) > 3 else ""))
        elif ths[:2] == ["Column", "Normal title"]:
            # Column | Normal title | Dim. | Type | Length | Menu | Link expression | Cancellation | Act
            for cells in rows:
                if len(cells) < 9:
                    continue
                c = [text(v) for v in cells]
                if not c[0]:
                    continue
                ty = HREF_RE.search(cells[3])
                mn = re.search(r"MEN0*(\d+)\.htm", cells[5])
                lk = HREF_RE.search(cells[6])
                t["fields"].append(dict(
                    name=c[0], title=c[1], dim=c[2], type=(ty.group(1)[4:] if ty and ty.group(1).startswith("ATY_") else c[3]),
                    length=c[4], menu=(mn.group(1) if mn else c[5]), link=c[6],
                    link_table=(lk.group(1) if lk and not lk.group(1).startswith(("ATY_", "MEN")) else ""),
                    cancel=c[7], act=c[8]))

print("parsing tables ...", flush=True)
for t in tables:
    parse_table(t)
empty = [t["name"] for t in tables if not t["fields"] and not t["read"]]
stubs = [t["name"] for t in tables if not t["fields"] and t["read"]]   # Sage publishes only the header block
print(f"  parsed; {len(stubs)} header-only tables (no column detail published), {len(empty)} pages not read", flush=True)

# -- local menus and data types -----------------------------------------------------------------------
menu_ids = sorted({f["menu"] for t in tables for f in t["fields"] if f["menu"].isdigit()}, key=int)
type_codes = sorted({f["type"] for t in tables for f in t["fields"] if re.fullmatch(r"[A-Z0-9]+", f["type"] or "")})
print(f"  {len(menu_ids)} local menus, {len(type_codes)} data types referenced", flush=True)
fetch_all([f"MEN{int(m):05d}.htm" for m in menu_ids], "menus")
fetch_all([f"ATY_{c}.htm" for c in type_codes], "types")

menus = {}                      # id -> dict(title, values=[(num, text)])
for m in menu_ids:
    x = fetch(f"MEN{int(m):05d}.htm")
    if not x:
        continue
    title, values = "", []
    for ths, rows in tables_by_header(x):
        if ths[:2] == ["Local menu", "Title"] and rows:
            c = [text(v) for v in rows[0]]
            title = c[1] if len(c) > 1 else ""
        elif ths[:2] == ["Number", "Text"]:
            for cells in rows:
                c = [text(v) for v in cells]
                if len(c) >= 2 and c[0]:
                    values.append((c[0], c[1]))
    menus[m] = dict(title=title, values=values)

types = {}                      # code -> dict(name, internal, linked_table)
for code in type_codes:
    x = fetch(f"ATY_{code}.htm")
    if not x:
        continue
    h1 = H1_RE.search(x)
    name = text(h1.group(1)) if h1 else code
    name = re.sub(r"^%s\s*\((.*)\)$" % re.escape(code), r"\1", name) if name.startswith(code) else name
    linked, internal, obj = "", "", ""
    for ths, rows in tables_by_header(x):
        if "Linked table" in ths and rows:
            c = [text(v) for v in rows[0]]
            cols = dict(zip(ths, c))
            obj = cols.get("Linked object", "")
            lt = cols.get("Linked table", "")
            m = HREF_RE.search(rows[0][ths.index("Linked table")])
            linked = m.group(1) if m else (lt.split()[-1] if lt else "")
            # the header has "Linked object", "Linked table" and then blank <th>s; the internal type
            # (Alphanumeric, Decimal, Local menu, Date ...) is the first unlabelled, non-empty column
            internal = next((v for h, v in zip(ths, c) if not h and v), "")
    types[code] = dict(name=name, internal=internal, linked_table=linked, linked_object=obj)

# ----------------------------------------------------------------------------------------------- write
SRC_NOTE = (f"<!-- source: {BASE}ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 {args.version} "
            f"online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 {args.version} "
            f"| verified: {TODAY} -->")

MODULE_FILE = {  # module name as shown in the help -> dict/ file stem
    "Sales": "Sales", "Purchasing": "Purchasing", "Stock": "Stock", "Common Data": "Common-Data",
    "Financials": "Financials", "A/P-A/R accounting": "AP-AR-accounting", "Manufacturing": "Manufacturing",
    "Supervisor": "Supervisor", "Development": "Development", "Fixed Assets": "Fixed-Assets",
    "Human Resources administration": "HR-administration", "Human Capital management": "HCM",
    "CRM activities": "CRM", "Help Desk": "Help-Desk",
}
def module_file(module):
    return MODULE_FILE.get(module) or re.sub(r"[^A-Za-z0-9]+", "-", module).strip("-") or "Other"

def menu_inline(mid):
    m = menus.get(mid)
    if not m:
        return f"[menu {mid}]"
    vals = m["values"]
    if len(vals) <= 15 and sum(len(v[1]) for v in vals) <= 220:
        return f"[menu {mid}: " + ",".join(f"{n}={v}" for n, v in vals) + "]"
    return f"[menu {mid}: {len(vals)} values, see local-menus.md]"

def field_line(f):
    ty = f["type"] or "?"
    if f["length"]:
        ty += "*" + f["length"]
    if f["dim"]:
        ty += f"({f['dim']})"
    parts = [f["name"], ty, f["title"]]
    if f["menu"].isdigit():
        parts.append(menu_inline(f["menu"]))
    elif not f["link"] and f["type"] in types and types[f["type"]]["linked_table"]:
        parts.append(f"-> {types[f['type']]['linked_table']}")   # type-level link only when no explicit one
    if f["link"]:
        tgt = f" ({f['link_table']})" if f["link_table"] else ""
        parts.append(f"-> {f['link']}{tgt}")
    if f["cancel"]:
        parts.append(f"!{f['cancel']}")
    if f["act"]:
        parts.append(f"act:{f['act']}")
    return "  " + " ".join(p for p in parts if p)

by_module = defaultdict(list)
for t in tables:
    by_module[t["module"] or "Other"].append(t)

for module, ts in sorted(by_module.items()):
    fn = os.path.join(OUT, "dict", module_file(module) + ".md")
    with open(fn, "w", encoding="utf-8", newline="\n") as f:
        f.write(SRC_NOTE + "\n")
        f.write(f"# {module} module - Sage X3 {args.version} table dictionary\n\n")
        f.write("Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, "
                "`(D)` = duplicates allowed) with their column expression; then one field per line: "
                "`NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. "
                "`(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the "
                "dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. "
                "Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.\n\n")
        for t in sorted(ts, key=lambda t: t["name"]):
            flags = []
            if t["act"]:
                flags.append(f"activity code {t['act']}")
            if t["new9"]:
                flags.append("not in V9.0 P12 (new table)")
            elif t["v9"]:
                flags.append(f"differs in V9.0 P12 (diff: AT3_{t['name']}.htm)")
            if t["new10"]:
                flags.append("not in V10 P1 (new table)")
            elif t["v10"]:
                flags.append(f"differs in V10 P1 (diff: ATD_{t['name']}.htm)")
            f.write(f"## {t['name']} ({t['abbr']}) - {t['desc']}\n")
            if flags:
                f.write("Notes: " + "; ".join(flags) + "\n")
            if t["keys"]:
                f.write("Keys (first = PK; D = duplicates allowed): " + "; ".join(
                    f"{k} {expr}" + (" (D)" if dups else "") for k, expr, dups, _ in t["keys"]) + "\n")
            if t["fields"]:
                f.write("Fields:\n")
                for fl in t["fields"]:
                    f.write(field_line(fl) + "\n")
            elif t["read"]:
                f.write("Fields: (Sage publishes no key or column detail for this table in this version's help - "
                        "read the structure from the client's folder)\n")
            else:
                f.write(f"Fields: (page not read - fetch {BASE}{t['name']}.htm)\n")
            f.write("\n")

with open(os.path.join(OUT, "table-index.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(SRC_NOTE + "\n")
    f.write(f"# Sage X3 {args.version} table index\n\n")
    f.write("Format: `TABLE` (ABBREVIATION) - description. Grouped by the module the dictionary assigns. Field details, keys, "
            "enum values and join links: read the table's entry in `dict/<Module>.md` (file named after the module heading "
            "below). Version marks, from Sage's own V9.0 P12 / V10 P1 columns: `+` = new table, absent from at least one "
            "of those versions; `*` = exists there but differs (Sage publishes the per-version difference at "
            "`AT3_<TABLE>.htm` (V9) / `ATD_<TABLE>.htm` (V10) under the same help folder). The table's `Notes:` line "
            "in `dict/` says which version.\n\n")
    for module, ts in sorted(by_module.items()):
        f.write(f"## {module} ({len(ts)} tables) - dict/{module_file(module)}.md\n\n")
        for t in sorted(ts, key=lambda t: t["name"]):
            mark = "+" if (t["new9"] or t["new10"]) else "*" if (t["v9"] or t["v10"]) else ""
            f.write(f"- `{t['name']}`{mark} ({t['abbr']}) - {t['desc']}\n")
        f.write("\n")

with open(os.path.join(OUT, "local-menus.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(SRC_NOTE + "\n")
    f.write(f"# Sage X3 {args.version} local menus (enum values)\n\n")
    f.write("Every local menu referenced by a type-M column in `dict/`. Format: `menu N - title: value=text, ...`. "
            "The stored value is the number; `[menu N: ...]` on a field line in `dict/` is this list inlined when short. "
            "Local menus are customizable per folder - confirm on the client's system before relying on a value that "
            "matters.\n\n")
    for mid in menu_ids:
        m = menus.get(mid)
        if not m:
            f.write(f"- menu {mid} - (page not read)\n")
            continue
        f.write(f"- menu {mid} - {m['title']}: " + ", ".join(f"{n}={v}" for n, v in m["values"]) + "\n")

with open(os.path.join(OUT, "data-types.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(SRC_NOTE + "\n")
    f.write(f"# Sage X3 {args.version} data types\n\n")
    f.write("Every data type referenced by a column in `dict/`. Format: `CODE - name | internal type | linked table`. "
            "The internal type decides the SQL storage (see `../conventions.md`); the linked table is the table a column "
            "of this type points at (its control table / foreign key), used when a field has no explicit link expression.\n\n")
    for code in type_codes:
        ty = types.get(code)
        if not ty:
            f.write(f"- {code} - (page not read)\n")
            continue
        f.write(f"- {code} - {ty['name']} | {ty['internal'] or '?'} | {ty['linked_table'] or '-'}"
                + (f" ({ty['linked_object']})" if ty['linked_object'] else "") + "\n")

report = dict(version=args.version, base=BASE, date=TODAY, tables=len(tables),
              tables_with_columns=len(tables) - len(stubs) - len(empty), header_only_tables=stubs,
              tables_not_read=empty, fields=sum(len(t["fields"]) for t in tables),
              keys=sum(len(t["keys"]) for t in tables), local_menus=len(menu_ids), data_types=len(type_codes),
              new_since_v9=sum(t["new9"] for t in tables), changed_vs_v9=sum(t["v9"] for t in tables),
              new_since_v10=sum(t["new10"] for t in tables), changed_vs_v10=sum(t["v10"] for t in tables),
              modules={m: len(ts) for m, ts in sorted(by_module.items())},
              failed_fetches=failed)
with open(os.path.join(CACHE, "build-report.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2)
print(json.dumps({k: v for k, v in report.items() if k not in ("header_only_tables", "tables_not_read", "failed_fetches")}, indent=2))
print(f"  failed fetches: {len(failed)}; header-only tables: {len(stubs)}; pages not read: {len(empty)}"
      f"  (details in {CACHE}/build-report.json)")
