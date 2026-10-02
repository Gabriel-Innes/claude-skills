# Maintaining the Sage 300 Assistant skill

Owner: Francois Taljaard. Format: [Agent Skills](https://agentskills.io/specification) —
the checks below keep the skill inside that spec and its best-practices guide.

## Structure and budgets (from the Agent Skills spec)

- `SKILL.md` is the only file loaded on activation: keep it **under 500 lines / ~5,000 tokens**. It holds
  routing, ground rules, one workflow section per capability, the gotchas list and the layout. Today it is
  ~130 lines; a new capability may add ~30 lines. Bulk always goes to `references/`.
- References are **one hop from SKILL.md** (`references/<domain>/<file>` or `.../INDEX.md`). Don't add an
  intermediate layer of "read this file to find out which file to read"; the per-folder `INDEX.md` is that layer.
- Paths in SKILL.md and references are **relative to the skill root**; no `<skill-dir>` placeholders.
- Frontmatter: `name` (matches the folder), `description` ≤ 1024 chars (describe domains and trigger
  contexts, don't enumerate phrases), `compatibility` ≤ 500 chars, `metadata` string map. Bump
  `metadata.version` (YYYY.MM) on each release.
- Every claim SKILL.md makes about a file must be true — no "planned" files in tables; describe planned
  capabilities in prose only.
- Gotchas (concrete corrections an engineer would otherwise get wrong) live in `SKILL.md` § 5, not buried in
  references — the agent must see them before it hits the situation. When the assistant gets something wrong in
  use, add the correction there.

## Packaging and validation

Keep the folder named `sage300-assistant` (the archive is named after it). From the skill-creator directory,
with `PYTHONUTF8=1` on Windows (the script prints emoji and otherwise dies with a cp1252 `UnicodeEncodeError`):

```
PYTHONUTF8=1 python -m scripts.package_skill path/to/skills/sage300-assistant path/to/dist
```

That runs the frontmatter validator first and writes `dist/sage300-assistant.skill`. The reference validator
`skills-ref validate ./sage300-assistant` (github.com/agentskills/agentskills, `pip install skills-ref`) checks
the same spec rules if you want an independent pass. Source material (`../docs/`) is never packaged.

After any change to SKILL.md wording, run the evals in `evals/evals.json` (skill-creator's eval loop, or by hand)
and compare against `expected_output`. Eval 5 (refusing an UPDATE) must always pass.

## Conventions for reference files

- **Provenance header** on every file:
  `<!-- source: <Sage document or URL> | version: <Sage 300 year / AOM version> | verified: YYYY-MM-DD -->`
- **INDEX.md** in every `references/<domain>/` folder: one line per file — path, what it covers, version,
  verified date. The agent reads the INDEX before opening files, so keep it accurate.
- Grep-friendly: one fact per line where possible, stable headings, no prose walls. Extract, don't paste;
  full source pages go under that folder's `raw/` so verbatim wording is available on demand.
- Version years (2023, 2024 …) and AOM codes (7.0A, 7.3A …) are both used; the map is in
  `references/dictionary/INDEX.md` and `references/upgrades/upgrade-guide.md` § 1.

## Add a capability

1. Add a `## N. <Capability>` section to `SKILL.md` (workflow steps, which reference files to read and *when*,
   delivery format) and a row to the routing table in § 1. Stay inside the line budget above.
2. Create `references/<name>/` with an `INDEX.md` and the first reference files (provenance headers).
3. Add at least two evals to `evals/evals.json` (one typical, one edge case).
4. If the new domain needs a new trigger-phrase family, adjust the description within the 1024 cap, then
   run the skill-creator description optimiser.

## Add a dictionary version

1. Obtain the AOM export for that Sage 300 version (`../docs/sage data dict/`). Two formats exist:
   - **HTML** (SDK 7.0A+, Sage 300 2023 and later — a folder of `<TABLE>.html` / `<ROTOID>.html` pages; some
     zips nest it one level down): `python scripts/build_dict_html.py <aom-folder> references/dictionary/<version>`
     (writes both `dict/` and `table-index.md`).
   - **XML** (older exports, e.g. AOM60): `python scripts/build_dict.py <aom-folder> references/dictionary/<version>/dict`
     then `python scripts/build_index.py <aom-folder> references/dictionary/<version>/table-index.md`.
   All scripts answer `--help` and fail with a clear message when pointed at the wrong folder.
2. Name the folder by AOM version (`7.3A`), not year; add the year mapping in `references/dictionary/INDEX.md`.
3. Add a provenance header line to `table-index.md`.
4. Diff against the previous version (table count, added/removed tables, field diff across all common tables,
   type changes, enum-bearing field count) and record the notable changes in INDEX.md and in
   `references/release-notes/<year>.md` § 3. Differences should be additive; type widenings are worth a gotcha.
5. Spot-check three tables against a live database of that version.

## Add a release-note year

1. Download that year's Release Notes and Technical Information pages (URL patterns in
   `references/upgrades/upgrade-guide.md` § 2; plain `urllib` with a browser User-Agent works — the pages are
   static HTML) into `../docs/release notes/<year>/` as `Sage 300 <year> Release Notes.html` and
   `Sage 300 <year> Technical Information.html`. Re-download when a new PU ships; the "Published" date at the
   foot of the page tells you whether anything changed.
2. Convert both: `PYTHONUTF8=1 python scripts/extract_release_notes.py "../docs/release notes/<year>/<saved>.html"
   references/release-notes/raw/<year>-<release-notes|technical-information>.md --source <URL> --year <year>`.
   Skim the output for leftover site chrome; the script trims nav/footer and rejoins nested bullets.
3. Write `references/release-notes/<year>.md` from the raw files (use `2026.md` as the template): a warnings table
   (Sage's "Important" notes + TI's upgrade floor, prerequisites and which PUs change Workstation Setup), then
   integration-relevant changes per PU with the notable TI fixes, then a schema verdict cross-checked against the
   dictionary diff for that AOM version. Note which PU of the previous year back-ported each feature. Provenance
   header required.
4. Update `upgrade-guide.md`: § 4 block (pointer to the new file; † any claim not on the RN page), cross-version
   table, § 5 compatibility row, and the "verified as of" line. Promote anything an integrator would trip over to
   `SKILL.md` § 5 Gotchas.
5. Add both files to `references/release-notes/INDEX.md`.

## Refresh a Compatibility Guide

1. Download `https://docs.sage.com/docs/en/customer/300erp/<year>/open/Sage300_CompatibilityGuide.pdf` into
   `../docs/compatibility guides/Sage300_CompatibilityGuide_<year>.pdf` (plain `urllib` works). The URL serves the
   *current edition* — check "Last updated" on page 2; Sage re-issues guides when platforms are retired.
2. `python scripts/extract_pdf_text.py <pdf> references/upgrades/raw/<year>-compatibility-guide.md --source <URL> --year <year>`
   (needs `pdftotext` on PATH for readable tables; falls back to pypdf).
3. Update the rows in `references/upgrades/compatibility-guides.md` § 1–3 and the summary in `upgrade-guide.md` § 5,
   with the new edition date. Update both INDEX entries.

## Add help or how-to content (planned capabilities)

- Create `references/help/` or `references/howto/` with an INDEX; one file per screen/module or per procedure,
  named `<module>-<topic>.md`. Extract, don't paste: summarise the behaviour and cite the Sage help page URL.
- Then follow "Add a capability" above.

## Update the .NET compose graphs

`references/dotnet/compose-graphs.md` holds verified `Compose()` wiring for the core transaction documents,
extracted from an AOM **HTML** export by `scripts/build_compose_graphs.py`.

1. Unzip the target version's AOM (e.g. `../docs/sage data dict/AOM2026.0.zip`) to a folder that directly
   contains the `<ROTOID>.html` pages (has `Advantage.html`).
2. Regenerate: `PYTHONUTF8=1 python scripts/build_compose_graphs.py <aom-html-folder> references/dotnet/compose-graphs.md`.
   The script walks each document root's composition list to its own downward view tree (same-module, skipping
   other documents' Header/Batch views and posting/audit structures) and prints any roots it couldn't find.
3. **Add a document**: append `("<ROOTID>", "<MODULE>", "<Name>")` to the `ROOTS` list in the script, then rerun.
   Verify a candidate root first with `--probe <ROTOID>` (prints its title, protocol and compositions); a document
   entry root has protocol `Header …` or `Batch …`. Confirm the generated block against a macro-recording or the
   codebase before trusting a newly-added document.
4. Bump the provenance `verified:` date; the file targets 7.3A but applies to 7.0A–7.3A (core compositions are
   stable). If a version diverges, note it in `references/dotnet/INDEX.md`.

## Retire or supersede

Never silently delete a reference a client's version may still need. Mark it `status: superseded by X`
in its provenance header and in INDEX.md; remove only when no supported Sage version uses it.
