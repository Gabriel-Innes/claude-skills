#!/usr/bin/env python3
"""Generate curated markdown from the parsed CHM tree (_tree.json) + html pages."""
import json, os, re, sys, html
from datetime import date

TREE = sys.argv[1]        # _tree.json
EX = sys.argv[2]          # decompiled CHM root
OUT = sys.argv[3]         # references/dotnet/api
TODAY = "2026-09-25"

tree = json.load(open(TREE, encoding="utf-8"))

# ------------------------------------------------------------- html helpers ---
_cache = {}
def page(local):
    if not local:
        return ""
    if local in _cache:
        return _cache[local]
    p = os.path.join(EX, local.replace("/", os.sep))
    try:
        t = open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        t = ""
    _cache[local] = t
    return t

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("﻿", " ").replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def _demissing(s):
    return re.sub(r'\[Missing <\w+>[^\]]*\]', '', s).strip()

def summary(h):
    m = re.search(r'<div class="summary">(.*?)</div>', h, re.S)
    return _demissing(clean(m.group(1))) if m else ""

def csharp(h):
    m = re.search(r'<span codeLanguage="CSharp"><table><tr><th>C#</th></tr>'
                  r'<tr><td><pre[^>]*>(.*?)</pre>', h, re.S)
    if not m:
        return ""
    c = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).replace("\xa0", " ")
    lines = []
    for ln in c.split("\n"):
        ln = re.sub(r"[ \t]+", " ", ln).strip()
        ln = ln.replace(" [", "[").replace(" ]", "]")
        ln = re.sub(r"\s+,", ",", ln)
        ln = re.sub(r"\(\s+", "(", ln).replace(" )", ")")
        if ln:
            lines.append(ln)
    # keep multi-line for readability when it has params
    if len(lines) > 1:
        head = lines[0]
        rest = ["    " + l for l in lines[1:]]
        return head + "\n" + "\n".join(rest)
    return lines[0] if lines else ""

def remarks(h):
    m = re.search(r'<div id="remarksSection"[^>]*>(.*?)</div><h1', h, re.S)
    if not m:
        m = re.search(r'<div id="remarksSection"[^>]*>(.*?)</div><div id="footer"', h, re.S)
    if not m:
        return ""
    r = clean(m.group(1))
    return r

def parameters(h):
    seg = re.search(r'<h4 class="subHeading">Parameters</h4>(.*?)'
                    r'(?:<h4 class="subHeading"|<h1 class="heading"|<div id="footer")', h, re.S)
    if not seg:
        return []
    out = []
    for block in re.findall(r'<dl paramName="[^"]*">(.*?)</dl>', seg.group(1), re.S):
        nm = re.search(r'<span class="parameter">(.*?)</span>', block, re.S)
        name = clean(nm.group(1)) if nm else ""
        dd = re.search(r'<dd>(.*?)</dd>', block, re.S)
        typ = desc = ""
        if dd:
            parts = re.split(r'<br\s*/?>', dd.group(1), maxsplit=1)
            typ = clean(parts[0])
            typ = re.sub(r'array<\s*(.*?)\s*>\s*\[\]\s*\(\)', r'\1[]', typ)
            typ = re.sub(r'array<\s*(.*?)\s*>', r'\1[]', typ)
            desc = clean(parts[1]) if len(parts) > 1 else ""
            desc = _demissing(desc)
        out.append((name, typ, desc))
    return out

def returns(h):
    m = re.search(r'<h4 class="subHeading">Return Value</h4>(.*?)'
                  r'(?:<h4 class="subHeading"|<h1 class="heading"|<div id="footer")', h, re.S)
    if not m:
        return ""
    return _demissing(clean(m.group(1)))

def kind_of(name):
    for k in ("Class", "Enumeration", "Interface", "Structure", "Delegate"):
        if name.endswith(" " + k):
            return k, name[:-(len(k) + 1)]
    return None, name

def short(name):
    # "GoNext Method" -> "GoNext"; strip trailing kind word + overload signature
    n = re.sub(r'\s+(Method|Property|Constructor|Field|Event)\s*(\(.*\))?\s*$', '', name).strip()
    return n

NOISE = {"COM interop interface member", "Internal use only.",
         "Reserved for ACCPAC internal use only.", ""}

# --------------------------------------------------------------- gather -------
types = []
for node in tree["children"]:
    k, base = kind_of(node["name"])
    if k:
        types.append((k, base, node))

classes = [(b, n) for k, b, n in types if k == "Class"]
enums = [(b, n) for k, b, n in types if k == "Enumeration"]
classes.sort(key=lambda x: x[0].lower())
enums.sort(key=lambda x: x[0].lower())

def member_group(node, group_name):
    for c in node["children"]:
        if c["name"] == group_name:
            return c["children"]
    return []

# ------------------------------------------------------------- enums.md -------
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "enums.md"), "w", encoding="utf-8") as f:
    f.write("# ACCPAC.Advantage enumerations\n\n")
    f.write(f"Every enumeration in the Sage Accpac .NET class library, with each "
            f"member's meaning. Use the **named constant** in C# (e.g. "
            f"`DBLinkType.Company`, `ViewOpenModes.Readonly`) — never a magic int. "
            f"Flags enums combine with `|`. Extracted from `Sage Accpac .NET "
            f"Libraries.chm` (library version 5.5.0.1). Verified {TODAY}.\n\n")
    f.write(f"{len(enums)} enumerations: " +
            ", ".join(f"`{b}`" for b, _ in enums) + "\n\n---\n\n")
    for base, node in enums:
        h = page(node["local"])
        f.write(f"## {base}\n\n")
        s = summary(h)
        if s:
            f.write(s + "\n\n")
        body = h[h.find("mainBody"):h.find('id="footer"')]
        rows = []
        for tr in re.findall(r"<tr>(.*?)</tr>", body, re.S):
            tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
            if len(tds) >= 2:
                nm = clean(tds[0]); ds = clean(tds[1])
                if nm and not nm.startswith(("public ", "Public ")):
                    rows.append((nm, ds))
        if rows:
            f.write("| Member | Description |\n|---|---|\n")
            for nm, ds in rows:
                f.write(f"| `{nm}` | {ds or '—'} |\n")
            f.write("\n")

# --------------------------------------------------- grouped class files -----

def write_member_detail(f, mnode):
    """Write detail for a method/property node, expanding overloads."""
    name = short(mnode["name"])
    kids = mnode["children"]
    pages = []
    if kids:  # overloaded: each child is a concrete signature
        for c in kids:
            pages.append(c)
    else:
        pages.append(mnode)
    for i, pnode in enumerate(pages):
        h = page(pnode["local"])
        sig = csharp(h)
        s = summary(h)
        if s in NOISE and not sig:
            continue
        params = parameters(h)
        ret = returns(h)
        rem = remarks(h)
        if sig:
            f.write(f"```csharp\n{sig}\n```\n\n")
        if params:
            for pn, pt, pd in params:
                line = f"- `{pn}`"
                if pt:
                    line += f" ({pt})"
                if pd:
                    line += f" — {pd}"
                f.write(line + "\n")
            f.write("\n")
        if ret and ret not in NOISE:
            f.write(f"**Returns:** {ret}\n\n")
        if rem and rem not in NOISE:
            f.write(f"{rem}\n\n")

def row_summary(m):
    return summary(page(m["local"]))

def render_class(f, base, node, L=2):
    """Write one class's markdown block. L = heading level for the class name
    (sections are L+1, per-method details L+2)."""
    h1, h2, h3 = "#" * L, "#" * (L + 1), "#" * (L + 2)
    h = page(node["local"])
    props = member_group(node, f"{base} Properties")
    methods = member_group(node, f"{base} Methods")
    ctors = member_group(node, f"{base} Constructor")
    f.write(f"{h1} {base} class\n\n")
    s = summary(h)
    if s:
        f.write(s + "\n\n")
    f.write("**Namespace:** ACCPAC.Advantage &nbsp;·&nbsp; "
            "**Assembly:** ACCPAC.Advantage.dll\n\n")
    decl = csharp(h)
    if decl:
        f.write(f"```csharp\n{decl}\n```\n\n")
    rem = remarks(h)
    if rem and rem not in NOISE:
        f.write(f"{rem}\n\n")
    if ctors:
        f.write(f"{h2} Constructors\n\n| Name | Description |\n|---|---|\n")
        for m in ctors:
            f.write(f"| `{short(m['name'])}` | {row_summary(m) or '—'} |\n")
        f.write("\n")
    if props:
        f.write(f"{h2} Properties\n\n| Name | Description |\n|---|---|\n")
        for m in sorted(props, key=lambda x: short(x["name"]).lower()):
            f.write(f"| `{short(m['name'])}` | {row_summary(m) or '—'} |\n")
        f.write("\n")
    if methods:
        f.write(f"{h2} Methods\n\n| Name | Description |\n|---|---|\n")
        for m in sorted(methods, key=lambda x: short(x["name"]).lower()):
            f.write(f"| `{short(m['name'])}` | {row_summary(m) or '—'} |\n")
        f.write("\n")
        f.write(f"{h2} Method details\n\n")
        for m in sorted(methods, key=lambda x: short(x["name"]).lower()):
            f.write(f"{h3} {base}.{short(m['name'])}\n\n")
            write_member_detail(f, m)

# Classes are grouped into a few bundle files (keeps the packaged file count
# well under the 200-file upload limit, and lets the agent load only the bundle
# it needs). GROUPS: (filename, title, intro, [class base names]); any class not
# listed falls into the last "catch-all" group (members == None).
GROUPS = [
    ("classes-session.md", "Session class",
     "The `Session` class — the authenticated entry point to the whole library "
     "(`new Session()` → `Init` → `Open` → `OpenDBLink`). Every other object is "
     "reached directly or indirectly from here.",
     ["Session"]),
    ("classes-view.md", "View data-access classes",
     "The view/data-access core: `DBLink.OpenView` returns a `View`; field and "
     "key access is through `ViewFields`/`ViewField` and `ViewKeys`/`ViewKey`. "
     "This is where read/create/post/compose logic lives.",
     ["DBLink", "View", "ViewFields", "ViewField", "ViewKeys", "ViewKey",
      "ViewFieldPresentationList", "ViewReturnCode", "ViewInternal"]),
    ("classes-system.md", "System, company, currency, admin & error classes",
     "Company profile, currency, fiscal calendar, organizations, activated "
     "applications, reporting/printing, multi-user locking, meters, spy log, and "
     "the exception/error classes.",
     None),  # catch-all
]

grouped = set(b for _, _, _, names in GROUPS if names for b in names)
class_by_base = dict(classes)
class_group = {}   # base -> group filename (for INDEX links)

for fname, title, intro, names in GROUPS:
    if names is None:
        members = [b for b, _ in classes if b not in grouped]
    else:
        members = [b for b in names if b in class_by_base]
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{intro}\n\n")
        f.write(f"Extracted from `Sage Accpac .NET Libraries.chm` (library "
                f"5.5.0.1). Verified {TODAY}. See [`INDEX.md`](INDEX.md) for the "
                f"full class/enum map and [`enums.md`](enums.md) for enumerations."
                f"\n\nClasses in this file: "
                + ", ".join(f"`{b}`" for b in members) + "\n\n---\n\n")
        for i, b in enumerate(members):
            if i:
                f.write("---\n\n")
            render_class(f, b, class_by_base[b], L=2)
            class_group[b] = fname

# ------------------------------------------------------------- INDEX.md -------
def counts(node, base):
    p = len(member_group(node, f"{base} Properties"))
    m = len(member_group(node, f"{base} Methods"))
    return p, m

with open(os.path.join(OUT, "INDEX.md"), "w", encoding="utf-8") as f:
    f.write("# ACCPAC.Advantage .NET API reference (from the CHM)\n\n")
    f.write("Authoritative class/enum surface of the Sage Accpac .NET class "
            "library (`ACCPAC.Advantage.dll` + `ACCPAC.Advantage.Types.dll`), "
            "extracted from `Sage Accpac .NET Libraries.chm` (library version "
            f"5.5.0.1). Verified {TODAY}. This is the *signature/enum* reference; "
            "for how to actually drive views end-to-end see `../view-api.md`, "
            "`../compose-graphs.md`, and `../common-mistakes.md`.\n\n")
    f.write("All applications start from `Session` → `OpenDBLink` → `DBLink` → "
            "`OpenView` → `View`. Field access is through `View.Fields` "
            "(`Fields`/`ViewFields`) and `FieldByName`.\n\n")
    f.write("- **Enums:** [`enums.md`](enums.md) — all "
            f"{len(enums)} enumerations with member meanings.\n")
    f.write("- **Classes:** grouped into "
            f"{len([g for g in GROUPS])} bundle files (each with summary, C# "
            "declaration, property & method tables, and per-method C# "
            "signatures/parameters/returns/remarks) — "
            "[`classes-session.md`](classes-session.md), "
            "[`classes-view.md`](classes-view.md), "
            "[`classes-system.md`](classes-system.md). The **File** column below "
            "links to each class's section.\n\n")
    f.write("## Classes\n\n| Class | File | Props | Methods | Summary |\n"
            "|---|---|--:|--:|---|\n")
    for base, node in classes:
        p, m = counts(node, base)
        s = summary(page(node["local"]))
        gf = class_group.get(base, "classes-system.md")
        anchor = f"{base.lower()}-class"
        f.write(f"| `{base}` | [{gf}]({gf}#{anchor}) | {p} | {m} | {s} |\n")
    f.write("\n## Enumerations\n\n| Enum | Summary |\n|---|---|\n")
    for base, node in enums:
        s = summary(page(node["local"]))
        f.write(f"| [`{base}`](enums.md#{base.lower().replace('.','')}) | {s} |\n")
    f.write("\n> The 25 `IXxxComInterop` interfaces in the assembly are internal "
            "COM-interop plumbing (undocumented) and are intentionally omitted.\n")

print("done. classes:", len(classes), "enums:", len(enums))
