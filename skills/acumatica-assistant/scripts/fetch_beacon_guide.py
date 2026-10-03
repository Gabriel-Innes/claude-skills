#!/usr/bin/env python3
"""Fetch an Acumatica Beacon guide (beacon.acumatica.com, a Fluid Topics portal) into a local cache (maintenance only).

    python scripts/fetch_beacon_guide.py --map UpQu337K_38feMdsBg0ruQ --cache <dir outside the repo> [--delay 0.3] [--filter REGEX]

The reader URLs (`/r/<Guide>/<Topic>`) are a JavaScript shell to curl, but the portal's public knowledge-hub API
returns each topic's HTML:

    GET /api/khub/maps/<mapId>                       map metadata (title, version, lastEdition)
    GET /api/khub/maps/<mapId>/toc                   nested table of contents (tocId, contentId, prettyUrl, title)
    GET /api/khub/maps/<mapId>/topics/<contentId>/content   the topic body as HTML

The map id is the first path segment of any `ft-internal-link` inside a topic (e.g. `/r/UpQu337K_38feMdsBg0ruQ/...`).
`UpQu337K_38feMdsBg0ruQ` is the Integration Development Guide at the time of writing; re-check it after a new
release is published, since a new edition may get a new map id.

For every topic the script writes `<cache>/<NNN>-<slug>.html` (raw) and `<cache>/<NNN>-<slug>.md` (a plain-text
rendering: headings, paragraphs, notes, fenced code blocks, pipe tables, list items), plus `<cache>/toc.json`
and `<cache>/map.json`. Re-running skips topics already cached. The cache is Acumatica's documentation and is
**not** to be committed: curate facts from it into `references/` and cite the topic titles and URLs.
"""
import argparse
import html
import json
import os
import re
import sys
import time
import urllib.request

BASE = "https://beacon.acumatica.com"
UA = "Mozilla/5.0 (compatible; claude-skills maintenance fetch; +https://github.com/fdtaljaard/claude-skills)"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, text/html"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def flatten(nodes, depth=0, out=None):
    out = [] if out is None else out
    for n in nodes:
        out.append({"tocId": n["tocId"], "contentId": n["contentId"], "prettyUrl": n["prettyUrl"],
                    "title": n["title"], "depth": depth})
        flatten(n.get("children", []), depth + 1, out)
    return out


# --- minimal HTML -> text ---------------------------------------------------------------------------------------

BLOCK_RE = re.compile(r"<(pre|table|h[1-6]|p|li|div|ul|ol|tr|td|th|section|br)\b[^>]*>|</(pre|table|h[1-6]|p|li|div|ul|ol|tr|td|th|section)>", re.I)


def strip_tags(s):
    """Remove tags only; entities (e.g. the &lt;placeholder&gt; in code samples) are unescaped once, at the end."""
    return re.sub(r"<[^>]+>", "", s)


def collapse(s):
    return re.sub(r"[ \t\r\f\v]+", " ", s).strip()


def render(doc):
    """Render the topic HTML to readable text. Good enough for curation, not a general converter."""
    out = []
    # code blocks first (keep whitespace)
    def code_repl(m):
        code = strip_tags(m.group(1))
        return "\n```\n" + code.strip("\n") + "\n```\n"
    doc = re.sub(r"<pre[^>]*>(.*?)</pre>", code_repl, doc, flags=re.S | re.I)
    # tables -> pipe rows
    def table_repl(m):
        rows = []
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(1), flags=re.S | re.I):
            cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr, flags=re.S | re.I)
            rows.append("| " + " | ".join(collapse(strip_tags(c)) for c in cells) + " |")
        return "\n" + "\n".join(rows) + "\n"
    doc = re.sub(r"<table[^>]*>(.*?)</table>", table_repl, doc, flags=re.S | re.I)
    # headings
    def h_repl(m):
        level = int(m.group(1))
        return "\n" + "#" * min(level + 1, 6) + " " + collapse(strip_tags(m.group(2))) + "\n"
    doc = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", h_repl, doc, flags=re.S | re.I)
    # notes
    doc = re.sub(r'<span class="(?:note|attention|important|tip|caution|warning)title">(.*?)</span>', r"**\1**", doc, flags=re.S | re.I)
    # list items and paragraphs
    doc = re.sub(r"<li[^>]*>", "\n- ", doc, flags=re.I)
    doc = re.sub(r"</(p|li|div|ul|ol|section)>", "\n", doc, flags=re.I)
    doc = re.sub(r"<(p|div|ul|ol|section)[^>]*>", "\n", doc, flags=re.I)
    doc = re.sub(r"<br\s*/?>", "\n", doc, flags=re.I)
    # inline code
    doc = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", doc, flags=re.S | re.I)
    text = html.unescape(strip_tags(doc))
    # tidy: collapse spaces per line outside fenced code, max two blank lines
    lines, fenced, out = text.split("\n"), False, []
    for ln in lines:
        if ln.strip().startswith("```"):
            fenced = not fenced
            out.append(ln.strip())
            continue
        out.append(ln if fenced else collapse(ln))
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def slug(pretty):
    """Topic path without the guide segment, kept short for Windows path limits."""
    path = pretty.split("/r/", 1)[-1].split("/", 1)[-1]
    return re.sub(r"[^A-Za-z0-9.-]+", "-", path.replace("/", "__"))[:90]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--map", required=True, help="Fluid Topics map id, e.g. UpQu337K_38feMdsBg0ruQ")
    ap.add_argument("--cache", required=True, help="output folder (outside the repo)")
    ap.add_argument("--delay", type=float, default=0.3, help="seconds between requests")
    ap.add_argument("--filter", default=None, help="regex on the pretty URL; fetch only matching topics")
    ap.add_argument("--rerender", action="store_true", help="rewrite the .md files from cached .html without fetching")
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)

    meta = json.loads(get(f"{BASE}/api/khub/maps/{a.map}"))
    json.dump(meta, open(os.path.join(a.cache, "map.json"), "w", encoding="utf-8"), indent=1)
    version = next((m["values"][0] for m in meta.get("metadata", []) if m["key"] == "version"), "?")
    print(f"{meta['title']} | version {version} | lastEdition {meta.get('lastEdition')} | words {next((m['values'][0] for m in meta.get('metadata', []) if m['key']=='ft:wordCount'), '?')}")

    toc = json.loads(get(f"{BASE}/api/khub/maps/{a.map}/toc"))
    flat = flatten(toc)
    json.dump(flat, open(os.path.join(a.cache, "toc.json"), "w", encoding="utf-8"), indent=1)
    print(f"{len(flat)} topics in the table of contents")

    pat = re.compile(a.filter) if a.filter else None
    fetched = skipped = failed = 0
    for i, t in enumerate(flat, 1):
        if pat and not pat.search(t["prettyUrl"]):
            continue
        base = os.path.join(a.cache, f"{i:03d}-{slug(t['prettyUrl'])}")
        if a.rerender and os.path.exists(base + ".html"):
            body = open(base + ".html", encoding="utf-8").read()
        elif os.path.exists(base + ".md"):
            skipped += 1
            continue
        else:
            url = f"{BASE}/api/khub/maps/{a.map}/topics/{t['contentId']}/content"
            try:
                body = get(url)
            except Exception as e:  # noqa: BLE001
                failed += 1
                print(f"FAILED {t['prettyUrl']}: {e}", file=sys.stderr)
                continue
            with open(base + ".html", "w", encoding="utf-8") as f:
                f.write(body)
            time.sleep(a.delay)
        header = f"<!-- {t['title']} | {BASE}{t['prettyUrl']} | version {version} | lastEdition {meta.get('lastEdition')} -->\n# {t['title']}\n\n"
        with open(base + ".md", "w", encoding="utf-8") as f:
            f.write(header + render(body))
        fetched += 1
    print(f"fetched {fetched}, skipped (cached) {skipped}, failed {failed} -> {a.cache}")


if __name__ == "__main__":
    main()
