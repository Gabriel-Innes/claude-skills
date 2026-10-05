# Maintaining the Cin7 Assistant skill

Owner: Francois Taljaard. Format: [Agent Skills](https://agentskills.io/specification).

This skill is a **scaffold**: no capability is implemented, no references are bundled, and `scripts/` holds
only the packaging script. This file records the conventions the skill will follow so that the first
capability is built the same way as the other assistants in this repository.

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
- Gotchas (corrections an engineer would otherwise get wrong) belong in `SKILL.md` § 4.

## File limit and packaging

Claude accepts at most **200 files** in an uploaded skill. Package for upload with
`python scripts/package_skill.py skills/cin7-assistant dist` (needs PyYAML). It refuses to write the archive
if the frontmatter is invalid or there are more than 200 files, and writes `dist/cin7-assistant.skill` plus
an identical `.zip`. Both are git-ignored. Upload in Claude under Settings, Capabilities, Skills.

## Conventions for reference files

- **Provenance header** on every file:
  `<!-- source: <URL or document> | version: <Cin7 product and version, or "not stated"> | verified: YYYY-MM-DD -->`
- **INDEX.md** in every `references/<domain>/` folder: one line per file (path, what it covers, product and
  version, verified date), plus a sources table with URL, role and date.
- **Extract the facts; do not paste.** Bundle endpoint shapes, parameter syntax, headers, status codes, field
  lists, enum values and rules, each attributed to its source page, never page text wholesale. Raw caches of
  vendor documentation stay in a scratch workspace, uncommitted.
- **Name the product.** Cin7 Core (formerly DEAR Systems) and Cin7 Omni have separate APIs and data models;
  every reference file and every fact must say which product it describes.
- Grep-friendly: one fact per line or table row, stable headings.

## Add a capability

1. Add a `## N. <Capability>` section to `SKILL.md` (workflow steps, which reference files to read and when,
   delivery format) and a row to the routing table in § 1. Stay inside the line budget.
2. Create `references/<name>/` with an `INDEX.md` and the first reference files (provenance headers), and
   update the top-level `references/INDEX.md`.
3. Add at least two evals to `evals/evals.json` (one typical, one edge case).
4. If the new domain needs a new trigger-phrase family, adjust the description within the 1024 cap.
5. Remove the scaffold status notice at the top of `SKILL.md` and the "no references" wording in § 5 once the
   first capability lands, and bump `metadata.version`.
6. Register the skill in `.claude-plugin/marketplace.json` and replace the "coming soon" row in the repository
   `README.md` with a real description.

Planned capabilities: not yet decided. Candidates follow the pattern of the other assistants (API integration
development from the vendor's own API reference, data model and field lookup, versions and changes), scoped
per product (Cin7 Core, Cin7 Omni).

## Validate

After any change to SKILL.md wording or the references, run the evals in `evals/evals.json` by hand or with
skill-creator's eval loop and compare against `expected_output`. Check the frontmatter against the spec with
`skills-ref validate ./cin7-assistant` (`pip install skills-ref`, github.com/agentskills/agentskills) if you
want an independent pass, and run `python scripts/package_skill.py skills/cin7-assistant dist` to confirm it
packages.
