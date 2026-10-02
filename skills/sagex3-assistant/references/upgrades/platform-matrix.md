<!-- source: https://online-help.sagex3.com/erp/12/en-us/Content/V7DEV/prerequisites_overview.html and the per-component V12 prerequisite pages (page date published 8 September 2026); https://online-help.sagex3.com/erp/11/en-US/V7DEV/prerequisites_overview.html and per-component V11 pages (undated, V11 is end of maintenance); component versions from Sage's Platform Readmes (Readme-Components-ENG-12.0.34 … 12.0.39, release-notes API) and the Sage Community "Sage X3 Version 12: Latest Release Information" post (read 2026-10-02) | version: Sage X3 V12 2019 R5 – 2026 R1, V11, V7/U8/U9 | verified: 2026-10-02 -->
# Sage X3 platform matrix - what each release supports

Sage keeps **one** prerequisites page per major version and re-publishes it; the V12 page states support *by
release* ("since release 2025 R1/V12.0.37 …"), so a client's patch level decides the row. Read § 1 for V12, § 2 for
V11 and older. Sage certifies at the "top" level: the latest patches of a listed OS / database / JDK version may be
applied (support deck, Dec 2024). Anything not listed is unsupported. For the full page text (hardware sizing,
service accounts, Oracle parameters), fetch the source URL in the header; it is not bundled.

## 1. Sage X3 V12 - by release

### 1.1 Database

| Database | Supported with | Notes |
|---|---|---|
| Microsoft SQL Server 2016, 2017 (SE, EE, BI) | releases **before 2020 R3 / 12.0.23** | **2016 no longer supported since 2026 R1 / 12.0.39** |
| SQL Server 2019 (SE, EE, BI) | 2020 R3 / 12.0.23 → 2023 R1 / 12.0.33 and later | |
| SQL Server 2022 (SE, EE, BI) | since 2023 R1 / 12.0.33 | the per-component page is titled "SQL Server 2022/2019" |
| Oracle 12c R1 / R2 (SE2, EE) | releases before 2020 R2 / 12.0.22 | **not supported since 2026 R1 / 12.0.39**; 12cR1 "should absolutely not be used", 12cR2 end of life |
| Oracle 19c (SE2, EE), 19.3.0.0+ | since 2020 R2 / 12.0.22 | only 19c certified on Windows Server 2019+; on Windows Server 2025 since Sept 2025 with the Oracle 19.27 patch; BEQ protocol only with 19c on a single host |

SQL Server instance rules (V12 page): named instance recommended (an unnamed one must be `MSSQLSERVER`); collation
**`Latin1_General_BIN2`** (databases created earlier with `Latin1_General_BIN` stay supported); **mixed-mode
authentication mandatory**; `sa` or another sysadmin login; TCP/IP enabled (mandatory when a runtime or print server
is on another host); SQL Server Browser running for a named instance. Oracle: TNS listener required (print server);
`SQLNET.AUTHENTICATION_SERVICES=NONE` during initial configuration (NTS may be restored after); **Oracle Unified
Auditing not supported**.

### 1.2 Server operating system

| OS | Supported with | Notes |
|---|---|---|
| Windows Server 2016 (Essentials, Standard, Datacenter) | releases before 2020 R2 / 12.0.22 | **not supported since 2026 R1 / 12.0.39**; since 2025 R1 / 12.0.37 Sage tells WS 2012/2016 sites to move to 2019/2022/2025 |
| Windows Server 2019 | 2020 R2 / 12.0.22 → 2022 R3 / 12.0.32 and later | |
| Windows Server 2022 | 2023 R1 / 12.0.33 → 2024 R2 / 12.0.36 and later | **recommended host for MongoDB 7/8** (see 1.3) |
| Windows Server 2025 | since 2025 R1 / 12.0.37 | MongoDB 7/8 not certified on it as of April 2025; Oracle 19c on it since Sept 2025 (19.27) |
| Windows Server 2012 R2 | - | Sage stopped supporting it in 2022; Microsoft EOL 10 Oct 2023 |
| Red Hat / Oracle Enterprise Linux 7 | before 2022 R4 / 12.0.32 | |
| RHEL / OEL 8 | 2022 R4 / 12.0.32 → 2024 R2 / 12.0.36 | |
| RHEL / OEL 9 | since 2025 R1 / 12.0.37 | Linux is Oracle-database only on the application tier |

### 1.3 Syracuse stack (web server), middleware, tooling

| Component | Version | Supported with |
|---|---|---|
| MongoDB 3.6 | | Syracuse 12.5 in 2019 R5 / 12.0.20 → 2020 R3 / 12.0.23 |
| MongoDB 4.0 | | Syracuse 12.8 in 2020 R3 / 12.0.23 |
| MongoDB 4.2 | | Syracuse 12.9 in 2020 R4 / 12.0.24 → 2021 R4 / 12.0.29 (MongoDB < 4.2 is incompatible with Windows Server 2019) |
| MongoDB 4.4 | | since Syracuse 12.14 in 2022 R1 / 12.0.29 (4.4 incompatible with Windows Server 2012 R2) |
| MongoDB 7 | 7.0.11 shipped with 2024 R2 | since Syracuse 12.21 in 2024 R2 / 12.0.36 |
| MongoDB 8 | 8.0.9 (2025 R2), 8.2.5 / 8.0.17.4 (2026 R1, MongoBleed CVE-2025-14847 fix) | since Syracuse 12.23 in 2025 R2 / 12.0.38 - **MongoDB 8 is mandatory from 2025 R2** (Sage announcement; the installer is on the X3 ISO) |
| Elasticsearch 6.4 / 6.8 | | Syracuse 12.3 (before 2020 R1) / Syracuse 12.6 (2020 R1 / 12.0.21 → 2020 R3) |
| Elasticsearch 7.16 | | Syracuse 12.9 in 2020 R4 / 12.0.24 → 2023 R1 / 12.0.33 |
| Elasticsearch 8 (latest) | | since Syracuse 12.19 in 2023 R2 / 12.0.34. **No longer mandatory since 2022 R4** (support deck); delete the indexes before upgrading it |
| Java | latest Java 8 | 2020 R2 / 12.0.22 → 2024 R1 / 12.0.35 |
| Java | **latest Java 11 (JDK/JRE 11)** | since 2024 R2 / 12.0.36 - a standalone JDK 11 must be installed before any component; Print Server and Classic Web embed their own Java |
| Node.js | bundled | a validated Node.js ships inside the Syracuse, X3 Services and ATP setups - do not install your own |
| Microsoft PowerShell | 7.2 or later (latest recommended) | **required since 2022 R4 / 12.0.32** on the runtime server (Windows and Linux); SQL Server module 21 (2022 R4 – 2023 R1), **22 or later since 2023 R2 / 12.0.34**, and since 2023 R2 also on the SQL Server database server |
| Apache HTTP server | - | **deprecated from 2022 R2**; install only for the specific applications the page lists. Console 2.63 (2026 R1) sets `UseApache=false` for new solutions |
| .NET Framework | 4.7.2 | Console and Print Server (installed by the Console setup; reboot mandatory) |
| Crystal Reports Designer | CR 2016, 2020, 2025 | Print Server ≥ 2.18 for CR 2016+; Print Server 2.19+ runs the CR 2020 runtime and reads older reports |

### 1.4 Clients

| Client | V12 (page of Sept 2026) |
|---|---|
| Browsers (desktop) | Chrome 136+ (certified), Firefox 138+ (certified), Chromium Edge 136+ (compatible), Safari 18+ on macOS (certified); Linux browsers "compatible only" |
| Mobile | iOS 18+, Android 15+ (Chrome 136+ / Firefox 138+ certified, Edge compatible, Safari 18.4+ compatible); iPad excluded |
| Workstation OS | Windows 10 and 11 (Sage: **Windows 10 no longer supported since October 2025 - use Windows 11**); Console also on Windows 7/8/8.1 |
| Office add-in | Office / Outlook 2010, 2013, 2016, 2019 and Office 365 on-premises (32/64-bit); no Office online, no macOS add-in |
| Management Console | Windows 7–11 or Windows Server 2019/2022/2025, .NET 4.7.2, JDK 11 |
| In-app guides | outbound 80/443 to the `pendo.io` domains listed on the overview page |

### 1.5 Component versions shipped per release (Platform Readmes)

| Release | Console | Syracuse | MongoDB | Print Server | Runtime | ATP | Other |
|---|---|---|---|---|---|---|---|
| 2023 R2 (12.0.34) | 2.58.0 | 12.19.0 | 4.4.22 | 2.29.0 | 96.1.206 | - | VTWebServer 2.42.1, X3 Services 30–33 |
| 2024 R1 (12.0.35) | 2.59.0 | 12.20.0 | - | 2.30.0 | 96.1.207 / 96.2.84 | - | VTWebServer 2.42.2/.3, X3 Services 36–41 |
| 2024 R2 (12.0.36) | 2.60.0 | 12.21.0 | 7.0.11 | 3.0.0 | - | 3.3.0 | VTWebServer 3.0.0, X3 Services 48.0.41 |
| 2025 R1 (12.0.37) | 2.61.0 | 12.22.0 | - | 3.1.0 | 96.3.114 | 4.0.0 | VTWebServer 3.1.0, X3 Services 54.0.36, Eclipse Studio 2.1.10 |
| 2025 R2 (12.0.38) | 2.62.0 | 12.23.0 (12.22.5 hotfix) | 8.0.9 | 3.2.0 | 96.4.188 | 4.1.0 | X3 Services 56 / 60.0.42 |
| 2026 R1 (12.0.39) | 2.63.0 | 12.24.0 | 8.2.5 (8.0.17.4) | 3.3.0 | 96.4.206 | 5.0.0 | VTWebServer 3.2.0, X3 Services 64.0.75, Adxadmin 96.4.206, Web Scheduling 2025.1.4 |

Sage's release-information post (Community, read 2026-10-02) lists the *currently recommended* Syracuse builds as
12.24.6.5 (2026 R1), 12.23.11.8 (2025 R2), 12.22.15.5 (2025 R1), 12.21.16.2 (2024 R2) and warns: **from February 2026
Syracuse versions are no longer backward compatible with earlier X3 patch levels - follow Sage's component matrix
for the client's exact patch.** A "-" above means the readme for that release carried no fixes for the component (the
previous version continues).

## 2. Sage X3 V11 and older (end of maintenance - for clients still running them)

V11 reached **end of maintenance on 1 April 2024** (final patch 11.0.22, March 2022). Values from the V11 prerequisites
overview (table columns V7 / Update 8 / Update 9 / Version 11):

| Component | V7 | Update 8 (U8) | Update 9 (U9) | Version 11 |
|---|---|---|---|---|
| Oracle | 11gR2 SE/EE, 12c SE/EE | 11gR2 (upgrade only), 12c | 11gR2 (upgrade/compatible only), 12c | **12c R1 SE2, EE** (12.1.0) |
| SQL Server | 2012 SP2 SE/EE, 2014 SE/EE/BI | 2012 SP2 (upgrade only), 2014 | 2012 SP2 (upgrade/compatible only), 2014 | **2014 SE/EE/BI, 2016 SE/EE/BI** |
| MongoDB | 2.4 | 2.6 | 3.0 → 3.2.6 (U9.4) → 3.2.11 (U9.6) → 3.4.16 (U9.11) → 3.6 (U9.19) → 4.0 (U9.24) | 3.2.6 → 3.2.11 (Web server 11.3) → 3.4.16 (11.11) → 3.6 (11.19 / V11.15) → 4.0 (11.23 / V11.18) → 4.2 (11.24 / WH 11.10) |
| Windows Server | 2008 R2, 2012 | 2008 R2 (upgrade only), 2012 | 2008 R2 (upgrade/compatible), 2012 | **2012 (R2), 2016** |
| RHEL / OEL | 6.x (6.2+) | 6.x | 7.x | 7.x; AIX 7.1 "to be deprecated, no new configuration" |
| Node.js | 0.10.46 | 0.10.46 | 0.12.15 – 10.0.0 | 4.6.0 – 12.20.x |
| Elasticsearch | 0.90 | 0.90 | 1.5 | 1.5 → 6.4 / 6.8 (Web server 11.22 / V11.17) → 7.9 (11.23 / V11.18) |
| JVM | 7.x | 7.x | 7.x | 8u291 |
| Apache | 2.2 | 2.2.25 | 2.2.25 | 2.2 (2.2.25 no_ssl) |
| .NET | 3.5 and 4 | 3.5 and 4 | 3.5 and 4 | 3.5 and 4 (Console: 4.6) |
| Browsers | Chrome 33+, Firefox 28+, IE10/11 | Chrome 38+, Firefox 36+ | Chrome 87+, Firefox 78+, Edge | Chrome 87+, Firefox 78+, Safari 13+, Edge (EdgeHTML 15); **IE 11 not supported** (keep it installed for the Office plugin) |
| Office | 2010, 2013 | 2010, 2013 | 2010, 2013, 2016 (+365 2013/2016 on-prem) | 2010, 2013, 2016 (+365 on-prem) |

V11-specific rules: SQL Server collation `Latin1_General_BIN`, mixed mode, named instance, SQL Browser running; with
SQL Server 2016 use **Console CFG.239 or later** (CFG.236 breaks sequence-value export) and **SSMS 16.5.3** (the SQL 2016
page says later versions should not be used; the Console page accepts 16.5.3–17.x but notes 17.1/17.2 may lack
`OSQL.exe`, which every machine running an X3 runtime needs); Oracle `SQLNET.AUTHENTICATION_SERVICES=NONE` (Windows) /
`BEQ` (Linux), `SQLNET.ALLOWED_LOGON_VERSION=8`; Crystal Reports 2013 / 2016 (Print Server ≥ 2.18 for CR 2016);
Production Scheduler 4.5.2 x64 mandatory (on-premise only).

## 3. Reading the matrix for a client

1. Pin the client's **release/patch** (`YYYY Rn` / `12.0.xx`) and database. The "since release" boundaries above decide
   whether their OS/DB is still supported *at their patch*, and what the target release requires.
2. The target release pulls platform moves with it - typical 2023 R1 → 2026 R1 consequences: Windows Server 2016 out,
   SQL Server 2016 / Oracle 12c out, MongoDB 8 mandatory (so Windows Server 2022, not 2025, for the Mongo host as of
   the April 2025 note), JDK 11, PowerShell 7.2+ with SQL Server module 22+, Elasticsearch 8 (optional), Windows 11
   clients.
3. Quote the page date ("prerequisites overview published 8 September 2026") - Sage re-issues it, and today's page
   states today's support, not the support at the release's launch.
