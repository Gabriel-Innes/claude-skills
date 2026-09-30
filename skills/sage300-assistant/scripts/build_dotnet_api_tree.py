#!/usr/bin/env python3
"""Step 1 of the .NET API reference build: parse the decompiled CHM's .hhc
table of contents into a nested type/member tree (_tree.json).

Usage:
    hh.exe -decompile <extractdir> <chm>      # copy CHM to a space-free path first
    PYTHONUTF8=1 python build_dotnet_api_tree.py <extractdir> <api-out>
    PYTHONUTF8=1 python build_dotnet_api.py <api-out>/_tree.json <extractdir> <api-out>

The Sandcastle .hhc nests <UL>/<LI><OBJECT> sitemap entries as
Namespace -> "<Type> Class"/"<Type> Enumeration" -> "<Type> Methods"/
"<Type> Properties" -> individual members, with overloaded members as child
nodes. Step 2 (build_dotnet_api.py) turns this tree + the html pages into
curated markdown, skipping the 25 IXxxComInterop interfaces and VB/C++ syntax.
"""
import re, os, sys, html
from html.parser import HTMLParser

EX = sys.argv[1]
OUT = sys.argv[2]
HHC = os.path.join(EX, "Sage Accpac .NET Libraries.hhc")

# ---------------------------------------------------------------- HHC tree ----
class Node:
    __slots__ = ("name", "local", "children")
    def __init__(self, name=None, local=None):
        self.name = name
        self.local = local
        self.children = []

class HHCParser(HTMLParser):
    """Build a tree from the nested <UL>/<LI><OBJECT> sitemap."""
    def __init__(self):
        super().__init__()
        self.root = Node("ROOT")
        self.stack = [self.root]      # UL nesting -> parent node for LIs
        self._cur_name = None
        self._cur_local = None
        self._last_node = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "ul":
            # children of the most recently created node
            parent = self._last_node if self._last_node is not None else self.stack[-1]
            self.stack.append(parent)
        elif tag == "object":
            self._cur_name = None
            self._cur_local = None
        elif tag == "param":
            if a.get("name") == "Name":
                self._cur_name = a.get("value")
            elif a.get("name") == "Local":
                self._cur_local = a.get("value")
    def handle_endtag(self, tag):
        if tag == "ul":
            if len(self.stack) > 1:
                self.stack.pop()
        elif tag == "object":
            if self._cur_name is not None:
                n = Node(self._cur_name.strip(), self._cur_local)
                self.stack[-1].children.append(n)
                self._last_node = n
            self._cur_name = self._cur_local = None

def parse_hhc():
    p = HHCParser()
    p.feed(open(HHC, encoding="utf-8", errors="replace").read())
    return p.root

# ------------------------------------------------------------- page helpers ---
_page_cache = {}
def load(local):
    if not local:
        return ""
    if local in _page_cache:
        return _page_cache[local]
    path = os.path.join(EX, local.replace("/", os.sep))
    try:
        t = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        t = ""
    _page_cache[local] = t
    return t

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = s.replace("﻿", " ").replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()

def get_summary(h):
    m = re.search(r'<div class="summary">(.*?)</div>', h, re.S)
    return clean(m.group(1)) if m else ""

def get_section(h, toggle_id):
    """Text of a collapsible section, e.g. remarksSection."""
    m = re.search(r'<div id="%s"[^>]*>(.*?)</div>\s*<h1' % toggle_id, h, re.S)
    if not m:
        m = re.search(r'<div id="%s"[^>]*>(.*?)</div><div id="footer"' % toggle_id, h, re.S)
    return clean(m.group(1)) if m else ""

def get_csharp_syntax(h):
    m = re.search(r'<span codeLanguage="CSharp"><table><tr><th>C#</th></tr>'
                  r'<tr><td><pre[^>]*>(.*?)</pre>', h, re.S)
    if not m:
        return ""
    code = m.group(1)
    code = re.sub(r"<[^>]+>", "", code)
    code = html.unescape(code)
    code = code.replace("\xa0", " ")
    return code.strip()

def get_title(h):
    m = re.search(r"<title>(.*?)</title>", h, re.S)
    return clean(m.group(1)) if m else ""

NOISE_SUMMARIES = {"COM interop interface member", ""}

def get_member_rows(h):
    """(name, summary) pairs from a Members-page methods/properties table."""
    seg = h[h.find("mainBody"):]
    rows = re.findall(
        r'<a href="[0-9a-f]{8}-[^"]+\.htm">([^<]+)</a></td>'
        r'<td[^>]*>(.*?)</td>', seg, re.S)
    out = []
    for name, summ in rows:
        out.append((clean(name), clean(summ)))
    return out

def get_enum_members(h):
    """(name, description) for enumeration values."""
    body = h[h.find("mainBody"):h.find('id="footer"')]
    out = []
    for tr in re.findall(r"<tr>(.*?)</tr>", body, re.S):
        tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        if len(tds) >= 2:
            name = clean(tds[0])
            desc = clean(tds[1])
            if name and not name.startswith(("public ", "Public ")):
                out.append((name, desc))
    return out

def get_parameters(h):
    """List of (paramName, typeText, description) from a method page."""
    m = re.search(r'>Parameters<.*?<div id="parametersSection"[^>]*>(.*?)</div>\s*<h1', h, re.S)
    if not m:
        m = re.search(r'>Parameters</span></h1><div[^>]*>(.*?)(?:<h1|<div id="footer")', h, re.S)
    if not m:
        return []
    seg = m.group(1)
    out = []
    # each param: <dt><span class="parameter">NAME</span></dt><dd>Type: <a>..</a><br/>desc</dd>
    for dt, dd in re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", seg, re.S):
        pname = clean(dt)
        ddc = clean(dd)
        ddc = re.sub(r'\[Missing <param>[^\]]*\]', "", ddc).strip()
        out.append((pname, ddc))
    return out

def get_return(h):
    m = re.search(r'>Return Value</span></h1><div[^>]*>(.*?)(?:<h1|<div id="footer")', h, re.S)
    if not m:
        return ""
    r = clean(m.group(1))
    r = re.sub(r'\[Missing <returns>[^\]]*\]', "", r).strip()
    return r

# ---------------------------------------------------------------- traversal ---
def find_namespace(root):
    # ROOT -> [namespace overview, namespace node...]; classes are under the
    # "ACCPAC.Advantage Namespace" node's children.
    for n in root.children:
        for c in n.children:
            if c.name.endswith("Namespace"):
                return c
    # fallback: deepest with many children
    best = root
    def rec(n):
        nonlocal best
        if len(n.children) > len(best.children):
            best = n
        for c in n.children:
            rec(c)
    rec(root)
    return best

def kind_of(name):
    for k in ("Class", "Enumeration", "Interface", "Structure", "Delegate"):
        if name.endswith(" " + k):
            return k
    return None

if __name__ == "__main__":
    root = parse_hhc()
    ns = find_namespace(root)
    os.makedirs(OUT, exist_ok=True)

    # Namespace children are the type nodes; each type node's children are its
    # Members/Properties/Methods/Constructor subtrees.
    types = []
    for node in ns.children:
        k = kind_of(node.name)
        if k:
            types.append((k, node))

    import json
    # dump a debug summary
    print("namespace:", ns.name, "types:", len(types))
    from collections import Counter
    print(Counter(k for k, _ in types))
    # Save the tree for the generator step
    def to_dict(n):
        return {"name": n.name, "local": n.local,
                "children": [to_dict(c) for c in n.children]}
    json.dump(to_dict(ns), open(os.path.join(OUT, "_tree.json"), "w", encoding="utf-8"))
    print("wrote _tree.json")
