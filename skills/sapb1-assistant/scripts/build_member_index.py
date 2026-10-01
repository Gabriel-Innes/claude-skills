"""Build flat member indexes for the DI API reference bundles.

Writes references/diapi/api/members.md (one line per class member) and
references/diapi/enums/members.md (one line per enumeration member) from the
classes-NN.md / enums-NN.md bundles, so a member or value can be checked with a
single grep instead of an INDEX lookup plus a line-range read.

Usage: python scripts/build_member_index.py [references/diapi]
Re-run after build_diapi_ref.py.
"""
import glob
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join("references", "diapi")

HEADER_RE = re.compile(r"^# (\S+) \((Object|Collection|Enumeration)\)")
MEMBER_RE = re.compile(
    r"^- `Public (Property|Function|Sub) (\w+)\((.*?)\)(?: As (\w+))?`(?: \[(R/W|R|W)\])?"
)
PROVENANCE_RE = re.compile(r"^<!--.*-->")

API_NOTE = (
    "members. One line each: `Class.Property : VBType [R/W]`, `Class.Method(params) -> VBType`, `Class.Sub(params)`. "
    "VB types map to C# per di-api-guide.md § 9 (Long -> int). "
    "Grep the class name followed by a dot for a class (for example `^Documents[.]`), a dot plus the member name "
    "for a member everywhere (`[.]CardCode `). Full description, remarks and samples: the class entry located "
    "through INDEX.md.\n\n"
)
ENUM_NOTE = (
    "members. One line each: `Enum.Member = Value`. Grep the enumeration name followed by a dot "
    "(`^BoObjectTypes[.]`) for an enumeration, `= 17$` for a value. "
    "Descriptions: the enumeration entry located through INDEX.md.\n\n"
)


def provenance(path):
    with open(path, encoding="utf-8") as f:
        first = f.readline().strip()
    return first if PROVENANCE_RE.match(first) else "<!-- source: REFDI.chm -->"


def build_api(root):
    rows = []
    files = sorted(glob.glob(os.path.join(root, "api", "classes-*.md")))
    for path in files:
        cls = None
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = HEADER_RE.match(line)
                if m:
                    cls = m.group(1)
                    continue
                m = MEMBER_RE.match(line)
                if m and cls:
                    kind, name, params, rtype, rw = m.groups()
                    if kind == "Property":
                        rows.append(f"{cls}.{name} : {rtype or '?'} [{rw or 'R/W'}]")
                    elif kind == "Function":
                        rows.append(f"{cls}.{name}({params}) -> {rtype or '?'}")
                    else:
                        rows.append(f"{cls}.{name}({params})")
    out = os.path.join(root, "api", "members.md")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(provenance(files[0]) + "\n\n")
        f.write("# DI API members (flat index)\n\n")
        f.write(f"{len(rows)} " + API_NOTE)
        for r in rows:
            f.write(r + "\n")
    return len(rows), out


def build_enums(root):
    rows = []
    files = sorted(glob.glob(os.path.join(root, "enums", "enums-*.md")))
    for path in files:
        enum = None
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = HEADER_RE.match(line)
                if m:
                    enum = m.group(1)
                    continue
                if enum and line.startswith("| ") and not line.startswith("| Member") and not line.startswith("|---"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if len(cells) >= 2 and cells[0]:
                        rows.append(f"{enum}.{cells[0]} = {cells[1]}")
    out = os.path.join(root, "enums", "members.md")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(provenance(files[0]) + "\n\n")
        f.write("# DI API enumeration members (flat index)\n\n")
        f.write(f"{len(rows)} " + ENUM_NOTE)
        for r in rows:
            f.write(r + "\n")
    return len(rows), out


if __name__ == "__main__":
    n, p = build_api(ROOT)
    print(f"{n} class members -> {p}")
    n, p = build_enums(ROOT)
    print(f"{n} enum members -> {p}")
