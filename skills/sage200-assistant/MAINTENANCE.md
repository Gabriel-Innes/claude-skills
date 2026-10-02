# Maintaining the Sage 200 Evolution Assistant skill

Owner: Francois Taljaard. Format: [Agent Skills](https://agentskills.io/specification) — the checks below keep
the skill inside that spec and its best-practices guide. Modelled on the `sage300-assistant` skill.

## Structure and budgets (from the Agent Skills spec)

- `SKILL.md` is the only file loaded on activation: keep it **under 500 lines / ~5,000 tokens**. It holds
  routing, ground rules, one workflow section per capability, the gotchas list and the layout. Bulk always
  goes to `references/`.
- References are **one hop from SKILL.md** (`references/<domain>/<file>` or `.../INDEX.md`). The per-folder
  `INDEX.md` is the only indirection layer; don't add another.
- Paths in SKILL.md and references are **relative to the skill root**; no placeholders.
- Frontmatter: `name` (matches the folder `sage200-assistant`), `description` ≤ 1024 chars (describe domains
  and trigger contexts, don't enumerate phrases), `compatibility` ≤ 500 chars, `metadata` string map. Bump
  `metadata.version` (YYYY.MM) on each release.
- Every claim SKILL.md makes about a file must be true — no "planned" files in tables; describe planned
  capabilities (SQL / data dictionary, versions / upgrades) in prose only.
- Gotchas (concrete corrections an engineer would otherwise get wrong) live in `SKILL.md` § 4. When the
  assistant gets something wrong in use, add the correction there.

## Rebuilding the SDK reference from the CHM

The SDK reference under `references/sdk/api/` and `references/sdk/enums/` is generated from the shipped
`docs/Pastel.Evolution.chm` (primary) with summaries backfilled from
`docs/Pastel.Evolution.11.0.0.10/Pastel.Evolution.xml`. Source material in `docs/` is **never packaged** and
**never read at runtime** — only the generated markdown is.

To regenerate (Windows), with `PYTHONUTF8=1` so the emoji/Unicode in output doesn't die on cp1252:

1. Decompile the CHM to a **space-free** path (the extractor is fussy about spaces):

   ```
   cp docs/Pastel.Evolution.chm /c/temp/evo/Pastel.Evolution.chm
   cd /c/temp/evo && hh.exe -decompile chm Pastel.Evolution.chm
   ```

   This yields ~4,000 `.htm` pages plus `EvolutionSdk.hhc` (the table of contents). 7-Zip also extracts CHMs.

2. Run the generator:

   ```
   PYTHONUTF8=1 python scripts/build_sdk_ref.py \
     /c/temp/evo/chm \
     docs/Pastel.Evolution.11.0.0.10/Pastel.Evolution.xml \
     references/sdk \
     --verified YYYY-MM-DD
   ```

   It parses `EvolutionSdk.hhc` (nested Sandcastle sitemap), emits only the main `Pastel.Evolution` namespace
   (skips `Pastel.Evolution.Internal`), and writes size-bounded bundles (`classes-NN.md` ~150 KB,
   `enums-NN.md` ~90 KB) plus `api/INDEX.md` and `enums/INDEX.md` with a **file + line range** per entry.
   `scripts/bundle_util.py` does the bundling. It prints the type/enum/file counts — sanity-check them
   (currently 152 types in 3 files, 41 enums in 1 file).

3. After a rebuild, update the counts cited in `SKILL.md` (§ 3, § 5), `references/sdk/INDEX.md` and the SDK
   version wherever it appears, and re-read one or two entries to confirm headings and line ranges align
   (the `INDEX.md` line range must land on the entry's `# <Type> (` heading).

### Upgrading to a newer SDK version

Replace the files in `docs/` with the newer CHM + DLLs + XML, rerun the generator with the new `--label`
(SDK version) and `--verified` date, and bump `metadata.version` and every "SDK 11.0.0.10" mention. The CHM is
Sandcastle format; if a future SDK ships a different help format the extraction regexes in `build_sdk_ref.py`
(`summary`, `csharp`, `parameters`, `returns`, `remarks`, the enum member table) may need adjusting.

## Packaging and validation

Keep the folder named `sage200-assistant` (the archive is named after it). Package with the skill-creator
packager (as for the other skills in this repo), `PYTHONUTF8=1` on Windows. `docs/` is source material and is
not packaged. The reference validator `skills-ref validate ./sage200-assistant`
(github.com/agentskills/agentskills, `pip install skills-ref`) checks the spec rules.

## Adding a capability

Planned next capabilities mirror `sage300-assistant`:

- **SQL / data dictionary** — the table/field layout of the Evolution company database, to turn a requirement
  into verified read-only SQL. Add `references/dictionary/` + a `build_dict.py`, a routing row and a workflow
  section in `SKILL.md`.
- **Versions & upgrades** — what an Evolution release needs and what changed. Add `references/upgrades/` +
  `references/release-notes/` and the matching `SKILL.md` sections.

Each new capability: add a routing-table row, a numbered workflow section, any gotchas, and a `references/`
subtree with its own `INDEX.md`; keep `SKILL.md` under budget.
