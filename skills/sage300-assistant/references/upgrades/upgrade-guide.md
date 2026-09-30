<!-- source: Sage 300 Release Notes / Technical Information / Compatibility Guide 2023–2026 (help.sage300.com, docs.sage.com) | version: 2023–2026 | verified: 2026-09-23 -->
# Sage 300 versions and upgrades

Curated reference for answering "client is on version X and wants to go to version Y" questions.
Read this whole file before answering any upgrade question. Sections 1–3 are stable facts;
Section 4 is a per-version changelog that must be **extended when a new Sage 300 version ships**
(see "Maintaining this file" at the end).

**Verified against Sage's published release notes, Technical Information and Compatibility Guides
as of September 2026.** Anything after that date must be confirmed with a web search of the
official docs (Section 2) before it is stated as fact.

## Contents
1. Version naming and support model
2. Where the official documentation lives (search these first)
3. Universal upgrade rules (apply to every version jump)
4. Per-version changelog, integration-relevant (2023 → 2026)
5. Compatibility matrix — SQL Server / Windows
6. What an upgrade does and does not do to the database
7. Post-upgrade verification SQL
8. Standard answer shape
9. Maintaining this file

## 1. Version naming and support model

- Versions are named by year: Sage 300 **2023**, **2024**, **2025**, **2026**. Internally these are
  7.0A, 7.1A, 7.2A, 7.3A ... but the year is what clients and Sage docs use. Older releases were
  named 6.xA. Bundled data dictionaries: 7.0A–7.3A (= 2023–2026) and 6.0A; see `references/dictionary/INDEX.md`.
- A major version ships once a year, roughly **August–September**. Sage 300 2026.0 was
  released September 2025; Product Updates (PU1, PU2, PU3 ...) follow every few months.
  A PU is a patch set, **not** a database-converting upgrade; it can include workstation-setup
  changes that require reinstalling Workstation Setup on every workstation.
- Sage supports the current version plus roughly two prior ones. Write "2026.3" for "2026 PU3".
- Sage 300 2026 accepts a direct upgrade from **version 5.6 or later** in one step — there is no
  need to hop through intermediate versions (e.g. 2023 → 2026 is one conversion). All Sage 300
  programs must be upgraded to the same version at once; mixed versions do not run.

## 2. Where the official documentation lives

Search/fetch these before stating anything not in this file. Substitute the year.

| Document | URL pattern |
|---|---|
| Release Notes (features + important upgrade warnings per version and PU) | `https://help.sage300.com/en-us/<YEAR>/classic/Content/ReleaseDocs/ReleaseNotes.htm` |
| Technical Information (program fixes, upgrade-from rule, known issues, PU workstation-setup rule) | `https://help.sage300.com/en-us/<YEAR>/classic/Content/ReleaseDocs/TechnicalInformation.htm` |
| Compatibility Guide PDF (SQL Server / Windows / Office matrix) | `https://docs.sage.com/docs/en/customer/300erp/<YEAR>/open/Sage300_CompatibilityGuide.pdf` |
| Installation & Administration Guide PDF | `https://docs.sage.com/docs/en/customer/300erp/<YEAR>/open/Sage300_InstallationGuide.pdf` |
| Upgrade Guide PDF | `https://docs.sage.com/docs/en/customer/300erp/<YEAR>/open/Sage300_UpgradeGuide.pdf` |
| Enhanced Security guide (2024+) | `https://docs.sage.com/docs/en/customer/300erp/2024/open/Sage300EnhancedSecurityForV2024.pdf` |
| Documentation index (all versions) | `https://docs.sage.com/docs/en/customer/300erp/Documentation.htm` |
| Community announcements (release/PU availability) | `https://communityhub.sage.com/us/sage300/f/announcements` |

Prefer these over reseller blogs and "upgrade guide" SEO sites (many carry phone numbers and
are not Sage). Release Notes are public; some Knowledgebase (KB) articles need a customer login —
if a KB link is behind a login, say so and give the article number.

## 3. Universal upgrade rules (every version jump)

1. **Back up everything first**: every company database, the system database, the Portal
   database (web screens), and from 2023+ the Vault and Store security databases. The
   conversion is one-way.
2. **Upgrade in a test environment first**, run Day End and a full transaction cycle, and have
   the integration posted against it before touching production.
3. **All Sage 300 programs go to the same version at once** — System Manager, all modules,
   Payroll, and every workstation via Workstation Setup. Mixed versions do not run.
4. **Data conversion is per company**: after installing the new programs, run Database Setup /
   Data Activation for each company; each module converts its tables in sequence. Large IC/OE/PO
   histories take the longest.
5. **Third-party and custom products must be re-certified**: any add-on, Crystal report,
   customised UI, macro, ODBC/DSN consumer, or SQL view/integration must be checked against
   the new version. Sage explicitly tells customers to verify third-party compatibility before
   installing product updates.
6. **Reinstall Workstation Setup** on every workstation after the upgrade and after any PU that
   changes workstation setup (the Technical Information page lists which PUs do).
7. **Web screens**: after any upgrade or PU, re-run Database Setup to reconfigure the Portal
   database, and clear browser caches. See the version-specific uninstall rule in Section 4.
8. **Sage CRM integration**: reinstall the CRM integration component and the Synchronization
   Component after every upgrade/PU.
9. **Payroll**: reinstall the latest Tax Update after the core upgrade; if both Canadian and
   US Payroll are installed, both tax updates must be on the same version or web-screen login
   fails.
10. **Check the OS/SQL matrix before anything else** (Section 5) — an upgrade is often blocked
    by an unsupported SQL Server or Windows version rather than by Sage itself.

## 4. Per-version changelog — integration-relevant

Only changes that matter to a consultant planning an upgrade or to a SQL/API integration are
listed. UI polish is omitted. "Schema" means the company/system SQL tables.

### Sage 300 2023 (7.0A) — released ~Aug 2022

Detail: `../release-notes/2023.md`.

- **Security overhaul begins (2023.0–2023.3 / PU2–PU3)**: enforced complex passwords, Sage 300
  users now backed by per-user SQL logins, and new **Vault** and **Store** security databases
  alongside the system and company DBs. There is no longer an option to turn Sage 300 security
  off.
- **ODBC Driver 18 for SQL Server** becomes the default for new DSNs (2023.0, 2022.3, 2021.6
  onward). † Technical Information 2023 lists *SQL Server Native Client 11.0* as the installed
  prerequisite while TI 2024 lists *ODBC Driver 18* — confirm on a client's DSN which driver is in use. Driver 18 enforces encrypted, certificate-validated connections: the SQL Server needs
  a **server certificate matching its name**, or the DSN must be set to trust the certificate.
  Existing DSNs upgraded to Driver 18 hit this. Any third-party process that uses Sage's DSNs
  (report runners, integrations) is affected; an integration using its own connection
  string is not, but the Sage side of the server still needs the certificate.
- Known pain point: the ADMIN user's password expiring under the new policy (2023 PU2+). Fixed
  by a "Password never expires" option in 2024. PU1 removed the A/P Electronic Filing screen
  (1099 filing moved to Aatrix); PU4 changes Workstation Setup.
- Schema: no restructuring of OE/IC/AR/AP/PO transaction tables.

### Sage 300 2024 (7.1A) — released ~Aug 2023 (2024.1 = Nov 2023)

Detail: `../release-notes/2024.md`.

- **Enhanced Security formalised** (see the Enhanced Security PDF): password policy is driven by
  the **Windows Local Security Policy on the SQL Server machine**; expired passwords can only be
  reset by a Sage 300 admin; per-user SQL logins named `##S3_Login_<user>` (Sage authentication)
  and `##S3_Domain_<user>` (Windows authentication). Integration service accounts should use the
  Sage-side "Password Never Expires" setting, which overrides the SQL policy. This is the release
  that broke several third-party integrations that logged into Sage with a shared user.
- Web API additions: CP/UP employee and **IC Item Location details** end-points; subclassing
  supported in Web Screens and Web API (2024.2).
- AP: five new 1099 fields on the vendor (2024.1; also shipped as 2023.5) — **appended columns**
  `APVEN.FIRSTNAME/LASTNAME/FATCA/SECONDTIN/TAXWHSTTE`, existing columns unchanged. PU9 changes
  Workstation Setup.
- Global Search introduced (2024.0); requires signing into Database Setup on each server.
- Financial Reporter for the Web introduced; Sage Intelligence Report Cloud deprecated.
- Schema: additive only.

### Sage 300 2025 (7.2A) — released ~Aug 2024

Detail: `../release-notes/2025.md`.

- **Payroll web screens are now installed by the Payroll Tax Update installer**, not the core
  installer (from Tax Update Q3 2024). Consequence for later upgrades: Payroll web-screen users
  coming from 2023/2024 must reinstall the tax update with the web-screens option ticked.
- Sage HR Integration v8.0 required for HR sync; workstation registration via `wssetup.cmd`.
- Bank Feeds re-platformed (2025.2): onboarding with a Sage ID and behind-the-scenes migration
  of existing feeds.
- 2025.5 / 2025.6 back-ported the 2026 items: OFX 2.x statement import, IC Manufacturers' Item
  Web API end-point, GL subledger-reversal warning, OE "Update Customer Number" security right
  (2024.9 carries the PU5 set too). PU6 changes Workstation Setup.
- Schema: additive, **except payroll `CHECKNUM`/`TRANSNUM` widened BCD*5.0 → BCD*8.0** (DECIMAL(9,0) →
  DECIMAL(15,0)) on CP/UP cheque, accrual and manual-cheque tables — payroll integrations must widen.

### Sage 300 2026 (7.3A) — released September 2025; PU3 = September 2026

Full extract with verbatim procedures and fixed-issue references: `../release-notes/2026.md`.

- **Upgrade warnings (from Release Notes)**:
  - Using Web Screens and coming from **any version before 2025** → uninstall the old Web
    Screens (Programs and Features → Sage 300 → Change → Modify → untick Web Screens) **before**
    installing 2026, then tick Web Screens in the 2026 installer. KB 250808163127480.
  - Using Payroll Web Screens and coming from 2023 or 2024 → reinstall the latest Payroll Tax
    Update with the Payroll Web Screens option checked after the upgrade.
  - Using Global Search and planning a Repair → back up and uninstall Global Search first, then
    reinstall via Modify and re-save a company in Database Setup.
- **Import/export engine replaced (2026.3)** (Technical Information, PU3 fixes): Sage 300 no longer uses the Microsoft Access
  Database Engine 2016 for import/export; Excel import/export now uses the web-screens engine.
  Retest any Sage import macros or scheduled imports.
- **OE "Update Customer Number" security right (2026.3)**: users can no longer change the
  customer on an OE Order / Shipment / Credit-Debit Note once detail lines exist unless the
  right is granted. Affects integrations or users that create the header first and re-key the
  customer.
- Web API: IC Manufacturers' Item end-point (2026.2).
- Bank Services: OFX 2.x (XML) statement files (2026.2).
- IC Day End Processing screen shows "Last Processed By" user (new field on the IC day-end
  options/status record — additive).
- GL: export Optional Fields for posted transactions from GL Transaction History.
- AR/AP finders search by customer/vendor name; AR Customer List exports directly.
- Currencies: BDT added to defaults; obsolete pre-Euro currencies removed from the **default
  set for new system databases** (existing databases keep their currency tables).
- Sage HR Integration 8.1 required (only compatible with 2026+; needs Payroll Tax Update
  Q3 2025 8.0E or later).
- PU3 changes Workstation Setup → reinstall on all workstations (Technical Information).
- Sage CRM 2026 R1 is the matching CRM release; Sage Fixed Assets 2026.0 (Compatibility Guide — not bundled; TI 2026 notes the FAS-integration printing issue applies only to FAS < 2026).
- Schema: additive only. No documented changes to OEORDH/OEORDD/ICITEM/ICILOC/ARCUS/APVEN
  keys or existing columns.

### Cross-version summary for the common jump 2023 → 2026

| Area | Impact | Action |
|---|---|---|
| Company DB tables used by SQL views/integrations | Additive only; existing columns, types and keys unchanged | Run the Section 7 diff; expect zero removed columns |
| Sage user / SQL login security | 2024 Enhanced Security applies: per-user `##S3_` logins, Windows password policy on the SQL box | Give the integration's Sage user "Password Never Expires"; check the SQL Server's Local Security Policy |
| ODBC / DSN | Driver 18 with certificate validation (already true on 2023 if freshly installed; may not be on an older-upgraded 2023) | Install a server certificate matching the SQL Server name or set the DSN to trust it |
| Web Screens | Must uninstall old Web Screens first | Follow the Release Notes procedure |
| Payroll Web Screens | Reinstall tax update with web-screens option | After core upgrade |
| Import/export macros | Access Database Engine dropped in 2026.3 | Retest |
| OE customer change on existing lines | New security right | Grant to integration/user if needed |
| SQL Server | 2026 requires SQL 2019/2022/2025 (the current 2023 guide also lists only 2019/2022 — SQL 2016/2017 were launch-era) | Upgrade SQL Server first if on 2016/2017 |
| Windows | Windows 10 no longer tested from the April 2026 releases; Server 2016 dropped | Move workstations to Windows 11, servers to 2019/2022/2025 |

## 5. Compatibility matrix — SQL Server / Windows

Summary of `compatibility-guides.md` (full per-year detail, Office versions, hardware sizing and the edition dates
live there — read it for any blocker question). Sage re-issues these guides, so the values are what Sage supports
**today** for each version, not what was supported at launch.

| Sage 300 | SQL Server (Express/Std/Ent) | App server OS (x64) | Workstation OS | Guide edition |
|---|---|---|---|---|
| 2026 | 2019, 2022, 2025 | Windows Server 2019, 2022, 2025 | Windows 11; Windows 10 only up to the March 2026 releases — not tested from April 2026 | May 2026 |
| 2025 | 2019, 2022, 2025 | Windows Server 2019, 2022, 2025 | as 2026 | May 2026 |
| 2024 | 2019, 2022 | Windows Server 2019, 2022, 2025 | as 2026 | Nov 2025 |
| 2023 | 2019, 2022 | Windows Server 2019, 2022, 2025 | Windows 10, 11 (Windows 10 issues may not be addressed after Oct 2025) | Mar 2025 |

A 2023 client on SQL Server 2016/2017 or Windows Server 2016 was within the original 2023 guide but is now outside
Sage's current support statement — flag it, and move the platform before or with the upgrade.

Other requirements (all four guides): 64-bit app server only; binary collation such as `Latin1_General_BIN`
recommended; web screens need IIS with static content + ASP.NET and a Portal database on a supported SQL Server;
Financial Reporter for the Web needs 64-bit Excel 365 on server and workstation; desktop Financial Reporter needs
Excel 2016/2019/2021/2024/365; .NET Framework 4.8 and MSXML 6.0 are installed by the Sage installer (Technical
Information); Terminal Server/Citrix supported for classic screens only, not web screens.

## 6. What an upgrade does and does not do to the database

Does:
- Runs each module's data-activation conversion per company; may **append** columns, add tables
  for new features, widen a field occasionally, and rebuild indexes.
- Updates the system database (users, security, currencies) and, from 2023, the Vault/Store
  databases.
- Changes the ODBC driver / DSN definitions on the Sage servers.

Does not:
- Rename or drop the core transaction tables (OE, IC, AR, AP, PO, GL) or their primary keys.
  Views written against the bundled 6.0A dictionary are still structurally valid on 2026.
- Change Sage's storage conventions (CHAR padding, NOT NULL everywhere, numeric YYYYMMDD dates,
  BCD → DECIMAL) — see `references/dictionary/conventions.md`.
- Touch non-Sage objects (custom views, procedures, third-party integration tables) in the company database —
  but they are not backed up by Sage's process either, so script them out first.

Risk register for integrations, in the order they actually bite:
1. Authentication/security (Sage user password expiry, `##S3_` logins, SQL policy).
2. ODBC Driver 18 certificate validation on Sage-owned DSNs.
3. Unsupported SQL Server / OS blocking the install.
4. Custom objects lost because the DBA restored a fresh DB instead of converting in place.
5. New security rights (e.g. OE Update Customer Number) blocking an integration user.
6. Actual schema breakage — rare; catch it with Section 7.

## 7. Post-upgrade verification SQL

Run against the **2023 backup restored as a side database** and the **converted 2026 database**,
then diff the two result sets (or run as a cross-database query when both are on one server).
Read-only; safe on production.

```sql
-- 1. Column inventory of the tables an integration touches. Edit the IN list.
SELECT c.TABLE_NAME, c.COLUMN_NAME, c.DATA_TYPE,
       c.CHARACTER_MAXIMUM_LENGTH, c.NUMERIC_PRECISION, c.NUMERIC_SCALE
FROM INFORMATION_SCHEMA.COLUMNS c
WHERE c.TABLE_SCHEMA = 'dbo'
  AND c.TABLE_NAME IN ('OEORDH','OEORDH1','OEORDD','OESHIH','OESHID','OEINVH','OEINVD',
                       'ICITEM','ICILOC','ICLOC','ICUNIT','ICCATG',
                       'ARCUS','APVEN','POPORH1','POPORH2','POPORL','PORCPH1','PORCPL')
ORDER BY c.TABLE_NAME, c.ORDINAL_POSITION;

-- 2. Cross-database diff when old (restored) and new are on the same server.
--    Rows returned = columns removed or changed by the upgrade. Expect none.
SELECT o.TABLE_NAME, o.COLUMN_NAME, o.DATA_TYPE, o.CHARACTER_MAXIMUM_LENGTH
FROM   OLDDB.INFORMATION_SCHEMA.COLUMNS o
LEFT JOIN NEWDB.INFORMATION_SCHEMA.COLUMNS n
       ON n.TABLE_NAME = o.TABLE_NAME AND n.COLUMN_NAME = o.COLUMN_NAME
      AND n.DATA_TYPE = o.DATA_TYPE
      AND ISNULL(n.CHARACTER_MAXIMUM_LENGTH,0) = ISNULL(o.CHARACTER_MAXIMUM_LENGTH,0)
WHERE  o.TABLE_SCHEMA = 'dbo' AND n.COLUMN_NAME IS NULL
ORDER BY 1,2;

-- 3. Columns the upgrade ADDED (informational — nothing to fix, but worth knowing).
SELECT n.TABLE_NAME, n.COLUMN_NAME, n.DATA_TYPE
FROM   NEWDB.INFORMATION_SCHEMA.COLUMNS n
LEFT JOIN OLDDB.INFORMATION_SCHEMA.COLUMNS o
       ON o.TABLE_NAME = n.TABLE_NAME AND o.COLUMN_NAME = n.COLUMN_NAME
WHERE  n.TABLE_SCHEMA = 'dbo' AND o.COLUMN_NAME IS NULL
ORDER BY 1,2;

-- 4. Confirm custom (non-Sage) objects survived the conversion.
SELECT name, type_desc, create_date, modify_date
FROM   sys.objects
WHERE  is_ms_shipped = 0 AND type IN ('V','P','FN','IF','TF','TR')
ORDER BY type_desc, name;

-- 5. Recompile every view so a broken one fails now, not at month end.
DECLARE @sql NVARCHAR(MAX) = N'';
SELECT @sql += N'BEGIN TRY EXEC sp_refreshview ''' + QUOTENAME(SCHEMA_NAME(schema_id)) + '.' + QUOTENAME(name)
             + '''; END TRY BEGIN CATCH PRINT ''BROKEN: ' + name + ' - '' + ERROR_MESSAGE(); END CATCH;' + CHAR(10)
FROM sys.views WHERE is_ms_shipped = 0;
EXEC sp_executesql @sql;
```

Also confirm the Sage version actually installed (System Manager → Help → System Information,
or `SELECT * FROM <SYSDB>.dbo.CSAPP` for module versions), and check the Sage 300 desktop's
Database Setup for the ODBC driver in use.

## 8. Standard answer shape

Every upgrade answer uses this order so nothing is missed. Keep it tight; a consultant reads it
before a client call.

1. **Path** — one sentence: source → target, single-step or not, and the supported-upgrade-from
   floor of the target version.
2. **Blockers** — SQL Server / Windows / Office versions that must move first (Section 5).
3. **Integration & SQL impact** — schema (usually "additive only"), security/login changes,
   ODBC driver, new security rights, anything that touches the integration user. Say
   explicitly what will *not* break.
4. **Version-specific gotchas** — the Release Notes "Important" items for the target version
   and every skipped version in between (Section 4).
5. **Plan** — the Section 3 checklist trimmed to this client: backup set, test environment,
   order of operations (SQL/OS first → Sage server → data activation → workstations → payroll
   tax update → web screens → CRM → integration retest).
6. **Verification** — point at Section 7 and name the tables to diff.
7. **Sources** — cite which Sage documents the answer rests on and flag anything after this
   file's verification date as "confirm on help.sage300.com".

If the source or target version is not stated, ask — the answer differs materially between
2024 → 2026 and 2019 → 2026. If a client is on a version with Pervasive/Btrieve data (5.x era),
add the SQL Server database-conversion step and say the bundled advice assumes SQL Server.

## 9. Maintaining this file

When a new Sage 300 version or notable PU ships:
1. Fetch that year's Release Notes, Technical Information and Compatibility Guide (Section 2).
2. Add a `### Sage 300 <year>` block in Section 4 in the same format — upgrade warnings first,
   then integration-relevant changes, then a one-line schema verdict.
3. Update the Section 5 matrix row and the Section 4 cross-version table.
4. Bump the "Verified against ... as of" line at the top.
