#!/usr/bin/env python3
"""Compile SAP Business One's DI API reference from the shipped REFDI.chm (maintenance only).

Step 0 (manual, Windows): copy REFDI.chm to a path without spaces and decompile it:
    hh.exe -decompile <extractdir> REFDI.chm
(`<SDK folder>\\Help\\REFDI.chm`, e.g. C:\\Program Files (x86)\\SAP\\SAP Business One SDK\\Help). 7-Zip also
extracts CHMs. The result is ~21,000 flat .html files plus DI_API.hhc (table of contents).

Step 1: python build_diapi_ref.py <extractdir> <out> --verified YYYY-MM-DD

Writes, under <out>:
  api/INDEX.md         one line per class (kind, member counts, source table, file/line/lines, first sentence)
  api/classes-NN.md    classes in alphabetical order, ~150 KB per file; each starts `# Class (Kind)`: description,
                       object-model/remarks, properties, methods, events
  enums/INDEX.md       one line per enumeration (member count, file/line/lines, first sentence)
  enums/enums-NN.md    enumerations, ~90 KB per file; each starts `# Enum (Enumeration)`: description + member table

The skill must stay under 200 files, hence the bundles; the INDEX files say where each entry is.

Structure of the CHM (Doc-O-Matic): DI_API.hhc nests Objects -> class -> Methods/Properties/Events -> member
pages (SAPbobsCOM~<Class>~<Member>.html); Enumerations -> SAPbobsCOM~Enumerations~<Enum>_EN.html. Every page is
a stack of `<h1 class="heading">Title</h1><div id="...Section">` blocks, parsed generically. Only the Visual
Basic syntax is shipped. Examples come from each page's Example section (C# preferred, else VB tagged as such);
the separate *_Sample_E.html sample pages are not read.
"""
import argparse, html, json, os, re, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bundle_util

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("extract")
ap.add_argument("out")
ap.add_argument("--verified", required=True)
ap.add_argument("--label", default="SAP Business One DI API 10.0 (10.00.190)")
ap.add_argument("--max-bytes", type=int, default=150_000, help="class bundle size")
ap.add_argument("--max-bytes-enums", type=int, default=90_000, help="enumeration bundle size")
A = ap.parse_args()
EX, OUT = A.extract, A.out
HEAD = f"<!-- source: REFDI.chm, {A.label} | version: DI API 10.0 | verified: {A.verified} -->"

CAP_CLASS, CAP_MEMBER, CAP_REMARK, CAP_EXAMPLE = 6000, 700, 2600, 3500


# ----------------------------------------------------------------- html helpers ---
def read(local):
    try:
        return open(os.path.join(EX, local), encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


def sections(h):
    out = {}
    for p in re.split(r'<h1 class="heading">', h)[1:]:
        title = re.sub(r"<[^>]+>", "", p.split("</h1>", 1)[0]).strip()
        out[title] = p.split("</h1>", 1)[1] if "</h1>" in p else ""
    return out


def text(h, cap=None):
    h = re.sub(r"<(script|style).*?</\1>", "", h, flags=re.S | re.I)
    h = re.sub(r"</?(P|DIV|BR|TR|DT|DD|UL|OL|TABLE)[^>]*>", "\n", h, flags=re.I)
    h = re.sub(r"<LI[^>]*>", "\n- ", h, flags=re.I)
    h = re.sub(r"</TD>|</TH>", " | ", h, flags=re.I)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h).replace("\ufeff", "").replace("\xa0", " ")
    lines = [re.sub(r"[ \t]+", " ", l).strip(" |") .strip() for l in h.split("\n")]
    lines = [l for l in lines if l and l != "-"]
    t = " ".join(lines)
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"\[Missing <\w+>[^\]]*\]", "", t)
    if cap and len(t) > cap:
        t = t[:cap].rsplit(" ", 1)[0] + " […]"
    return t


def vb_syntax(h):
    m = re.search(r'<PRE CLASS="syntax" LANG="VB">(.*?)</PRE>', h, re.S | re.I)
    if not m:
        return "", None
    raw = m.group(1)
    enum = re.search(r'ByVal[^<]*<i><a[^>]*>[^<]*</a></i> As <a href="SAPbobsCOM~Enumerations~(\w+?)_EN\.html"', raw, re.I)
    s = re.sub(r"<[^>]+>", "", raw)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"\s*_\s*\n", " ", s)
    s = re.sub(r"\s+", " ", s).replace("( ", "(").replace(" )", ")").strip()
    return s, (enum.group(1) if enum else None)


VB_MARK = re.compile(r"^\s*(Dim |End (If|Sub|Function|Try)\b|Next\b|Set \w+ ?=|Sub |Function |Private |Public |Call )|\bThen\s*$|^\s*'", re.M)


def _code_blocks(h, lang):
    blocks = []
    for m in re.finditer(r'<CODE Class="%s">(.*?)</CODE>' % lang, h, re.S | re.I):
        c = re.sub(r"<BR\s*/?>", "\n", m.group(1), flags=re.I)
        c = html.unescape(re.sub(r"<[^>]+>", "", c)).replace("\xa0", " ").replace("﻿", "")
        c = "\n".join(l.rstrip() for l in c.split("\n")).strip("\n")
        c = re.sub(r"\n{3,}", "\n\n", c)
        if c.strip() and c not in blocks:
            blocks.append(c)
    return blocks


def example_lines(h, indent):
    """Example section -> markdown lines. C# examples are kept; where a page has no C# sample, its Visual
    Basic sample is kept and tagged as VB (SAP's canonical pattern, to translate - not to paste)."""
    pre = re.split(r"<DIV class=LanguageSpecific", h, maxsplit=1, flags=re.I)[0]
    inner = re.search(r"id=Example_(?:CS|VB)>(.*?)<table", h, re.S | re.I)
    intro = text(pre + " " + (inner.group(1) if inner else ""), 500)
    cs = _code_blocks(h, "CS")
    blocks = [(c, "cs") for c in cs] if cs else [(c, "vb-only") for c in _code_blocks(h, "VB")]
    out = []
    for n, (c, how) in enumerate(blocks):
        if intro and n == 0:
            out.append(f"{indent}- example note: {intro}")
        if len(c) > CAP_EXAMPLE:
            c = c[:CAP_EXAMPLE].rsplit("\n", 1)[0] + "\n// ... (truncated)"
        # SAP's help labels a few Visual Basic samples as C#; tag them by their content so they aren't pasted as C#
        is_vb = how == "vb-only" or (bool(VB_MARK.search(c)) and not (re.search(r";\s*$", c, re.M) or "{" in c))
        if how == "vb-only":
            out.append(f"{indent}- VB example (SAP provides no C# sample for this - translate, don't paste):")
        elif is_vb:
            out.append(f"{indent}- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):")
        else:
            out.append(f"{indent}- C# example (from SAP's help):")
        out.append(f"{indent}  ```{'vb' if is_vb else 'csharp'}")
        out += [f"{indent}  {l}" if l else "" for l in c.split("\n")]
        out.append(f"{indent}  ```")
    return out


def params(h):
    """Parameters section -> [(name, description)]; enum-value tables are replaced by a pointer."""
    out = []
    for dt, dd in re.findall(r"<DT>(.*?)</DT>\s*<DD>(.*?)</DD>", h, re.S | re.I):
        name = text(dt)
        if re.search(r"FilteredItemListTable", dd):
            lead = text(re.split(r"<TABLE", dd, flags=re.I)[0], 300)
            out.append((name, (lead + " " if lead else "") + "one of the enumeration's values (see the enum file)"))
        else:
            out.append((name, text(dd, CAP_MEMBER)))
    return out


# ------------------------------------------------------------------- TOC tree ---
def parse_toc():
    s = open(os.path.join(EX, "DI_API.hhc"), encoding="utf-8", errors="replace").read()
    depth, ents, cur = 0, [], None
    for m in re.finditer(r'<UL>|</UL>|<LI>|<param name="(Name|Local)" value="([^"]*)"', s):
        t = m.group(0)
        if t == "<UL>":
            depth += 1
        elif t == "</UL>":
            depth -= 1
        elif t == "<LI>":
            if cur:
                ents.append(cur)
            cur = {"d": depth}
        else:
            cur[m.group(1)] = html.unescape(m.group(2))
    ents.append(cur)
    return ents


toc = parse_toc()
secs = [(i, e["Name"]) for i, e in enumerate(toc) if e["d"] == 1]
bounds = {n: (a, secs[k + 1][0] if k + 1 < len(secs) else len(toc)) for k, (a, n) in enumerate(secs)}
if "Objects" not in bounds or "Enumerations" not in bounds:
    sys.exit("DI_API.hhc doesn't have the expected Objects / Enumerations sections")

classes = collections.OrderedDict()
a, b = bounds["Objects"]
cur_cls = cur_kind = None
for e in toc[a + 1:b]:
    if e["d"] == 2:
        nm, kind = e["Name"].rsplit(" ", 1)
        cur_cls = classes[nm] = {"kind": kind, "local": e.get("Local"), "props": [], "methods": [], "events": []}
        cur_kind = None
    elif e["d"] == 3:
        cur_kind = e["Name"]
    elif e["d"] == 4 and cur_cls is not None:
        mname, mkind = e["Name"].rsplit(" ", 1)
        bucket = {"Property": "props", "Method": "methods", "Event": "events"}.get(mkind)
        if bucket:
            cur_cls[bucket].append((mname, e.get("Local")))

enums = []
a, b = bounds["Enumerations"]
for e in toc[a + 1:b]:
    if e["d"] == 2:
        enums.append((e["Name"].rsplit(" ", 1)[0], e.get("Local")))

ci = {n.lower() for n in classes}
if len(ci) != len(classes) or len({n.lower() for n, _ in enums}) != len(enums):
    sys.exit("class/enum names collide case-insensitively; file names would clash")

os.makedirs(os.path.join(OUT, "api"), exist_ok=True)
os.makedirs(os.path.join(OUT, "enums"), exist_ok=True)

# ---------------------------------------------------------------------- members ---
def member_block(kind, name, local, owner):
    s = read(local)
    if not s:
        return f"- `{name}` (page missing)", False
    sc = sections(s)
    syn, enum = vb_syntax(sc.get("Syntax", ""))
    desc = text(sc.get("Description", ""), CAP_MEMBER)
    out = []
    if kind == "props":
        pt = text(sc.get("Property type", ""))
        rw = {"read-write": "R/W", "read-only": "R", "write-only": "W"}.get(pt.lower().replace(" property", ""), pt)
        out.append(f"- `{syn or name}` [{rw}] {desc}")
    else:
        out.append(f"- `{syn or name}` {desc}")
    if kind == "methods":
        ps = params(sc.get("Parameters", ""))
        for pn, pd in ps:
            out.append(f"  - param `{pn}`: {pd}")
        ret = text(sc.get("Return Type", ""), CAP_MEMBER)
        if ret:
            out.append(f"  - returns: {ret}")
    rem = text(sc.get("Remarks", ""), CAP_REMARK)
    if rem:
        out.append(f"  - remarks: {rem}")
    if enum:
        out.append(f"  - enum: `{enum}` in `../enums/{enum_where[enum][0]}`" if enum in enum_where else f"  - enum: `{enum}`")
    out += example_lines(sc.get("Example", ""), "  ")
    return "\n".join(out), True


# ------------------------------------------------------------------------ enums ---
# Enumerations are bundled first: class members point at the bundle that holds each enumeration.
enum_entries, enum_meta = [], []
for ename, local in enums:
    s = read(local)
    sc = sections(s)
    L = [HEAD, f"# {ename} (Enumeration)", ""]
    d = text(sc.get("Description", ""), 1500)
    if d:
        L += [d, ""]
    L.append("| Member | Value | Description |\n|---|---|---|")
    for tr in re.findall(r"<TR[^>]*>(.*?)</TR>", sc.get("Members", ""), re.S | re.I)[1:]:
        tds = [text(x) for x in re.findall(r"<TD[^>]*>(.*?)</TD>", tr, re.S | re.I)]
        if len(tds) >= 2:
            tds = (tds + [""] * 3)[:3]
            L.append("| " + " | ".join(x.replace("|", "/") for x in tds) + " |")
    rem = text(sc.get("Remarks", ""), 1500)
    if rem:
        L += ["", f"**Remarks:** {rem}"]
    nm = sum(1 for l in L if l.startswith("| ")) - 1
    first = re.split(r"(?<=[.!?])\s", d, maxsplit=1)[0][:200] if d else ""
    enum_entries.append((ename, "\n".join(L[1:])))
    enum_meta.append((ename, nm, first))
enum_where = bundle_util.write_bundles([("enums", enum_entries)], os.path.join(OUT, "enums"), HEAD,
                                       A.max_bytes_enums, numbered_prefix="enums")

# ---------------------------------------------------------------------- classes ---
class_entries, class_meta, nmem, missing = [], [], 0, 0
for cname, c in classes.items():
    s = read(c["local"])
    sc = sections(s)
    desc = text(sc.get("Description", ""), CAP_CLASS)
    first = re.split(r"(?<=[.!?])\s", desc, maxsplit=1)[0][:220] if desc else ""
    L = [HEAD, f"# {cname} ({c['kind']})", ""]
    L += [desc, ""] if desc else []
    for k in ("Object Model", "Remarks"):
        t = text(sc.get(k, ""), CAP_CLASS)
        if t:
            L += [f"**{k}:** {t}", ""]
    ex = example_lines(sc.get("Example", ""), "")
    if ex:
        L += ["**Example:**"] + ex + [""]
    st = re.search(r"Source tables?:?\s*([A-Z][A-Z0-9_]{1,7}(?:\s*(?:,|and|/)\s*[A-Z][A-Z0-9_]{1,7})*)", desc)
    src_table = st.group(1).strip() if st else ""
    for key, title in (("props", "Properties"), ("methods", "Methods"), ("events", "Events")):
        if c[key]:
            L.append(f"## {title} ({len(c[key])})")
            for mname, local in c[key]:
                blk, ok = member_block(key, mname, local, cname)
                missing += not ok
                nmem += 1
                L.append(blk)
            L.append("")
    class_entries.append((cname, "\n".join(L[1:])))
    class_meta.append((cname, c["kind"], len(c["props"]), len(c["methods"]), src_table, first))
class_where = bundle_util.write_bundles([("classes", class_entries)], os.path.join(OUT, "api"), HEAD,
                                        A.max_bytes, numbered_prefix="classes")

# ---------------------------------------------------------------------- indexes ---
with open(os.path.join(OUT, "enums", "INDEX.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(HEAD + "\n\n# DI API enumerations\n\n")
    f.write(f"{len(enums)} enumerations. Each is in `enums/<File>` from line `Line` for `Lines` lines (read exactly that range, "
            "or grep `^# <Enum> `). Grep a member name across `enums/` to find its enumeration.\n\n")
    f.write("| Enumeration | Members | File | Line | Lines | Description |\n|---|---|---|---|---|---|\n")
    for ename, nm, first in enum_meta:
        fn, ln, nl = enum_where[ename]
        f.write(f"| {ename} | {nm} | {fn} | {ln} | {nl} | {first.replace('|', '/')} |\n")

with open(os.path.join(OUT, "api", "INDEX.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(HEAD + "\n\n# DI API classes\n\n")
    f.write(f"{len(classes)} classes. Each is in `api/<File>` from line `Line` for `Lines` lines (read exactly that range, "
            "or grep `^# <Class> (`); enumerations are in `../enums/`. Kind is the CHM's own label (Object or Collection).\n\n")
    f.write("| Class | Kind | Props | Methods | Source table | File | Line | Lines | Description |\n|---|---|---|---|---|---|---|---|---|\n")
    for cname, kind, npr, nme, src_table, first in class_meta:
        fn, ln, nl = class_where[cname]
        f.write(f"| {cname} | {kind} | {npr} | {nme} | {src_table.replace('|', '/')} | {fn} | {ln} | {nl} | {first.replace('|', '/')} |\n")
print(f"{len(classes)} classes in {len(set(v[0] for v in class_where.values()))} files, {nmem} members ({missing} pages missing), "
      f"{len(enums)} enums in {len(set(v[0] for v in enum_where.values()))} files -> {OUT}")
