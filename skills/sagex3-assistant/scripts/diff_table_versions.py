"""Compare one Sage X3 table's dictionary definition between two help versions (e.g. V11 and V12) and list the
columns and keys that were added, removed or changed - the evidence for "will this view break after the upgrade".

Usage:
    python scripts/diff_table_versions.py SORDER                 # V11 -> V12 (defaults)
    python scripts/diff_table_versions.py SORDER SORDERQ --from 11 --to 12
    python scripts/diff_table_versions.py BPCUSTOMER --to-url https://online-help.sagex3.com/erp/12/fr-fr/Content/MCD/

Reads the public table pages of Sage's online help (same pages the bundled dictionary is compiled from):
    V11: https://online-help.sagex3.com/erp/11/en-US/MCD/<TABLE>.htm
    V12: https://online-help.sagex3.com/erp/12/en-us/Content/MCD/<TABLE>.htm
A page that does not exist in one version means the table is absent there. The V12 help documents the current
V12 release only (no per-patch history); for the patch that changed a table, see the "Tables whose dictionary
definition changed" section of references/release-notes/<release>.md. Needs only the Python standard library and
internet access; nothing is written.
"""
import argparse, html, re, sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

VERSION_URLS = {"11": "https://online-help.sagex3.com/erp/11/en-US/MCD/",
                "12": "https://online-help.sagex3.com/erp/12/en-us/Content/MCD/"}
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("tables", nargs="+", help="table names, e.g. SORDER BPCUSTOMER")
ap.add_argument("--from", dest="src", default="11", help="source version (11 or 12), default 11")
ap.add_argument("--to", dest="dst", default="12", help="target version (11 or 12), default 12")
ap.add_argument("--from-url", help="explicit MCD folder URL for the source instead of --from")
ap.add_argument("--to-url", help="explicit MCD folder URL for the target instead of --to")
args = ap.parse_args()
SRC = args.from_url or VERSION_URLS.get(args.src) or sys.exit(f"unknown version {args.src}; use --from-url")
DST = args.to_url or VERSION_URLS.get(args.dst) or sys.exit(f"unknown version {args.dst}; use --to-url")
UA = "Mozilla/5.0 (compatible; claude-skills table diff; +https://github.com/fdtaljaard/claude-skills)"

TAG, WS = re.compile(r"<[^>]+>"), re.compile(r"\s+")
TABLE_RE = re.compile(r"<table\b[^>]*>(.*?)</table>", re.S | re.I)
TR_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.S | re.I)
TD_RE = re.compile(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", re.S | re.I)
TH_RE = re.compile(r"<th\b[^>]*>(.*?)</th>", re.S | re.I)
HREF_RE = re.compile(r'href="(?:\.\./MCD/)?([A-Za-z0-9_]+)\.htm"', re.I)

def text(s):
    s = re.sub(r"</a\s*$", "", s.strip())
    return WS.sub(" ", html.unescape(TAG.sub(" ", s)).replace("\xa0", " ")).strip()

def fetch(base, table):
    try:
        with urlopen(Request(f"{base}{table}.htm", headers={"User-Agent": UA}), timeout=60) as r:
            return r.read().decode("utf-8", errors="replace")
    except HTTPError as e:
        if e.code == 404:
            return None
        raise

def parse(page):
    """Return (header dict, keys {name: (expr, dups)}, columns {name: (type, length, dim, menu, link, title)})."""
    header, keys, cols = {}, {}, {}
    for t in TABLE_RE.findall(page):
        rows = TR_RE.findall(t)
        ths = [text(h) for h in TH_RE.findall(rows[0])] if rows else []
        data = [TD_RE.findall(r) for r in rows[1:]]
        if ths[:2] == ["Table", "Abbreviation"] and data:
            c = [text(v) for v in data[0]]
            header = dict(zip(["table", "abbr", "desc", "module", "act"], c))
        elif ths[:2] == ["Key", "Description"]:
            for cells in data:
                c = [text(v) for v in cells]
                if len(c) >= 3 and c[0]:
                    keys[c[0]] = (c[1], c[2].lower().startswith("y"))
        elif ths[:2] == ["Column", "Normal title"]:
            for cells in data:
                if len(cells) < 9:
                    continue
                c = [text(v) for v in cells]
                if not c[0]:
                    continue
                ty = HREF_RE.search(cells[3]); mn = re.search(r"MEN0*(\d+)\.htm", cells[5])
                link = re.sub(r"\s*=\s*", "=", c[6])      # V11 writes "BPR0 =[SOH]…", V12 "BPR0=[SOH]…"
                cols[c[0]] = (ty.group(1)[4:] if ty and ty.group(1).startswith("ATY_") else c[3], c[4], c[2],
                              mn.group(1) if mn else c[5], link, c[1])
    return header, keys, cols

def fmt(col):
    ty, ln, dim, menu, link, title = col
    s = ty + (f"*{ln}" if ln else "") + (f"({dim})" if dim else "")
    if menu: s += f" menu {menu}"
    if link: s += f" -> {link}"
    return s

exit_code = 0
for table in args.tables:
    table = table.upper()
    a, b = fetch(SRC, table), fetch(DST, table)
    print(f"\n=== {table}: {args.src if not args.from_url else SRC} -> {args.dst if not args.to_url else DST} ===")
    if a is None or b is None:
        print(f"  {'source' if a is None else 'target'} page not found - the table does not exist in that version's help"
              f" ({SRC if a is None else DST}{table}.htm)")
        exit_code = 1
        continue
    ha, ka, ca = parse(a); hb, kb, cb = parse(b)
    if not ca and not cb:
        print("  neither page lists columns (Sage publishes no detail for this table); compare on the databases")
        continue
    if ha.get("desc") != hb.get("desc") or ha.get("abbr") != hb.get("abbr"):
        print(f"  header: {ha.get('abbr')} '{ha.get('desc')}' -> {hb.get('abbr')} '{hb.get('desc')}'")
    added = sorted(set(cb) - set(ca)); removed = sorted(set(ca) - set(cb))
    changed = sorted(n for n in set(ca) & set(cb) if ca[n][:5] != cb[n][:5])
    print(f"  columns: {len(ca)} -> {len(cb)}; added {len(added)}, removed {len(removed)}, changed {len(changed)}")
    for n in added:   print(f"    + {n} {fmt(cb[n])}  {cb[n][5]}")
    for n in removed: print(f"    - {n} {fmt(ca[n])}  {ca[n][5]}")
    for n in changed: print(f"    ~ {n} {fmt(ca[n])}  ->  {fmt(cb[n])}")
    kadd = sorted(set(kb) - set(ka)); krem = sorted(set(ka) - set(kb))
    kchg = sorted(k for k in set(ka) & set(kb) if ka[k] != kb[k])
    if kadd or krem or kchg:
        print(f"  keys: added {kadd}, removed {krem}, changed {kchg}")
        for k in kchg: print(f"    ~ {k}: {ka[k][0]}{' (D)' if ka[k][1] else ''} -> {kb[k][0]}{' (D)' if kb[k][1] else ''}")
    else:
        print(f"  keys: unchanged ({len(ka)})")
    if not (added or removed or changed or kadd or krem or kchg):
        print("  no dictionary difference between the two versions' help pages")
sys.exit(exit_code)
