# Objects index

SAP Business One object types: object type number ↔ table ↔ description ↔ primary key.

| Path | Covers | Verified |
|---|---|---|
| `object-types.md` | **The list.** 326 object types sorted by number, one line each: table, description, primary key, which sources carry it, and a Notes column flagging source conflicts and blanks. Read this first and grep it; don't open `raw/`. | 2026-10-01 |
| `raw/sapbusinessone.in.md` | Verbatim extract of the sapbusinessone.in table (326 rows). Kept so the next refresh can be diffed against what was last ingested. | 2026-10-01 |
| `raw/sap-b1-blog.com.md` | Verbatim extract of the sap-b1-blog.com table (320 rows), including its garbled translated columns. | 2026-10-01 |

## Sources

| Id | URL | Role | Rows | Page date |
|---|---|---|---|---|
| `in` | https://sapbusinessone.in/list-of-object-types-sap-business-one.html | Authoritative for table name, description, primary key (uses real DB column names) | 326 | none on page |
| `blog` | https://sap-b1-blog.com/en/glossary/list-of-object-types-in-sap-business-one/ | Cross-check only. Machine-translated from German, so some table names are corrupted | 320 | modified 2025-01-19 |

Both are community sites, not SAP documentation, and neither states a B1 version. Fetched 2026-10-01.

## Known source issues

- 6 rows exist only on `in` and are empty or near-empty: 209 (no data), 225-227 (`OAPA3`-`OAPA5`, no description or key), 300 (`RecordSet`, no table), 305 (`Bridge`, no table). They are kept so the numbering stays complete; don't infer anything about them.
- 8 table names are corrupted on `blog` (e.g. 16 `ORDER` vs `ORDN`, 10000206 `WHETHER IN` vs `OBIN`, 10000196 `TYPE` vs `RTYP`). `object-types.md` uses the `in` value and flags each one.
- `in` has a few typos carried through verbatim in descriptions: "Catagories" (134), "Bill Of Exchang" (182), "Autorization" (214).
- Descriptions and primary-key spellings differ cosmetically between the sources in about 50 rows; the `in` spelling is used.
