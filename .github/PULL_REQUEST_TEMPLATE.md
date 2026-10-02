<!-- Keep PRs focused. Commit messages: type(scope): summary (feat / fix / docs / refactor / chore …). -->

## What and why

<!-- What changed, and why. For a reference correction, state your source and its date. -->

## Type

- [ ] Reference correction (wrong/missing fact in a bundled reference)
- [ ] New capability on an existing skill
- [ ] New skill
- [ ] Docs / tooling / chore

## Checklist

- [ ] Every new or changed claim is **verifiable from a bundled reference or the vendor's docs, and cited**
- [ ] No SQL that **modifies** vendor-owned tables; generated code uses the vendor's API/SDK for writes
- [ ] No **vendor source material** (CHMs, DLLs, raw SDK help) committed; generated references only
- [ ] If a reference is script-generated, I changed the **source/builder and regenerated** (not the output by hand)
- [ ] Affected `INDEX.md` / provenance headers / `README` row updated; **no broken links or claimed-but-missing files**
- [ ] `SKILL.md` frontmatter still valid (name matches folder, description ≤ 1024, compatibility ≤ 500)
- [ ] Evals updated/added if a skill's behaviour or wording changed
