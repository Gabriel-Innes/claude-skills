# Dictionary index

SAP Business One data dictionary: every table, with columns, indexes, valid values and parent-table links.

| Path | Covers | Version | Verified |
|---|---|---|---|
| `9.3/table-index.md` | **Start here.** One line per table (2,546): name, description, module, column and index counts, `ObjType` where the table appears in `../objects/object-types.md`. Grep it by topic. | B1 9.3 | 2026-10-01 |
| `9.3/dict/<TABLE>.md` | One file per table, named exactly as the table (`dict/ORDR.md`). Header (module, column count, ObjType), `Indexes:` block (first = primary key, `U` = unique), then one line per column: `name type(len) description default=… [valid values] ->parent table`. | B1 9.3 | 2026-10-01 |

## Version map

| B1 release | Folder | Source |
|---|---|---|
| 9.3 | `9.3/` | erpref.com, see below |
| 10.0 and later | **not bundled** | erpref.com lists releases only up to 9.3. A client on a newer release can have tables and columns this lacks; a different source is needed. |

Pick `9.3/` for any client and **say so**: the dictionary is a 9.3 snapshot, and a client's own user-defined
tables and fields are never in it. Confirm any column that matters on the client's database.

## Source

| | |
|---|---|
| URL | https://erpref.com/BusinessOne9.3/Schema/Detail/BusinessOne9.3 |
| Fetched | 2026-10-01, with `scripts/fetch_erpref_schema.py` (2,546 tables, 0 failures) |
| Built | `scripts/build_schema_dict.py`; every table's column and index count matches the site's listing |
| Terms | The site's terms state that the page content belongs to ERPRef.com and that the database schema IP belongs to SAP. Neither is affiliated with this project. No warranty is provided by the site. |

## Contents

2,546 tables, 84,383 columns, 4,230 indexes; 12,949 columns carry a parent-table link and 13,654 carry a
valid-value list. About 5.0 MB.

| Module | Tables | Columns |
|---|---|---|
| Marketing Documents | 866 | 47,274 |
| General | 395 | 4,663 |
| Inventory and Production | 352 | 12,945 |
| Administration | 307 | 4,910 |
| Finance | 220 | 5,319 |
| Banking | 128 | 3,935 |
| Reports | 99 | 1,431 |
| Business Partners | 78 | 2,070 |
| Service | 43 | 958 |
| Human Resources | 28 | 440 |
| Sales Opportunities | 20 | 283 |
| MRP | 10 | 155 |

Module is the site's grouping, shown in `table-index.md`; it is not a B1 module name you can rely on beyond
topic search.

## Known source issues

- **Links are the source's own mapping**, naming the parent table only (never its key column), and are not
  enforced foreign keys. 862 `ObjType`/`ObjectType` columns link to `ADP1` (Object Settings - History), which
  is not a join; 289 other `ObjType`/`ObjectType` columns have no link. Links to `OACT` (1,723), `OOCR` (1,142),
  `OUSR` (781), `OCRD`, `OITM` and `OWHS` look like genuine references.
- **Valid-value lists vary per table and can be partial.** `CANCELED` has three values on `OINV` and two on
  `ORDR`; `RDR1.BaseType` lists one real value beside two blank labels. 1,066 values have a blank label
  (`[0=, 1=, 2=]`): the value exists, its meaning isn't given.
- **`OSES`** is the only table without an index named `PRIMARY` (its key is `PK_CODE`); the first index is
  the primary key in all 2,546 tables. The site's own "Primary" flag is "No" even on `PRIMARY` indexes, so it
  isn't used.
- **Types are shown as the source gives them**: `VarChar`, `nVarChar`, `Int`, `Num`, `Date`, `Text` and
  `Identity` (37 columns). `Int(11)` vs `Int(6)`, `Text(16)` and `Date(8)` lengths are unexplained, and no
  physical SQL Server or HANA type is stated.
- **84 tables have a description identical to their name** (e.g. `OSES`); none is blank.
- Defaults are shown only where the source gives a non-empty one.
