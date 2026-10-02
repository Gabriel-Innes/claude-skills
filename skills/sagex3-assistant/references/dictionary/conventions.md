<!-- source: Sage X3 V11 online help table dictionary (online-help.sagex3.com/erp/11/en-US/MCD/) as compiled in V11/, plus standard Sage X3 storage behaviour; items marked "confirm on site" are to be checked on the client's folder | version: Sage X3 V11 | verified: 2026-10-02 -->
# Sage X3 - how the dictionary maps to SQL, and how to write views against it

Read this before writing SQL. Every table, column, key and value still has to be verified in `V11/` (SKILL.md § 3);
this file explains how to turn what the dictionary says into correct SQL.

## 1. Folder = schema

- An X3 **folder** is a database schema (SQL Server: `[FOLDER].[TABLE]`, e.g. `SEED.SORDER`; Oracle: the folder's
  user/schema). The same tables exist once per folder; `X3` is the reference/root folder. Always schema-qualify and
  ask which folder the client wants.
- Indexes are named `<TABLE>_<KEY>` after the dictionary key (`SORDER_SOH0`), and the first key listed in `Keys`
  (duplicates not allowed) is the table's primary key. Join and filter on those column expressions.
- Every table also has a technical `ROWID` (unique numeric, not in the dictionary). Many tables carry the audit
  columns `CREDATTIM`/`UPDDATTIM` (datetime), `CREUSR`/`UPDUSR` (user), `AUUID` (GUID) and `EXPNUM` (export
  number) - they are listed in `dict/` when present.

## 2. Reading a field line

`NAME TYPE*LENGTH(DIM) title [menu N: v=text,...] -> link`

| Part | Meaning for SQL |
|---|---|
| `TYPE` | X3 data type (`V11/data-types.md`: internal type + linked table). Internal type decides storage, § 3. |
| `*LENGTH` | declared length (characters for alphanumeric). Absent = defined by the type. |
| `(DIM)` | **array field**: stored as `NAME_0 … NAME_(DIM-1)`, one SQL column per element. When the dimension is driven by an activity code, the folder's actual column count is that activity code's value - confirm on site. |
| `[menu N: …]` | local menu N = the enum; stored as the **number**. Long menus: `V11/local-menus.md`. |
| `-> [ABR]KEY =expr (TABLE)` | the dictionary's **link expression**: the referenced table (by abbreviation) and the key its columns match. `[BPR]BPR0 =[SOH]BPCORD (BPARTNER)` means `SORDER.BPCORD` joins `BPARTNER` on its key `BPR0` (`BPRNUM`). Use it as the join. |
| `-> TABLE` | no explicit link, but the column's data type is keyed to that table (e.g. type `CRY` → `TABCOUNTRY`). Join on that table's primary key. |
| `!Block` / `!Delete` / `!Other` | the dictionary's cancellation rule for the linked record (what happens to this row when the referenced record is deleted). Informational for SQL. |
| `act:CODE` | column exists only where activity code `CODE` is active in the folder. |

## 3. Type mapping (SQL Server)

Confirm the physical type with `sys.columns` when precision matters - the dictionary gives X3 types, not DDL.

| Internal type (data-types.md) | X3 codes (examples) | SQL Server storage | Notes |
|---|---|---|---|
| Alphanumeric | `A`, `BPR`, `ITM`, `CRY`, `DES`, `NAM`, `ADL` … | `NVARCHAR(n)` | empty = `''`, never NULL |
| Local menu | `M` | `TINYINT`/`SMALLINT` | the value number; booleans = menu 1 (1=No, 2=Yes) |
| Short integer / Long integer | `C` / `L` | `SMALLINT` / `INT` | empty = `0` |
| Decimal | `DCB`, `MD1`, `QTY`, `PRI`, `RAT` … | `NUMERIC(p,s)` | scale for amount types follows the currency format (`=GDEVFMT`) - read `sys.columns` |
| Date | `D` | `DATETIME` (00:00:00) | **empty date = `1599-12-31`** |
| Date time | `ADATIM` | `DATETIME` | |
| Time | `HM` | `NVARCHAR` / numeric hh:mm | check the folder |
| GUID | `AUUID` | `UNIQUEIDENTIFIER` | |
| Clob / Blob | `ACLOB`, `ABLOB` | `NVARCHAR(MAX)` / `VARBINARY(MAX)` | |

## 4. Empty-value semantics (no NULLs)

X3 writes every column, so SQL `NULL` does not occur in X3 tables and `IS NULL` never matches:

- strings: `''` → test `<> ''`
- numbers and local menus: `0` → test `<> 0` (a local menu `0` means "not set")
- dates: `1599-12-31` → test `> '1599-12-31'`
- booleans (menu 1): `2` = Yes, `1` = No → `WHERE FLAG = 2` for "yes" rows

## 5. Join map (starter - verify each table and key in `V11/` before use)

| From | To | On | Dictionary source |
|---|---|---|---|
| `SORDER` (SOH, order header) | `SORDERQ` (SOQ, order lines/quantities) | `SOHNUM` (+ `SOPLIN`, `SOQSEQ`) | keys in `dict/Sales.md` |
| `SORDER` | `SORDERP` (SOP, order line prices) | `SOHNUM` + `SOPLIN` | `dict/Sales.md` |
| `SORDER.BPCORD` | `BPCUSTOMER` (BPC) / `BPARTNER` (BPR) | `BPCNUM` / `BPRNUM` | link expression on `BPCORD` |
| `SDELIVERY` (SDH) | `SDELIVERYD` (SDD) | `SDHNUM` | `dict/Sales.md` |
| `SINVOICE` (SIH) | `SINVOICED` (SID), `SINVOICEV` (SIV) | `NUM` | `dict/Sales.md` |
| `PORDER` (POH) | `PORDERQ` (POQ), `PORDERP` (POP) | `POHNUM` (+ line/seq) | `dict/Purchasing.md` |
| `PRECEIPT` (PTH) | `PRECEIPTD` (PTD) | `PTHNUM` | `dict/Purchasing.md` |
| `ITMMASTER` (ITM, item) | `ITMFACILIT` (ITF, item-site) | `ITMREF` + `STOFCY` | `dict/Common-Data.md` / `dict/Stock.md` |
| `STOCK` (STO) | `ITMMASTER` | `ITMREF` | `dict/Stock.md` |
| `GACCENTRY` (HAE, journal header) | `GACCENTRYD` (DAE, journal lines) | `TYP` + `NUM` | `dict/Financials.md` |
| any `*FCY` / `FCY` column | `FACILITY` (FCY, site) | `FCY` | type `FCY` linked table |
| any `CPY` column | `COMPANY` (CPY) | `CPY` | type `CPY` linked table |
| any `CRY` column | `TABCOUNTRY` (TCY) | `CRY` | type `CRY` linked table |
| any `CUR` column | `TABCUR` (TCU, currency) | `CUR` | type `CUR` linked table |

Abbreviations in parentheses are what the link expressions use (`[SOH]`, `[BPR]`); `table-index.md` maps them to table
names. Where the dictionary line gives a link expression, prefer it over this table.

## 6. View-writing rules

1. `CREATE OR ALTER VIEW <reporting schema>.<name>` - never create objects in the folder schema; put views in your own
   schema (or database) and reference `[FOLDER].[TABLE]`.
2. Expose decoded local menus with `CASE` (values from the dictionary), keep the raw number too.
3. Expand dimensioned columns explicitly (`BPCADDLIG_0`, `_1`, `_2`), never `SELECT *` - the column set depends on
   activity codes and changes between folders/versions.
4. Treat empties per § 4; don't `COALESCE` on NULL.
5. Dates are `DATETIME`: compare with date literals, and exclude `1599-12-31` when "no date" must not count.
6. `ORDER BY` inside a view is ignored by SQL Server - sort in the consumer.
7. Multi-folder reporting: one view per folder or a `UNION ALL` with a literal `FOLDER` column - never cross-join folders
   on `ROWID`.

## 7. Worked example (names and values verified in `V11/dict/Sales.md`, `Common-Data.md` and `local-menus.md` on 2026-10-02)

```sql
-- One row per sales order (grain: SORDER, key SOH0 = SOHNUM), folder SEED
CREATE OR ALTER VIEW rpt.SalesOrderHeader AS
SELECT  soh.SOHNUM,                                            -- SORDER.SOHNUM VCR  Order no.
        soh.ORDDAT,                                            -- SORDER.ORDDAT D    Order date
        soh.BPCORD,                                            -- SORDER.BPCORD BPR  Sold-to
        bpr.BPRNAM_0                     AS CustomerName,      -- BPARTNER.BPRNAM NAM(2): dimensioned -> BPRNAM_0 / BPRNAM_1
        soh.ORDSTA,                                            -- SORDER.ORDSTA M*15 Order state, local menu 415
        CASE soh.ORDSTA WHEN 1 THEN 'Open' WHEN 2 THEN 'Closed' END AS OrderStatus,
        soh.ALLSTA,                                            -- SORDER.ALLSTA M*15 Allocation status, local menu 416
        CASE soh.ALLSTA WHEN 1 THEN 'Not allocated' WHEN 2 THEN 'Partly allocated' WHEN 3 THEN 'Allocated' END AS AllocationStatus,
        soh.BPCADDLIG_0, soh.BPCADDLIG_1, soh.BPCADDLIG_2,     -- SORDER.BPCADDLIG ADL(3): three columns, not one
        soh.CUR                                                -- SORDER.CUR CUR -> TABCUR
FROM    SEED.SORDER   AS soh
JOIN    SEED.BPARTNER AS bpr ON bpr.BPRNUM = soh.BPCORD        -- link expression on BPCORD: [BPR]BPR0 =[SOH]BPCORD (BPARTNER)
WHERE   soh.ORDSTA = 1;                                        -- open orders only (menu 415 value 1); drop for all orders
```

Sanity check first: `SELECT TOP 20 * FROM rpt.SalesOrderHeader ORDER BY ORDDAT DESC;`
