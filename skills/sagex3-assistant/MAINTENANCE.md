# Maintaining the Sage X3 Assistant skill

Owner: Francois Taljaard. Format: [Agent Skills](https://agentskills.io/specification) -
the checks below keep the skill inside that spec and its best-practices guide.

## Structure and budgets (from the Agent Skills spec)

- `SKILL.md` is the only file loaded on activation: keep it **under 500 lines / ~5,000 tokens**. It holds
  routing, ground rules, one workflow section per capability, the gotchas list and the layout. Today it is
  ~110 lines; a new capability may add ~30 lines. Bulk always goes to `references/`.
- References are **one hop from SKILL.md** (`references/<domain>/<file>` or `.../INDEX.md`). The per-folder
  `INDEX.md` is the only intermediate layer.
- Paths in SKILL.md and references are **relative to the skill root**; no `<skill-dir>` placeholders.
- Frontmatter: `name` (matches the folder), `description` <= 1024 chars (describe domains and trigger
  contexts, don't enumerate phrases), `compatibility` <= 500 chars, `metadata` string map. Bump
  `metadata.version` (YYYY.MM) on each release.
- Every claim SKILL.md makes about a file must be true - no "planned" files in tables; describe planned
  capabilities in prose only.
- Gotchas (concrete corrections an engineer would otherwise get wrong) live in `SKILL.md` § 4, not buried in
  references. When the assistant gets something wrong in use, add the correction there.

## Packaging and validation

Keep the folder named `sagex3-assistant` (the archive is named after it). With `PYTHONUTF8=1` on Windows:

```
PYTHONUTF8=1 python skills/sagex3-assistant/scripts/package_skill.py skills/sagex3-assistant dist
```

That runs the frontmatter validator first and writes `dist/sagex3-assistant.skill` (+ a `.zip`). The archive
must stay under 200 files - the dictionary is bundled per module (14 files) for that reason. The reference
validator `skills-ref validate ./sagex3-assistant` (github.com/agentskills/agentskills, `pip install skills-ref`)
checks the same spec rules if you want an independent pass. Raw source pages (the fetch cache) are never
packaged and never committed.

After any change to SKILL.md wording, run the evals in `evals/evals.json` (skill-creator's eval loop, or by hand)
and compare against `expected_output`. The ground-rule eval (refusing an UPDATE) must always pass.

## Conventions for reference files

- **Provenance header** on every file:
  `<!-- source: <Sage URL> | version: <Sage X3 version> | verified: YYYY-MM-DD -->`
- **INDEX.md** in every `references/<domain>/` folder: one line per file - path, what it covers, version,
  verified date. The agent reads the INDEX before opening files, so keep it accurate.
- Grep-friendly: one fact per line where possible, stable headings, no prose walls. **Extract the facts; do
  not paste verbatim vendor pages.** Don't bundle Sage's help pages in the skill - the dictionary files hold
  the extracted names, types, values and links only, and cite the page URL pattern so the original can be
  fetched on demand. Keep the raw fetch cache outside the repository (the builder's `--cache` folder).

## Add a capability

1. Add a `## N. <Capability>` section to `SKILL.md` (workflow steps, which reference files to read and *when*,
   delivery format) and a row to the routing table in § 1. Stay inside the line budget above.
2. Create `references/<name>/` with an `INDEX.md` and the first reference files (provenance headers).
3. Add at least two evals to `evals/evals.json` (one typical, one edge case).
4. If the new domain needs a new trigger-phrase family, adjust the description within the 1024 cap, then
   run the skill-creator description optimiser.

Planned: development (4GL / classic scripts, web services / Sage X3 Services GraphQL, import-export templates),
screen and process help.

## Refresh the versions / upgrades references (twice a year, after each May / November GA)

1. **Release notes**: `PYTHONUTF8=1 python skills/sagex3-assistant/scripts/build_release_notes_x3.py skills/sagex3-assistant/references/release-notes --cache <folder outside the repo>`.
   It reads Sage's release-notes API (`archive.json` → `data.json`, Applicative and Platform Readmes per release) and
   rewrites one `<release-id>.md` per release; a new release appears automatically when Sage adds it to the archive.
   Paste the printed summary table into `references/release-notes/INDEX.md` and bump the verified dates.
2. **Platform matrix**: re-read `https://online-help.sagex3.com/erp/12/en-us/Content/V7DEV/prerequisites_overview.html`
   (and the per-component pages it links) for new "Since release …" statements; update `references/upgrades/platform-matrix.md`
   § 1 and record the page's "Date published" in the header. The V11 page is frozen (end of maintenance).
3. **Lifecycle / release table**: re-read the Sage Community post "Sage X3 Version 12: Latest Release Information"
   for each release's stage and the recommended Syracuse builds; update `upgrade-guide.md` § 1. If the help footer
   names a newer Lifecycle Policy edition than November 2024, re-read the PDF and re-check the stage durations.
4. **Upgrade procedures**: the three help pages in `upgrade-guide.md` § 2 change rarely; skim them for new component
   steps (e.g. a new MongoDB major) and update § 5 / § 6.
5. Add an eval if a new kind of question appeared in use; re-run the upgrade evals (9–13).

`scripts/diff_table_versions.py` needs no maintenance unless Sage changes the help URL patterns (`VERSION_URLS`).

## Rebuild or add a dictionary version

The dictionary is compiled by `scripts/build_dict_x3.py` from the "Table dictionary" pages of Sage's online
help (`https://online-help.sagex3.com/erp/<version>/en-US/MCD/ATB_0.htm` and the pages it links to: one page
per table, per local menu `MEN00nnn.htm`, per data type `ATY_<code>.htm`). It needs only the Python standard
library and internet access, caches every page it fetches, and prints a build report.

1. Build (first run fetches ~3,300 pages, a few minutes with 8 workers; re-runs are offline from the cache):
   ```
   PYTHONUTF8=1 python skills/sagex3-assistant/scripts/build_dict_x3.py skills/sagex3-assistant/references/dictionary/V11 --cache <folder outside the repo>
   ```
   For another version point `--base` at that version's `MCD/` folder and `--version` at its label, e.g.
   `--base https://online-help.sagex3.com/erp/12/en-us/Content/MCD/ --version V12` into `references/dictionary/V12`.
   `--limit 5` builds five tables for parser testing; `--offline` forbids fetching.
2. Read `build-report.json` in the cache folder: tables without columns and failed fetches should be empty
   (re-run to retry transient failures - cached pages are not refetched). Spot-check three tables
   (`SORDER`, `BPCUSTOMER`, `ITMMASTER`) against the live help page and, if available, a live folder.
3. Update `references/dictionary/INDEX.md` (counts per file, verified date, version notes) and the version
   bullets in `SKILL.md` § 2–3 if a new version folder was added. Keep the folder named by the Sage version
   label used in the help URL (`V11`, `V12`).
4. If a new version is added, diff `table-index.md` against the previous version (tables added/removed) and
   record the notable changes in INDEX.md. The index also carries Sage's own V9/V10 change flags per table.
5. Sage's help markup is regular but not valid HTML (unterminated `</a` in link expressions, blank `<th>`s on
   the data-type pages): the parser is positional and header-driven, so when a page family changes shape,
   adjust `parse_table` / the menu and type loops and re-run offline from the cache.
