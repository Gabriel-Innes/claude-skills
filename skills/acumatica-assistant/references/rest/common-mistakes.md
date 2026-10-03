<!-- source: facts from the Acumatica Integration Development Guide topics named per row (URLs in INDEX.md); the "wrong" column is the mistake an integrator makes, the "right" column is the guide's rule | version: Acumatica ERP 2026 R2 (guide edition 2026-09-30) | verified: 2026-10-03 -->

# Common mistakes when coding against the Acumatica REST API

Use as a review checklist. Grep a request or codebase for the pattern in "Looks like", then apply the rule.

| # | Looks like | Why it is wrong | Rule (guide topic) |
|---|---|---|---|
| 1 | `POST .../Customer` to create a record | Create and update are both **PUT**; POST is for actions and reports. | *Create a Record*, *Execute an Action ...* |
| 2 | `"CustomerID": "JOHNGOOD"` | General fields are wrapped: `{"value": "JOHNGOOD"}`; only `id`, `rowNumber` (and `delete`) are bare. | *Representation of a Record in JSON Format* |
| 3 | `GET .../SalesOrder/SO/000001` expecting `Details` in the response | Nothing nested is returned unless listed in `$expand`, including in PUT/PATCH responses. | *$expand Parameter*, *Create a Record* |
| 4 | `$filter=Details/InventoryID eq 'X'` | Filtering on detail entities is unsupported; results are unpredictable. Filter on top-level or linked-entity fields, or fetch and filter client-side. | *$filter Parameter* |
| 5 | `$filter=Status eq 'Completed'` on `Default/26.200.001` | Contract Version 5 filters drop-down fields by **ID** (`'CL'`), and requests send `{"value": {"id": "CL"}}`. | *Contract Versions*, *$filter (CV5)* |
| 6 | `datetimeoffset'2024-...'` or `date'2025-06-17'` on a Contract Version 5 endpoint, or bare literals on Contract Version 4 | Literal syntax differs: CV5 bare OData 4.01 literals, CV4 typed OData 3.0 literals. | *$filter (CV5)* vs *$filter (CV4)* |
| 7 | `$expand=MainContact/Address` on Contract Version 5 | CV5 nests: `$expand=MainContact($expand=Address)`; the slash form is CV4. Same for `$select` of nested fields. | *$expand*, *$select* |
| 8 | `$custom=...` on Contract Version 5 | Custom fields go in `$select` on CV5 (`$select=*,Document.AttributePRODUCT`); `$custom` is CV4. | *$custom Parameter (CV4)* |
| 9 | Sending a custom field without `"type"` | CV5 requires `type` on every custom field in a request body. | *Representation of a Record ...* |
| 10 | Treating HTTP 200 on PUT/PATCH as "saved" | 200 can be returned without saving (view-only rights, field not settable through the endpoint, graph logic). Re-read and compare. | *Update a Record* |
| 11 | PUT with a field value that "doesn't stick" | PUT only writes fields that differ from stored values and lets graph logic win; use PATCH for fields PUT skips. | *Update a Record*, *Update Particular Fields of a Record* |
| 12 | `DELETE .../SalesOrder/SO/000001/Details/<id>` | Detail lines are deleted with PUT and `"delete": true` on the line. | *Remove a Record by Key Fields* |
| 13 | Caching the `id` of a detail line or inquiry row across sessions | Only top-level entities have persistent IDs (NoteID); others are session-scoped. | *Retrieve a Record by ID* |
| 14 | Treating 202 from an action as success | 202 = in progress; poll the `Location` URL with a delay until 204; then read the record's status. | *Execute an Action ...*, *Retrieve the Status of the Release Operation* |
| 15 | Issuing other requests on the same form while a long-running operation runs in the session | They fail until the operation completes; only the status request is allowed. | *Execute an Action ...* |
| 16 | Running the processing-form filter PUT and the Process POST in different sessions | Both must run in the same session; the POST body is the filter response (or its `id` for Process All). | *Narrow the List of Records on a Processing Form* |
| 17 | `GET .../InventorySummaryInquiry` | Generic-inquiry entities are read with **PUT** (parameters in the body) plus `$expand=<Results entity>`. | *Retrieve Data from an Inquiry Form* |
| 18 | Expecting a total count or `@odata.count` | There is no count parameter; page with `$top`/`$skip` until a short page. | *$skip Parameter* |
| 19 | Fetching 50,000 records in one GET, or one sales order of 10,000 lines in one PUT | Risk of timeout; batch reads with `$top`/`$skip` and writes in chunks (guide: 500 lines per request). | *Retrieve the List of Records in Batches*, *Create a Record* |
| 20 | Never calling `/entity/auth/logout` | Sessions count against the license; unclosed ones linger 10 minutes; sign-ins then fail with the API session limit. | *Sign Out from the Service*, *License Restrictions ...* |
| 21 | New integration on `/entity/auth/login` with username/password | Acumatica announces it will be discontinued; implement OAuth 2.0 / OIDC. | *Sign In to the Service* |
| 22 | Requesting `api:concurrent_access` by default | Only when concurrent sessions are really needed; each session counts against the license and each must be signed out. | *Authorization Code Flow: Obtaining of an Authorization Code* |
| 23 | Using an old refresh token after a refresh | Each refresh returns a new refresh token; discard the previous one. | *Refreshing of an Access Token* |
| 24 | `client_id=58FCCFBD-...` without `@Tenant` | The client ID includes the tenant (`<GUID>@<Tenant>`), which also fixes the tenant the token can access. | *Obtaining of an Authorization Code* |
| 25 | Hard-coding `/identity/connect/token` when discovery is available | Acumatica recommends reading the token endpoint from `/identity/.well-known/openid-configuration`. | *Refreshing of an Access Token* |
| 26 | Retrying immediately on a 429 or hammering the API in parallel | Requests are queued; past 50 % of the per-minute limit each request is delayed; more than 20 queued or 10 minutes waiting = declined. Throttle client-side. | *License Restrictions for API Sessions and Requests* |
| 27 | Replying with an error to a push notification you already processed | Acumatica resends (up to five attempts), so you get duplicates; reply success once accepted and dedupe on `Id`. | *Push Notifications: Destinations*, *Format* |
| 28 | Relying on the SignalR hub for guaranteed delivery | Notifications with no connected client are lost and cannot be resent; use a webhook address or MSMQ. | *Push Notifications: Destinations* |
| 29 | Inventing an entity, field or action name | The contract is per endpoint and version: read `swagger.json`, `$adHocSchema` or the Web Service Endpoints form; check the version comparison for renames. | *OpenAPI 3.0*, *Comparison of System Endpoints* |
| 30 | Using `Default/26.200.001` on a 2025 R2 instance | The endpoint list comes from `GET /entity`; a system endpoint exists only from its release onward (it keeps working on later releases). | *Endpoints and Contracts*, *Retrieve the ... Endpoints* |
| 31 | Sending `[{en:...}]` in `value` for one language only | That form blanks every language not listed; use `"Translations": {"fr": ...}` on the field instead, and never both forms together. | *Specify All/Any Number of Localized Values ...* |
| 32 | Updating an archived record after `PX-ApiArchive: SHOW` | The guide warns this can lead to unpredictable consequences. | *Retrieve Archived Records* |
| 33 | Key value containing `/` in the URL path | Use `|` as the key separator or address the record by ID. | *Retrieve a Record by Key Fields* |
| 34 | Reading the `Location` header unconditionally after an action POST | An action answers **202 + `Location`** when it is still running, or **204 with no `Location`** when it already completed. A client that indexes the header throws on 204 and reports a released document as "failed to release"; a retry then creates a duplicate. Treat 204 as done. | *Execute an Action That Is Present in an Endpoint* |
| 35 | Polling the status URL with no ceiling, or failing the whole operation when one poll errors | The guide only says to poll with a delay until 204. One transient error on a status GET does not mean the release failed, and a stuck operation must not hang the integration forever. Bound the wait, retry the poll, and decide from the document's status read afterwards. | *Retrieve the Status of the Release Operation*, *Check the Status of a Sales Invoice* (practice) |
| 36 | Creating documents with a timestamped reference and retrying after a timeout | A PUT without key fields always creates; a request that timed out client-side may still have been saved. With a wall-clock reference the retry cannot find the first document and creates a second. Use a deterministic reference (your own document or transaction id in `ExternalRef`, `VendorRef`, `Description` or a custom field) and GET by `$filter` on it before creating. | *Create a Record* (timeout note), *Retrieve Records by Conditions* (practice) |
