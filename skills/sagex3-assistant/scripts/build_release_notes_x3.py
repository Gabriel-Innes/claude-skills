"""Compile Sage X3 V12 release notes from Sage's official release-notes API into one compact, grep-friendly
file per release (maintenance only - never needed at runtime).

Usage:
    python scripts/build_release_notes_x3.py references/release-notes --cache <folder outside the repo>
    python scripts/build_release_notes_x3.py references/release-notes --cache ... --offline

Source: https://online-help.sagex3.com/x3-release-notes/ (Sage's release-notes web app). Its public API is read:
  api/en-US/archive.json                       the releases it covers (id, title "2026 R1 (12.0.39)", GA month)
  api/en-US/<id>/data.json                     what's new: modules -> Features / Improvements -> items (key, title,
                                               HTML text, legislation / software / version tags)
  api/en-US/<id>/Readme-X3-ENG-<patch>.txt     "Applicative Readme": behaviour changes, entry points, bug fixes, and
                                               for each the modified dictionary elements (ATB tables, AMK screens,
                                               TRT scripts ...) - the schema-impact evidence
  api/en-US/<id>/Readme-Components-ENG-<patch>.txt  "Platform Readme": component versions shipped (Syracuse, MongoDB,
                                               Console, Runtime, Print Server, ATP) with their fixes

Writes <out>/<release-id>.md per release and prints a summary table to paste into INDEX.md. Facts are extracted and
condensed (titles, keys, one-line gists, element lists); the verbatim Sage text is not reproduced - the file cites the
API URLs so the original can be fetched. Every fetched file is cached under --cache (outside the skill folder).
"""
import argparse, html, json, os, re, sys, time
from collections import Counter, defaultdict
from urllib.request import Request, urlopen

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("out", help="output folder, normally references/release-notes")
ap.add_argument("--cache", required=True, help="folder for the raw API files (outside the skill folder)")
ap.add_argument("--base", default="https://online-help.sagex3.com/x3-release-notes/api/en-US/")
ap.add_argument("--offline", action="store_true", help="never fetch; use the cache only")
ap.add_argument("--gist", type=int, default=200, help="max characters of the one-line gist per item (default 200)")
args = ap.parse_args()
OUT, CACHE, BASE = args.out, args.cache, args.base.rstrip("/") + "/"
os.makedirs(OUT, exist_ok=True); os.makedirs(CACHE, exist_ok=True)
TODAY = time.strftime("%Y-%m-%d")
UA = "Mozilla/5.0 (compatible; claude-skills release-notes builder; +https://github.com/fdtaljaard/claude-skills)"

def fetch(rel):
    path = os.path.join(CACHE, rel.replace("/", "__"))
    if os.path.exists(path):
        return open(path, encoding="utf-8", errors="replace").read()
    if args.offline:
        sys.exit(f"error: {rel} not in cache and --offline given")
    with urlopen(Request(BASE + rel, headers={"User-Agent": UA}), timeout=60) as r:
        data = r.read().decode("utf-8", errors="replace")
    open(path, "w", encoding="utf-8").write(data)
    return data

TAG = re.compile(r"<[^>]+>")
def text(s, limit=None):
    s = html.unescape(TAG.sub(" ", s.replace("</li>", "; ").replace("</p>", " ")))
    s = re.sub(r"\s+", " ", s).strip(" ;")
    if limit and len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0] + " …"
    return s

archive = json.loads(fetch("archive.json"))
summary_rows = []
for rel in archive["releases"]:
    rid, title = rel["id"], rel["title"]
    patch = re.search(r"\(([\d.]+)\)", title).group(1)
    year = re.match(r"(\d{4})", title).group(1)
    ga = f"{rel.get('date') or '?'} {year}"
    data = json.loads(fetch(f"{rid}/data.json"))
    readme_x3 = fetch(f"{rid}/Readme-X3-ENG-{patch}.txt")
    readme_cmp = fetch(f"{rid}/Readme-Components-ENG-{patch}.txt")

    # ---- what's new -------------------------------------------------------------------------------------------
    modules = []            # (module title, [(group title, [(key, title, legislations, gist)])])
    n_items = 0
    for m in data.get("content_parts", []):
        groups = []
        for g in m.get("content_parts", []):
            items = []
            for it in g.get("content_parts", []):
                tax = it.get("taxonomies") or {}
                legs = ", ".join(tax.get("legislation", [])) if isinstance(tax, dict) else ""
                gist = text(" ".join(p.get("content", "") for p in it.get("content_parts", []) if isinstance(p, dict)), args.gist)
                items.append((it.get("key", ""), text(it.get("title", "")), legs, gist))
                n_items += 1
            if items:
                groups.append((g.get("title") or g.get("type") or "", items))
        if groups:
            modules.append((m.get("title", ""), groups))

    # ---- applicative readme: behaviour changes, entry points, modified elements -------------------------------
    # The readme is "~~~ Module ~~~" sections holding "--- Bug ---" / "--- Entry Point ---" blocks of items:
    #   - <title> [#X3-key]\n<text>\nN modified element(s):\n. KIND (CATEGORY) NAME ...
    items_re = re.compile(r"^- (?P<title>.+?) \[#(?P<key>X3-\d+)\]\n(?P<body>.*?)(?=^- .+? \[#X3-\d+\]|^~{3,}|\Z)", re.S | re.M)
    elem_re = re.compile(r"^\. ([A-Z0-9]+) \(([^)]+)\) (\S+)", re.M)
    behaviour, entry_points, tables, elem_kinds = [], [], defaultdict(set), Counter()
    DICT_CATS = {"META/TABLES": "table", "META/LOCALMENUS": "local menu", "META/DATATYPES": "data type",
                 "META/ACTIVITYCODES": "activity code", "META/MISCTABLES": "misc table", "META/MISCELLANEOUSTABLE": "misc table"}
    dict_changes = defaultdict(lambda: defaultdict(set))     # category label -> element -> fix keys
    bug_count = 0
    section = ""
    for block in re.split(r"^(~{3,}\n.+\n~{3,})\n", readme_x3, flags=re.M):
        hdr = re.match(r"~{3,}\n(.+)\n~{3,}", block)
        if hdr:
            section = hdr.group(1).strip(); continue
        kind = ""
        for sub in re.split(r"^(-{3,}\n.+\n-{3,})\n", block, flags=re.M):
            h2 = re.match(r"-{3,}\n(.+)\n-{3,}", sub)
            if h2:
                kind = h2.group(1).strip(); continue
            for it in items_re.finditer(sub):
                t, k, body = it.group("title").strip(), it.group("key"), it.group("body")
                elems = elem_re.findall(body)
                for ek, ecat, ename in elems:
                    elem_kinds[f"{ek} ({ecat})"] += 1
                    if ecat == "META/TABLES":
                        tables[ename].add(k)
                    if ecat in DICT_CATS:
                        dict_changes[DICT_CATS[ecat]][ename].add(k)
                if "[BEHAVIOUR CHANGE]" in t:
                    behaviour.append((section, k, t.replace("[BEHAVIOUR CHANGE]", "").strip(), text(body.split("\n")[0], 220), [f"{a} {c}" for a, b, c in elems]))
                elif kind.lower().startswith("entry point"):
                    entry_points.append((section, k, t, [c for a, b, c in elems if b == "TRT"]))
                else:
                    bug_count += 1

    # ---- platform readme: component versions ------------------------------------------------------------------
    components = re.findall(r"^=+\n(.+?)\n=+$", readme_cmp, flags=re.M)
    comp_fixes = Counter()
    for chunk, name in zip(re.split(r"^=+\n.+?\n=+\n", readme_cmp, flags=re.M)[1:], components):
        comp_fixes[name] = len(re.findall(r"^- .+\[#X3-\d+\]", chunk, flags=re.M))

    # ---- write ------------------------------------------------------------------------------------------------
    src = (f"<!-- source: {BASE}{rid}/data.json, {BASE}{rid}/Readme-X3-ENG-{patch}.txt and "
           f"{BASE}{rid}/Readme-Components-ENG-{patch}.txt (Sage X3 release notes, official) compiled by "
           f"scripts/build_release_notes_x3.py | version: Sage X3 {title}, GA {ga} | verified: {TODAY} -->")
    with open(os.path.join(OUT, rid + ".md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(src + "\n")
        f.write(f"# Sage X3 {title} - release notes, integration-relevant extract\n\n")
        f.write(f"GA {ga} (Sage publishes the month; V12 releases are bi-annual). Previous release: {data.get('previous') or '-'}. "
                f"For Sage's full wording, the bug-fix list ({bug_count} fixes) and known issues, read the source files in the header; "
                f"the human-readable page is https://online-help.sagex3.com/x3-release-notes/index.html#/release/en-US/{rid}.\n\n")
        f.write("## 1. Components shipped (Platform Readme)\n\n")
        for c in components:
            f.write(f"- {c} ({comp_fixes[c]} fixes)\n")
        f.write("\n## 2. Tables whose dictionary definition changed in this patch (SQL / integration impact)\n\n")
        f.write("From the `ATB (META/TABLES)` entries of the Applicative Readme: a fix or change touched the table definition. "
                "Check these against the client's views and integrations; confirm the exact column change on the V12 table page "
                "(`https://online-help.sagex3.com/erp/12/en-us/Content/MCD/<TABLE>.htm`) or with `scripts/diff_table_versions.py`.\n\n")
        if tables:
            for t in sorted(tables):
                f.write(f"- `{t}` ({', '.join(sorted(tables[t]))})\n")
        else:
            f.write("- none listed\n")
        others = {c: v for c, v in dict_changes.items() if c != "table"}
        if others:
            f.write("\nOther dictionary objects touched (enum values and types change what SQL decodes):\n")
            for cat in sorted(others):
                f.write(f"- {cat}s: " + ", ".join(f"`{e}` ({', '.join(sorted(ks))})" for e, ks in sorted(others[cat].items())) + "\n")
        f.write("\n## 3. Behaviour changes (flagged `[BEHAVIOUR CHANGE]` by Sage)\n\n")
        for sec, k, t, gist, elems in behaviour:
            f.write(f"- **{sec}**: {t} ({k}) - {gist}" + (f" Elements: {', '.join(elems)}" if elems else "") + "\n")
        if not behaviour:
            f.write("- none flagged\n")
        f.write("\n## 4. What's new, by module (Features = new; Improvements = changed)\n\n")
        for mt, groups in modules:
            f.write(f"### {mt}\n")
            for gt, items in groups:
                f.write(f"{gt}:\n")
                for k, t, legs, gist in items:
                    tag = f" [{legs}]" if legs else ""
                    f.write(f"- {t}{tag} ({k}) - {gist}\n")
            f.write("\n")
        f.write("## 5. Entry points added or changed (customization hooks)\n\n")
        for sec, k, t, scripts in entry_points:
            f.write(f"- {sec}: {t} ({k})" + (f" - scripts {', '.join(scripts)}" if scripts else "") + "\n")
        if not entry_points:
            f.write("- none listed\n")
        f.write("\n## 6. Modified dictionary elements by kind (all fixes and changes)\n\n")
        for ek, n in elem_kinds.most_common():
            f.write(f"- {ek}: {n}\n")
    summary_rows.append((title, ga, n_items, len(tables), len(behaviour), len(entry_points), bug_count,
                         "; ".join(c for c in components if re.match(r"(SyracuseServer|MongoDB|Console|Runtime|PrintServer|ATP)", c))))
    print(f"  {title}: {n_items} what's-new items, {len(tables)} tables touched, {len(behaviour)} behaviour changes, "
          f"{len(entry_points)} entry points, {bug_count} fixes")

print("\nSummary (for INDEX.md):")
print("| Release | GA | What's-new items | Tables touched | Behaviour changes | Entry points | Fixes | Components |")
print("|---|---|---|---|---|---|---|---|")
for r in summary_rows:
    print("| " + " | ".join(str(x) for x in r) + " |")
