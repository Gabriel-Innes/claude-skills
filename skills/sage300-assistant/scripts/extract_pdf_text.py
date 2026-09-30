"""Turn a Sage PDF (Compatibility Guide, Upgrade Guide ...) into a plain-text markdown file for references/.../raw/.

Usage:
    python scripts/extract_pdf_text.py <file.pdf> <out.md> [--source URL] [--year YYYY]

Uses `pdftotext -layout` (poppler) when available - it keeps tables readable - and falls back to pypdf.
Collapses blank runs and drops running page headers/footers ("Sage 300 2026 Compatibility Guide 7").
Writes a provenance header with the document's own "Last updated" date when it has one.
"""
import argparse, re, shutil, subprocess, sys
from datetime import date

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--source", default=""); ap.add_argument("--year", default="")
a = ap.parse_args()

if shutil.which("pdftotext"):
    t = subprocess.run(["pdftotext", "-layout", a.src, "-"], capture_output=True, check=True).stdout.decode("utf-8", "replace")
else:
    from pypdf import PdfReader
    t = "\n\f".join(p.extract_text() or "" for p in PdfReader(a.src).pages)

t = t.replace("\f", "\n").replace("�", "-")
# page headers/footers: "2 Sage 300 2026 Compatibility Guide" (even pages) / "Sage 300 2026 Compatibility Guide 3" (odd)
footer = re.compile(r"^(?:\d+ )?Sage 300 \d{4} [A-Za-z ]+Guide(?: \d+| i+)?$")
t = "\n".join(l.rstrip() for l in t.splitlines() if not footer.match(l.strip()))
t = re.sub(r"\n{3,}", "\n\n", t).strip()

upd = re.search(r"Last updated: ([^\n]+)", t)
hdr = (f"<!-- source: {a.source or a.src} | version: Sage 300 {a.year or '?'}"
       f" | document last updated: {upd.group(1).strip() if upd else 'unknown'}"
       f" | extracted: {date.today().isoformat()} by scripts/extract_pdf_text.py -->\n\n")
open(a.out, "w", encoding="utf-8").write(hdr + t + "\n")
print(f"{a.out}: {len(t)} chars, last updated {upd.group(1).strip() if upd else '?'}")
