# Dictionary index

| Path | Covers | Sage X3 version | Verified |
|---|---|---|---|
| `conventions.md` | How X3 stores data in SQL (folder = schema, dimensioned columns, no NULLs, 1599-12-31 empty date, booleans 1/2), type mapping, starter join map, view rules, worked example | V11 (behaviour is version-independent) | 2026-10-02 |
| `V11/table-index.md` | **1,899 tables**, one line each (`TABLE` (ABBR) - description), grouped by the 14 modules below, with Sage's V9.0 P12 / V10 P1 marks (`+` new table, `*` differs) | **V11** | 2026-10-02 |
| `V11/dict/<Module>.md` | Per table: keys/indexes with column expressions, every column (type, length, dimension, title, local menu values inline, link expression = FK join, cancellation rule, activity code). 1,551 tables carry columns (**45,708 fields, 2,835 keys**); 348 tables are header-only because Sage publishes no column detail for them (mostly HR/payroll localisation) - their entries say so | V11 | 2026-10-02 |
| `V11/local-menus.md` | **1,048 local menus** (enum values) referenced by type-M columns, one line each (`menu N - title: 1=…, 2=…`) | V11 | 2026-10-02 |
| `V11/data-types.md` | **540 data types** (`CODE - name \| internal type \| linked table`) - storage type and the control table a typed column points at | V11 | 2026-10-02 |

Source: Sage's public online help, "Table dictionary" (`https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm` and the
table / `MEN00nnn.htm` / `ATY_<code>.htm` pages it links to), compiled by `scripts/build_dict_x3.py` on 2026-10-02. The files hold
extracted facts only, not the pages. Local menu 2014 is referenced by the dictionary but its page is missing on Sage's site (404),
so it has no values here.

## Module → file

| Module (as Sage names it) | Tables | File |
|---|---|---|
| Common Data | 585 | `V11/dict/Common-Data.md` |
| Supervisor | 331 | `V11/dict/Supervisor.md` |
| Financials | 202 | `V11/dict/Financials.md` |
| Human Resources administration | 178 | `V11/dict/HR-administration.md` |
| Fixed Assets | 136 | `V11/dict/Fixed-Assets.md` |
| A/P-A/R accounting | 110 | `V11/dict/AP-AR-accounting.md` |
| Stock | 86 | `V11/dict/Stock.md` |
| Manufacturing | 66 | `V11/dict/Manufacturing.md` |
| Purchasing | 60 | `V11/dict/Purchasing.md` |
| CRM activities | 48 | `V11/dict/CRM.md` |
| Sales | 44 | `V11/dict/Sales.md` |
| Human Capital management | 36 | `V11/dict/HCM.md` |
| Help Desk | 13 | `V11/dict/Help-Desk.md` |
| Development | 4 | `V11/dict/Development.md` |

Note that Sage files the big master tables under **Common Data** (`BPARTNER`, `BPCUSTOMER`, `BPSUPPLIER`, `ITMMASTER`, `ITMFACILIT`,
`FACILITY`, `COMPANY`, `TABCOUNTRY`, `TABCUR`), not under the functional module - grep `table-index.md` by name or topic rather
than guessing the module.

## Version map

| Client version | Use | Notes |
|---|---|---|
| V11 | `V11/` | the bundled dictionary |
| V12 and later | `V11/` as a starting point, then confirm on `https://online-help.sagex3.com/erp/12/en-US/MCD/<TABLE>.htm` | not bundled; `MAINTENANCE.md` explains how to build a `V12/` folder |
| V10 P1 | `V11/`; tables marked `+` do not exist there (446), tables marked `*` differ (194) | per-table diff at `ATD_<TABLE>.htm` |
| V9.0 P12 | `V11/`; tables marked `+` do not exist there (489), tables marked `*` differ (234) | per-table diff at `AT3_<TABLE>.htm` |

Selection rule: the bundled dictionary is V11; say so whenever the client runs something else, and confirm the specific table on
Sage's help for that version before shipping SQL. Folder-level differences (activity codes, dimensions, customized local menus)
are never in any dictionary - confirm those on the client's folder.
