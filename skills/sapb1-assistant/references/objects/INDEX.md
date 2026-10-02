# Objects index

SAP Business One object types: object type number ↔ table ↔ description ↔ primary key.

| Path | Covers | Verified |
|---|---|---|
| `object-types.md` | **The list.** 329 object types sorted by number, one line each: table, description, primary key, the DI API `BoObjectTypes` member (134 rows), which sources carry it, and a Notes column flagging source conflicts and blanks. Read this first and grep it. | 2026-10-01 |

This is the reconciled, factual list. Verbatim copies of the third-party source tables are **not** bundled; the
`Sources` table below records each source's URL, role and row count so a refresh can be re-fetched and diffed
against `object-types.md`.

## Sources

| Id | URL | Role | Rows | Page date |
|---|---|---|---|---|
| `in` | https://sapbusinessone.in/list-of-object-types-sap-business-one.html | Authoritative for table name, description, primary key (uses real DB column names) | 326 | none on page |
| `blog` | https://sap-b1-blog.com/en/glossary/list-of-object-types-in-sap-business-one/ | Cross-check only. Machine-translated from German, so some table names are corrupted | 320 | modified 2025-01-19 |
| `sap-di` | the `BoObjectTypes` enum in `../diapi/enums/` (find it through `../diapi/enums/INDEX.md`; compiled from SAP's `REFDI.chm`, DI API 10.0) | SAP's own documentation. Confirms object numbers and gives the DI API enum member; names a class, not a table, so it doesn't override table/key | 134 | copyright 2022 |

`in` and `blog` are community sites, not SAP documentation, and neither states a B1 version. Fetched 2026-10-01.

## Known source issues

- 6 rows exist only on `in` and are empty or near-empty: 209 (no data), 225-227 (`OAPA3`-`OAPA5`, no description or key), 300 (`RecordSet`, no table), 305 (`Bridge`, no table). They are kept so the numbering stays complete. SAP's enum confirms 300 (`BoRecordset`, "Recordset object") and 305 (`BoBridge`, "SBObob object"); nothing confirms 209 or 225-227, so don't infer anything about those.
- 8 table names are corrupted on `blog` (e.g. 16 `ORDER` vs `ORDN`, 10000206 `WHETHER IN` vs `OBIN`, 10000196 `TYPE` vs `RTYP`). `object-types.md` uses the `in` value and flags each one.
- `in` has a few typos carried through verbatim in descriptions: "Catagories" (134), "Bill Of Exchang" (182), "Autorization" (214).
- Descriptions and primary-key spellings differ cosmetically between the sources in about 50 rows; the `in` spelling is used.
- **SAP's enum vs the community list**: 131 of SAP's 134 numbers were already on the community list, which independently validates it. Three were missing and are added with `sap-di` only: 301 (`BoRecordsetEx`), 234000031 (`oReturnRequest`) and 234000032 (`oGoodsReturnRequest`). Of 102 rows where SAP's class has a source table to compare, 99 match the community table; 28, 46 and 219 differ in the way noted on those rows (the SAP class spans tables or names a variant). The community table is kept and the difference is noted.
- SAP's enum is **DI API 10.0**; the 195 rows without `sap-di` are not covered by it and may still be valid B1 objects.
