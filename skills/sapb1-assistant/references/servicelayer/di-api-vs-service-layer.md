<!-- source: SAP "Working with SAP Business One Service Layer" v1.29 (2026-07-27), chapters 2.2, 8, 9, 10 and Appendices I-II (page numbers below are that document's); DI API facts from references/diapi/ | version: SAP Business One 10.0 | verified: 2026-10-04 -->

# DI API or Service Layer: choosing, and porting between them

Use this when the question is "which API should we build on", "can Service Layer do X that the DI API does",
"port this DI API code to Service Layer" or "why does the entity name differ". Every row below says whether it
comes from SAP's text or is engineering practice. Cite SAP's rows; label practice as practice.

## 1. Same core, different transport

SAP describes Service Layer as a 3-tier web application server whose **DI Core is the same interface the DI API
uses**, so "Service Layer API and DI API have identical definitions for objects and object properties"
(guide p. 12). The FAQ (p. 227) draws the lines between SAP's three data-integration APIs:

| API | SAP's characterisation |
|---|---|
| DI API | Microsoft COM; "fits best in the Windows native environment" |
| DI Server | SOAP-based data integration; web-services architecture |
| Service Layer | OData-compliant REST data service; "smoother learning curve"; add-ons in Java, JavaScript, .NET through third-party OData libraries; a full web application server with high availability and scalable performance |

Same objects, same business rules (tax, posting, approvals). The choice is about transport, transactions,
deployment and the few things each side cannot do.

## 2. Decision table

| Factor | DI API | Service Layer | Source |
|---|---|---|---|
| Runtime and language | COM library loaded in-process; Windows; .NET/C# (or anything that speaks COM) | Any HTTP client in any language; JSON only | p. 11, p. 227 |
| Where it runs | On the machine running your code; the installed DI API release must match the server (practice) | Server side: Apache load balancer + member nodes on SUSE Linux or Windows (Windows from 10.0 PL01); integrated or distributed mode | p. 12-14 |
| Multi-object transaction | `Company.StartTransaction` / `EndTransaction` spans any number of objects (diapi guide § 5) | **Not supported across requests.** A transaction is per request, or per `$batch` change set; a batch stops at the first failure and there is no rollback call. SAP: "you can enclose complex business logic in one transaction via DI API, while you cannot do it via Service Layer" | p. 225, p. 76-78, p. 234 |
| Escape hatch for complex transactions | n/a | Server-side **JavaScript extension** (9.2 PL04+, V8 engine): a script can `startTransaction`, add an order and a delivery, then commit or roll back in one HTTP call | p. 116, p. 132-133 |
| Server-side state | Connection object holds state between calls | Stateless HTTP; SAP: "may not be a good choice to implement complex or distributed transactions where server-side state management is a must-have" | p. 227 |
| Direct SQL | `Recordset.DoQuery` (reads only, skill rule) | **No Recordset.** Read paths: OData `$filter`/`$select`; `SQLQueries` (10.0 FP 2011, allowlisted tables, read-only); SQL views ending `B1SLQuery` (10.0 PL02, SQL Server only); Semantic Layer views (HANA only) | p. 225, ch. 4, p. 67, p. 52 |
| Query expressiveness | Full SELECT through Recordset | `$filter` supports only `startswith`, `endswith`, `contains`, `substringof` and the comparison/logical operators; no arithmetic operators; `$apply` aggregation, `$crossjoin` and the row-level `QueryService_PostQuery` are documented for HANA | p. 32, p. 225, p. 35, p. 42, p. 47 |
| XML import/export | `GetAsXML`, `SaveXML`, `UpdateFromXML`, `Company.GetBusinessObjectFromXML` (api/members.md) | **Not supported** (`ImportFromXML`/`ExportToXML`); XML request/response not supported for entity CRUD | p. 225 |
| UDF / UDT / UDO metadata | `UserFieldsMD`, `UserTablesMD`, `UserObjectsMD` | `UserFieldsMD`, `UserTablesMD`, `UserObjectsMD`, `UserKeysMD` entities with the same property names; **a newly created UDO/UDF/UDT is not accessible until Service Layer is restarted** | p. 86-96, p. 225, App. I 11.5-11.6 |
| Optimistic concurrency | Nothing equivalent in the bundled DI API reference (do not claim one) | Weak ETags with `If-Match`, HTTP 412 / SAP -2039 on conflict; 10.0 FP 2102, on 28 listed entities | p. 161-165 |
| Event notification | No subscription object in the DI API reference (desktop-client events belong to the UI API, out of scope) | Webhooks from 10.0 FP 2602 (see fp2602.md) | ch. 7 |
| Scaling and failover | One COM connection per process; scale by running more processes (practice) | Load balancer, multi-process nodes, sticky sessions; on node failure the next node re-validates the session from the database and re-logs the user in without credentials | p. 13, p. 226 |
| Login cost | One connect per process lifetime (practice: keep it open) | SAP calls login "a heavy job in SAP Business One"; sticky sessions exist to avoid repeating it (practice: pool and reuse sessions, respect `SessionTimeout`) | p. 226, p. 172 |
| Browser / mobile clients | Not applicable | CORS (configurable allowed origins and headers), Windows domain login (FP 2305), SSO | p. 136, p. 16 |
| Attachments | `Attachments2` object copies files from a source folder (api/INDEX.md) | `Attachments2` entity: multipart upload from a remote client, 50 MB cap, lines cannot be deleted; `Slug` stream upload from FP 2202 | p. 104-110 |
| Operations and diagnostics | Your process logs; `GetLastError` | Service Layer Controller (settings, nodes, logs, request monitor from FP 2202), Ping Pong API, per-request `B1S-<option>` headers | ch. 6, p. 137 |
| Licensing | Not covered by this guide. Both consume SAP Business One user licences; confirm with SAP's licensing guide for the client's contract | not in guide |

## 3. When the DI API is the right answer

SAP's own limitation list (p. 225) decides most of these:

- The work must be **one atomic unit across several business objects** and a change set cannot express it
  (for example conditional logic between the steps, or a step that reads the result of the previous one and
  then decides). Service Layer's only alternative is a server-side JavaScript extension, which is a different
  deployment model (`.ard` package, partner namespace) and a separate skill set.
- The integration **imports or exports B1 XML** documents.
- The process **creates UDFs/UDTs/UDOs and uses them straight away** in the same run; Service Layer needs a
  restart in between.
- The team already ships a Windows .NET add-on and the DI API is installed where the code runs.

## 4. When Service Layer is the right answer

- The caller is **not a Windows process**: web, mobile, Linux containers, iPaaS, a serverless function, Java or
  Node. There is nothing to install on the client side.
- You need **concurrency safety** on updates (ETags) or **event-driven** integration (webhooks, FP 2602+).
- You need **scale or availability**: many concurrent clients, failover without re-login (p. 226).
- The reads are entity-shaped (`$select`/`$filter`/`$expand`) or fit a small catalogue of `SQLQueries`.
- SAP positions it as the "new generation of extension API" (p. 11); new integrations should default here unless
  § 3 applies.

## 5. Hybrid (practice, not SAP guidance)

A common split is Service Layer for the integration surface and a small DI API worker only for the operations
in § 3. Keep the two behind one interface in your code so the choice can change per operation. Do not mix them
inside one business transaction: the DI API transaction cannot see uncommitted Service Layer work and vice versa.

## 6. Porting DI API code to Service Layer

Appendix I (p. 229-244) shows every operation side by side. The mapping:

| DI API | Service Layer | Notes |
|---|---|---|
| `GetBusinessObject(oOrders)`; set properties; `Lines.Add()`; `Add()` | `POST /Orders` with `DocumentLines` array | Response is the created entity (201) unless `Prefer: return-no-content` (204 + `Location`) (p. 28) |
| `GetByKey(2)` | `GET /Orders(2)`; string keys quoted `('c1')`, composite keys `(Code='AK',Type=-3)` | p. 26-27 |
| `GetByKey`; change; `Update()` | `PATCH /Orders(2)` with only the changed properties | `PUT` resets omitted properties to defaults; read-only properties in a PATCH are **silently ignored** (p. 27) |
| `Remove()` | `DELETE /Orders(2)` | Same business rule applies: a sales order cannot be deleted (error -5006, p. 28) |
| `CompanyService.GetCompanyInfo()` / `UpdateCompanyInfo` | `POST /CompanyService_GetCompanyInfo` / `POST /CompanyService_UpdateCompanyInfo` | Services become global actions named `<Service>_<Method>` (p. 232-233) |
| Object methods such as close or cancel | Bound actions: `POST /Orders(22)/Close`, `/Cancel` | p. 29 |
| `StartTransaction` … `EndTransaction(wf_Commit)` | One `$batch` change set with `Content-ID` references (`PATCH /b1s/v1/$1`) | Atomic per change set only; SAP shows `$n` in sub-request URLs, not inside JSON bodies, so a based document referencing `$1` in `BaseEntry` is untested; see § 2 (p. 76, p. 233-234) |
| `Recordset.DoQuery("select ...")` | `GET /BusinessPartners?$select=CardCode,CardName&$filter=CardCode ge 'C001'` or a `SQLQueries` entity | p. 234-235 |
| `bp.UserFields.Fields.Item("U_u1").Value` | Plain property `"U_u1"` on the entity; filter with `$filter=startswith(U_u1,'udf')` | p. 243-244 |
| UDT rows through `UserTable` / `CompanyService` | Entity `U_<TABLENAME>` (UDT `MYTBL` becomes `/U_MYTBL`, key `Code`) | p. 91 |
| UDO child lines `ChildTables` | Property `<ChildCode>Collection` (for example `MyOrderLinesCollection`) | p. 96 |
| Return code + `Company.GetLastError` | HTTP status + JSON `error.code` / `error.message.value`; the B1 message text is the same (for example `1320000140 - Business partner code ... already assigned`) | p. 25 |
| Enum member `BoCardTypes.cCustomer` | Either the member name `"cCustomer"` or the stored value `"C"`; both accepted on write and in `$filter` | p. 24, p. 33 |

### Names differ (Appendix II, p. 245-248)

Service Layer reuses DI Core metadata but renames to fit OData, so a DI API class or collection name is not a
safe guess for an entity or property. Patterns:

- **Child collections**: Service Layer drops underscores and pluralises. `Document_Lines` → `DocumentLines`,
  `JournalEntries_Lines` → `JournalEntryLines`, `Items_Prices` → `ItemPrices`, `ItemWarehouseInfo` →
  `ItemWarehouseInfoCollection`, `Payments_Invoices` → `PaymentInvoices`, `StockTransfer_Lines` →
  `StockTransferLines`, `ProductionOrders_Lines` → `ProductionOrderLines`, `PickLists_Lines` → `PickListsLines`.
  SAP lists about 70 such pairs; look up any collection you port rather than inferring the rule.
- **Singular business objects become plural**: `InventoryGenEntry` → `InventoryGenEntries`, `InventoryGenExit`
  → `InventoryGenExits`.
- **A property named like its own type gets `Property` appended**: `BatchNumber.BatchNumber` →
  `BatchNumber.BatchNumberProperty`, `Activity.Activity` → `Activity.ActivityProperty`,
  `PeriodCategory.PeriodCategory` → `PeriodCategory.PeriodCategoryProperty`.

Confirm the final name against the client's `/b1s/v2/$metadata` (the DI API side can be checked with
`Company.GetBusinessObjectXmlSchema`, p. 245).

## 7. Questions that settle the choice

1. Where will the code run, and can the SAP DI API be installed there?
2. Does any operation need more than one business object committed or rolled back together?
3. Is XML import/export part of the requirement?
4. Will the process create UDFs/UDTs/UDOs and use them in the same run?
5. How many concurrent callers, and is failover without re-login needed?
6. Is event notification (webhooks) wanted, and is the system on 10.0 FP 2602 or later?
7. SQL Server or HANA? Some Service Layer query features are documented for one database only (§ 2).

## 8. What this file does not say

It does not compare performance numbers, licensing cost or SAP's support roadmap for the DI API; SAP's guide
does not either. State that gap rather than filling it.
