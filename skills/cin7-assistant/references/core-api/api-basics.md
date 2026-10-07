<!-- source: https://dearinventory.docs.apiary.io/ (Cin7 Core Developer Portal, API Blueprint export: introduction, "Connecting to the API", "Pagination", "API Status Codes", "Date Format" sections and the group-level notes named per section) | version: Cin7 Core API v2 (https://inventory.dearsystems.com/ExternalApi/v2/) | verified: 2026-10-07 -->

# Cin7 Core API v2: the basics

Protocol facts that apply to every endpoint, extracted from the portal's introduction and from the notes the
portal places at the top of a group. Endpoint-specific facts (fields, parameters, bodies) are in `groups/`.
Everything here is **Cin7 Core** (formerly DEAR Inventory); Cin7 Omni is a different product with a different API
and is not covered.

## 1. Product, base URL and format

| Fact | Value | Portal section |
|---|---|---|
| Product | Cin7 Core Inventory (web application at `https://inventory.dearsystems.com`) | API introduction |
| Base URL | `https://inventory.dearsystems.com/ExternalApi/v2/` and append the endpoint name, e.g. `.../ExternalApi/v2/me` | API introduction |
| Format | JSON only, in and out (`Content-type: application/json`) | API introduction, PHP sample |
| Scope | The API is a subset of the UI: check the endpoint list before promising a function | API introduction |
| Accounts | A Cin7 Core account is needed; trial accounts may use the API | API introduction |
| Previous version | A separate "previous API version" (v1) is documented at `http://support.dearsystems.com/solution/folders/1000134185`; nothing of it is bundled | Previous API version |
| Resilience | The portal tells integrators to queue every request and retry on network failure, never to assume the API is online | API introduction |

## 2. Authentication

| Fact | Value | Portal section |
|---|---|---|
| Credentials | an **Account ID** and an **API Application Key**, created on the API setup page inside Cin7 Core (`https://inventory.dearsystems.com/ExternalAPI`) | Connecting to the API |
| Headers on every request | `api-auth-accountid: <Account ID>` and `api-auth-applicationkey: <Application Key>` | Connecting to the API |
| Scope of an Account ID | one per company: each company the user can access has a different Account ID | Connecting to the API |
| Applications | several API Applications can exist on one account; **API limits are applied per API Application**, so give each integration its own key | Connecting to the API |
| Secrecy | the pair is equivalent to a login and password; never share or log it | Connecting to the API |
| Other schemes | none documented: no OAuth, no session, no token endpoint in the portal | (absence) |

There is no sign-in call: the first real request (for example `GET /me`, which returns the company name, base
currency, time zone, lock date and tax settings; `groups/me.md`) doubles as the connectivity test.

## 3. Pagination

| Fact | Value | Portal section |
|---|---|---|
| Parameters | `page` (default 1) and `limit` (default 100; minimum 1, maximum 1000) on the query string | Pagination |
| Response | paginated responses carry `Total` (overall record count) beside the list, e.g. `{ "Products": [...], "Total": 41 }` | Pagination |
| Endpoints named by the intro | SaleList, PurchaseList, StockAdjustmentList, StockTakeList, StockTransferList, Product, Category; the intro says "all remaining API endpoints do not support pagination" | Pagination |
| Endpoints that document `Page`/`Limit` | 47 GET actions list `Page` and `Limit` parameters in their own section (reference books, customers, suppliers, locations, `/me/addresses`, CRM lists and more); a few document a default `Limit` of 25 | each action's Parameters list in `groups/` |

The intro's list is narrower than the per-endpoint documentation. Trust the action's own Parameters list, and
page until a short page or until `Page * Limit >= Total`.

## 4. Status codes and limits

| Code | Portal meaning |
|---|---|
| `200 OK` | operation successful |
| `204 No Content` | successful, nothing to return |
| `400 Bad Request` | malformed request or posted data failed validation; read the error message in the body |
| `403 Forbidden` | method authentication failed (wrong or missing headers) |
| `404 Not found` | endpoint does not exist, e.g. `/Products` instead of `/Product` |
| `405 Not allowed` | method not allowed on that endpoint (e.g. PUT or DELETE where only GET/POST exist) |
| `429 Too Many Requests` | "You reached **60 calls per minute** API limit" |
| `500 Internal Server Error` | the object could not be parsed, or an unexpected server error |

Read both the status code and the error message. Rate-limit detail beyond the 60-per-minute line (burst rules,
daily caps, per-plan differences) is **not in the portal**; say so and point the user to Cin7 support.

## 5. Dates

All date fields, parameters included, are ISO 8601 in **UTC**: `yyyy-MM-ddTHH:mm:ss.fff`, e.g.
`2012-11-14T13:28:33.363` (Date Format section). `ModifiedSince`, `UpdatedSince` and `CreatedSince` filters take
the same format. A few fields are documented as "formatted in Tenant date format" (`LockDate`,
`OpeningBalanceDate` on `/me`): treat them as display strings.

## 6. How the documented endpoints are shaped

Patterns that repeat across the groups (each is restated in the group file where it applies):

- **Reference entities** (`/ref/brand`, `/ref/location`, `/customer`, `/supplier`, `/product`, ...): `GET` with
  filters and paging, `POST` to create, `PUT` to update, `DELETE ?ID=`. The field tables say `ID`: "Required for
  PUT, Ignored for POST" or "Required for PUT and DELETE, Ignored for POST".
- **Tasks** (sale, purchase, stock adjustment, stock take, stock transfer, journal, money task, finished goods,
  disassembly, inventory write-off): a list endpoint (`/saleList`, `/purchaseList`, `/stockTakeList`, ...), a
  detail endpoint (`GET ?ID=` or `?TaskID=`), `POST` to create, `PUT` to update (`TaskID`/`ID` "Required for
  PUT") and `DELETE ?ID=<id>&Void=<bool>`.
- **Void versus undo**: the `DELETE` of a task takes `Void` (optional, boolean, default `false`). `Void=true`
  voids the task; without it the call *undoes* it (the portal's wording is "Void or Undo"). Say which one the user
  wants before writing the call.
- **Sub-documents of a sale or purchase** (`/sale/quote`, `/sale/order`, `/sale/fulfilment/pick|pack|ship`,
  `/sale/invoice`, `/sale/creditnote`, `/sale/payment`, `/sale/manualJournal`, `/sale/attachment`;
  `/advanced-purchase/stock|put-away|invoice|creditnote|payment|manualJournal`): keyed by the parent `SaleID` /
  `TaskID`. The Purchase group states the common approach: **a `POST` overwrites the data of the related document
  (lines, additional charges) and adds the supplied entries**. Each `POST`/`PUT` lists the statuses it requires
  ("POST method will return exception if Order status is not DRAFT or NOT AVAILABLE"): read them before writing.
- **An empty collection deletes**: on `PUT /sale/invoice` it is allowed to omit attributes such as `Lines` and
  `AdditionalCharges`, but "provided empty collection means deleting existing records if there were any".
- **Creating a new task under a parent**: for sale invoices, sale credit notes and advanced-purchase stock
  receiving, a `TaskID` of `00000000-0000-0000-0000-000000000000` (or omitted, for stock receiving) creates a new
  task; an existing `TaskID` addresses that task.
- **Totals on POST**: `TotalBeforeTax`, `Tax`, `Total` on order, invoice and quote models are "Not required for
  POST": Cin7 Core computes them. Line `Total` fields are "for validation".
- **Deprecated records**: customers, suppliers and products carry `Status` = `Active` | `Deprecated`; list
  endpoints hide deprecated rows unless `IncludeDeprecated=true`. Locations use a `Deprecated` boolean.
- **Lookups by name**: many filters match "start with" (`Name` on reference books) while the product list's
  `Name` and `Sku` filters match "containing"; the Sale and Purchase lists have a `Search` parameter over several
  columns. The action's Parameters list says which.

## 7. Sales (group notes, `groups/sale.md`)

- **Sale types**: *Simple Sale* (one invoice, fulfilment and credit note per order), *Advanced Sale* (several
  per order), *Service-Only sale* (simple, service products only, no additional charges).
- **Service sale**: set `ServiceOnly = true` when creating; it cannot be changed later. The Sale Order and Sale
  Fulfilment endpoints are unavailable for it; the credit note `Restock` property is read-only; `TaskID` always
  equals `SaleID`.
- **Statuses**: the `Status` of a sale is derived from the quote, order, pick, pack, ship, invoice and credit
  note statuses (`enums.md`, "Available Sale Statuses"); `BACKORDERED` means the order is authorised with at least
  one backordered line.
- **Backorders are silent**: authorising an order with more quantity than is in stock creates a backorder record
  without an error.
- **`AutoPickPackShipMode`** on `POST /sale/order`: `NOPICK` (default), `AUTOPICK`, `AUTOPICKPACK`,
  `AUTOPICKPACKSHIP`; only for Simple Sales with no backorder, applied when the order becomes `AUTHORISED`.
- **Fulfilment**: adding a new fulfilment task to a Simple Sale turns it into an Advanced Sale; `DELETE
  /sale/fulfilment` works only on Advanced Sales; `POST /sale/fulfilment/pick` with `AutoPickMode = AUTOPICK`
  authorises the pick automatically; ship cannot be used when the sale has a product in an external location
  (external fulfilment service); `AddTrackingNumbers = true` lets a `PUT /sale/fulfilment/ship` change tracking
  numbers or carrier on an authorised shipment.
- **Payments**: prepayments only with an authorised quote and non-authorised order/invoice; payments only with
  an authorised invoice; refunds only with an authorised credit note; a `Prepayment` payment cannot be modified.
- **Quote**: `POST /sale/quote` fails when `SkipQuote` is `true`; stand-alone credit notes are not supported by
  POST.

## 8. Purchases (group notes, `groups/purchase.md`)

- **Two families of endpoints**. `/purchase/order|stock|invoice|creditnote|payment|manualJournal` are marked
  **deprecated and Simple Purchases only**; `/advanced-purchase/...` supports Simple, Advanced and Service
  Purchases. New work goes to `/advanced-purchase/...`.
- `POST` or `PUT` on `/advanced-purchase/stock` converts a Simple Purchase into an Advanced Purchase; `DELETE`
  there is not available for Simple Purchases.
- `/advanced-purchase/put-away` is the put-away stage. The portal's notes on `/advanced-purchase/stock` say, in
  consecutive bullets, that a Simple Purchase is converted to Advanced on POST/PUT **and** that the endpoint is
  "applicable only for Advanced Purchases and if `Use Put Away` option set to true in General Settings"; the two
  cannot both hold, so confirm on the account which setting gates stock receiving (`INDEX.md`, known limits).
- **Service purchases** contain additional charges only: GET returns empty `Lines` and filled additional lines;
  stock receiving is not available for them.
- **Approach**: with `Approach = INVOICE`, stock cannot be received until the invoice is `AUTHORISED`; with
  `Approach = STOCK`, the invoice cannot be posted until stock received is `AUTHORISED`.
- Stock receiving: duplicated lines in one payload are merged by quantity; a line that already exists for the
  same product, location, batch and expiry date raises an error; an empty-lines request authorises the receiving
  (same for put away). Manual-journal lines with `IsSystem = true` cannot be modified or deleted.
- Status values accepted on `POST` of a sub-document are only `DRAFT` and `AUTHORISED` (the full set of values
  is read-only state).

## 9. Other group notes

- **Chart of accounts**: updating accounts is not allowed while a Xero or QuickBooks integration is enabled.
- **Locations**: bins cannot be modified, only created and deleted.
- **Product**: `Type` (`Stock` | `Service`) is read-only on PUT; the COGS, expense and inventory accounts apply
  only to `Stock` products; `AverageCost` and `LastModifiedOn` (UTC) are read-only; `BOMType` is read-only.
- **Product family**: products listed in a PUT are added or updated, never deleted.
- **Product markup prices** (`/product/markup-prices`): the portal marks it "a planned API and is not available
  yet".
- **Production**: factory calendar days, resource capacities/costs/remarks/attachments and work centers do not
  support modification (create and delete only); a production order can be updated only in Draft or Planned
  status and only for a few fields; `BOMVersion` can change until the order is released.
- **Stock take**: `POST` creates the stock take with status `IN PROGRESS`; `PUT` modifies it.
- **Stock transfer**: `SkipOrder` defaults to `true` (no transfer order stage).
- **Webhooks** (`groups/webhooks.md`): need the automation module on the subscription; at most **5 webhooks of
  the same type** at a time; delivery is retried **6 times** (1 minute after the event, then 5, 10, 15, 20 and 25
  minutes after the previous attempt) and the webhook is **deactivated** when all fail; authorisation types
  `noauth`, `basicauth`, `bearerauth` with the matching required fields; event types and sample payloads are in
  the group file and in `enums.md` ("Available values for Webhook Type").
- **Transactions** (`GET /transactions`): the accounting transactions of a task, read-only.
