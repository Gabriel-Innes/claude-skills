<!-- source: SAP "Working with SAP Business One Service Layer" v1.29 (2026-07-27) chapters 2-3, 5, 6, 8-9 (page numbers below are that document's) and the Service Layer API Reference; URLs in INDEX.md | version: SAP Business One 10.0 | verified: 2026-10-04 -->

# Service Layer guide

How to build and review SAP Business One Service Layer integrations without guessing protocol, session,
query or concurrency behaviour. Exact business-object members still need verification against
`/b1s/v2/$metadata` or SAP's current API reference. For "DI API or Service Layer" and for porting code between
them, read `di-api-vs-service-layer.md`.

## 1. Protocol, versions and metadata

- Service Layer is an Apache-based application server in front of the same **DI Core** the DI API uses; objects
  and properties have identical definitions (p. 12). It runs on SUSE Linux and, from 10.0 PL01, on Windows.
- `/b1s/v1` is OData v3, `/b1s/v2` is OData v4 (p. 11). SAP's API reference states that **from FP 2405 OData v3 is
  deprecated and v4 is primary**; prefer `/b1s/v2` for new work. Most samples in SAP's guide still show `/b1s/v1`;
  the behaviour applies to v2 unless stated. Known v3/v4 differences: next-link annotation `odata.nextLink`
  versus `@odata.nextLink`; `$inlinecount` is v3-only; batch returns 202 on v3 and 200 on v4; actions are
  `FunctionImport` in v3 metadata; `Content-ID` is mandatory in v4 change sets (p. 29, p. 33, p. 35, p. 76, p. 78).
- `GET /b1s/v2/$metadata` is the authority for entity sets, types, properties, enums, actions and functions on the
  client's installation. Do not infer a Service Layer property name from a database column or a DI API name.
- From **10.0 FP 2608** the v4 metadata carries annotations (`Common.Label`, `SAPB1.TableName`,
  `SAPB1.ColumnName`, `SAPB1.ValidValue`) and scoped queries (`scope=entityset|enum`, `entityset=`,
  `dependency=`). SAP says the shape may change and not to build extensions on it (p. 19-20).

Sources: `guide-pdf`, `api-ref` in `INDEX.md`.

## 2. Login, session and logout (p. 16-17)

```http
POST /b1s/v2/Login
Content-Type: application/json

{ "CompanyDB": "SBODEMOUS", "UserName": "manager", "Password": "..." }
```

- Success returns `SessionId`, `Version` and `SessionTimeout` (minutes; default 30, a `b1s.conf` option) and sets
  two cookies. **`B1SESSION` is mandatory** on every later request. **`ROUTEID` is optional**: Apache adds it for
  load-balancer stickiness, and sending it back avoids a node hop. Send both.
- A missing or expired session answers `401` with error code `301` "Invalid session or session already timeout".
- `POST /b1s/v2/Logout` returns `204`.
- From 10.0 FP 2305 a Windows domain user can log in once Active Directory binding is configured (p. 16).
- Login is expensive for B1 (p. 226): reuse sessions and refresh before `SessionTimeout`, rather than logging in
  per request (practice).

## 3. Read and query (p. 23-35, p. 50-51, p. 79-83)

- Key syntax: `GET /BusinessPartners('c1')` or `(CardCode='c1')`; integers unquoted `GET /Orders(22)`; composite
  `GET /SalesTaxAuthorities(Code='AK',Type=-3)`.
- `$filter` functions supported: **`startswith`, `endswith`, `contains`, `substringof` only**; operators
  `eq ne gt ge lt le and or not` with parentheses. **Arithmetic operators and the other OData functions (string,
  date, math, type cast) are not supported** (p. 32, p. 225). Enum properties accept the member name or the stored
  value (`CardType eq 'cCustomer'` or `'C'`). Dates accept `'2014-04-23'`, `'20140423'` or `datetime'…'`; the
  time part of a date is ignored and the date part of a time is ignored (p. 33-34).
- `$select`, `$orderby`, `$top`, `$skip` (`$skip` applies before `$top`), `/$count`.
- **Paging**: collections page at `PageSize` (default 20, `b1s.conf`); override per request with
  `Prefer: odata.maxpagesize=<n>` (confirmed by `Preference-Applied`); 0 disables paging. Follow the next link
  rather than computing `$skip` yourself (p. 34-35).
- `$expand` only where metadata defines a navigation property; from 10.0 FP 2105 it takes a nested `$select`:
  `ServiceCalls(1)?$expand=BusinessPartner($select=CardCode,ContactPerson)&$select=Subject`. SAP warns that
  `$expand` on collections can be slow (p. 50-51, p. 83).
- Individual property: `GET /Orders(1)/DocEntry` (`{"value": 1}`, or `@odata.null`); raw with `/$value`.
  Properties of a complex type cannot be addressed (p. 79-80).
- **HANA-only query features** per the guide: `$apply` aggregation and `groupby` (9.1 PL12 / 9.2 PL03 HANA),
  `$crossjoin` (9.2 PL07 HANA) and the row-level filter `POST /QueryService_PostQuery` with `QueryPath` +
  `QueryOption` (9.2 PL11 HANA). Do not propose them on SQL Server without confirming on the client (p. 35-49).
- Per-request options via `B1S-<option>` headers, for example `B1S-PageSize: 100`, `B1S-CaseInsensitive`, or
  `B1S-Schema: <file>` to apply a server-side trimmed schema (p. 84-86, p. 174-175).

## 4. Create, update, delete, actions (p. 24-31)

- `POST /<EntitySet>` returns `201` with the entity; add `Prefer: return-no-content` for `204` + `Location`.
- `PATCH /<EntitySet>(key)` changes only the given properties (`204`). `PUT` replaces: omitted properties go to
  default or null. **Read-only properties in a PATCH are ignored silently**, not rejected. A client without PATCH
  can send `POST` with `X-HTTP-Method-Override: PATCH` (also PUT, MERGE, DELETE) (p. 27, p. 227).
- `DELETE /<EntitySet>(key)`; business rules still apply (deleting a sales order fails with `-5006`).
- **Bound actions**: `POST /Orders(22)/Close`, `/Cancel`. **Global actions** expose services as
  `<Service>_<Method>`: `POST /CompanyService_GetCompanyInfo`, `POST /ActivitiesService_AddActivity`.
  `POST /OrdersService_Preview` returns the document as B1 would compute it (totals, accounts) without saving.
- Errors are `4xx` with `{"error": {"code": <B1 code>, "message": {"lang", "value"}}}`; the message text is the
  same B1 message the DI API returns.

A Service Layer write is a supported B1 write path. Direct SQL against B1 tables is not.

## 5. Optimistic concurrency with ETags (p. 161-166)

Available from **10.0 FP 2102**, weak validators (`W/"…"`) returned in the `ETag` header and `@odata.etag`.

1. `GET` the entity and keep the ETag.
2. Send it as `If-Match` on `PATCH`, `DELETE` or a bound action such as `POST /Orders(8)/Cancel`.
3. `412 Precondition Failed` with SAP error `-2039` ("Another user or another operation modified data") means
   re-read and reconcile, never resend the stale payload. Without `If-Match` the write overwrites blindly.

SAP's list of ETag-enabled objects (p. 164-165): the marketing documents (Orders, Quotations, DeliveryNotes,
Returns, ReturnRequest, GoodsReturnRequest, Invoices, CreditNotes, DownPayments, Drafts, PurchaseQuotations,
PurchaseRequests, PurchaseOrders, PurchaseDeliveryNotes, PurchaseReturns, PurchaseInvoices,
PurchaseCreditNotes, PurchaseDownPayments, the CorrectionInvoice and CorrectionPurchaseInvoice variants),
InventoryGenEntries, InventoryGenExits, Activities, AdditionalExpenses, Items and BusinessPartners. Other
entities may not return an ETag; check the response. In v4 metadata the entity set carries the
`Org.OData.Core.V1.OptimisticConcurrency` annotation on `DataVersion`.

## 6. Batch and transactions (p. 74-79, p. 225, p. 233-234)

- `POST /b1s/v2/$batch`, `Content-Type: multipart/mixed;boundary=…`; each sub-request is
  `Content-Type: application/http` + `Content-Transfer-Encoding: binary`; a `GET` sub-request needs two blank
  lines after the request line. Sub-requests run sequentially.
- A **change set** is the atomic unit: any failure rolls back the whole change set, and only one response is
  returned for it. Change sets cannot contain `GET`s or nested change sets. `Content-ID: n` lets later
  requests reference a created entity as `$n` (`PATCH /b1s/v1/$1`, `POST $1/Cancel`); mandatory in v4.
- A valid batch answers `202` (v3) or `200` (v4) even if sub-requests failed; **the batch stops at the first
  failing sub-request**. Read every sub-response.
- **There is no `StartTransaction`/`EndTransaction` and no batch rollback call.** A transaction never spans
  requests. For logic that must be atomic across objects with branching in between, the options are the DI API
  or a server-side JavaScript extension (9.2 PL04+, `slContext.startTransaction()` … `commitTransaction()`,
  p. 116-135); see `di-api-vs-service-layer.md`.

## 7. User-defined fields, tables and objects (p. 86-100)

- Metadata entities: `UserFieldsMD` (key `TableName`, `FieldID`), `UserTablesMD`, `UserObjectsMD`,
  `UserKeysMD`. Payload property names match the DI API (`Type: db_Alpha`, `SubType: st_None`,
  `TableType: bott_NoObject | bott_Document | bott_DocumentLines`, `ObjectType: boud_Document`).
- UDF names get the `U_` prefix on entities. Creating a UDF on a table also creates it on the related tables
  (archive table; for `RDR1` on every marketing-document row table). DDL on heavily referenced tables is slow.
- A "no object" UDT `MYTBL` is exposed as entity `U_MYTBL` with key `Code` and properties `Name`, `U_F1`…
  The database table is `@MYTBL` and UDF requests use that name.
- A UDO entity is addressed by its **code** (`POST /MyOrder`); child tables appear as `<ChildCode>Collection`
  (`MyOrderLinesCollection`); `Cancel`/`Close` need `CanCancel`/`CanClose` set to `tYES` on `UserObjectsMD` first.
  Schema files use the UDO **name**, URLs the code.
- **New UDO/UDF/UDT metadata is visible only after a Service Layer restart** (p. 225). Plan deployments
  accordingly.

## 8. Attachments and images (p. 100-116)

- `Attachments2`: `POST` with a local `SourcePath` (file already on the Service Layer host) or
  `multipart/form-data` with one or more `files` parts; `PATCH` replaces or appends lines; download with
  `GET /Attachments2(3)/$value?filename='line2.png'`. Attachment lines **cannot be deleted**; uploads over
  **50 MB** fail with `413`. The attachment folder must be reachable by the Service Layer service account
  (Network Service on Windows; CIFS mount as `b1service0` on Linux).
- From 10.0 FP 2202, `Attachments2` and `Pictures` accept a stream upload with a `Slug` header (OData media
  entity). `ItemImages('i001')/$value` and `EmployeeImages` read images; item images are uploaded by `PATCH`,
  not `POST`, and cannot be queried as a collection.

## 9. SQL views and Semantic Layer views (p. 52-73)

- **SQL views (SQL Server, 10.0 PL02+)**: a view in schema `dbo` whose name ends in `B1SLQuery` can be exposed
  with `POST /SQLViews('<name>')/Expose` (or `('*')`) and read at `/b1s/v2/view.svc/<name>` with ordinary
  query options. Views have no key, so Service Layer adds a virtual `id__` that only supports simple access.
  Normal users need the view granted under Authorizations (error 804 otherwise); changes may take about a
  minute to apply.
- **Semantic Layer views (HANA only, 9.3 PL02+)**: calculation views with the `Query` suffix, exposed per view in
  the HANA Model Management window, served at `/b1s/v1/sml.svc` (OData v4 by default) after a restart.
- `SQLQueries` (`sql-queries.md`) is SAP's lighter alternative on both databases.

## 10. Configuration and operations (ch. 6, p. 136-139, p. 226)

- `conf/b1s.conf` (JSON, case-sensitive, restart to apply) holds `PageSize` (20), `SessionTimeout` (30),
  `Schema`, `SLDAddress`, `CorsEnable` + `CorsAllowedOrigins` (`;`-separated; `*` discouraged) +
  `CorsAllowedHeaders` (default `content-type, accept`), `WCFCompatible` (enums become strings, same-named
  properties get `Property`, `Edm.Time` becomes `Edm.DateTime`), `LogLevel`, `EnableCoreDump`,
  `EnableAccessLog` (**off by default from FP 2305**), and `EnableAudienceValidation` for SPA tokens.
  Any option except connection options can be overridden per request with a `B1S-<option>` header.
- **Service Layer Controller** at `https://<host>:<port>/ServiceLayerController` (10.0 PL00 HANA / PL02 SQL):
  node add/remove, settings, log download, and from FP 2202 a request monitor (normal and error requests with
  duration, session, node, PID and client IP). Request/response dumps are a separate switch. It cannot manage
  nodes on other machines in distributed mode.
- **Ping Pong API** (9.3 PL10+): `GET /ping/`, `/ping/load-balancer`, `/ping/node/<n>` answer `pong` from Apache
  without touching B1, so network latency can be separated from B1 processing. A down node answers `503`.
- **High availability**: Apache load balancer with sticky sessions; if a node fails, the next node validates the
  session from shared session data in the database and re-logs the user in without credentials. SAP
  recommends firewalling member nodes so only the load balancer reaches them (HTTP between them).

## 11. Limitations to remember (p. 225)

No OData 1.0/2.0; no XML for entity CRUD; no access to complex-type sub-properties; no batch rollback; no
`odata.metadata=full`; no arithmetic operators or most OData functions in queries; no `Recordset`; no
`ImportFromXML`/`ExportToXML`; new UDO/UDF/UDT need a restart; no user transactions across requests; no JSONP.

## 12. Errors and verification

- Preserve the HTTP status and SAP error body in logs; never log credentials or session cookies.
- A missing entity or property in this curated guide is **not** proof that Service Layer lacks it: check the
  client's `$metadata`.
- For feature-pack behaviour, identify the installed version and read the sequential API change log.

## 13. Engineering pattern (practice)

Separate base URL and credentials, session handling (login, cookie jar, refresh before timeout, re-login on
`401`/`301`), business operations, DTOs and ETag handling. Treat batch change sets as the only atomic unit and
design retries to be idempotent. These are practices; the protocol facts they rely on are the documented
behaviour above.
