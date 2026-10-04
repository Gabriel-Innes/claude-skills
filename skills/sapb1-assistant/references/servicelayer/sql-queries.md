<!-- source: SAP "Working with SAP Business One Service Layer" v1.29 (2026-07-27) chapter 4 (pp. 140-160) and the FP 2011 change log; URLs in INDEX.md | version: SAP Business One 10.0 FP 2011+ | verified: 2026-10-04 -->

# Service Layer SQLQueries

`SQLQueries` exposes a controlled, read-only SQL facility through Service Layer, on both SQL Server and HANA.
SAP positions it as lighter than deploying SQL or Semantic Layer views and as a complement to OData queries
(p. 140).

## 1. Availability and versions

| Fact | Version | Source |
|---|---|---|
| `SQLQueries` entity, bound `List` function | 10.0 FP 2011 | p. 140, `fp2011-change` |
| UDO and UDT tables queryable | 10.0 FP 2102 | p. 160 |
| Query allowlist updated | guide 1.26 (2024-02) | Document History |

## 2. The entity

`SQLQuery` has key `SqlCode` and properties `SqlName`, `SqlText`, `ParamList`, `CreateDate`, `UpdateDate`.
Ordinary CRUD applies (`POST /SQLQueries`, `GET /SQLQueries('code')`, `PATCH`, `DELETE`, `GET /SQLQueries`
paged). Execution is the bound function `List`, callable with `GET` or `POST` (p. 140-143).

```http
POST /b1s/v2/SQLQueries
Content-Type: application/json

{
  "SqlCode": "open_orders",
  "SqlName": "Open orders",
  "SqlText": "select DocEntry, CardCode, DocTotal from ORDR where DocTotal > :docTotal"
}
```

The create response echoes `SqlText` **normalized** (bracketed identifiers on SQL Server, double-quoted on
HANA), `ParamList` as the parameter names, and an ETag. Run it either way:

```http
POST /b1s/v2/SQLQueries('open_orders')/List
{ "ParamList": "docTotal=10.1" }
```

```http
GET /b1s/v2/SQLQueries('open_orders')/List?docTotal=10.1
```

Several parameters: `stringParam1='val1'&integerParam2=val2` (strings quoted). The result is
`{ "SqlText": ..., "value": [ {column: value} ] }` with one key per select-list column or alias, paged with
`odata.nextLink` (`@odata.nextLink` on v4). Change the page size per request with
`Prefer: odata.maxpagesize=<n>`; the server confirms with `Preference-Applied` (p. 144-145, p. 151-153).

## 3. Read-only boundary

All DML (`update`, `insert`, `delete`, `alter`, …) is rejected at parse time with error 701
(`mismatched input 'update' expecting {SELECT, '('}`) (p. 157). That matches this skill's global rule: changes to
B1 data go through business objects or entities, never SQL.

## 4. What the SQL may contain

**Allowlist.** Only tables in `<install>/ServiceLayer/conf/b1s_sqltable.conf` can be queried. SAP's published
list covers company info and administration (`CINF`, `OADM`, `ADM1`, `OADP`), currencies and rates (`OCRN`,
`ORTT`), business partners (`OCRD`, `OCRP`, `CRD1`, `OCPR`), every marketing document header with row tables
1-14 (quotations to A/R and A/P credit notes, down payments, requests, returns), drafts (`ODRF`+`DRF1-14`),
payments (`ORCT`/`RCT1-4`, `OVPM`/`VPM1-4`, `ODPS`), banks (`ODSC`, `DSC1`), periods and branches (`OFPR`,
`OACP`, `OBPL`, `OHLD`/`HLD1`), items, warehouses, bins, batches and serials (`OITM`, `OITW`, `OIBQ`, `OBIN`,
`OBTQ`, `OBBQ`, `OBTN`, `OSRQ`, `OSBQ`, `OSRN`), prices (`OPLN`, `ITM1`), activities (`OCLG`, `OCLT`, `OCLS`),
attachments (`ATC1`), resources and routes (`ORSC`/`RSC1-6`, `ORST`), BOM and production (`OITT`/`ITT1-2`,
`OWOR`/`WOR1`/`WOR4`, `ORCJ`, `ORCM`), journal entries (`OJDT`, `JDT1`), credit cards (`OCRC`, `OCRH`) and
`ECM2` (p. 146-147). A table outside the list fails with error 702 `Table 'X' not accessible`; SAP says
removing tables is fine but adding is unsupported and a security risk. Check the client's file, not this list.

**Column lists.** The same file can carry `ColumnExcludeList` and `ColumnIncludeList` per table; a blocked
column fails with 703 `Column 'Algo' from table 'CINF' not accessible`. Names must match the database's case
(p. 147-148).

**Keywords** (p. 148-149): `select … from … where`, aliases, `and`/`or`/`not`, parentheses, `between`,
`order by`, `group by … having`, `is (not) null`, constants, `like`, `top`, `union (all)`, `in`, `exists`,
inner / left / right / full outer joins and mixes of them.

**Functions** (p. 149): `sum`, `avg`, `min`, `max`, `count`, `count(distinct …)`, `isnull`/`ifnull` (each is
normalized to the other database's spelling), `lower`, `upper`, `left`, `right`. Anything else, for example
`length`, fails with 701 `Cannot support this function or expression` (p. 155).

**Rules the parser enforces** (p. 155-157):

- `select *` in the select list is rejected (`Cannot support asterisk(*) in select list`); `select *` inside an
  `exists` subquery is accepted.
- Two columns with the same name or alias are rejected, because they would be duplicate JSON keys.
- A computed column needs an alias.

**Not queryable** (p. 160): log tables such as `AITM`, `ACRD`; `SBO-COMMON`; data ownership is not applied.

## 5. Normalization

Service Layer parses the raw SQL and rewrites identifiers for the target database (`[OITM]` or `"OITM"`), fixes
column aliases so JSON keys keep their case on HANA (which would otherwise upper-case them), and swaps
`isnull`/`ifnull`. A statement already quoted for one database is re-normalized, so the same `SqlText` works on
both (p. 150-151). Normalization is cosmetic: it does not verify that a column exists. Check names in the bundled
dictionary (`references/dictionary/<ver>/`) and on the client's database.

## 6. Permissions and audit

- A normal user gets 403 `-6006 You are not permitted to perform this action` until a superuser grants the
  specific query under the authorization subject **Service Layer SQL Query**; creating, updating and deleting
  queries needs **Modify SQL Queries in Service Layer**. Retrieval of definitions is allowed by default. The
  permission cache can take about a minute to refresh (p. 157-159).
- Parameter values are tokenized or prepared; an injection attempt such as
  `itemCode='i001';truncate table OITM` fails with 704 `Parameter error` (p. 159-160). Still never build
  `SqlText` from untrusted input: the protection covers parameter values, not the statement.
- Changes to query definitions are logged in table `ASQL` (p. 160).

## 7. Error codes

| Code | Meaning | Source |
|---|---|---|
| 701 | SQL grammar error, unsupported keyword or function, duplicate alias, `select *`, DML | p. 154-157 |
| 702 | Table not in allowlist | p. 154 |
| 703 | Column excluded or not included | p. 148 |
| 704 | Parameter error (including injection attempts) | p. 160 |
| -6006 (HTTP 403) | User lacks the query authorization | p. 158 |

## 8. Integration pattern (practice)

For an application or MCP server, keep a small catalogue of named, parameterised queries rather than an endpoint
that accepts arbitrary SQL. The allowlist and permission subjects make per-query authorization natural; the
catalogue makes output contracts and audit easier. Where a query needs a table outside the allowlist, use the
entity API or, on SQL Server, an exposed SQL view (`service-layer-guide.md` § 9) instead of editing the allowlist.
