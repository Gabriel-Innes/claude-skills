#!/usr/bin/env python3
"""Compile the Pastel Evolution (Sage 200 Evolution) SDK reference from the shipped
Pastel.Evolution.chm (maintenance only).

Step 0 (manual, Windows): copy the CHM to a path without spaces and decompile it:
    hh.exe -decompile <extractdir> Pastel.Evolution.chm
(7-Zip also extracts CHMs.) The result is ~4,000 flat .htm pages plus EvolutionSdk.hhc
(the table of contents). The CHM is Sandcastle format: every page is a stack of
`<div class="summary">`, `<span codeLanguage="CSharp">...<pre>` and `<h4 class="subHeading">`
blocks, the same template family as the Sage 300 .NET CHM.

Step 1:
    PYTHONUTF8=1 python build_sdk_ref.py <extractdir> <xml> <out> --verified YYYY-MM-DD

<xml> is the shipped Pastel.Evolution.xml (standard .NET XML doc comments). The CHM is the
primary source; a member whose CHM page carries no <summary> is backfilled from the XML.

Writes, under <out>:
  api/INDEX.md       one line per type (kind, prop/method counts, file/line/lines, first sentence)
  api/classes-NN.md  classes/interfaces/structs/delegates, alphabetical, ~150 KB per file; each
                     starts `# <Type> (<Kind>)`: summary, C# declaration, remarks, constructors,
                     properties, methods, fields, events
  enums/INDEX.md     one line per enumeration (member count, file/line/lines, first sentence)
  enums/enums-NN.md  enumerations, ~90 KB per file; each starts `# <Enum> (Enumeration)` + member table

The skill must stay under 200 files, hence the numbered bundles; the INDEX files say where each
entry is (read the exact line range, or grep the `^# <Name> (` heading). Only the main
`Pastel.Evolution` namespace is emitted; `Pastel.Evolution.Internal` is skipped.
"""
import argparse, html, json, os, re, sys
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bundle_util

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("extract")
ap.add_argument("xml")
ap.add_argument("out")
ap.add_argument("--verified", required=True)
ap.add_argument("--label", default="Pastel.Evolution SDK 11.0.0.10")
ap.add_argument("--namespace", default="Pastel.Evolution Namespace")
ap.add_argument("--hhc", default="EvolutionSdk.hhc")
ap.add_argument("--max-bytes", type=int, default=150_000, help="class bundle size")
ap.add_argument("--max-bytes-enums", type=int, default=90_000, help="enumeration bundle size")
A = ap.parse_args()
EX, OUT = A.extract, A.out
HEAD = f"<!-- source: Pastel.Evolution.chm, {A.label} | verified: {A.verified} -->"

CAP_SUMMARY, CAP_REMARK = 1200, 2000


# ----------------------------------------------------------------- HHC tree ----
class Node:
    __slots__ = ("name", "local", "children")
    def __init__(self, name=None, local=None):
        self.name, self.local, self.children = name, local, []


class HHCParser(HTMLParser):
    """Build a tree from the nested <UL>/<LI><OBJECT> sitemap."""
    def __init__(self):
        super().__init__()
        self.root = Node("ROOT")
        self.stack = [self.root]
        self._cur_name = self._cur_local = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "ul":
            # a <UL> nests the most recent <LI> of the current level
            parent = self.stack[-1]
            self.stack.append(parent.children[-1] if parent.children else parent)
        elif tag == "object":
            self._cur_name = self._cur_local = None
        elif tag == "param":
            if a.get("name") == "Name":
                self._cur_name = a.get("value")
            elif a.get("name") == "Local":
                self._cur_local = a.get("value")

    def handle_endtag(self, tag):
        if tag == "ul":
            if len(self.stack) > 1:
                self.stack.pop()
        elif tag == "object" and self._cur_name is not None:
            n = Node(self._cur_name.strip(), self._cur_local)
            self.stack[-1].children.append(n)
            self._cur_name = self._cur_local = None


def parse_hhc():
    p = HHCParser()
    p.feed(open(os.path.join(EX, A.hhc), encoding="utf-8", errors="replace").read())
    return p.root


# --------------------------------------------------------------- xml backfill ---
def load_xml():
    """{(TypeShort, MemberShort|None): summary} from the .NET XML doc. MemberShort is None for
    the type itself; '#ctor' for constructors. Parameters are stripped, so overloads share a key
    (first summary wins) - enough to backfill a blank CHM summary."""
    out = {}
    try:
        raw = open(A.xml, encoding="utf-8", errors="replace").read()
    except OSError:
        return out
    for m in re.finditer(r'<member name="([TPMFE]):([^"]+)">(.*?)</member>', raw, re.S):
        kind, ident, body = m.group(1), m.group(2), m.group(3)
        sm = re.search(r"<summary>(.*?)</summary>", body, re.S)
        if not sm:
            continue
        summ = xml_clean(sm.group(1))
        if not summ:
            continue
        ident = ident.split("(", 1)[0]               # drop parameter list
        if not ident.startswith("Pastel.Evolution."):
            continue
        rest = ident[len("Pastel.Evolution."):]
        if kind == "T":
            out.setdefault((rest, None), summ)
        else:
            if "." in rest:
                typ, mem = rest.rsplit(".", 1)
                out.setdefault((typ, mem), summ)
    return out


def xml_clean(s):
    s = re.sub(r"<see\s+cref=\"[A-Z]:([^\"]+)\"\s*/?>", lambda m: m.group(1).split(".")[-1], s)
    s = re.sub(r"<(c|see|paramref|typeparamref)[^>]*>(.*?)</\1>", r"\2", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ").replace("﻿", " ")
    return re.sub(r"\s+", " ", s).strip()


# --------------------------------------------------------------- html helpers ---
_cache = {}
def page(local):
    if not local:
        return ""
    if local not in _cache:
        try:
            _cache[local] = open(os.path.join(EX, local.replace("/", os.sep)),
                                 encoding="utf-8", errors="replace").read()
        except OSError:
            _cache[local] = ""
    return _cache[local]


def collapse_lst(s):
    """Collapse Sandcastle's multi-language punctuation spans to the C# variant, e.g.
    System<span class="languageSpecificText"><span class="cs">.</span>...</span>String
    -> System.String. The whole group holds one inner span per language (cs/vb/cpp/nu/fs)."""
    def _lst(m):
        cs = re.search(r'<span class="cs">(.*?)</span>', m.group(0), re.S)
        return cs.group(1) if cs else ""
    return re.sub(r'<span class="languageSpecificText">(?:\s*<span class="\w+">.*?</span>)*\s*</span>',
                  _lst, s, flags=re.S)


def clean(s):
    s = collapse_lst(s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("﻿", " ").replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()


def _demissing(s):
    return re.sub(r"\[Missing <\w+>[^\]]*\]", "", s).strip()


def summary(h):
    m = re.search(r'<div class="summary">(.*?)</div>', h, re.S)
    return _demissing(clean(m.group(1))) if m else ""


def csharp(h):
    m = re.search(r'<span codeLanguage="CSharp"><table><tr><th>C#</th></tr>'
                  r'<tr><td><pre[^>]*>(.*?)</pre>', h, re.S)
    if not m:
        return ""
    c = html.unescape(re.sub(r"<[^>]+>", "", collapse_lst(m.group(1)))).replace("\xa0", " ")
    lines = []
    for ln in c.split("\n"):
        ln = re.sub(r"[ \t]+", " ", ln).strip()
        ln = ln.replace(" [", "[").replace(" ]", "]")
        ln = re.sub(r"\s+,", ",", ln)
        ln = re.sub(r"\(\s+", "(", ln).replace(" )", ")")
        if ln:
            lines.append(ln)
    if len(lines) > 1:
        return lines[0] + "\n" + "\n".join("    " + l for l in lines[1:])
    return lines[0] if lines else ""


def _oneline(sig):
    return re.sub(r"\s+", " ", sig).strip()


def remarks(h):
    m = re.search(r'<div id="remarksSection"[^>]*>(.*?)</div><h1', h, re.S)
    if not m:
        m = re.search(r'<div id="remarksSection"[^>]*>(.*?)</div><div id="footer"', h, re.S)
    return _demissing(clean(m.group(1))) if m else ""


def parameters(h):
    seg = re.search(r'<h4 class="subHeading">Parameters</h4>(.*?)'
                    r'(?:<h4 class="subHeading"|<h1 class="heading"|<div id="footer")', h, re.S)
    if not seg:
        return []
    out = []
    for block in re.findall(r'<dl paramName="[^"]*">(.*?)</dl>', seg.group(1), re.S):
        nm = re.search(r'<span class="parameter">(.*?)</span>', block, re.S)
        name = clean(nm.group(1)) if nm else ""
        dd = re.search(r"<dd>(.*?)</dd>", block, re.S)
        typ = desc = ""
        if dd:
            parts = re.split(r"<br\s*/?>", dd.group(1), maxsplit=1)
            typ = clean(parts[0])
            typ = re.sub(r"^Type:\s*", "", typ)
            typ = re.sub(r"array<\s*(.*?)\s*>\s*\[\]\s*\(\)", r"\1[]", typ)
            typ = re.sub(r"array<\s*(.*?)\s*>", r"\1[]", typ)
            desc = _demissing(clean(parts[1])) if len(parts) > 1 else ""
        out.append((name, typ, desc))
    return out


def returns(h):
    m = re.search(r'<h4 class="subHeading">Return Value</h4>(.*?)'
                  r'(?:<h4 class="subHeading"|<h1 class="heading"|<div id="footer")', h, re.S)
    return _demissing(clean(m.group(1))) if m else ""


KINDS = ("Class", "Enumeration", "Interface", "Structure", "Delegate")
def kind_of(name):
    for k in KINDS:
        if name.endswith(" " + k):
            return k, name[:-(len(k) + 1)].strip()
    return None, name.strip()


def short(name):
    return re.sub(r"\s+(Method|Property|Constructor|Field|Event)\s*(\(.*\))?\s*$", "", name).strip()


def member_group(node, suffix):
    for c in node.children:
        if c.name.strip() == suffix:
            return c.children
    return []


def cap(s, n):
    if s and len(s) > n:
        return s[:n].rsplit(" ", 1)[0] + " […]"
    return s


# --------------------------------------------------------------------- gather ---
XML = load_xml()


def type_summary(base, h):
    return summary(h) or XML.get((base, None), "")


def mem_summary(base, mshort, h):
    s = summary(h)
    if s:
        return s
    key = "#ctor" if mshort == base else mshort
    return XML.get((base, key), "")


def overload_pages(mnode):
    """Concrete signature pages for a member node, skipping the Overload_ index page."""
    kids = [c for c in mnode.children if c.local and "Overload_" not in c.local]
    return kids or [mnode]


# ------------------------------------------------------------------- render -----
def render_type(base, kind, node):
    h = page(node.local)
    L = [f"# {base} ({kind})", ""]
    s = type_summary(base, h)
    if s:
        L += [cap(s, CAP_SUMMARY), ""]
    L.append("**Namespace:** Pastel.Evolution")
    decl = csharp(h)
    if decl:
        L += ["", "```csharp", decl, "```"]
    rem = remarks(h)
    if rem:
        L += ["", f"**Remarks:** {cap(rem, CAP_REMARK)}"]
    L.append("")

    ctors = member_group(node, f"{base} Constructor")
    props = member_group(node, f"{base} Properties")
    methods = member_group(node, f"{base} Methods")
    fields = member_group(node, f"{base} Fields")
    events = member_group(node, f"{base} Events")

    if ctors:
        L.append(f"## Constructors ({len(ctors)})")
        for c in ctors:
            for pn in overload_pages(c):
                ph = page(pn.local)
                sig = _oneline(csharp(ph)) or short(c.name)
                ds = mem_summary(base, base, ph)
                L.append(f"- `{sig}`" + (f" — {ds}" if ds else ""))
        L.append("")

    if props:
        L.append(f"## Properties ({len(props)})")
        for m in sorted(props, key=lambda x: short(x.name).lower()):
            ph = page(m.local)
            sig = _oneline(csharp(ph)) or short(m.name)
            ds = mem_summary(base, short(m.name), ph)
            L.append(f"- `{sig}`" + (f" — {ds}" if ds else ""))
        L.append("")

    if methods:
        L.append(f"## Methods ({len(methods)})")
        for m in sorted(methods, key=lambda x: short(x.name).lower()):
            for pn in overload_pages(m):
                ph = page(pn.local)
                sig = _oneline(csharp(ph)) or f"{short(m.name)}(…)"
                ds = mem_summary(base, short(m.name), ph)
                L.append(f"- `{sig}`" + (f" — {ds}" if ds else ""))
                for prm, pt, pd in parameters(ph):
                    line = f"  - param `{prm}`"
                    if pt:
                        line += f" ({pt})"
                    if pd:
                        line += f" — {pd}"
                    L.append(line)
                ret = returns(ph)
                if ret:
                    L.append(f"  - returns: {ret}")
                rem = remarks(ph)
                if rem:
                    L.append(f"  - remarks: {cap(rem, CAP_REMARK)}")
        L.append("")

    if fields:
        L.append(f"## Fields ({len(fields)})")
        for m in sorted(fields, key=lambda x: short(x.name).lower()):
            fh = page(m.local)
            sig = _oneline(csharp(fh)) or short(m.name)
            ds = mem_summary(base, short(m.name), fh)
            L.append(f"- `{sig}`" + (f" — {ds}" if ds else ""))
        L.append("")

    if events:
        L.append(f"## Events ({len(events)})")
        for m in sorted(events, key=lambda x: short(x.name).lower()):
            eh = page(m.local)
            sig = _oneline(csharp(eh)) or short(m.name)
            ds = mem_summary(base, short(m.name), eh)
            L.append(f"- `{sig}`" + (f" — {ds}" if ds else ""))
        L.append("")

    first = re.split(r"(?<=[.!?])\s", s, maxsplit=1)[0][:220] if s else ""
    return "\n".join(L).rstrip(), len(props), len(methods), first


def render_enum(base, node):
    h = page(node.local)
    L = [f"# {base} (Enumeration)", ""]
    s = type_summary(base, h)
    if s:
        L += [cap(s, CAP_SUMMARY), ""]
    body = h[h.find("mainBody"):h.find('id="footer"')]
    rows = []
    for tr in re.findall(r"<tr>(.*?)</tr>", body, re.S):
        tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        if len(tds) >= 3:   # Member | Value | Description
            nm, val, ds = clean(tds[0]), clean(tds[1]), clean(tds[2])
            if nm and not nm.lower().startswith(("public ", "protected ")):
                rows.append((nm, val, ds))
    L.append("| Member | Value | Description |\n|---|---|---|")
    for nm, val, ds in rows:
        L.append(f"| `{nm}` | {val or '—'} | {ds.replace('|', '/') or '—'} |")
    first = re.split(r"(?<=[.!?])\s", s, maxsplit=1)[0][:200] if s else ""
    return "\n".join(L).rstrip(), len(rows), first


# --------------------------------------------------------------------- main -----
def find_namespace(root):
    stack = list(root.children)
    while stack:
        n = stack.pop()
        if n.name == A.namespace:
            return n
        stack.extend(n.children)
    sys.exit(f"namespace node {A.namespace!r} not found in {A.hhc}")


root = parse_hhc()
ns = find_namespace(root)

type_nodes = []
for node in ns.children:
    k, base = kind_of(node.name)
    if k:
        type_nodes.append((k, base, node))

classes = [(b, n) for k, b, n in type_nodes if k in ("Class", "Interface", "Structure", "Delegate")]
enums = [(b, n) for k, b, n in type_nodes if k == "Enumeration"]
kindmap = {b: k for k, b, n in type_nodes}
classes.sort(key=lambda x: x[0].lower())
enums.sort(key=lambda x: x[0].lower())

ci = {b.lower() for b, _ in classes} | {b.lower() for b, _ in enums}
if len(ci) != len(classes) + len(enums):
    sys.exit("type names collide case-insensitively; bundle headings would clash")

os.makedirs(os.path.join(OUT, "api"), exist_ok=True)
os.makedirs(os.path.join(OUT, "enums"), exist_ok=True)

# enums first
enum_entries, enum_meta = [], []
for base, node in enums:
    body, nmem, first = render_enum(base, node)
    enum_entries.append((base, body))
    enum_meta.append((base, nmem, first))
enum_where = bundle_util.write_bundles([("enums", enum_entries)], os.path.join(OUT, "enums"),
                                       HEAD, A.max_bytes_enums, numbered_prefix="enums")

# classes
class_entries, class_meta = [], []
for base, node in classes:
    body, npr, nme, first = render_type(base, kindmap[base], node)
    class_entries.append((base, body))
    class_meta.append((base, kindmap[base], npr, nme, first))
class_where = bundle_util.write_bundles([("classes", class_entries)], os.path.join(OUT, "api"),
                                        HEAD, A.max_bytes, numbered_prefix="classes")

# indexes
with open(os.path.join(OUT, "enums", "INDEX.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(HEAD + "\n\n# Pastel Evolution SDK enumerations\n\n")
    f.write(f"{len(enums)} enumerations from the `Pastel.Evolution` namespace. Each is in "
            "`enums/<File>` from line `Line` for `Lines` lines (read exactly that range, or grep "
            "`^# <Enum> (`). Grep a member name across `enums/` to find its enumeration.\n\n")
    f.write("| Enumeration | Members | File | Line | Lines | Description |\n|---|---|---|---|---|---|\n")
    for base, nmem, first in enum_meta:
        fn, ln, nl = enum_where[base]
        f.write(f"| {base} | {nmem} | {fn} | {ln} | {nl} | {first.replace('|', '/')} |\n")

with open(os.path.join(OUT, "api", "INDEX.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(HEAD + "\n\n# Pastel Evolution SDK types\n\n")
    f.write(f"{len(classes)} classes/interfaces/structs/delegates from the `Pastel.Evolution` "
            "namespace. Each is in `api/<File>` from line `Line` for `Lines` lines (read exactly "
            "that range, or grep `^# <Type> (`); enumerations are in `../enums/`.\n\n")
    f.write("| Type | Kind | Props | Methods | File | Line | Lines | Description |\n"
            "|---|---|---|---|---|---|---|---|\n")
    for base, kind, npr, nme, first in class_meta:
        fn, ln, nl = class_where[base]
        f.write(f"| {base} | {kind} | {npr} | {nme} | {fn} | {ln} | {nl} | {first.replace('|', '/')} |\n")

print(f"{len(classes)} types in {len(set(v[0] for v in class_where.values()))} files, "
      f"{len(enums)} enums in {len(set(v[0] for v in enum_where.values()))} files -> {OUT}")
print(f"xml summaries loaded: {len(XML)}")
