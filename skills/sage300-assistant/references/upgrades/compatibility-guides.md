<!-- source: https://docs.sage.com/docs/en/customer/300erp/<YEAR>/open/Sage300_CompatibilityGuide.pdf for 2023 (ed. March 6, 2025), 2024 (ed. November 4, 2025), 2025 (ed. May 21, 2026), 2026 (ed. May 21, 2026) | version: Sage 300 2023–2026 | verified: 2026-09-23 -->
# Sage 300 Compatibility Guides 2023–2026 — platform matrix

Sage **re-issues** each version's Compatibility Guide as platforms are retired or added, and the URL always serves the
current edition. The values below are therefore *what Sage supports today* for that version, not what was supported at
its launch (e.g. the 2023 guide no longer lists SQL Server 2016/2017 or Windows Server 2016). When a client runs an
older platform, say so: it may have been supported at the time but is now outside Sage's support statement.
For the full guide text (incl. hardware sizing tables), see Sage's official Compatibility Guide PDF for that
version (the source URL in this file's header); the verbatim PDF is not bundled.

## 1. Database, application server, workstation

| Sage 300 | SQL Server (Express / Standard / Enterprise) | Application server OS (64-bit only) | Workstation OS (64-bit, Pro/Enterprise) | Guide edition |
|---|---|---|---|---|
| 2026 | 2019, 2022, **2025** | Windows Server 2019, 2022, 2025 | Windows 11; Windows 10 only up to the March 2026 releases | May 21, 2026 |
| 2025 | 2019, 2022, **2025** | Windows Server 2019, 2022, 2025 | Windows 11; Windows 10 only up to the March 2026 releases | May 21, 2026 |
| 2024 | 2019, 2022 | Windows Server 2019, 2022, 2025 | Windows 11; Windows 10 only up to the March 2026 releases | November 4, 2025 |
| 2023 | 2019, 2022 | Windows Server 2019, 2022, 2025 | Windows 10, 11 (Windows 10 "support discontinued October 2025; issues may not be addressed") | March 6, 2025 |

Windows 10 statement (2024–2026 guides, verbatim in substance): Sage tested the December 2025, January and March 2026
payroll tax updates and the November 2025 product updates (2026.1, 2025.4, 2024.8) on Windows 10; **from the releases
planned for April 2026, Sage 300 is no longer tested on Windows 10**. Any PU or tax update from April 2026 on → Windows 11.

Applies to every version listed:
- Binary collation such as `Latin1_General_BIN` recommended for the Sage databases.
- Terminal Server / Citrix XenApp supported for **classic (VB) screens only**, not web screens; Citrix/TS servers should be dedicated and separate from the database engine, with full System Manager installed on them.
- Virtual: VMware ESX, Hyper-V, Azure supported; Sage only addresses issues reproducible in a physical environment and no performance issues in virtual ones.
- Unlisted platforms are unsupported; Sage's support for platforms their vendor has retired is not guaranteed.

## 2. Office and web screens

| Sage 300 | Excel for desktop Financial Reporter (per workstation) | Financial Reporter for the Web | Outlook for e-mail print destination | Web-screen server | Browsers |
|---|---|---|---|---|---|
| 2026, 2025, 2024 | 2016, 2019, 2021 (32/64-bit), 2024 (64-bit), 365 (32/64-bit) | Excel 365 **64-bit** on server and workstation | 2016, 2019, 2021, 2024 (64-bit), 365 | Windows Server 2019/2022/2025 + IIS (static content, ASP.NET) + Portal DB on a supported SQL Server | current Edge, Chrome, Firefox |
| 2023 | 2016, 2019, 2021, 365 | Excel 365 on the server | 2016, 2019, 2021, 365 | as above | as above |

Office deployed through App-V is not supported (all years). Sage Intelligence Analysis module is not compatible with Excel 2003 (still stated).

## 3. End-to-end matrix (other Sage products tested with each version)

| Sage 300 | Sage CRM | Sage Fixed Assets | Sage HRMS |
|---|---|---|---|
| 2026 | 2026 R1 | 2026.0 | latest tax update |
| 2025 | 2026 R1 | 2026.0 | latest tax update |
| 2024 | 2025 R1 | 2026.0 | Q3-2025 |
| 2023 | 2024 R1 | 2024.1 | Q2-2024 |

CRM integrates A/R, A/P, O/E, P/O, PJC; Fixed Assets integrates G/L, A/P, P/O.

## 4. Hardware sizing (2026 guide; earlier guides are the same shape)

Sage's "recommended configurations" by edition — Standard 1–5 users, Advanced 5–10, Premium 10+:
- **Sage 300 application server**: quad-core, 32 GB RAM (Premium: quad-core/Xeon, 64 GB), 5 GB for program files.
- **Database server**: quad-core, 32 GB (Premium 64 GB), SQL Server 2019/2022/2025 on Windows Server 2019/2022/2025 x64; 500 GB / 1 TB / 1.5 TB free disk; RAID 5/10 for data files, RAID 1 for log files. Standard edition may share the application server (extra resources).
- **Web-screen server**: quad-core, 16 GB (Premium 32 GB), 5 GB; may share the application server on Standard/Advanced.
- **Workstation**: Core i5+, 8 GB RAM, 100 MB, Windows 10/11.
- **Citrix/Terminal server** (Premium): quad-core/Xeon, 64 GB, ~40 concurrent sessions.
- SQL Express is acceptable for Standard edition only; hot-standby database recommended; RAID 10 (min 5) for DB/file servers, RAID 1 for app/web servers.

## 5. Using this file
- Blockers question ("can they upgrade to 2026 on SQL 2017 / Server 2016?") → § 1: no; SQL Server and/or Windows must move first.
- Quote the guide edition date with the answer; if the client's target PU is newer than the edition, re-fetch the PDF (URL in `upgrade-guide.md` § 2).
- Everything here is platform support, not functionality — release-level changes are in `../release-notes/<year>.md`.
