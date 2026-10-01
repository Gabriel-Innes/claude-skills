# Dictionary index

SAP Business One data dictionary: every table, with columns, indexes, valid values and parent-table links.
Two versions are bundled. **Use 10.0 unless the client is on 9.3.**

| Path | Covers | Version | Verified |
|---|---|---|---|
| `10.0/table-index.md` | **Start here.** One line per table (2,784): name, description, module, column and index counts, `ObjType` where the table appears in `../objects/object-types.md`. Grep it by topic. | B1 10.0 | 2026-10-01 |
| `10.0/dict/<TABLE>.md` | One file per table, named exactly as the table (`dict/ORDR.md`). Header (module, column count, ObjType), `Indexes:` block (first = primary key, `U` = unique), then one line per column: `name type(len) description default=… [valid values] ->parent table`. | B1 10.0 | 2026-10-01 |
| `9.3/table-index.md`, `9.3/dict/<TABLE>.md` | Same layout for B1 9.3 (2,546 tables). Kept for clients still on 9.3. **Composite-key column order is unreliable here, see Known issues.** | B1 9.3 | 2026-10-01 |

## Version map

| B1 release | Folder | Source | Quality |
|---|---|---|---|
| 10.0 | `10.0/` | SAP's own `REFDB.chm`, "SAP Business One SDK 10.0 - Database Tables Reference" | SAP documentation; use this |
| 9.3 | `9.3/` | erpref.com (third party), see below | Complete, but key column order is reversed against SAP's reference |
| anything else (9.0, 9.2, 10.0 FPs, newer than 10.0) | **not bundled** | | Use the nearest folder and **say so** |

The 10.0 reference is a single release (the CHM file is dated June 2022 and its overview names only "10.0"), so a
client on a later feature pack or release can have columns it lacks. A client's own user-defined tables and fields are never in
either dictionary. Confirm any column that matters on the client's database.

## Sources

| | 10.0 | 9.3 |
|---|---|---|
| Source | `REFDB.chm`, shipped with the SAP Business One SDK (`<SDK>\Help\REFDB.chm`); not redistributed, only compiled | https://erpref.com/BusinessOne9.3/Schema/Detail/BusinessOne9.3 |
| Built with | `scripts/build_refdb_schema.py` | `scripts/fetch_erpref_schema.py` + `scripts/build_schema_dict.py` |
| Checks | all 2,784 pages in the CHM's table of contents read; every table name matches its page; every row has the expected cells | every table's column and index count matches the site's listing |
| Terms | SAP's documentation; this project is not affiliated with or endorsed by SAP, and SAP's terms apply | The site's terms state its page content belongs to ERPRef.com and the schema IP to SAP; no `robots.txt`, no ban on automated access |

## Contents

| | 10.0 | 9.3 |
|---|---|---|
| Tables | 2,784 | 2,546 |
| Columns | 94,120 | 84,383 |
| Index definitions | 4,612 | 4,230 |
| Columns with a parent-table link | 14,641 | 12,949 |
| Size | about 5.9 MB | about 5.0 MB |

10.0 by module (the CHM's own grouping; a topic aid, not an SAP hierarchy):

| Module | Tables | Columns |
|---|---|---|
| Marketing Documents | 967 | 54,323 |
| General | 452 | 5,145 |
| Inventory and Production | 364 | 13,748 |
| Administration | 330 | 5,323 |
| Finance | 234 | 5,642 |
| Banking | 137 | 4,151 |
| Reports | 109 | 1,683 |
| Business Partners | 86 | 2,195 |
| Service | 45 | 997 |
| Human Resources | 30 | 466 |
| Sales Opportunities | 20 | 292 |
| MRP | 10 | 155 |

## What changed from 9.3 to 10.0

Measured by diffing the two folders (the sources differ, so treat small counts with care):

- **Tables**: 2,538 are in both; **246 are new in 10.0** (101 in Marketing Documents, 63 in General, 22 in Administration,
  14 in Finance, e.g. `AAAR`, `ACEST`, `ADO27`, `AEBK`); **8 are in 9.3 only** (`AEC6`, `ARPA`, `ARPR`, `GRTS`, `OPBU`,
  `ORPA`, `ORPR`, `WOR2V`).
- **Columns**: 753 shared tables gained columns (+5,308 in total); 7 lost some (19 in total, e.g. `AADM`/`OADM` lose
  `AuthURL`, `ClientID`, `ClntSecret`, `RedrctURL`, `TokenURL`, `EDocSeqNum`; `JDT1`/`BTF1`/`AJD1` lose `CAOutCode`).
  `ORDR` goes from 424 to 448 columns, `OCRD` from 367 to 388, `OITM` from 322 to 332.
- **Shared columns that changed**: 491 types (for example `MDP2.JrnlMemo` `nVarChar(50)` to `(254)`, `DRF1.Dscription`
  100 to 200), 779 valid-value lists (for example `OCMT.DataSource` gains `S=Service Layer` and `W=Web Client`,
  `ADO5.BaseType` gains `U=UoM`), 129 parent links, 49 defaults, 620 descriptions (the samples are rewordings).
- **DI API link**: of the 438 distinct source tables named by DI API classes (`../diapi/api/INDEX.md`), 420 are in the
  10.0 dictionary and 404 in 9.3.

## Known issues

- **9.3 composite-key column order is reversed against SAP's reference.** For the 2,613 keys that have the same
  columns in both folders and more than one column, 2,611 list them in exactly the opposite order. SAP's order
  looks right: it leads with the documented leading column (`RDR1` primary key is `DocEntry, LineNum` in 10.0 and
  `LineNum, DocEntry` in 9.3; `OITL.ITEM_CODE` leads with `ItemCode` in 10.0). Only the **order** differs; the
  column sets agree. Use `10.0/` for key and join questions, and for a 9.3 client read 9.3 key lists as sets.
  To confirm on a SQL Server database: select the index name, `key_ordinal` and column name from `sys.indexes`,
  `sys.index_columns` and `sys.columns` for the table, ordered by index name and `key_ordinal`.
- **Parent links are SAP's own mapping**, naming the parent table only (never its key column), and aren't enforced
  foreign keys. 955 `ObjType`/`ObjectType` columns in 10.0 link to `ADP1` (Object Settings - History), which is not
  a join; resolve object numbers through `../objects/object-types.md`. Links to `OACT`, `OOCR`, `OUSR`, `OCRD`,
  `OITM` and `OWHS` look like genuine references.
- **24 links in 10.0 point at tables with no page** in the reference: 23 at `OINM` (the inventory audit table; for
  example `AMR2.md`, `CIFV.md`, `IVLG.md`) and 1 at `OPMN`. They are kept as the source gives them.
- **Valid-value lists vary per table and can be partial.** `CANCELED` has three values on `OINV` and two on `ORDR`.
  1,030 values in 10.0 (1,066 in 9.3) have a blank label (`[0=, 1=, 2=]`): the value exists, its meaning isn't given.
- **First index is the primary key** (named `PRIMARY`) in all tables except `OSES` (`PK_CODE`), `TAAS` and `TAASF`
  (both `DUMMY`), so the rule is "first index".
- **Types are shown as the source gives them**: `VarChar`, `nVarChar`, `Int`, `Num`, `Date`, `Text`, `Identity`.
  `Int(11)` vs `Int(6)`, `Text(16)` and `Date(8)` sizes are unexplained, and no physical SQL Server or HANA type is
  stated. 10.0 writes `Num` as `Num(19,6)`; its page prints `19.6`.
- **Descriptions**: 83 tables in 10.0 have a blank description (their header reads `# NAME -`); in 9.3, 84 tables have
  a description identical to their name.
- Defaults are shown only where the source gives a non-empty one.
