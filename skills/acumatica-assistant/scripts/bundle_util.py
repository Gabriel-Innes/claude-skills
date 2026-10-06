"""Shared by the build scripts: write many small entries (tables, classes, enumerations) into a few bundle files.

The skill must stay under 200 files, so each build script groups its entries into bundles of about `max_bytes` and
records where each entry landed (file, 1-based start line, line count). The index files carry those three values so
a reader can open exactly one entry with a line-range read, or grep for its heading.
"""
import os
import re


def slug(label):
    return re.sub(r"[^A-Za-z0-9]+", "-", label).strip("-")


def _chunk(entries, max_bytes):
    chunks, cur, size = [], [], 0
    for e in entries:
        b = len(e[1].encode("utf-8")) + 2
        if cur and size + b > max_bytes:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(e)
        size += b
    if cur:
        chunks.append(cur)
    return chunks


def write_bundles(groups, out_dir, header, max_bytes, numbered_prefix=None):
    """groups: ordered list of (label, [(name, text), ...]).  text is the entry's markdown, starting with its heading.

    Files are named from the group label (`Marketing-Documents.md`, `Marketing-Documents-2.md` when a group is split) or,
    with numbered_prefix, `<prefix>-01.md`, `<prefix>-02.md` ... over all groups in order.
    Returns {name: (file name, start line, line count)}.
    """
    os.makedirs(out_dir, exist_ok=True)
    plan = []  # (file name, entries)
    if numbered_prefix:
        entries = [e for _, es in groups for e in es]
        for n, ch in enumerate(_chunk(entries, max_bytes), 1):
            plan.append((f"{numbered_prefix}-{n:02d}.md", ch))
    else:
        for label, es in groups:
            chunks = _chunk(es, max_bytes)
            for n, ch in enumerate(chunks, 1):
                plan.append((f"{slug(label)}{'' if len(chunks) == 1 else '-' + str(n)}.md", ch))
    where = {}
    for fname, ch in plan:
        head = header.rstrip("\n") + "\n\n"
        line = head.count("\n") + 1
        parts = [head]
        for name, text in ch:
            text = text.rstrip("\n")
            n_lines = text.count("\n") + 1
            where[name] = (fname, line, n_lines)
            parts.append(text + "\n\n")
            line += n_lines + 1
        with open(os.path.join(out_dir, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write("".join(parts).rstrip("\n") + "\n")
    return where
