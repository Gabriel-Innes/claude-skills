"""Extract *verified view-composition graphs* for the core Sage 300 transaction documents from an
AOM HTML export (SDK 7.0A+ format, e.g. Sage 300 2026 / 7.3A) and write a compact reference the .NET
capability uses to emit correct ACCPAC.Advantage `Compose()` wiring.

The data dictionary build (build_dict_html.py) keeps field/table info but drops the composition tree;
this script keeps only the composition tree, for a curated set of document root views.

Usage:
    python scripts/build_compose_graphs.py <aom-html-folder> references/dotnet/compose-graphs.md
    python scripts/build_compose_graphs.py <aom-html-folder> --probe OE0520   # inspect one view

For each ROOT document view it walks the composition list transitively (same-module views only -
the views an integration actually opens), and emits, per view, its ordered composition slots. Slot
order = the array order for `view.Compose(new View[]{ ... })`. A GENSTUB slot or a cross-module/master
composition is not opened by the integration -> pass `null` in that slot.
"""
import argparse, html, os, re, sys
from collections import OrderedDict

# --- Curated document roots. rotoid -> (module, document name). Verified to exist + be Header-protocol.
#     Extend this list (and re-run) to add a document; see MAINTENANCE.md.
ROOTS = [
    ("OE0520", "OE", "OE Order"),
    ("OE0420", "OE", "OE Invoice"),
    ("OE0240", "OE", "OE Credit/Debit Note"),
    ("OE0692", "OE", "OE Shipment"),
    ("PO0620", "PO", "PO Purchase Order"),
    ("PO0700", "PO", "PO Receipt"),
    ("PO0420", "PO", "PO Invoice"),
    ("PO0731", "PO", "PO Return"),
    ("PO0311", "PO", "PO Credit/Debit Note"),
    ("IC0120", "IC", "IC Adjustment"),
    ("IC0740", "IC", "IC Transfer"),
    ("IC0640", "IC", "IC Inventory Shipment"),
    ("IC0590", "IC", "IC Inventory Receipt"),
    ("IC0288", "IC", "IC Internal Usage"),
    ("AR0031", "AR", "AR Invoice Batch"),
    ("AR0041", "AR", "AR Receipt/Adjustment Batch"),
    ("AP0020", "AP", "AP Invoice Batch"),
    ("AP0030", "AP", "AP Payment/Adjustment Batch"),
    ("GL0008", "GL", "GL Journal Entry Batch"),
]

TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")
def text(s):
    return WS.sub(" ", html.unescape(TAG.sub(" ", s))).strip()

dll_re = re.compile(r"<b>DLL:\s*</b>\s*([A-Z0-9]+)", re.I)
prot_re = re.compile(r"<b>Protocol:\s*</b>([^<]*)<br>", re.I)
tables_re = re.compile(r"<b>Tables:\s*</b>(.*?)<br>", re.I | re.S)
title_re = re.compile(r"<h1>View:\s*([^<]*)</h1>", re.I)
comp_head_re = re.compile(r"<h3>\s*Compositions:\s*\d+\s*</h3>", re.I)
row_re = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
cell_re = re.compile(r"<td[^>]*>(.*?)</td>", re.S)
roto_re = re.compile(r'href="([A-Z]{2}\d{4})\.html"')
tbl_href_re = re.compile(r'href="([A-Z0-9]+)\.html"')


def load_view(src, rotoid):
    """Return dict(rotoid,title,dll,protocol,tables[],comps[(rotoid,table,title,dll)]) or None."""
    p = os.path.join(src, rotoid + ".html")
    if not os.path.exists(p):
        return None
    x = open(p, encoding="utf-8", errors="replace").read()
    if "<h1>View:" not in x:
        return None
    tm = title_re.search(x)
    dm = dll_re.search(x)
    pm = prot_re.search(x)
    tabm = tables_re.search(x)
    tables = tbl_href_re.findall(tabm.group(1)) if tabm else []
    # slice the Compositions table: from the "Compositions:" heading to the next </table>
    comps = []
    hm = comp_head_re.search(x)
    if hm:
        seg = x[hm.end(): x.find("</table>", hm.end())]
        for rowhtml in row_re.findall(seg):
            cells = cell_re.findall(rowhtml)
            if len(cells) < 4:
                continue
            rm = roto_re.search(cells[0])
            if not rm:
                continue
            crot = rm.group(1)
            ctbl_m = tbl_href_re.search(cells[1])
            ctbl = ctbl_m.group(1) if ctbl_m else ""
            comps.append((crot, ctbl, text(cells[2]), text(cells[3])))
    return {
        "rotoid": rotoid,
        "title": text(tm.group(1)) if tm else "",
        "dll": dm.group(1) if dm else "",
        "protocol": text(pm.group(1)) if pm else "",
        "tables": tables,
        "comps": comps,
    }


def probe(src, rotoid):
    v = load_view(src, rotoid)
    if not v:
        print(f"{rotoid}: NOT FOUND / not a view page")
        return
    print(f"{rotoid}  {v['title']}  [dll {v['dll']}; protocol: {v['protocol']}; tables {','.join(v['tables'])}]")
    print(f"  compositions ({len(v['comps'])}):")
    for i, (crot, ctbl, ctitle, cdll) in enumerate(v["comps"]):
        stub = "  <-- GENSTUB (null slot)" if cdll == "GENSTUB" or not crot else ""
        print(f"    [{i}] {crot:<8} {ctbl:<8} {ctitle} (dll {cdll}){stub}")


def is_entry(v):
    """A document entry point (its own root) - Header or Batch protocol."""
    return v and (v["protocol"].startswith("Header") or v["protocol"].startswith("Batch"))

# Posting-time / audit structures are never opened during document entry; exclude from the opened tree.
SKIP_TITLE = re.compile(r"\b(Audit|Posting|Postings)\b", re.I)


def build_graph(src, root, module):
    """BFS the composition closure to the document's own *downward* view tree: same-module views only,
    and never recurse into another document's Header/Batch view (that is a separate document) - except
    directly under the root, so a Batch root can reach the one Header it owns. Returns
    (ordered rotoids in open order, {rotoid: view}, set of opened rotoids)."""
    views = OrderedDict()
    order = []
    queue = [root]                            # BFS of views we open
    seen = {root}
    while queue:
        rid = queue.pop(0)
        v = load_view(src, rid)
        if not v:
            continue
        views[rid] = v
        order.append(rid)
        for crot, _ctbl, _ct, cdll in v["comps"]:
            if not crot or cdll == "GENSTUB" or crot in seen:
                continue
            if crot[:2] != module:            # cross-module master/shared view: not opened
                continue
            child = load_view(src, crot)
            if child is None:
                continue
            # skip another document's entry (Header/Batch) unless we're expanding the root itself
            if rid != root and is_entry(child):
                continue
            # skip posting/audit structures (not part of document entry)
            if SKIP_TITLE.search(child["title"]):
                continue
            seen.add(crot)
            queue.append(crot)
    opened = set(views.keys())
    return order, views, opened


def slot_repr(v, opened):
    """Render a view's composition list as slot tokens for a Compose() array."""
    out = []
    for crot, _ctbl, _ct, cdll in v["comps"]:
        if not crot or cdll == "GENSTUB":
            out.append("-")                    # stub -> null
        elif crot in opened:
            out.append(crot)                   # an opened view -> its View variable
        else:
            out.append(f"{crot}*")             # cross-module/not-opened -> null
    return "[" + ", ".join(out) + "]"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", help="folder of AOM HTML pages (must contain Advantage.html)")
    ap.add_argument("out", nargs="?", help="output markdown file, e.g. references/dotnet/compose-graphs.md")
    ap.add_argument("--probe", metavar="ROTOID", help="print one view's title/protocol/compositions and exit")
    a = ap.parse_args()
    if not os.path.isfile(os.path.join(a.src, "Advantage.html")):
        sys.exit(f"error: {a.src} has no Advantage.html - point at the folder with the <ROTOID>.html pages.")
    if a.probe:
        probe(a.src, a.probe.upper())
        return
    if not a.out:
        ap.error("out is required unless --probe is used")

    blocks, missing = [], []
    for root, module, name in ROOTS:
        order, views, opened = build_graph(a.src, root, module)
        if root not in views:
            missing.append(f"{name} ({root})")
            continue
        h = views[root]
        lines = [f"### {name} - root `{root}` ({module}, verified 7.3A / Sage 300 2026)",
                 f"Header view `{root}` {h['title']} (protocol: {h['protocol']}; tables {', '.join(h['tables'])}).",
                 "",
                 "Open these views (rotoID - main table - title):"]
        for rid in order:
            v = views[rid]
            lines.append(f"  {rid}  {(v['tables'][0] if v['tables'] else ''):<8}  {v['title']}")
        lines += ["",
                  "Compose slots (array order = `Compose(new View[]{...})` order; `-` = GENSTUB -> null; "
                  "`*` = cross-module/master, not opened -> null):"]
        for rid in order:
            lines.append(f"  {rid}: {slot_repr(views[rid], opened)}")
        blocks.append("\n".join(lines))

    with open(a.out, "w", encoding="utf-8") as f:
        f.write("<!-- source: Sage 300 2026 (7.3A) AOM export, view composition lists | "
                "version: 7.3A = Sage 300 2026 | verified: 2026-09-25 -->\n\n")
        f.write("# Sage 300 core transaction documents - verified view-composition graphs\n\n")
        f.write("Machine-extracted from the 7.3A AOM view definitions (the ordered `Compositions` list per "
                "view). Use these to emit correct `OpenView(...)` + `Compose(...)` C# for the core documents "
                "without guessing or macro-recording. Composition of core OE/IC/AR/AP/PO/GL documents is "
                "stable across 7.0A-7.3A; confirm on the client's install if in doubt. For any document NOT "
                "listed here, macro-record the UI (view-api.md section 7).\n\n")
        f.write("How to read a block: open every view in the list, then for each `rotoID: [slots]` line call "
                "that view's `.Compose(new View[]{ ... })` passing, in the given order, the View variable for "
                "each opened rotoID and `null` for every `-` or `*` slot. Verify field names in "
                "`references/dictionary/7.3A/dict/<MODULE>.md`.\n\n")
        f.write("\n\n".join(blocks) + "\n")
        if missing:
            f.write("\n<!-- roots not found in this export (fix ROOTS in build_compose_graphs.py): "
                    + "; ".join(missing) + " -->\n")
    print(f"{len(blocks)} document graphs -> {a.out}"
          + (f"  (MISSING roots: {', '.join(missing)})" if missing else ""))


if __name__ == "__main__":
    main()
