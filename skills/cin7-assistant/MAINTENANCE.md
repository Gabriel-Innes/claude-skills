# Maintaining the Cin7 Assistant skill

Owner: Francois Taljaard. Format: [Agent Skills](https://agentskills.io/specification).

One capability is implemented: **Cin7 Core API integration development**, backed by `references/core-api/`.
This file records the conventions, how to regenerate the references from a fresh portal export, and how to add
a capability.

## Structure and budgets

- `SKILL.md` is the only file loaded on activation: keep it **under 500 lines**. It holds routing, ground rules,
  one workflow section per capability, gotchas and the layout. Bulk goes to `references/`.
- References are **one hop from SKILL.md** (`references/<domain>/INDEX.md` and the files it lists). The
  per-folder `INDEX.md` is the routing layer; don't add another.
- Paths in SKILL.md and references are relative to the skill root.
- Frontmatter: `name` (matches the folder, lowercase), `description` ≤ 1024 chars, `compatibility` ≤ 500 chars,
  `metadata` string map. Bump `metadata.version` (YYYY.MM.N) on each release.
- Every claim SKILL.md makes about a file must be true: describe planned capabilities in prose only, never as
  rows in the routing table or layout.
- Gotchas (corrections an engineer would otherwise get wrong) belong in `SKILL.md` § 4, each backed by a
  reference file.

## File limit and packaging

Claude accepts at most **200 files** in an uploaded skill (this skill has 45). Package for upload with
`python scripts/package_skill.py skills/cin7-assistant dist` (needs PyYAML). It refuses to write the archive
if the frontmatter is invalid or there are more than 200 files, and writes `dist/cin7-assistant.skill` plus
an identical `.zip`. Both are git-ignored. Upload in Claude under Settings, Capabilities, Skills.

## Conventions for reference files

- **Provenance header** on every file:
  `<!-- source: <URL or document> | version: <Cin7 product and version, or "not stated"> | verified: YYYY-MM-DD -->`
- **INDEX.md** in every `references/<domain>/` folder: one line per file (path, what it covers, product and
  version, verified date), a sources table with URL, role and date, lookup recipes, and known limits.
- **Extract the facts; do not paste.** Bundle endpoint shapes, parameter syntax, headers, status codes, field
  lists, enum values and rules, each attributed to its source, never page text wholesale. The portal's own
  field tables, parameter lists and example bodies *are* the facts and are bundled; its sample
  `api-auth-*` header values are never written. Raw exports of vendor documentation stay in a scratch
  workspace, uncommitted.
- **Name the product.** Cin7 Core (formerly DEAR Systems) and Cin7 Omni have separate APIs and data models;
  every reference file and every fact must say which product it describes.
- Grep-friendly: one fact per line or table row, stable headings, one `<a id="...">` anchor per action.

## Refreshing `references/core-api/` from the portal

The source is the API Blueprint export of the Cin7 Core developer portal, https://dearinventory.docs.apiary.io/
(Apiary serves the `.apib` behind the "Download" / raw link of the documentation; the file starts with
`FORMAT: 1A` and `HOST: https://inventory.dearsystems.com/ExternalApi/v2/`). Keep it outside the repository,
for example `../cin7-source/dearinventory.apib`.

1. Regenerate the generated files (every file under `groups/`, `endpoints.md` and `enums.md` is rewritten):

   ```bash
   python skills/cin7-assistant/scripts/build_core_api_reference.py \
       --apib ../cin7-source/dearinventory.apib \
       --out skills/cin7-assistant/references/core-api --verified YYYY-MM-DD
   ```

   The script refuses to write if a sample header value from the export survives in the output. It prints the
   counts and the per-group table: paste the table into `references/core-api/INDEX.md` and update the counts
   there, in `SKILL.md` (description, § 5) and in `README.md`.
2. Diff the regenerated files against the previous commit. New groups, actions or renamed fields mean
   `api-basics.md` § 6 to § 9, `common-mistakes.md` and the gotchas in `SKILL.md` § 4 need re-reading against
   the new export: those two files are hand-written from the portal's introduction and group-level notes
   (`grep -n "^+ " dearinventory.apib` lists the notes; the introduction is everything before the first
   `# Group`).
3. Re-check the known limits in `references/core-api/INDEX.md` (the portal inconsistencies listed there may be
   fixed or new ones may appear) and bump every `verified` date you re-checked.
4. Run the evals (below), bump `metadata.version`, and package.

## Add a capability

1. Add a `## N. <Capability>` section to `SKILL.md` (workflow steps, which reference files to read and when,
   delivery format) and a row to the routing table in § 1. Stay inside the line budget.
2. Create `references/<name>/` with an `INDEX.md` and the first reference files (provenance headers), and
   update the top-level `references/INDEX.md`.
3. Add at least two evals to `evals/evals.json` (one typical, one edge case).
4. If the new domain needs a new trigger-phrase family, adjust the description within the 1024 cap.
5. Bump `metadata.version` and update the marketplace and repository README descriptions.

Planned capabilities (candidates): Cin7 Omni API integration (its own developer documentation; a separate
`references/omni-api/` folder, and the product-pinning rule in `SKILL.md` § 2 already anticipates it); Cin7
Core UI and setup procedures (modules, settings that gate API behaviour such as "Use Put Away" and the
automation module); the previous (v1) API for legacy integrations.

## Validate

After any change to SKILL.md wording or the references, run the evals in `evals/evals.json` by hand or with
skill-creator's eval loop and compare against `expected_output`. Check the frontmatter against the spec with
`skills-ref validate ./cin7-assistant` (`pip install skills-ref`, github.com/agentskills/agentskills) if you
want an independent pass, and run `python scripts/package_skill.py skills/cin7-assistant dist` to confirm it
packages.
