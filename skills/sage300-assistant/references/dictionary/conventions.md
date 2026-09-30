<!-- source: Sage 300 AOM data dictionary + SQL Server storage conventions | version: 6.0A, applies to all | verified: 2026-09 -->
# Sage 300 T-SQL conventions

How Sage 300 (Accpac) stores data in SQL Server, and the patterns to use when writing views and queries against it.

## Contents
1. Physical storage basics
2. Data type mapping (dictionary → SQL Server)
3. Dates and times
4. Decoding list fields (enums)
5. Split ("overflow") tables
6. Optional field tables
7. Common join map
8. View-writing rules
9. Worked example

## 1. Physical storage basics

- All tables live in the **company database**, schema **dbo**, named exactly as in the dictionary (`OEORDH`, `ARCUS`, ...).
- **Every column is NOT NULL.** "Empty" means `''` (spaces) for strings, `0` for numerics and dates. Never write `IS NULL` checks against Sage columns; compare to `''` or `0`.
- Strings are **CHAR, space-padded**. T-SQL `=` comparison ignores trailing spaces, but always `RTRIM()` string columns you expose in a view, and `RTRIM()` before concatenating.
- Every table carries audit columns `AUDTDATE`, `AUDTTIME`, `AUDTUSER`, `AUDTORG` (last-modified stamp, not creation).
- The dictionary's `<keylist>` entries are the physical indexes; the **first key is the primary key**. Use key fields in JOINs and WHERE clauses so queries use indexes.
- Item numbers: master files store the **unformatted** item number (`ICITEM.ITEMNO`, `OEORDD.ITEM` — no segment separators). Transaction detail tables usually also carry a formatted version (`OEORDD.FMTITEMNO`) for display. Join on the unformatted one.

## 2. Data type mapping (dictionary → SQL Server)

| Dictionary type | SQL Server type | Notes |
|---|---|---|
| `String*n` | `CHAR(n)` | space-padded, never NULL |
| `BCD*b.d` | `DECIMAL(2b-1, d)` | e.g. `BCD*10.0` → `DECIMAL(19,0)`, `BCD*8.3` → `DECIMAL(15,3)`, `BCD*5.4` → `DECIMAL(9,4)` |
| `Integer` | `SMALLINT` | 16-bit |
| `Long` | `INT` | 32-bit |
| `Boolean` | `SMALLINT` | 0 = No, 1 = Yes |
| `Date` | `DECIMAL(9,0)` | `YYYYMMDD`, `0` when empty |
| `Time` | `DECIMAL(9,0)` | `HHMMSSHH` (last 2 digits = hundredths), `0` when empty |

## 3. Dates and times

Dates are numeric `YYYYMMDD`. Convert for output and for comparing against real dates:

```sql
-- numeric Sage date -> SQL date (NULL when empty)
CONVERT(date, NULLIF(CAST(h.ORDDATE AS varchar(8)), '0'), 112)
```

Filtering is cheaper without conversion — compare numerically so indexes stay usable:

```sql
WHERE h.ORDDATE >= 20260101 AND h.ORDDATE < 20270101
```

Time `HHMMSSHH` → `hh:mm:ss`:

```sql
STUFF(STUFF(RIGHT('00000000' + CAST(h.AUDTTIME AS varchar(8)), 8), 5, 0, ':'), 3, 0, ':')  -- take first 8 then drop hundredths as needed
-- simpler, usually sufficient:
CONVERT(varchar(8), DATEADD(second,
    (h.AUDTTIME / 1000000) * 3600 + (h.AUDTTIME / 10000 % 100) * 60 + (h.AUDTTIME / 100 % 100), 0), 108)
```

## 4. Decoding list fields (enums)

Integer "list" fields (order TYPE, document status, etc.) carry their stored-value→label lists inline in the compiled dictionary (`references/dict/<MODULE>.md`), e.g. `TYPE Integer Order Type [1=Active,2=Future,3=Standing,4=Quote]`. Always decode them with CASE so the view is readable:

```sql
CASE h.[TYPE] WHEN 1 THEN 'Active' WHEN 2 THEN 'Future'
              WHEN 3 THEN 'Standing' WHEN 4 THEN 'Quote' END AS OrderType
```

Never guess enum values — read them from the table's field list in the compiled dictionary.

Note: `TYPE`, `STATUS`, `VALUE`, `DESC` and similar are reserved-ish words — bracket them: `[TYPE]`.

## 5. Split ("overflow") tables

Wide logical tables are physically split. A table's entry in the compiled dictionary carries a `Physical tables of this view:` line when this applies:

- **PO documents**: headers are `POPORH1` + `POPORH2` (purchase orders), `PORCPH1` + `PORCPH2` (receipts), `POINVH1` + `POINVH2` (invoices), etc. There is **no** `POPORH` table. Each split table has its own dictionary entry listing its fields; join the pair 1:1 on the sequence key (`PORHSEQ`, `RCPHSEQ`, ...).
- **OE orders**: `OEORDH` has a companion `OEORDH1` (1:1 on `ORDUNIQ`) holding later-added fields. If a field you expect isn't in the `OEORDH` entry, it is likely in `OEORDH1` — verify against `INFORMATION_SCHEMA.COLUMNS` when connected.

## 6. Optional field tables

Optional (user-defined) fields live in child tables named after the parent + `O` (e.g. `OEORDHO` for order headers, `ARCUSO` for customers): one row per parent key + `OPTFIELD`, with the value in `VALUE`. To show them as columns, pivot:

```sql
LEFT JOIN (
    SELECT ORDUNIQ,
           MAX(CASE WHEN OPTFIELD = 'PROJECT'  THEN RTRIM([VALUE]) END) AS Project,
           MAX(CASE WHEN OPTFIELD = 'REGION'   THEN RTRIM([VALUE]) END) AS Region
    FROM dbo.OEORDHO GROUP BY ORDUNIQ
) opt ON opt.ORDUNIQ = h.ORDUNIQ
```

## 7. Common join map

Header ↔ detail (1:N unless noted):

| Area | Join |
|---|---|
| OE orders | `OEORDH.ORDUNIQ = OEORDD.ORDUNIQ` |
| OE shipments | `OESHIH.SHIUNIQ = OESHID.SHIUNIQ` |
| OE invoices | `OEINVH.INVUNIQ = OEINVD.INVUNIQ` |
| OE credit/debit notes | `OECRDH.CRDUNIQ = OECRDD.CRDUNIQ` |
| PO purchase orders | `POPORH1.PORHSEQ = POPORL.PORHSEQ` (and `POPORH1 = POPORH2` 1:1) |
| PO receipts | `PORCPH1.RCPHSEQ = PORCPL.RCPHSEQ` |
| AP invoices (batch) | `APIBH.CNTBTCH/CNTITEM = APIBD.CNTBTCH/CNTITEM` |
| AR invoices (batch) | `ARIBH.CNTBTCH/CNTITEM = ARIBD.CNTBTCH/CNTITEM` |
| GL journals | `GLJEH.BATCHID = GLJED.BATCHNBR AND GLJEH.BTCHENTRY = GLJED.JOURNALID` |

Master-file lookups:

| From | To |
|---|---|
| `OEORDH.CUSTOMER` | `ARCUS.IDCUST` (customer name = `ARCUS.NAMECUST`) |
| `OEORDD.ITEM` | `ICITEM.ITEMNO` (item desc = `ICITEM.DESC`) |
| `OEORDD.LOCATION` | `ICLOC.LOCATION` |
| `POPORH1.VDCODE` | `APVEN.VENDORID` (vendor name = `APVEN.VENDNAME`) |
| `ICITEM.CATEGORY` | `ICCATG.CATEGORY` |
| AR open documents | `AROBL` (`IDCUST`, `IDINVC`, amounts `AMTDUEHC`/`AMTDUETC`) |
| AP open documents | `APOBL` (`IDVEND`, `IDINVC`) |
| IC on-hand by location | `ICILOC` (`ITEMNO`, `LOCATION`, `QTYONHAND`, `QTYONORDER`, `QTYSALORDR`) |

These are conventions, not gospel — confirm exact key fields on the table's `Keys:` line in the compiled dictionary before writing the JOIN.

## 8. View-writing rules

- **Read-only.** Never INSERT/UPDATE/DELETE Sage tables, never add triggers or alter them. Views, functions and separate reporting tables only.
- Name views `vw_<Subject>` (or the client's convention) and create them in the company database, schema `dbo`, with `CREATE OR ALTER VIEW`.
- Give business-friendly column aliases (`OrdNumber`, `CustomerName`), `RTRIM` all CHAR output, decode enums, convert dates.
- Multicurrency: many transaction tables carry both customer/source-currency and functional (home) currency amounts (e.g. `AMTDUETC` vs `AMTDUEHC`, or a `RATE` + `CURRENCY`). Ask which the user wants, or expose both.
- Quantities in OE/IC can be in different units — detail tables carry unit-of-measure and conversion factor fields; check before summing.
- Completed/status filters matter and are rarely what you'd guess: e.g. `OEORDH.COMPLETE` has FIVE values (1 Incomplete/Not Included, 2 Incomplete/Included, 3 Complete/Not Included, 4 Complete/Included, 5 Complete/Day End) — "open orders" is `COMPLETE IN (1,2)`. Always read the rotoid XML before writing a status filter, and ask whether the user wants open, completed, or all documents when the requirement is ambiguous.

## 9. Worked example

Requirement: "open sales orders with customer name, order value, item lines".

```sql
CREATE OR ALTER VIEW dbo.vw_OpenSalesOrderLines
AS
SELECT
    RTRIM(h.ORDNUMBER)                                          AS OrderNumber,
    CONVERT(date, NULLIF(CAST(h.ORDDATE AS varchar(8)),'0'),112) AS OrderDate,
    RTRIM(h.CUSTOMER)                                           AS CustomerNo,
    RTRIM(c.NAMECUST)                                           AS CustomerName,
    CASE h.[TYPE] WHEN 1 THEN 'Active' WHEN 2 THEN 'Future'
                  WHEN 3 THEN 'Standing' WHEN 4 THEN 'Quote' END AS OrderType,
    d.LINENUM                                                   AS LineNumber,
    RTRIM(d.ITEM)                                               AS ItemNo,
    RTRIM(d.[DESC])                                             AS ItemDescription,
    d.QTYORDERED, d.QTYSHIPPED, d.UNITPRICE,
    d.EXTOPRICE                                                 AS ExtendedPrice
FROM dbo.OEORDH h
JOIN dbo.OEORDD d ON d.ORDUNIQ = h.ORDUNIQ
LEFT JOIN dbo.ARCUS c ON c.IDCUST = h.CUSTOMER
WHERE h.COMPLETE IN (1, 2)  -- incomplete = open (5 values; verified in dict/OE.md)
  AND h.[TYPE] = 1;         -- active orders only
```

(Field names above were verified against the `OEORDH` / `OEORDD` entries in `dict/OE.md` — do the same for every field you emit.)
