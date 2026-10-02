# Release notes index

One distilled extract per Sage 300 version year. Read `<year>.md` first (upgrade warnings table -> changes per
PU with integration impact -> schema verdict). Each `<year>.md` also names which PU of the *previous* year
back-ported the same feature, so "is X in 2025 PU5?" is answerable. For exact Sage wording, a step list, a
fixed-issue reference number, or the full known-issues list, go to Sage's official Release Notes and Technical
Information pages (URLs in `../upgrades/upgrade-guide.md` § 2) — the verbatim Sage pages are **not** bundled.

| Path | Covers | Sage page published | Verified |
|---|---|---|---|
| `2026.md` | Sage 300 2026 (7.3A): 5 warnings, 2026.0 -> PU3, schema verdict vs 7.2A | 2026-09-14 | 2026-09-23 |
| `2025.md` | Sage 300 2025 (7.2A): 4 warnings (payroll web screens via tax update, CA/US tax-update parity, HR 8.0), 2025.0 -> PU6, payroll CHECKNUM widening | 2026-09-10 | 2026-09-23 |
| `2024.md` | Sage 300 2024 (7.1A): 4 warnings (PU1 hotfix, Global Search, HR 8.0), 2024.0 -> PU9, 1099 vendor columns | 2026-04-24 | 2026-09-23 |
| `2023.md` | Sage 300 2023 (7.0A): 7 warnings (security overhaul PU2/PU3, Fixed Assets, CRM CORS, SSL), 2023.0 -> PU10 | 2025-12-29 | 2026-09-23 |

Workstation Setup must be reinstalled after these PUs (from each year's Technical Information): 2023 PU4, 2024 PU9, 2025 PU6, 2026 PU3.
Not bundled: Compatibility Guide PDFs (SQL Server / Windows / Office matrix) - see `../upgrades/upgrade-guide.md` § 5.
Source HTML is archived in `../../../docs/release notes/<year>/` (outside the package); regenerate with
`scripts/extract_release_notes.py` per MAINTENANCE.md.
