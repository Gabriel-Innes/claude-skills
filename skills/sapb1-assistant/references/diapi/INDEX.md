# DI API index

SAP Business One **DI API** (`SAPbobsCOM`): how to program it from C#, and the full class and enumeration reference.
Read `di-api-guide.md` first, then open only what the request needs.

| Path | Covers | Version | Verified |
|---|---|---|---|
| `di-api-guide.md` | **Start here.** The how-to: the Company/business-object/service model, connect, errors, create/read/update (documents and lines), transactions, COM release, `Recordset`, user-defined fields/tables/objects, VB → C# type mapping | DI API 10.0 | 2026-10-01 |
| `common-mistakes.md` | 17 wrong patterns → the correct one, each tied to the reference file that backs it | DI API 10.0 | 2026-10-01 |
| `api/INDEX.md` | One line per class (1,378: 1,044 Objects, 334 Collections): kind, property/method counts, **source table** (557 classes name one), description. Find the class here | DI API 10.0 | 2026-10-01 |
| `api/<Class>.md` | One file per class, named exactly as the class: description, remarks, then every property (`[R]`/`[R/W]`/`[W]`) and method with its VB signature, parameters, return value, remarks, enum pointer and SAP's C# (or tagged VB) example | DI API 10.0 | 2026-10-01 |
| `enums/INDEX.md` | One line per enumeration (633): member count, description | DI API 10.0 | 2026-10-01 |
| `enums/<Enum>.md` | One file per enumeration: Member / Value / Description table (`BoObjectTypes` holds the object numbers) | DI API 10.0 | 2026-10-01 |

## Source

| | |
|---|---|
| File | `REFDI.chm`, "SAP Business One DI API 10.0 - Objects Reference (10.00.190)", copyright 2022 SAP SE |
| Where | `<SAP Business One SDK>\Help\REFDI.chm`, supplied with the SDK; not redistributed in this repo, only compiled |
| Built | `scripts/build_diapi_ref.py` (decompile with `hh.exe -decompile`, then run the script); 1,378 classes, 17,799 members, 633 enumerations, 0 pages missing |
| Terms | SAP's documentation. This project is not affiliated with or endorsed by SAP; check SAP's terms before redistributing |

## Contents and what's left out

- **Classes** include the "Services" (for example `AccountCategoryService`), data structures and collections; the
  CHM's own Object/Collection label is kept.
- **Examples**: SAP's C# examples are kept (334 blocks). Where a page has no C# sample, its Visual Basic sample is
  kept and tagged VB (235 blocks, to translate and not paste). Samples are truncated at 3,500 characters.
- **Left out**: the 466 separate `*_Sample_E.html` pages (generic samples repeated across many classes), the VB/C++
  syntax variants, the CHM's images and the global Methods/Properties cross-indexes (they duplicate the class files).
- **Remarks** are capped at 2,600 characters and descriptions at 700 (class descriptions 6,000); the cut is marked
  `[…]`. The CHM is the source of record.

## Known source issues

- **Mislabelled samples**: 11 examples that SAP's help labels C# are Visual Basic; they are tagged `vb` with a warning.
- **Only Visual Basic signatures** are shipped; see the VB → C# table in `di-api-guide.md` § 9.
- **Version**: this is DI API 10.0, which matches the default schema dictionary (`../dictionary/10.0/`, from SAP's
  `REFDB.chm`). Of the 438 distinct source tables named by classes, 420 exist in the 10.0 dictionary and 404 in 9.3.
  The 18 missing from 10.0 (`BTNT`, `BTNT1`, `IN10V`, `INC1V`, `INC2V`, `OAT4V`, `OFDV`, `OFEV`, `OGCL`, `OPB1`,
  `OPCH6`, `OTTG`, `OWDDV`, `SRNT`, `SRNT1`, `TTG1`, `VTR4`, `VTR5`) look like views (names ending in `V`) or
  localization tables; the reference doesn't say.
- Descriptions are SAP's and sometimes rough ("method GetLastErrorContext"). Some members have no useful text.
- The reference lists `dst_MSSQL2019` as its newest SQL Server enum member; confirm anything newer on the client's install.
