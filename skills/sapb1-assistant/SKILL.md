---
name: sapb1-assistant
description: "SAP Business One (SAP B1 / B1) ERP assistant for consultants and integrators. Use for anything SAP Business One, even if the user only says \"B1\", \"SBO\", a table name (OINV, ORDR, OCRD, OITM), an object type number (\"object type 17\", \"ObjType 13\"), or the DI API / Service Layer / UDOs. Capabilities - (1) Object types: look up the object type number for a table or document, the table and primary key behind a number, or list objects by topic. (2) SQL / schema: turn a business requirement into verified SQL views and queries against a B1 company database using a bundled B1 9.3 data dictionary (tables, columns, indexes, valid values, parent-table links), and answer \"what table/field holds X\". More capabilities are added over time, so trigger on any SAP Business One question, casually phrased or not, and route to the matching capability."
compatibility: "Runtime needs file read + grep over the bundled references. Refreshing references needs web access to the source sites, curl, and Python 3.10+ (scripts/ for the schema, a documented procedure for the object list); none of that is needed to answer questions."
metadata:
  author: Francois Taljaard
  version: "2026.10"
  domain: SAP Business One ERP
---

# SAP Business One Assistant

> **Version disclaimer:** the bundled schema dictionary is **SAP Business One 9.3** only. Releases after 9.3 (10.0 and later) can have tables and columns it lacks, and a client's own user-defined tables and fields are never in it. State this whenever you give SQL, and confirm any column that matters on the client's own database.

Reference-backed assistant for SAP Business One consultants and integrators. The rule that makes it
trustworthy: **every material claim comes from a bundled reference and is cited** — never from memory alone.
Object type numbers, table names and key columns are exactly the things a model guesses plausibly and wrongly.

## 1. Route the request

| Request looks like | Go to |
|---|---|
| "what's the object type for X", "what is object type N", "which table / primary key is behind N", "list the objects for sales / inventory / banking", UDO or DI API work that needs an object number | § 3 Object types |
| a view, query, report extract, "what table/field holds X", join, valid-value / status questions against B1 data | § 4 SQL / schema |
| both — "build a view over sales orders and tell me the ObjType" | § 4, using § 3 for object numbers |

Anything else (DI API / Service Layer code, version and upgrade questions, how-to procedures) is a planned
capability, see `MAINTENANCE.md`. Say so, answer what you can with the caveat that it is not
reference-backed, and note that the skill could be extended.

## 2. Ground rules

- **Never write SQL or code that modifies B1 tables directly.** Direct writes bypass B1's business logic and
  corrupt integrity; the supported write paths are the application, the DI API and the Service Layer. Don't
  print the modifying statement even as an illustration of what not to run; describe it in words.
- **Verify, then cite.** Quote the object number, table and key from `references/objects/object-types.md`
  and say that is where it came from. If a number or table isn't in the list, say it isn't in the list —
  don't fill the gap from memory.
- **Know the source's limits.** The list is compiled from two community websites, not SAP documentation, and
  states no B1 version. For anything that ships (DI API, UDO registration, Service Layer calls), tell the user
  to confirm the number against SAP's reference for the client's version.
- **Match the client's version** when it changes the answer, and ask if you can't tell. The bundled schema is
  **B1 9.3 only**; a client on a newer release (10.0 and later) can have tables and columns it lacks, and a
  client's own user-defined tables and fields are never in it. Say so whenever the client's version isn't 9.3,
  and give the user a way to confirm a column on their own database before they rely on it.
- **Ask which database** (SQL Server or SAP HANA) before writing SQL: the dictionary records column types, not
  dialect, and the two dialects differ.
- If the user reports a fact the references lack or contradict, say the reference should be updated
  (`MAINTENANCE.md`) rather than silently preferring either.

## 3. Object types

1. **Pin the question**: number → table, table → number, or a topic search ("everything about bins"). Note
   whether the user wants one object or a list.
2. **Read** `references/objects/INDEX.md` for the sources, their reliability and the known issues, then grep
   `references/objects/object-types.md`. One line per object: `| ObjType | Table | Description | Primary Key | Src | Notes |`.
   - By number: `^| 17 |`
   - By table: `\| ORDR \|`
   - By topic: `(?i)bin|batch|serial` against the Description column
3. **Read the Notes column** on every row you use. It flags blank source data (209, 225-227, 300, 305) and
   table-name conflicts between the sources. Don't present a flagged row as settled.
4. **Watch for shared tables**: `ODRF` carries two object numbers (112 and 1179), so a table name alone is not
   a unique key.
5. **Deliver** the number, table, description and key as a short table, cite `object-types.md`, and add the
   source caveat from § 2 when the answer will end up in code. If the user's table or number is missing from
   the list, say so and offer to check SAP's documentation.

## 4. SQL / schema

Bundled dictionary: `references/dictionary/9.3/` — every table of the B1 9.3 schema, from erpref.com
(see `references/dictionary/INDEX.md` for the source, counts, known issues and what 9.3 can't tell you).

1. **Pin the requirement**: entities, columns, filters (open only? date range? which currency?) and the
   **grain** (one row per document / per line / per item). B1 documents split into a header table and row
   tables, so grain decides the join. If grain, open-vs-closed or the database (SQL Server / HANA) is
   ambiguous, ask — status fields are multi-valued and a wrong guess silently drops or duplicates rows.
2. **Find the tables** by grepping `references/dictionary/9.3/table-index.md` (one line per table: name,
   description, module, column and index counts, `ObjType`). Header and row tables read as a family
   (e.g. an order and its lines); check both.
3. **Verify every column** in `references/dictionary/9.3/dict/<TABLE>.md` (one file per table, named exactly
   as the table). Never emit a column you haven't seen there. Lines read
   `name type(len) description default=… [valid values] ->parent table`. The `Indexes:` block lists physical
   indexes; the **first one is the primary key** (usually named `PRIMARY`) — join and filter on it.
4. **Join through the `->PARENT` links and index columns**, not by name similarity. A `->` link names the table
   a column refers to; it doesn't give the parent's key column, so confirm that against the parent file's
   first index. The links are the source's own mapping, not enforced foreign keys: don't join on `->ADP1`
   (see § 5 Gotchas).
5. **Decode valid values from the bracketed `[…]` lists**, never from memory: status flags, document types,
   Y/N fields. Decode with CASE in the output and cite the values used in filters. Read the list on the exact
   table, since the same column name can carry different values on different tables. A column with no list,
   or a value with a blank label (`[0=, 1=]`), has no documented meaning — say so rather than inventing one.
6. **Object numbers**: where a column holds an object type number, resolve it through
   `references/objects/object-types.md` (§ 3) and cite that file.
7. **Deliver**: one ```sql block with the complete `CREATE VIEW` (or query) in the right dialect, then a short
   note on the tables used and why, the joins, the status filters in business terms, and explicit assumptions
   (grain, currency, which date field). Add a sanity-check `SELECT TOP 20 …` (or `LIMIT 20` on HANA) to run
   first, and say that the schema is 9.3, so columns should be confirmed on the client's database.

Grep recipes (paths relative to the skill root): `(?i)bin` in `references/dictionary/9.3/table-index.md` →
tables by topic; `^  CardCode ` across `references/dictionary/9.3/dict/` → which tables carry a column;
`->OCRD` across `references/dictionary/9.3/dict/` → every column that points at the business partner table.

## 5. Gotchas (things a careful engineer still gets wrong)

- **The schema is B1 9.3.** Newer releases and every client's user-defined tables and fields are absent; a
  column missing here isn't proof it's missing on the client's database.
- **Valid-value lists are per table.** `CANCELED` is `Y=Yes, N=No` on the sales order (`ORDR`) but also has
  `C=Cancellation` on the A/R invoice (`OINV`). A list can be partial too (`RDR1.BaseType` lists only
  `23=Sales Quotation` beside two blank labels), so treat it as "the values the source documents".
- **"Open" is not one column.** Documents carry `DocStatus` (`O`/`C`) and a separate `CANCELED` flag, and row
  tables carry their own `LineStatus`. Decide which the requirement means and say which you used.
- **`->ADP1` is not a join.** 862 `ObjType`/`ObjectType` columns are linked to `ADP1` (Object
  Settings - History); the other 289 have no link at all. Resolve object numbers through `references/objects/object-types.md` instead. Links to
  `OACT`, `OOCR`, `OUSR`, `OCRD`, `OITM` and similar are genuine references (account, dimension, user,
  business partner, item).
- **Header and rows are separate tables** with a composite key on the row table (`RDR1`: `LineNum, DocEntry`).
  Joining header to rows on `DocEntry` alone is right; joining rows to rows without `LineNum` multiplies them.
- **Types are the source's, not SQL Server's.** `Num(19,6)`, `Int(11)` vs `Int(6)` (unexplained by the source)
  and `Identity(11)` are shown as given; the physical type on the client's database is the authority.
- **84 tables have a description equal to their name** (e.g. `OSES`): the source gave nothing better.
- **`OSES` is the one table whose primary key isn't named `PRIMARY`** (`PK_CODE`), which is why the rule is
  "first index".
- The object list behind `ObjType` comes from community websites and carries its own caveats (§ 2).

## 6. Layout

```
references/objects/      INDEX.md, object-types.md (the list), raw/<source>.md (verbatim extracts per source site)
references/dictionary/   INDEX.md, 9.3/table-index.md, 9.3/dict/<TABLE>.md (one file per table)
scripts/                 maintenance only (fetch + compile the schema dictionary) — never needed to answer
evals/evals.json         test prompts per capability
MAINTENANCE.md           how to refresh the object list or the schema, add a source, add a capability
```

Every `references/` folder has an `INDEX.md` with sources and verified dates per file — read it first, open
only what the request needs.
