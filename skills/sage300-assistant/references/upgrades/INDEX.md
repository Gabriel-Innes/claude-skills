# Upgrades index

| Path | Covers | Verified |
|---|---|---|
| `upgrade-guide.md` | Version naming/support model, official doc URLs, universal upgrade rules, per-version changelog 2023→2026 (pointers to `../release-notes/<year>.md`), SQL Server/Windows matrix summary, post-upgrade verification SQL, standard answer shape, maintenance steps | 2026-09-23 |
| `compatibility-guides.md` | Platform matrix from the Sage Compatibility Guides 2023–2026: SQL Server, Windows Server, workstation OS (Windows 10 cut-off), Office/Excel, web-screen server, CRM/Fixed Assets/HRMS pairing, hardware sizing. Read for any "can they run X on Y" blocker question. | 2026-09-23 |
| `raw/<year>-compatibility-guide.md` | Full text of each year's Compatibility Guide PDF (current edition), incl. virtual/Citrix guidance and the recommended-configuration tables | 2026-09-23 |

Per-year release detail lives in `../release-notes/<year>.md` (2023–2026, with the full Release Notes and Technical
Information pages under `raw/`); the guide keeps the cross-version view. Source PDFs are archived in
`../../../docs/compatibility guides/` (outside the package).
