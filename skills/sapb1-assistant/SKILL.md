---
name: sapb1-assistant
description: "SAP Business One (SAP B1 / B1) ERP assistant for consultants and integrators. Use for anything SAP Business One, even if the user only says \"B1\", \"SBO\", a table name (OINV, ORDR, OCRD, OITM), an object type number (\"ObjType 13\"), the DI API (SAPbobsCOM) or UDOs. Capabilities - (1) Object types: the object type number for a table or document, the table and key behind a number, objects by topic. (2) SQL / schema: verified SQL views and queries against a B1 company database from bundled B1 10.0 and 9.3 data dictionaries (tables, columns, indexes, valid values, parent links), and \"what table/field holds X\". (3) DI API development: generate and review C# against the DI API - connect, create/update documents and master data, services, transactions, errors, user-defined fields/tables/objects - from a bundled DI API 10.0 class and enum reference. More capabilities are added over time, so trigger on any SAP Business One question, casually phrased or not."
compatibility: "Runtime needs file read + grep over the bundled references. Refreshing references needs web access to the source sites, curl, and Python 3.10+ (scripts/ for the schema and the DI API reference, a documented procedure for the object list); none of that is needed to answer questions."
metadata:
  author: Francois Taljaard
  version: "2026.10"
  domain: SAP Business One ERP
---

# SAP Business One Assistant

> **Version disclaimer:** the bundled schema dictionaries cover **SAP Business One 10.0** (SAP's own reference, the default) and **9.3** only. Any other release, including later feature packs, can have tables and columns they lack, and a client's own user-defined tables and fields are never in them. State which version you used whenever you give SQL, and confirm any column that matters on the client's own database.

Reference-backed assistant for SAP Business One consultants and integrators. The rule that makes it
trustworthy: **every material claim comes from a bundled reference and is cited** — never from memory alone.
Object type numbers, table names and key columns are exactly the things a model guesses plausibly and wrongly.

## 1. Route the request

| Request looks like | Go to |
|---|---|
| "what's the object type for X", "what is object type N", "which table / primary key is behind N", "list the objects for sales / inventory / banking", UDO or DI API work that needs an object number | § 3 Object types |
| a view, query, report extract, "what table/field holds X", join, valid-value / status questions against B1 data | § 4 SQL / schema |
| generate or fix **C# against the DI API** (`SAPbobsCOM`): connect, create/update an invoice, order, business partner or item, read errors, transactions, UDFs/UDTs/UDOs, "what does this DI API property/method do", an enum value | § 5 DI API |
| both — "build a view over sales orders and tell me the ObjType" | § 4, using § 3 for object numbers |

Anything else (Service Layer or UI API code, version and upgrade questions, how-to procedures) is a planned
capability, see `MAINTENANCE.md`. Say so, answer what you can with the caveat that it is not
reference-backed, and note that the skill could be extended.

## 2. Ground rules

- **Never write SQL or code that modifies B1 tables directly.** Direct writes bypass B1's business logic and
  corrupt integrity; the supported write paths are the application, the DI API and the Service Layer. Don't
  print the modifying statement even as an illustration of what not to run; describe it in words. **In the DI
  API (§ 5) writes through its business objects and services ARE the correct path**, but `Recordset.DoQuery` is
  for reading only: never use it to change B1 data, and never invent an object number, enum value or member.
- **Verify, then cite.** Quote the object number, table and key from `references/objects/object-types.md`
  and say that is where it came from. If a number or table isn't in the list, say it isn't in the list —
  don't fill the gap from memory.
- **Know the source's limits.** Rows marked `sap-di` in the object list are confirmed by SAP's own DI API 10.0
  reference (`BoObjectTypes`); the other rows come only from two community websites that state no B1 version.
  For a number without `sap-di` that will ship (UDO registration, Service Layer calls), tell the user to confirm
  it against SAP's reference for the client's version.
- **Match the client's version** when it changes the answer, and ask if you can't tell. The bundled schemas are
  **B1 10.0** (default) and **9.3**; use the folder matching the client, otherwise 10.0, and say which. 10.0 has
  246 more tables and about 5,300 more columns than 9.3, so a 9.3 client can lack columns 10.0 shows and a later
  release can have ones it lacks. A client's own user-defined tables and fields are never in either. Give the user
  a way to confirm a column on their own database before they rely on it.
- **Ask which database** (SQL Server or SAP HANA) before writing SQL: the dictionary records column types, not
  dialect, and the two dialects differ.
- If the user reports a fact the references lack or contradict, say the reference should be updated
  (`MAINTENANCE.md`) rather than silently preferring either.

## 3. Object types

1. **Pin the question**: number → table, table → number, or a topic search ("everything about bins"). Note
   whether the user wants one object or a list.
2. **Read** `references/objects/INDEX.md` for the sources, their reliability and the known issues, then grep
   `references/objects/object-types.md`. One line per object: `| ObjType | Table | Description | Primary Key | DI API | Src | Notes |`.
   - By number: `^| 17 |`
   - By table: `\| ORDR \|`
   - By topic: `(?i)bin|batch|serial` against the Description column
3. **Read the Notes column** on every row you use. It flags blank source data (209, 225-227), table-name
   conflicts between the sources and where SAP's DI API class names a different table. Don't present a flagged
   row as settled. The **DI API** column is the `BoObjectTypes` member to use in C# (§ 5); a blank there means
   SAP's enumeration has no member for that number.
4. **Watch for shared tables**: `ODRF` carries two object numbers (112 and 1179), so a table name alone is not
   a unique key.
5. **Deliver** the number, table, description and key as a short table, cite `object-types.md`, and add the
   source caveat from § 2 when the answer will end up in code. If the user's table or number is missing from
   the list, say so and offer to check SAP's documentation.

## 4. SQL / schema

Bundled dictionaries: `references/dictionary/10.0/` (**default**, 2,784 tables, from SAP's own `REFDB.chm`) and
`references/dictionary/9.3/` (2,546 tables, from erpref.com, for clients still on 9.3). Below, `<ver>` is the
folder you chose. `references/dictionary/INDEX.md` has the sources, counts, the 9.3 to 10.0 changes and known issues.
**9.3 lists composite-key columns in reversed order; take key order from 10.0.**

1. **Pin the requirement**: entities, columns, filters (open only? date range? which currency?) and the
   **grain** (one row per document / per line / per item). B1 documents split into a header table and row
   tables, so grain decides the join. If grain, open-vs-closed or the database (SQL Server / HANA) is
   ambiguous, ask — status fields are multi-valued and a wrong guess silently drops or duplicates rows.
2. **Find the tables** by grepping `references/dictionary/<ver>/table-index.md` (one line per table: name,
   description, module, column and index counts, `ObjType`). Header and row tables read as a family
   (e.g. an order and its lines); check both.
3. **Verify every column** in `references/dictionary/<ver>/dict/<TABLE>.md` (one file per table, named exactly
   as the table). Never emit a column you haven't seen there. Lines read
   `name type(len) description default=… [valid values] ->parent table`. The `Indexes:` block lists physical
   indexes; the **first one is the primary key** (usually named `PRIMARY`) — join and filter on it.
4. **Join through the `->PARENT` links and index columns**, not by name similarity. A `->` link names the table
   a column refers to; it doesn't give the parent's key column, so confirm that against the parent file's
   first index. The links are the source's own mapping, not enforced foreign keys: don't join on `->ADP1`
   (see § 6 Gotchas).
5. **Decode valid values from the bracketed `[…]` lists**, never from memory: status flags, document types,
   Y/N fields. Decode with CASE in the output and cite the values used in filters. Read the list on the exact
   table, since the same column name can carry different values on different tables. A column with no list,
   or a value with a blank label (`[0=, 1=]`), has no documented meaning — say so rather than inventing one.
6. **Object numbers**: where a column holds an object type number, resolve it through
   `references/objects/object-types.md` (§ 3) and cite that file.
7. **Deliver**: one ```sql block with the complete `CREATE VIEW` (or query) in the right dialect, then a short
   note on the tables used and why, the joins, the status filters in business terms, and explicit assumptions
   (grain, currency, which date field). Add a sanity-check `SELECT TOP 20 …` (or `LIMIT 20` on HANA) to run
   first, and say which schema version you used, so columns should be confirmed on the client's database.

Grep recipes (paths relative to the skill root): `(?i)bin` in `references/dictionary/<ver>/table-index.md` →
tables by topic; `^  CardCode ` across `references/dictionary/<ver>/dict/` → which tables carry a column;
`->OCRD` across `references/dictionary/<ver>/dict/` → every column that points at the business partner table.

## 5. DI API development (C#)

Generate or review C# against the **DI API** (`SAPbobsCOM`): `Company` -> business objects and services. Scope is
this object library only, not the UI API, the Service Layer or DI Server. The reference is **DI API 10.0**
(10.00.190), which matches the default **10.0** schema dictionary; for a 9.3 client use the 9.3 folder and say so.

1. **Pin the request**: which object or document (invoice, order, business partner, item, UDO…), whether it is a
   **read** or a **create/update**, the B1 version and database (SQL Server / HANA), and what already exists
   (solution, connection handling). Ask when read-vs-write or the version changes the answer.
2. **Read** `references/diapi/INDEX.md`, then `references/diapi/di-api-guide.md`, and
   `references/diapi/common-mistakes.md` before writing code, so you produce the documented pattern and not the
   usual wrong one.
3. **Look up every class, member and enum you use** — never from memory. Find the class in
   `references/diapi/api/INDEX.md`, read `references/diapi/api/<Class>.md` (VB signature, parameters, return value,
   remarks, SAP's C# example where there is one), and read enum values in `references/diapi/enums/<Enum>.md`
   (`BoObjectTypes` holds the object numbers). An unfamiliar member gets looked up, not guessed.
4. **Verify table and column names** (for `Recordset` reads, field names, UDFs next to standard fields) in
   `references/dictionary/<ver>/` (§ 4) and say which version. A class's source table is in `api/INDEX.md`.
5. **Generate the documented pattern**: connect with the mandatory properties from configuration; check every
   return code and call `GetLastError` straight away; read lines in the order SAP's sample shows; wrap
   multi-object changes in `StartTransaction`/`EndTransaction`; `Marshal.ReleaseComObject` the `UserFieldsMD` /
   `UserTablesMD` / `UserObjectsMD` objects; disconnect in `finally`/`Dispose`.
6. **Examples are SAP's, labelled by language.** Prefer a `C# example`; a `VB example` is a pattern to translate
   (and a few SAP-labelled "C#" samples are really VB). Translate VB types with the table in the guide § 9.
7. **Deliver**: one ```csharp block, then a short note: which members and enums were verified in the reference,
   what is still unverified (for example a 10.0-only member on a 9.3 client, or a later feature pack), and the environment caveats from § 6.
   Offer a test plan or the matching read-only SQL (§ 4) as follow-ups.

## 6. Gotchas (things a careful engineer still gets wrong)

- **The schemas are B1 10.0 and 9.3 only.** Other releases and every client's user-defined tables and fields are
  absent; a column missing here isn't proof it's missing on the client's database. 9.3 to 10.0 added 246 tables,
  widened types (`MDP2.JrnlMemo` 50 to 254) and extended valid-value lists, so don't mix versions in one query.
- **9.3 key column order is reversed** against SAP's reference (`RDR1`: `LineNum, DocEntry` in 9.3,
  `DocEntry, LineNum` in 10.0). The column sets agree; use 10.0 for order.
- **Valid-value lists are per table.** `CANCELED` is `Y=Yes, N=No` on the sales order (`ORDR`) but also has
  `C=Cancellation` on the A/R invoice (`OINV`). A list can be partial too (`RDR1.BaseType` lists only
  `23=Sales Quotation` beside two blank labels), so treat it as "the values the source documents".
- **"Open" is not one column.** Documents carry `DocStatus` (`O`/`C`) and a separate `CANCELED` flag, and row
  tables carry their own `LineStatus`. Decide which the requirement means and say which you used.
- **`->ADP1` is not a join.** In 10.0, 955 of 1,279 `ObjType`/`ObjectType` columns are linked to `ADP1`
  (Object Settings - History). Resolve object numbers through `references/objects/object-types.md` instead.
  Links to `OACT`, `OOCR`, `OUSR`, `OCRD`, `OITM` and similar are genuine references (account, dimension, user,
  business partner, item). 24 links point at `OINM`/`OPMN`, which have no file.
- **Header and rows are separate tables** with a composite key on the row table (`RDR1`: `DocEntry, LineNum`).
  Joining header to rows on `DocEntry` alone is right; joining rows to rows without `LineNum` multiplies them.
- **Types are the source's, not SQL Server's.** `Num(19,6)`, `Int(11)` vs `Int(6)` (unexplained by the source)
  and `Identity(11)` are shown as given; the physical type on the client's database is the authority.
- **83 tables have a blank description** in 10.0 (84 have one equal to the table name in 9.3, e.g. `OSES`): the
  source gave nothing better.
- **`OSES`, `TAAS` and `TAASF` are the tables whose first index isn't named `PRIMARY`** (`PK_CODE`, `DUMMY`), which
  is why the rule is "first index".
- The object list behind `ObjType` comes from community websites and carries its own caveats (§ 2).

**DI API (§ 5):**
- **`Long` is `int`** in C#, and the reference prints Visual Basic signatures only; use the guide § 9 table and
  confirm anything unusual (`Integer`, `Variant`) in IntelliSense on the install.
- **Check the code, then call `GetLastError` immediately**; the error is lost on the next call. Business objects
  return a code, services throw `COMException`.
- **A failed call inside `StartTransaction` has already rolled back**; code that carries on is outside the
  transaction.
- **`Recordset.DoQuery` runs anything.** Reads only; writes go through business objects.
- **SAP's own samples are not all C#**: some blocks labelled C# are Visual Basic (tagged `vb` in `api/`).
- **Release `UserFieldsMD`/`UserTablesMD`/`UserObjectsMD` with `Marshal.ReleaseComObject`** after creating a UDF,
  table or UDO in .NET; SAP marks it IMPORTANT.
- **The DI API reference and the default schema are both 10.0.** 420 of the 438 source tables its classes name are
  in the 10.0 dictionary (404 in 9.3); the rest look like views or localization tables. Confirm columns on the
  client's database.

## 7. Layout

```
references/objects/      INDEX.md, object-types.md (the list), raw/<source>.md (verbatim extracts per source site)
references/dictionary/   INDEX.md, 10.0/ and 9.3/ each with table-index.md + dict/<TABLE>.md (one file per table)
references/diapi/        INDEX.md, di-api-guide.md (how-to), common-mistakes.md, api/ (INDEX.md + one file per class), enums/ (INDEX.md + one file per enumeration)
scripts/                 maintenance only (compile the 10.0 schema and the DI API reference from the SDK's CHMs; fetch + compile the 9.3 schema) — never needed to answer
evals/evals.json         test prompts per capability
MAINTENANCE.md           how to refresh the object list, the schema or the DI API reference, add a source, add a capability
```

Every `references/` folder has an `INDEX.md` with sources and verified dates per file — read it first, open
only what the request needs.
