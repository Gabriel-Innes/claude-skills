# Upgrades index

| Path | Covers | Verified |
|---|---|---|
| `upgrade-guide.md` | Version naming (V6 … V11, V12 `YYYY Rn` = `12.0.xx`), the Sage X3 Lifecycle Policy (Current / Standard / Extended, 24 months per V12 release, end-of-maintenance dates), where the official documentation lives (URL patterns), supported upgrade paths and minimum patches, the three upgrade methods (in-place "easy" upgrade, folder upgrade / migration, re-implementation), the official in-place and folder-upgrade procedures step by step, the `UU*` upgrade processes by module, how to assess SQL / integration impact (dictionary V11 → V12, tables touched per release, `scripts/diff_table_versions.py`), verification SQL, the standard answer shape | 2026-10-02 |
| `platform-matrix.md` | What each release supports: database (SQL Server 2016 → 2022, Oracle 12c → 19c), Windows Server 2016 → 2025, RHEL/OEL 7 → 9, MongoDB 3.6 → 8, Elasticsearch, Java 8 → 11, PowerShell, Apache deprecation, browsers / Office / Crystal, component versions shipped per release 2023 R2 → 2026 R1; the V7 / U8 / U9 / V11 matrix for legacy clients | 2026-10-02 |

Per-release detail (what's new, behaviour changes, **tables and local menus whose dictionary definition changed**,
entry points, component versions) lives in `../release-notes/<release-id>.md` for 2023 R2 → 2026 R1; `../release-notes/INDEX.md`
lists them. The verbatim Sage pages, PDFs and readmes are not bundled - the guide § 2 gives the URL of each so the
exact wording can be fetched on demand.
