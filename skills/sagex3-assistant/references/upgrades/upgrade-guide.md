<!-- source: Sage X3 Lifecycle Policy, November 2024 (docs.sage.com/docs/en/customer/erpx3/assets/Sage X3 Lifecycle Policy_Nov 2024_LCP.pdf); Sage Community "Sage X3 Version 12: Latest Release Information" (communityhub.sage.com/sage-global-solutions/sage_x3/f/announcements/271321, read 2026-10-02) and "INFO: V11 enters End of Maintenance 1st April 2024"; Sage KB 224924850073492 "Sage X3 upgrade path" (updated 7 March 2023); Sage X3 online help V12: "Upgrading an existing Sage X3 solution" (getting-started_quick-upgrade-guide.html), "Folder upgrade" (getting-started_upgrade-of-a-folder_v11&v12.html), "List of upgrade procedures by module" (getting-started_list-of-x3-upgrade-procedures-by-module-v11.html); Sage X3 UK Support blog "Should I Easy Upgrade, Folder Upgrade and/or Migrate my V11 instance to V12?" (12 Oct 2021); Sage X3 UK support update deck (4 Dec 2024); release-notes API archive.json | version: Sage X3 V6 → V12 2026 R1 | verified: 2026-10-02 -->
# Sage X3 versions and upgrades

What a consultant needs to answer "the client is on X and wants Y": how versions are named and how long Sage
maintains them, where the official documentation is, which paths and methods exist, what the procedures do to the
folder and its database, how to tell whether SQL views and integrations break, and the shape of a good answer.
Platform support per release is in `platform-matrix.md`; per-release changes in `../release-notes/`.

## Contents

1. Version naming and the lifecycle policy
2. Where the official documentation lives
3. Supported upgrade paths
4. Three ways to get to V12
5. In-place upgrade of an existing V12 (or V11) solution - the official procedure
6. Folder upgrade (migration) - the official procedure and the `UU*` processes
7. What the upgrade does to the database, and how to assess SQL / integration impact
8. Verification SQL
9. Standard answer shape
10. Maintaining this file

## 1. Version naming and the lifecycle policy

| Generation | Names you will hear | Status (as of 2026-10-02) |
|---|---|---|
| Sage X3 **V12** | `YYYY Rn (12.0.xx)` - e.g. 2026 R1 = 12.0.39; "patch 39"; releases 2019 R1 → 2022 R3 were quarterly, **bi-annual since 2022 R4 (12.0.32)**, GA around **May and November** | the only maintained line; a release is maintained **24 months** from GA (see below) |
| V11 (11.0.x) | "V11", final patch **11.0.22** (March 2022) | **end of maintenance 1 April 2024** (extended once, from April 2023) |
| Update 9 / PU9 (U9) | "V9", "PU9" | end of maintenance 1 July 2021 |
| V6, V7, Update 8 / PU8 | "V6", "V7", "U8" | end of maintenance 1 July 2020 |
| V5, V140, V130, V120, V110 | legacy Adonix generations | not upgradeable directly (§ 3) |

**End of maintenance** means Sage issues no bug fixes, updates or security updates for that version; a customer with a
valid contract can still raise support cases and keeps access to existing patches, the knowledgebase and online help,
and holds the licence right to the current version (Lifecycle Policy, Introduction).

**Lifecycle stages of a V12 release** (Lifecycle Policy Nov 2024; durations from Sage's release-information post):

| Stage | Length | Sage may deliver |
|---|---|---|
| Current | first **6 months** from GA | service packs (compliance for Sage core legislations, features, fixes) and hotfixes for severity 0 / 1 defects |
| Standard | next **12 months** | hotfixes for severity 0 / 1 |
| Extended | last **6 months** | hotfixes for severity 0 only |
| End of maintenance | GA + **24 months** | nothing |

Compliance features ship only in the upcoming release or, for a time-bound legal milestone, as a service pack **for the
current release only**. V12 updates are **cumulative since 2019 R4** (one update brings every intermediate change).
Hotfixes are "subject to technical and commercial feasibility" and may be built for a non-current release at Sage's
discretion - never promise one.

**Release list** (Sage release-notes archive; GA month as Sage publishes it; end of maintenance derived as GA + 24
months - confirm the stage on Sage's release-information post, which is updated with each release):

| Release | Patch | GA | Stage (Sage post, read 2026-10-02) | Derived end of maintenance |
|---|---|---|---|---|
| 2026 R1 | 12.0.39 | May 2026 | **Current** | ~May 2028 |
| 2025 R2 | 12.0.38 | November 2025 | Standard | ~November 2027 |
| 2025 R1 | 12.0.37 | May 2025 | Standard | ~May 2027 |
| 2024 R2 | 12.0.36 | November 2024 | Extended | ~November 2026 |
| 2024 R1 | 12.0.35 | April 2024 | past end of maintenance | ~April 2026 |
| 2023 R2 | 12.0.34 | November 2023 | past end of maintenance | ~November 2025 |
| 2023 R1 | 12.0.33 | ~2023 | past end of maintenance | - |
| 2022 R4 | 12.0.32 | ~late 2022 | past end of maintenance (first bi-annual release; PowerShell required) | - |

Earlier V12 patches are referenced in `platform-matrix.md` by the platform boundaries they introduced (2019 R5 =
12.0.20, 2020 R1 = 12.0.21, 2020 R2 = 12.0.22, 2020 R3 = 12.0.23, 2020 R4 = 12.0.24, 2021 R4 = 12.0.29 … 2023 R1 =
12.0.33). Their release notes are archived (§ 2).

## 2. Where the official documentation lives

| Need | URL pattern | Notes |
|---|---|---|
| Prerequisites (platform support) per major version | `https://online-help.sagex3.com/erp/12/en-us/Content/V7DEV/prerequisites_overview.html` and `prerequisites_<component>.html` (`windows-sql-server`, `windows-oracle`, `linux-oracle`, `red_hat_oracle`, `web-syracuse-server-on-windows`, `mongodb-on-windows`, `elastic-search`, `console`, `browsers`, `print-server-on-windows`, `atp` …); V11: `https://online-help.sagex3.com/erp/11/en-US/V7DEV/prerequisites_overview.html` | one page per major version, re-published; states support *by release*. Page footer shows "Date published" |
| Release notes 2023 R2 → 2026 R1 | `https://online-help.sagex3.com/x3-release-notes/index.html#/release/en-US/<id>` with `<id>` = `2026-r1-39`, `2025-r2-38`, `2025-r1-37`, `2024-r2-36`, `2024-r1-35`, `2023-r2-34`; machine-readable `…/x3-release-notes/api/en-US/archive.json` and `…/api/en-US/<id>/data.json` | plus per release the **Applicative Readme** `…/api/en-US/<id>/Readme-X3-ENG-12.0.xx.txt` (behaviour changes, entry points, fixes with the modified dictionary elements) and **Platform Readme** `…/Readme-Components-ENG-12.0.xx.txt` (component versions) |
| Release notes 2023 R1 and earlier | `https://online-help.sagex3.com/x3-release-notes-arch/en_US/ReleaseNote/RELNOTE_V12.0.33.htm` (and the same pattern for earlier patches) | archived HTML |
| Patch documents (what the patch installs, prerequisites, known issues) | `x3-patch-documents-12.0.xx.zip` on the regional Sage FTP / download site (e.g. `ukienterprisedownloads.sage.co.uk/Support/SageX3/X3V12/Patches/12.0.xx/`) | partner / customer login |
| Upgrade procedures | `https://online-help.sagex3.com/erp/12/en-us/Content/V7DEV/getting-started_quick-upgrade-guide.html` (in-place), `…/getting-started_upgrade-of-a-folder_v11&v12.html` (folder upgrade), `…/getting-started_list-of-x3-upgrade-procedures-by-module-v11.html` (`UU*` processes), `…/getting-started_sage-erp-x3-installation-procedure.html` (fresh install) | V11 equivalents under `erp/11/en-US/V7DEV/` |
| Table dictionary (schema) per version | V11 `https://online-help.sagex3.com/erp/11/en-US/MCD/<TABLE>.htm` (bundled in `../dictionary/V11/`); **V12 `https://online-help.sagex3.com/erp/12/en-us/Content/MCD/<TABLE>.htm`**; V9 / V10 differences `AT3_<TABLE>.htm` / `ATD_<TABLE>.htm` under the V11 folder | `scripts/diff_table_versions.py TABLE` compares V11 ↔ V12 |
| Lifecycle policy | `https://docs.sage.com/docs/en/customer/erpx3/assets/Sage%20X3%20Lifecycle%20Policy_Nov%202024_LCP.pdf` (linked from every help page footer); KB 220924460105518 | current release stages: Sage Community announcement "Sage X3 Version 12: Latest Release Information" |
| Upgrade path matrix | Sage KB `us-kb.sage.com … solutionid=224924850073492` ("Sage X3 upgrade path", 7 March 2023) | |
| Availability announcements | `communityhub.sage.com` → Sage X3 → Announcements: "INFO: Version 2026 R1 (12.0.39) is now available" etc. (component versions, ISO / patch file names) | some regional forums need a login |

Reseller "what's new" blogs are useful pointers but **not sources**; quote Sage's page and its date.

## 3. Supported upgrade paths

From the folder-upgrade help page (minimum patch of the source) and KB 224924850073492 (direct paths):

| Source | Minimum level | Path to V12 |
|---|---|---|
| V11 | none (any patch; the KB lists V11 P2+) | direct |
| Update 9 / PU9 | none | direct |
| Update 8 / PU8 | patch 3 | direct |
| V7 | patch 9 | direct |
| V6 | patch 29 (help); the KB lists **V6 P40** - it includes the VAT form and VAT form entry | direct (V6.5 and later) |
| V5 | P10 | → V7 P9 → V12 |
| V140 | P25 | → V6 P29 → V12 |
| V130 | - | → V5 P10 → V7 P9 → V12 |
| V120, V110 | - | not upgradeable: export data, new system / project |

Source patch level is read in **? > About** (V6) or **Administration > Version information** (V7+). Rules: a
**migrated folder cannot carry the TEST flag**; everything moves at once (there is one application version per
solution); the target is the **current** V12 release unless the client has a reason to stop earlier, because
anything older is already part-way through its 24 months. V12 → newer V12 is an *update* (patch), not an upgrade,
but the same in-place procedure (§ 5) applies.

## 4. Three ways to get to V12

From Sage UK Support's comparison (Oct 2021), still the vocabulary Sage uses:

| Method | What it is | Choose when | Watch out |
|---|---|---|---|
| **Easy / in-place upgrade** | apply the V12 components and patches over the live instance; same servers, OS, database, hostnames | infrastructure already meets the target release's prerequisites; minimal change wanted | overwrites the original - the only rollback is a restore; architecture changes are hard; test coverage weaker |
| **Folder upgrade (migration)** | install V12 fresh on new servers, copy the live folder in, upgrade it there; patch and tune outside the migration window | OS / DB / hardware must change anyway (usual for V6-V11 → V12 given § platform-matrix); you want the old instance kept for comparison | extra hardware and licences; live data copied during the window; MongoDB data (Syracuse: users, roles, endpoints, dashboards) must be transferred separately |
| **Re-implementation** | new folder, selective data load | structural redesign wanted (chart of accounts, sites, codes) | manual mapping, balance reconciliation |

Customizations (specific developments, `X_`/`Y_`-type objects, entry points) need assessment in every method; the
upgrade keeps them but does not validate them - § 6 explains the `GTRALIG` safeguard for testing on folders that
carry specifics.

## 5. In-place upgrade of an existing solution - the official procedure

From "Upgrading an existing Sage X3 solution" (V12 help). Before anything: **a new licence from Sage**, a **full
backup**, batch server and accounting tasks disabled, no active sessions; on Red Hat/Oracle install `libunwind`.
Component order (each `*.jar` setup from the `X3Installs` tree, "Modify installation" onto the existing path):

1. **Console** (`console-M.m.P.jar`, Windows) - uninstall a SAFE X3 V1-generation console first.
2. **Main runtime** (`runtime-M.m.P.jar`); on Windows the update detects every installed component.
3. **PowerShell** (SQL Server architectures: PowerShell 7.2.3+ MSI and `Install-Module -Name SqlServer -Scope AllUsers -force`; Red Hat: Microsoft repo + `yum install powershell`) - required since 2022 R4.
4. **Application** (`x3-application-M.m.P.jar`, up to 30 minutes).
5. Additional runtimes ("Full" / "Test") if any.
6. **Print Server** (`print-server-M.m.P-win.jar`).
7. **Elasticsearch** - delete the indexes on the current version first, upgrade to the version the prerequisites give for the target release (7.16 minimum on that page; Elasticsearch 8 since 2023 R2), set `network.host` / `http.port`, note hostname and port.
8. **MongoDB** - stop the "agent sage Syracuse" and "sage Syracuse" services; follow the upgrade guide for the target version (3.6 → 4.0 → 4.2 → 4.4 → 7 → 8 as the matrix requires; 3.4.16 is the oldest the page accepts); a manually installed MongoDB needs a different port and "Import and initialize db".
9. **Syracuse** (`syracuse-server-M.m.P.jar`, up to 30 minutes; needs a user with service-modification rights and the initial passphrase).
10. **Console reconfiguration** - load the solution, click Application, reconfigure additional runtimes, print server, Java bridge, web service / ADC components (30+ minutes).

Then in Syracuse as super administrator: **licence upload** (Administration > Licenses) and the "Supervisor update";
**Personalization and menus initialization from X3 folder**; for V7 / U8 P3-or-older Oracle sources the **ADX_SYS
role update** (`update_SYS_role_17R301.sql` / `Update_Role_17r3xx.bat`); then **folder revalidation** - Setup > General
parameters > Folders (`GESADS`): *save the definition of every folder except X3 and SEED*, Validation, choose immediate,
deferred or batch - **"revalidation can last for several hours"**. Finally apply the patches from the installation
medium (Administration > Utilities > Update), decide the SEED folder (keep the old one and install the V12 SEED is the
certified route; overwriting SEED is "technically possible but not certified"), `Ctrl+F5` on every browser, and
re-index search (Administration > Usage > Search Index Management).

## 6. Folder upgrade (migration) - procedure and the `UU*` processes

From "Folder upgrade" (V11 & V12 help). Four phases:

1. **Controls in the source folder, without stopping operations.** Check the minimum patch (§ 3) and the functional
   prerequisites, then run the **`UU*` processes** from Development > Utilities > Miscellaneous > Run processes:
   *control* procedures reveal data errors to fix first; *pre-loading* procedures pre-fill fields to shorten the
   downtime (optional). Supplied as a patch list dedicated to upgrading, per release.
2. **Data transfer - operations stopped.** Development > Utilities > Extraction/integration > **Data extract** (flat
   format for small folders, database tools for large ones); copy to the new solution; create the folder tree;
   import; the folder record is created by the Console (or by hand when database tools were used). Then **adjust the
   activity codes on the folder record in the Supervisor folder** - validation will not continue otherwise.
3. **Folder revalidation** (Setup > General parameters > Folders > Validation): purges temporary / totalling tables
   (`ALSTRD`, `ALISTER`, `AWRKLOG`, `AWRKLOGIND`, `AWRKLOGMES`, `ATMPTRA` and functional ones), **upgrades the dictionary
   and Supervisor tables, restructures the data tables to the target version**, runs the sequenced functional upgrade
   procedures (default values, resynchronisations), then the post-upgrade step. Deleting the temporary tables
   (`TRTMIGDEL`) is manual, can be postponed, and is irreversible - only after every routine succeeded. Even though
   the post-upgrade step is not needed to restart operations, "it must be carried out at some point for a folder to
   be considered as completely upgraded".
4. **Functional post-requisites** - check and adapt setups as the per-module notes say.

Large folders: define an **upgrade plan** (Usage > Upgrades > Sequencing monitor) to run independent tables in
parallel - max simultaneous procedures (bounded by batch server parameters and licence), automatic launch, linked
post-upgrade. Steps: Initialization → Common data → Module → Post-upgrade. Without a plan, validation generates one
named after the folder (or `MIGmmddM##`). Folders with **specific developments**: set the global variable `GTRALIG`
to `1` (default `200`) during upgrade tests so operations can be recovered after an error, and restore `200` after.
Custom procedures may be inserted between the standard ones following Sage's methodology.

`UU*` processes by module (from "List of upgrade procedures by module"; names are exact, run them from the list Sage
supplies for the release, not from memory):

| Phase | Module | Processes |
|---|---|---|
| Control (before extraction) | Financials | `UUMGCTLCPT00` (entries), `UUMGCTLTRS00` (A/P-A/R and BP invoices) |
| | Sales | `UUMGCTLSAL01` quotes, `02` orders, `06` deliveries, `07` returns, `08` invoices |
| | Purchasing | `UUMGCTLPUR01` requests, `02` orders, `03` contract orders, `06` receipts, `07` returns, `08` invoices |
| Pre-loading (optional) | Common data | `UUMGPRETRC04` (`GACCDUDATE`), `07` (`BPCUSTOMER`), `08` (`BPSUPPLIER`) |
| | Sales / Purchasing | `UUMGPRESAL01–08`, `UUMGPREPUR02/04/06/07/08` |
| Main upgrade (sequencing monitor) | Common data | `UUMGTRTTRC01–18` (products, product-sites, accounting, open items … configurator) |
| | Accounting | `UUMGTRTCPT01–06`, balance resync `UUMGTRTCPT51–54` (closed fiscal years) |
| | Sales | `UUMGINISAL01/02/06/07/08` |
| | A/P-A/R, Purchasing, Stock, Manufacturing | phase-specific `UUMGTRT*` procedures (transactions and balance resyncs) |
| Post-upgrade | Common data | `UUMGPOSTRC03–04` (`GACCDUDATE`), `UUMGPOSTRC51–54` (invoice FIY/PER) |
| | Accounting | `UUMGPOSCPT03/05` (UOM), `UUMGPOSCPT51–54` |
| | Sales | `UUMGPOSSAL01` (quote valuation, only if `VALORISATION` set), `UUMGPOSSAL02` (back-to-back assignments) |

`CRITSEL` / `VERIFSEL` entry points allow filtering inside the procedures that document them.

## 7. What the upgrade does to the database, and how to assess SQL / integration impact

- The folder revalidation **restructures tables to the target dictionary**: columns are added (with default values
  set by the functional procedures), types/lengths and dimensions may change, local menus gain values, and
  temporary tables are purged. Sage does not publish a consolidated schema diff; the evidence is:
  1. **Per patch**: `../release-notes/<release>.md` § 2 lists every table (`ATB`), local menu (`AML`) and data type
     (`ATY`) whose definition a fix or change touched in that patch, with the issue keys - from Sage's Applicative
     Readme. Read every release between the client's source and target.
  2. **V11 → V12 for a named table**: `python scripts/diff_table_versions.py SORDER SORDERQ …` compares the V11 and
     V12 help pages (columns added / removed / type, length, dimension, menu changes; keys). Or read the V12 page
     yourself (`erp/12/en-us/Content/MCD/<TABLE>.htm`) against `../dictionary/V11/dict/`.
  3. **V9 / V10 → V11**: the `*` / `+` marks in `../dictionary/V11/table-index.md` and Sage's `AT3_<TABLE>.htm` /
     `ATD_<TABLE>.htm` pages.
- The honest default for the core transaction and master tables is **additive**: existing columns keep their names
  and types; new columns appear (`NAME_0` as always); so a view that names its columns keeps working, and `SELECT *`
  consumers break. What actually bites, in order: (a) **local-menu values** added or renumbered behind status
  columns the view decodes; (b) **dimension growth** (an array field gaining `_3`, `_4` …) or activity-code driven
  columns; (c) **Syracuse / web-service layer changes** - classic SOAP web services, X3 Services / GraphQL versions
  (`X3Services` ships with each release, § platform-matrix 1.5), and since February 2026 Syracuse builds pinned to
  the patch level; (d) **platform retirements** that stop the integration host, not X3 (SQL Server 2016 / Windows
  Server 2016 / Oracle 12c dropped at 2026 R1, Java 11 since 2024 R2, PowerShell since 2022 R4); (e) **entry points
  and scripts** customizations hook into (`TRT` elements in the readmes - thousands change per release).
- Local menus are folder data: an upgrade can add values, and a site may have customized them. Decode from the
  dictionary, then confirm on the upgraded folder (`APLSTD`).
- The `ROWID` of a row is preserved by in-place upgrades but **not** by an export/import folder upgrade - never key
  an integration on `ROWID` across a migration.

## 8. Verification SQL

Run on the folder before and after (schema = folder; every column `_0`; verified in `../dictionary/V11/dict/Supervisor.md`):

```sql
-- Which patches this folder has received (APATCH, key APT0 = NUM): the last rows show the current release / patch
SELECT TOP 20 NUM_0, DAT_0, RELEASE_0, PATNUM_0, TYP_0, FIC_0, FICRELABR_0, USR_0
FROM   [FOLDER].APATCH
ORDER  BY NUM_0 DESC;

-- Column inventory of the tables your views and integrations use - diff the two result sets (before / after)
SELECT t.name AS TableName, c.name AS ColumnName, ty.name AS TypeName, c.max_length, c.precision, c.scale
FROM   sys.columns c
JOIN   sys.tables  t  ON t.object_id = c.object_id
JOIN   sys.types   ty ON ty.user_type_id = c.user_type_id
WHERE  SCHEMA_NAME(t.schema_id) = 'FOLDER'
  AND  t.name IN ('SORDER', 'SORDERQ', 'SORDERP', 'BPCUSTOMER', 'BPARTNER', 'ITMMASTER', 'STOCK', 'GACCENTRY', 'GACCENTRYD')
ORDER  BY t.name, c.column_id;

-- Values actually present behind a status column you decode (compare with local-menus.md and the upgraded APLSTD)
SELECT ORDSTA_0, COUNT(*) FROM [FOLDER].SORDER GROUP BY ORDSTA_0;

-- Views and procedures in your own schema that reference folder tables (what to re-test)
SELECT OBJECT_SCHEMA_NAME(d.referencing_id) + '.' + OBJECT_NAME(d.referencing_id) AS Consumer, d.referenced_entity_name
FROM   sys.sql_expression_dependencies d
WHERE  d.referenced_schema_name = 'FOLDER'
ORDER  BY 1, 2;
```

Then: run every reporting view with `SELECT TOP 20 *`, re-test each integration end-point, and compare row counts of
the main documents between the two folders (`SORDER`, `SINVOICE`, `GACCENTRY` …) when a folder upgrade copied data.

## 9. Standard answer shape

1. **Path** - source and target (release, patch, DB, OS), which method (§ 4) and why.
2. **Blockers** - platform retirements at the target (`platform-matrix.md` § 1, quote the page date), licence,
   MongoDB / Java / PowerShell moves, Syracuse build pinning, legacy sources needing an intermediate hop (§ 3).
3. **Integration & SQL impact** - the named tables checked (readme § 2 lists + `diff_table_versions.py`), web
   services / X3 Services version, entry points touched; the honest additive default where nothing was found.
4. **Release-specific gotchas** for the target *and every skipped release* (`../release-notes/`, behaviour changes).
5. **Plan in order of operations** (§ 5 or § 6), with the `UU*` controls and the hours-long revalidation called out.
6. **Verification SQL** (§ 8) - include it.
7. **Sources with dates** - the Sage pages used.

Scale to the question: "will these three views break?" gets steps 3, 6 and 7 plus one line on what else the jump
involves; a full move gets all seven. Never invent a release date, a patch number or a support end - if the Sage page
cannot be fetched, say "confirm on online-help.sagex3.com / the Sage Community release-information post".

## 10. Maintaining this file

Twice a year (May / November GA): re-run `scripts/build_release_notes_x3.py` (new release appears in `archive.json`),
re-read the prerequisites overview for new "since release" statements and update `platform-matrix.md` § 1 and the
release table in § 1 above, re-read the Community release-information post for the stage of each release, and bump
the verified dates. When Sage re-issues the Lifecycle Policy (the help footer names the edition), re-check § 1.
