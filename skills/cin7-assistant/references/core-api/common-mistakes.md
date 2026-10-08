<!-- source: facts from the Cin7 Core Developer Portal (https://dearinventory.docs.apiary.io/) sections named per row; the "Looks like" column is the mistake an integrator makes, the "Rule" column is the portal's statement | version: Cin7 Core API v2 | verified: 2026-10-07 -->

# Common mistakes when coding against the Cin7 Core API

Use as a review checklist. Grep a request or codebase for the pattern in "Looks like", then apply the rule. The
last column names the file and section that backs the rule.

| # | Looks like | Why it is wrong | Rule (reference) |
|---|---|---|---|
| 1 | `Authorization: Bearer ...`, `?apikey=`, basic auth, or a sign-in call | The API has no token or session flow; every request carries two headers: `api-auth-accountid` and `api-auth-applicationkey`. | `api-basics.md` § 2 (Connecting to the API) |
| 2 | One Application Key shared by several integrations | API limits are applied per API Application; sharing a key makes one integration's traffic throttle the others. | `api-basics.md` § 2 |
| 3 | Account ID or Application Key in source, logs or examples | The pair is equivalent to a login and password. Use placeholders and secrets storage. | `api-basics.md` § 2 |
| 4 | `GET /ExternalApi/v2/Products`, `/Sales`, `/Customers` | Endpoint names are singular or exact (`/product`, `/sale`, `/customer`); a wrong name is a 404. Copy the path from `endpoints.md`. | `api-basics.md` § 4; `endpoints.md` |
| 5 | `GET /ExternalApi/v2/saleList` with no paging, expecting everything | Paginated endpoints return one page (`limit` default 100, max 1000) plus `Total`; loop on `page` until a short page or `page * limit >= Total`. | `api-basics.md` § 3 |
| 6 | `?limit=5000` | The maximum page size is 1000; the minimum is 1. | `api-basics.md` § 3 |
| 7 | Firing requests in parallel or retrying a 429 immediately | 429 means the 60-calls-per-minute limit of the application; throttle client-side and back off. | `api-basics.md` § 4 |
| 8 | Treating a 400 or 500 as transient and retrying the same body | 400 is validation or shape; 500 includes "the object passed could not be parsed". Read the error message, fix the body. The portal also says to queue requests and retry only network failures. | `api-basics.md` § 1, § 4 |
| 9 | `ModifiedSince=14/11/2012` or a local-time stamp | All dates are ISO 8601 **UTC** `yyyy-MM-ddTHH:mm:ss.fff`, parameters included. | `api-basics.md` § 5 |
| 10 | `PUT /customer` without `ID`, or `POST /customer` with an `ID` to "upsert" | `ID` is "Required for PUT, Ignored for POST": POST always creates; PUT needs the ID. Same for `TaskID` on tasks. | field tables in `groups/` (e.g. `brand.md`, `customer.md`, `sale.md` Sale POST/PUT Attributes) |
| 11 | `DELETE /sale?ID=...` intended to void a sale | Without `Void=true` the DELETE *undoes* the task (portal: "Void or Undo"; `Void` default `false`). Decide void versus undo and set the parameter. | `api-basics.md` § 6; the DELETE action in each task group |
| 12 | `POST /sale/order` to "add one more line" | On sub-documents a POST overwrites the related document's lines and additional charges and adds the supplied entries; send the full intended set. | `api-basics.md` § 6 (Purchase group note); `groups/purchase.md` |
| 13 | `PUT /sale/invoice` with `"Lines": []` meaning "leave lines alone" | An empty collection deletes the existing records; omit the attribute instead. | `groups/sale.md` Sale Invoice PUT notes |
| 14 | Posting an order while the quote is still `DRAFT`, or an invoice while the order is not authorised | Each sub-document POST/PUT lists the statuses it requires and "will return exception" otherwise. Read the state first (`GET /sale?ID=`) and follow the sequence quote → order → fulfilment → invoice. | `groups/sale.md` per-action notes; `enums.md` sale statuses |
| 15 | Expecting an error when ordering more than is in stock | Authorising the order silently creates a backorder; check `Status = BACKORDERED` or line `BackorderQuantity` afterwards. | `api-basics.md` § 7 |
| 16 | Using `/sale/order` or `/sale/fulfilment` on a service-only sale | Those endpoints are unavailable for Service Sales; `ServiceOnly` cannot be changed after creation. | `api-basics.md` § 7 |
| 17 | Hard-coding `TaskID = SaleID` for invoices on every sale | True only for Simple and Service sales; an Advanced Sale has several invoice/fulfilment tasks with their own `TaskID`s. Read them from `GET /sale?ID=`. | `api-basics.md` § 7; `groups/sale.md` |
| 18 | New integration on `/purchase/stock`, `/purchase/invoice`, `/purchase/order` | Those endpoints are deprecated and support Simple Purchases only; use `/advanced-purchase/...`. | `api-basics.md` § 8; `groups/purchase.md` |
| 19 | Receiving stock on an `INVOICE`-approach purchase before the invoice is authorised (or the reverse for `STOCK`) | Stock receiving requires `InvoiceStatus = AUTHORISED` when `Approach = INVOICE`; the invoice requires authorised stock when `Approach = STOCK`. | `api-basics.md` § 8 |
| 20 | Sending `Status: "PAID"` or `"VOIDED"` on a POST of an invoice or order | POST accepts only `DRAFT` and `AUTHORISED`; the other values are read-only state. | field tables in `groups/sale.md`, `groups/purchase.md` |
| 21 | Computing and sending `Total`, `Tax`, `TotalBeforeTax` on a create | They are "Not required for POST"; Cin7 Core computes them. Line `Total` is for validation only. | `api-basics.md` § 6 |
| 22 | Modifying a `Prepayment` payment, or posting a payment before the invoice is authorised | Prepayment payments cannot be modified; payments need an authorised invoice, refunds an authorised credit note. | `api-basics.md` § 7, § 8 |
| 23 | Syncing customers or products with the default list and wondering where the inactive ones went | Lists hide `Deprecated` rows unless `IncludeDeprecated=true`. | `api-basics.md` § 6; `groups/customer.md`, `groups/product.md` |
| 24 | Filtering `/ref/brand?Name=and` to find "Brand and Co" | Reference-book `Name` filters match "start with"; only some lists (product `Name`/`Sku`, sale and purchase `Search`) match "containing". | the action's Parameters list in `groups/` |
| 25 | `PUT /ref/location` to rename a bin, `PUT` on factory calendar days or work centers | Bins, factory calendar days, resource capacities/costs and work centers support creation and deletion only. | `api-basics.md` § 9 |
| 26 | Updating the chart of accounts over the API on an account linked to Xero or QuickBooks | Not allowed while the integration is enabled. | `api-basics.md` § 9 |
| 27 | Setting `Type`, `AverageCost` or `BOMType` on `PUT /product` | Read-only (`Type` read-only for PUT); the field tables mark read-only columns, check them before building the body. | `groups/product.md` field table |
| 28 | Registering a sixth webhook of one type, or expecting unlimited retries | At most 5 webhooks of the same type; 6 delivery attempts, then the webhook is deactivated. Acknowledge fast with 2xx and re-enable after outages. | `api-basics.md` § 9; `groups/webhooks.md` |
| 29 | Building webhooks on an account without the automation module | Webhooks need the automation module on the subscription. | `groups/webhooks.md` |
| 30 | Coding against `/product/markup-prices` | The portal marks it a planned API, not available yet. | `api-basics.md` § 9 |
| 31 | Inventing a field, enum value or endpoint | Every name comes from the field tables in `groups/`, every value from `enums.md` or the field's Notes, every path from `endpoints.md`. The portal has a few internal inconsistencies (`INDEX.md`, known limits), so say when a name needs confirming on the account. | `INDEX.md` |
