"""Convert a saved Sage 300 help page (help.sage300.com, MadCap Flare "classic" site saved as
"Web page, complete") into clean markdown for references/release-notes/raw/.

Usage:
    python scripts/extract_release_notes.py "<saved page>.html" <out.md> [--source URL] [--year YYYY]

Keeps headings, paragraphs, lists, tables and link targets (KB article numbers, external URLs);
drops the site chrome (top nav, side nav, in-document TOC, footer, scripts). Writes a provenance
header so the file can be cited. Prints nothing fancy - safe on a cp1252 Windows console.
"""
import argparse, html, re, sys
from datetime import date

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--source", default="", help="URL the page was saved from")
ap.add_argument("--year", default="", help="Sage 300 version year, for the provenance header")
a = ap.parse_args()

s = open(a.src, encoding="utf-8", errors="replace").read()
title = html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip()) if "<title>" in s else a.src
body = s[s.find("<body"):]

# site chrome. Scripts/nav/footer go here; the rest of the wrapper (nav list, "Skip to main
# content", feedback link, copyright) is trimmed at text level below, because MadCap's layout
# divs nest the whole page and cannot be cut out safely with a regex.
body = re.sub(r"<(script|style|nav|header|footer|noscript)[^>]*>.*?</>", "", body, flags=re.S | re.I)

# block structure -> markdown
body = re.sub(r"<(h[1-6])[^>]*>", lambda m: "\n\n" + "#" * int(m.group(1)[1]) + " ", body)
body = re.sub(r"</h[1-6]>", "\n\n", body)
body = re.sub(r"<li[^>]*>", "\n- ", body)
body = re.sub(r"<(p|div|tr|ul|ol|table)[^>]*>", "\n", body)
body = re.sub(r"<br\s*/?>", "\n", body)
body = re.sub(r"<t[hd][^>]*>", " | ", body)
body = re.sub(r"<(b|strong)[^>]*>(.*?)</\1>", lambda m: "**" + m.group(2).strip() + "**" if m.group(2).strip() else "", body, flags=re.S)

# links: keep KB numbers and external targets
def link(m):
    href, txt = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
    if href.startswith("http") and "sage300.com" not in href:
        return f"{txt} <{href}>"
    if re.fullmatch(r"\d{12,16}", txt):          # Knowledgebase article number
        return f"KB {txt}"
    return txt
body = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', link, body, flags=re.S)

t = html.unescape(re.sub(r"<[^>]+>", "", body))
t = t.replace(" ", " ").replace("‑", "-")
t = re.sub(r"[ \t]+", " ", t)
t = "\n".join(l.strip() for l in t.splitlines())
t = re.sub(r"\n{3,}", "\n\n", t).strip()

# drop everything before the H1 (top nav, "Skip to main content") and the footer tail
h1 = t.find("\n# ")
if h1 > 0: t = t[h1 + 1:]
# footer: everything from the trailing "Feedback" link (or the "Version: ... Language: ..." switcher) to the
# end, keeping only the Published date
fm = re.search(r"\n(?:Feedback\n|Version: \d{4} Language:)[\s\S]*?Published: ([^\n]+)[\s\S]*$", t)
if fm:
    t = t[:fm.start()].rstrip() + f"\n\nPublished: {fm.group(1)}"
# nested <li><p> pairs come out as a bare "-" line followed by the text: rejoin them
t = re.sub(r"\n- ?\n+(?=\S)", "\n- ", t)
# drop the in-document TOC ("In this document:" followed by a bare list of headings)
t = re.sub(r"In this document:\n\n(?:- [^\n]*\n\n?)+", "", t)

pub = re.search(r"Published: ([^\n]+)", t)
hdr = (f"<!-- source: {a.source or a.src} | version: Sage 300 {a.year or '?'}"
       f" | page published: {pub.group(1) if pub else 'unknown'} | extracted: {date.today().isoformat()}"
       f" by scripts/extract_release_notes.py -->\n\n")
open(a.out, "w", encoding="utf-8").write(hdr + t + "\n")
print(f"{a.out}: {len(t)} chars, {t.count(chr(10)+'#')} headings, title='{title}'")
