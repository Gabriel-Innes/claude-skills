# Release notes index

One distilled extract per Sage X3 V12 release, compiled from Sage's official release-notes API
(`https://online-help.sagex3.com/x3-release-notes/api/en-US/`) by `scripts/build_release_notes_x3.py` on 2026-10-02.
Read `<release-id>.md` § 1–3 first (components shipped → **tables / local menus / data types whose dictionary definition
changed** → behaviour changes), then § 4 for what's new by module, § 5 for entry points. For Sage's wording, the full
bug-fix list and known issues, open the human-readable page `https://online-help.sagex3.com/x3-release-notes/index.html#/release/en-US/<release-id>`
or the Applicative / Platform Readme named in each file's header - the verbatim Sage text is **not** bundled.

| Path | Release | GA | What's-new items | Tables touched | Behaviour changes | Entry points | Fixes | Key components shipped | Verified |
|---|---|---|---|---|---|---|---|---|---|
| `2026-r1-39.md` | 2026 R1 (12.0.39) | May 2026 | 70 | 11 | 3 | 13 | 305 | Syracuse 12.24.0, Console 2.63.0, MongoDB 8.2.5 / 8.0.17.4, Print Server 3.3.0, Runtime 96.4.206, ATP 5.0.0 | 2026-10-02 |
| `2025-r2-38.md` | 2025 R2 (12.0.38) | November 2025 | 62 | 6 | 5 | 16 | 286 | Syracuse 12.23.0 (12.22.5), Console 2.62.0, MongoDB 8.0.9, Print Server 3.2.0, Runtime 96.4.188, ATP 4.1.0 | 2026-10-02 |
| `2025-r1-37.md` | 2025 R1 (12.0.37) | May 2025 | 68 | 9 | 6 | 22 | 284 | Syracuse 12.22.0, Console 2.61.0, Print Server 3.1.0, Runtime 96.3.114, ATP 4.0.0 | 2026-10-02 |
| `2024-r2-36.md` | 2024 R2 (12.0.36) | November 2024 | 59 | 5 | 5 | 23 | 293 | Syracuse 12.21.0, Console 2.60.0, MongoDB 7.0.11, Print Server 3.0.0, ATP 3.3.0 | 2026-10-02 |
| `2024-r1-35.md` | 2024 R1 (12.0.35) | April 2024 | 36 | 2 | 2 | 16 | 216 | Syracuse 12.20.0, Console 2.59.0, Print Server 2.30.0, Runtime 96.1.207 / 96.2.84 | 2026-10-02 |
| `2023-r2-34.md` | 2023 R2 (12.0.34) | November 2023 | 41 | 13 | 4 | 19 | 285 | Syracuse 12.19.0, Console 2.58.0, MongoDB 4.4.22, Print Server 2.29.0, Runtime 96.1.206 | 2026-10-02 |

"Tables touched" counts the distinct tables named as `ATB (META/TABLES)` modified elements in that patch's Applicative
Readme - Sage's own record that a fix or change altered the table definition. It is the per-patch schema evidence; for
the resulting V11 → V12 column differences of a given table run `python scripts/diff_table_versions.py TABLE`.

Not bundled: 2023 R1 (12.0.33) and earlier - archived by Sage at
`https://online-help.sagex3.com/x3-release-notes-arch/en_US/ReleaseNote/RELNOTE_V12.0.33.htm` (same pattern per patch);
their platform boundaries are in `../upgrades/platform-matrix.md`. Lifecycle stage per release:
`../upgrades/upgrade-guide.md` § 1.
