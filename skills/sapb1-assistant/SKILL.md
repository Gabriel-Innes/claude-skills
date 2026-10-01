---
name: sapb1-assistant
description: "SAP Business One (SAP B1 / B1) ERP assistant for consultants and integrators. Use for anything SAP Business One, even if the user only says \"B1\", \"SBO\", a table name (OINV, ORDR, OCRD, OITM), an object type number (\"object type 17\", \"ObjType 13\"), or the DI API / Service Layer / UDOs. Capability today - (1) Object types: look up the SAP B1 object type number for a table or document, the table and primary key behind a number, or list objects by topic, from a bundled list of all object types. More capabilities are added over time, so trigger on any SAP Business One question, casually phrased or not, and route to the matching capability."
compatibility: "Runtime needs file read + grep over the bundled references. Refreshing the object list needs web access to the source sites and a shell with curl and Python 3.10+; none of that is needed to answer questions."
metadata:
  author: Francois Taljaard
  version: "2026.10"
  domain: SAP Business One ERP
---

# SAP Business One Assistant

Reference-backed assistant for SAP Business One consultants and integrators. The rule that makes it
trustworthy: **every material claim comes from a bundled reference and is cited** — never from memory alone.
Object type numbers, table names and key columns are exactly the things a model guesses plausibly and wrongly.

## 1. Route the request

| Request looks like | Go to |
|---|---|
| "what's the object type for X", "what is object type N", "which table / primary key is behind N", "list the objects for sales / inventory / banking", UDO or DI API work that needs an object number | § 3 Object types |

Anything else (SQL against B1 tables, DI API / Service Layer code, version and upgrade questions, how-to
procedures) is a planned capability, see `MAINTENANCE.md`. Say so, answer what you can with the caveat that
it is not reference-backed, and note that the skill could be extended.

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
- **Match the client's version** when it changes the answer, and ask if you can't tell. Objects, tables and
  columns differ between B1 versions and between SQL Server and HANA.
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

## 4. Layout

```
references/objects/   INDEX.md, object-types.md (the list), raw/<source>.md (verbatim extracts per source site)
evals/evals.json      test prompts per capability
MAINTENANCE.md        how to refresh the object list from a website, add a source, add a capability
```

Every `references/` folder has an `INDEX.md` with sources and verified dates per file — read it first, open
only what the request needs.
