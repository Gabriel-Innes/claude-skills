<!-- source: Acumatica Integration Development Guide (beacon.acumatica.com), chapters "Configuring the REST API" and "REST API Examples > Basic Requests"; topic titles cited inline, URLs in INDEX.md | version: Acumatica ERP 2026 R2 (guide edition 2026-09-30); older releases differ where stated | verified: 2026-10-03 -->

# Contract-based REST API guide

How to build and review integrations against the Acumatica ERP **contract-based REST API** without guessing
URLs, payload shapes, headers or status codes. Every section names the guide topic it comes from. Exact entity,
field and action names are **not** in this file: they come from the endpoint's OpenAPI document or the
Web Service Endpoints (SM207060) form of the client's instance (§ 2).

## 1. Endpoints, versions and URLs

- Base URL of an endpoint: `http(s)://<instance URL>/entity/<Endpoint name>/<Endpoint version>/`. The instance
  URL includes the site name when the instance is not at the root (`https://my.acumatica.com/MyInstance`).
  (Topics: *Endpoints and Contracts*, every *Basic Requests* topic.)
- **System endpoints** are preconfigured, named `Default`, and their contract cannot be changed. The **endpoint
  version** (for example `26.200.001`) fixes the list of entities, fields and actions; the **contract version**
  (4 or 5) fixes the request/response conventions (§ 3 and `query-parameters.md`). A system endpoint keeps
  working on later Acumatica releases: an integration written for `Default/26.200.001` can be used against
  future versions. Obsolete system endpoints may be removed in some version. (*Endpoints and Contracts*.)
- The instance can also expose preconfigured endpoints with other names that the system uses internally;
  Acumatica recommends not using them. The guide's own examples use `Default` and `MANUFACTURING`
  (manufacturing entities such as `BillOfMaterial`, `ProductionOrderDetail`). (*Endpoints and Contracts*;
  `examples-catalogue.md`.)
- **Custom endpoints** are created on the Web Service Endpoints (SM207060) form, either from scratch (always the
  latest contract version, Contract Version 5 in 2026 R2) or as an **extension** of an existing endpoint (keeps
  the base endpoint's contract version; inherited elements cannot be renamed or retyped, but new entities,
  fields and actions can be added). Custom endpoints must be maintained by the customer across upgrades. (*Custom
  Endpoints and Endpoint Extensions*, *To Create a Custom Endpoint*, *To Extend an Existing Endpoint*.)
- Naming rules for custom endpoints: endpoint name = letters, digits, underscores, periods, not starting with a
  digit; entity/field/action names = letters, digits, underscores; reserved field names `Action`, `CustomFields`,
  `Delete`, `Entity`, `ID`, `Note`, `ReturnBehavior`, `RowNumber`; a nested-entity field cannot be named `Files`
  or `Translations`. (*Naming Rules for Endpoints*.)
- **Discover what an instance exposes**: `GET <instance URL>/entity` returns `version.acumaticaBuildVersion`,
  `version.databaseVersion` and `endpoints[]` (`name`, `version`, `href`). Sent with authentication it also
  returns the tenant's custom endpoints and `features[]` (enabled feature switches such as
  `PX.Objects.CS.FeaturesSet+FinancialModule`). (*Retrieve the Acumatica ERP Version, Enabled Features, and
  Endpoints*.) See `endpoint-versions.md` for the system endpoint versions the 2026 R2 guide compares.

## 2. Contract discovery: OpenAPI and $adHocSchema

- `GET <Base endpoint URL>/swagger.json?company=<tenant>` returns the endpoint's **OpenAPI 3.0** document
  (entities, fields, actions, parameters). Without `company`, the tenant of the signed-in user is used. The
  same file is available from the More menu (OpenAPI 3.0) of the Web Service Endpoints (SM207060) form.
  `GET <instance URL>/entity/swagger.json` describes the instance-level API (sign-in, sign-out, `/entity`).
  (*OpenAPI 3.0*.) It can be fed to editor.swagger.io / a client generator to produce a typed client
  (*To Import a REST Schema to a Visual Studio Solution*).
- `GET <Base endpoint URL>/<Top-level entity>/$adHocSchema` returns, per entity, the **custom fields** that are
  not in the contract (`custom.<ViewName>.<FieldName>` with `type`) and `_workflowActions[]` (workflow actions not
  in the endpoint, with their `parameters.custom.<View>.<Param>` and types). Use it to find view and field names
  for § 7 and action parameter names for § 6. (*Retrieve the Schema of Custom Fields and Workflow Actions*.)
- In the UI, Settings > Inspect Element (Ctrl+Alt+click) on an element shows **Data Field** (field name), **View
  Name** and, for buttons, **Action Name**. (*Custom Fields*, *Execute a Custom Action*.)

## 3. JSON representation of a record

(*Representation of a Record in JSON Format*.)

- **System fields** are plain values: `"id": "<GUID>"`, `"rowNumber": 1`. `note` is written like a general field.
- **General fields** are wrapped: `"CustomerID": {"value": "JOHNGOOD"}`. Only the fields you need are required.
- **Linked entity** = nested object: `"MainContact": {"Email": {"value": "..."}, "Address": {...}}`.
- **Detail entity** = array of objects: `"Details": [{"InventoryID": {"value": "AALEGO500"}, "Quantity": {"value": 10}}, ...]`.
- **Drop-down fields, Contract Version 5**: a response holds `{"value": {"id": "CL", "description": "Completed"}}`;
  a request sends the ID only: `{"value": {"id": "CL"}}`. Multi-select values are always an array of such objects.
  Types: `StringSingleSelectValue`, `IntSingleSelectValue`, `StringMultiSelectValue` (no integer multi-select).
  In **Contract Version 4** a selected value is a plain string (`{"value": "AC"}`).
- **Date-only fields** (`DateOnlyValue`, Contract Version 5): `"Date": {"value": "2026-09-09"}`, no time or zone.
  Date-time fields carry an offset (`2023-12-03T14:59:30.693+03:00`).
- **Custom fields** (not in the contract) go in a `custom` block inside the entity (top-level, detail or linked)
  that owns them: `"custom": {"<ViewName>": {"<FieldName>": {"type": "CustomStringField", "value": "AB123456"}}}`.
  In Contract Version 5 `type` is **required** on every custom field sent. Custom select types:
  `CustomStringSingleSelectField`, `CustomIntSingleSelectField`, `CustomStringMultiSelectField`. Other types seen
  in the guide's `$adHocSchema` example: `CustomDecimalField`, `CustomIntField`, `CustomGuidField`,
  `CustomDateTimeField` (the latter from the `cf.DateTime` filter function). User-defined fields are
  `Attribute<AttributeID>` in the view that owns them (for example `Document.AttributeOPERATSYST` on Sales Orders).
- **Response envelope**: every top-level entity returned carries `id`, `rowNumber`, `note`, `custom`, the
  requested fields, `_links` (`self`: GET/DELETE URL by ID; `files:put`: URL template for attaching a file) and,
  when expanded, `files[]` (`id`, `filename`, `href`, `comment`). (*Retrieve a Record by ID*, *Attach a File to a
  Record*, *Retrieve Comments for Attached Files*.)

## 4. Headers and status codes common to data requests

(*Create a Record*, *Update a Record*, *Retrieve Records by Conditions* and the other *Basic Requests* topics.)

| Header | Use |
|---|---|
| `Accept: application/json` | Response format for data requests. Files: `application/octet-stream`. Reports: `application/pdf`, `text/html` or the xlsx MIME type. |
| `Content-Type: application/json` | Request body format. File upload: `application/octet-stream`. Sign-in also accepts `application/x-www-form-urlencoded`. |
| `Cookie` | The cookies received at sign-in (cookie-based auth), or when using OAuth with the `api:concurrent_access` scope and managing sessions by cookie. |
| `Authorization: Bearer <token>` | OAuth 2.0 / OIDC access token (see `authentication.md`). |
| `If-None-Match: *` | On PUT: create only; 412 if the record already exists. |
| `If-Match: *` | On PUT: update only; 412 if the record does not exist. |
| `PX-ApiArchive: SHOW` | Include archived records in a GET (updating archived records is unsupported). |
| `PX-CbApiBusinessDate`, `PX-CbApiBranch` | Business date (any date format) and current branch (branch **name**) for this request only. |
| `PX-CbFileComment` | Comment stored with an attached file (max 500 characters; several headers are joined with commas). |
| `Accept-Language` | Locale for a report (`fr-FR`, weighted lists, `*` = en-US). |

| Code | Meaning in the guide |
|---|---|
| 200 | Success with a body (GET, PUT, PATCH, inquiry, processing-filter). For PUT/PATCH the body is the resulting record. **200 does not prove the values were saved** (§ 5). |
| 202 | Long-running operation started (actions, reports); `Location` header holds the status URL (§ 6). |
| 204 | Success without body: sign-in, sign-out, DELETE, file attached (with `Location` of the file), action completed, status poll of a finished operation. |
| 400 | Request data invalid. |
| 401 | Not signed in. |
| 403 | User lacks access rights to the form behind the entity. |
| 404 | PATCH: record not found; action: no action with that name. |
| 412 | `If-None-Match: *` and the record exists; `If-Match: *` and it does not; `If-None-Match: *` on PATCH. |
| 422 | Validation errors; each failing field carries `"error": "..."` next to its `value` in the body. |
| 429 | License request limits exceeded (see `authentication.md` § 5). |
| 500 | Internal server error. |

## 5. CRUD

- **Create**: `PUT <Base endpoint URL>/<Top-level entity>` with the JSON record; the response contains only the
  fields you sent or asked for with `$select`/`$expand`. A single PUT can carry many detail lines. For very large
  documents send the lines in batches of a few hundred (the guide's example: 10,000 lines as requests of 500)
  rather than one huge request (timeout) or one request per line (slow). (*Create a Record*.)
- **Update (PUT)**: same URL; identify the record by its key fields in the body, by `id`, or by `$filter`. PUT
  compares the body with stored values and **only writes the fields that differ**; values the graph logic changes
  as a side effect are not overwritten from the body. Delete a detail line by sending `"delete": true` on the
  line (identified by `id` or its key fields). (*Update a Record*.)
- **Update (PATCH)**: `PATCH <Base endpoint URL>/<Top-level entity>`; submits the listed fields regardless of
  the stored value (graph logic still wins). Use it for synchronisation where you know exactly which fields
  changed, or when PUT silently skips a field. Cannot insert (412 with `If-None-Match: *`). (*Update Particular
  Fields of a Record*.)
- **Verify writes**: a 200 can be returned without saving when the user can view but not edit the form, or when
  a field cannot be set through the endpoint. Re-read the record and compare the fields you changed. (*Update a
  Record*.)
- **Retrieve one record**: `GET .../<Entity>/<Key1>/<Key2>` (keys in the order the form defines them; `|` may
  replace `/`; a key containing `/` forces lookup by ID) or `GET .../<Entity>/<GUID>`. Prefer keys in the URL over
  `$filter` for a single record: a filter is treated as a multi-record query with extra optimisation work.
  (*Retrieve a Record by Key Fields*, *Retrieve a Record by ID*.)
- **Entity IDs**: top-level entities have **persistent** IDs (the `NoteID` of the record) usable across sessions.
  Detail lines, generic-inquiry entities and custom entities without a NoteID get a **session-scoped** ID that is
  invalid after the next sign-in. (*Retrieve a Record by ID*.)
- **Retrieve many**: `GET .../<Entity>?$filter=...&$select=...&$expand=...&$top=N&$skip=M`. By default no linked or
  detail entity is returned: **every nested entity you want must be in `$expand`**. If the optimised multi-record
  query fails, the error names the entities/fields responsible: drop them from `$expand`/`$select` or fetch the
  records one by one. (*Retrieve Records by Conditions*.)
- **Paging**: `$skip` is applied before `$top`; there is **no count parameter**. Page until a short page comes back.
  Without `$top`, all records are returned (an error if a SQL Server Resource Governor limit is exceeded).
  (*Retrieve the List of Records in Batches*, *$top*, *$skip*.)
- **Delete**: `DELETE .../<Entity>/<Key1>/<Key2>` or `DELETE .../<Entity>/<GUID>` (204). Detail lines are removed
  with PUT and `"delete": true`, not with DELETE. (*Remove a Record by Key Fields*, *Remove a Record by ID*.)
- **Attributes**: exposed through the `Attributes` detail entity (`AttributeValue`): `AttributeID` (internal value
  returned), `AttributeDescription` (read-only), `Value` (internal value returned; set with internal or external
  value; check boxes return `0`/`1`, accept `0`/`1`/`true`/`false`; multi-select internal values are
  comma-separated), `ValueDescription` (read-only external value), `Required`, `RefNoteID`.
  `GET .../Contact?$expand=Attributes($select=AttributeID,Value)&$select=FirstName,LastName`. (*Retrieve Records
  with Attributes*.)
- **Multilingual fields**: read all translations with `$select=<View>.<Field>Translations` (string like
  `[{en:Item},{fr:Pièce}]`) or `$expand=Translations`; write the default-language value in `value` and other
  languages in `"Translations": {"fr": "..."}` on the field (recommended; unspecified languages keep their value).
  The older form puts `[{en:...},{fr:...}]` in `value` and **blanks every language not listed**; mixing both
  forms fails. (*Retrieve/Specify Localized Values ...* topics.)

## 6. Actions, long-running operations, processing forms, reports

- **Action in the endpoint**: `POST <Base endpoint URL>/<Entity>/<Action name>` with body
  `{"entity": {<record, keys or id>}, "parameters": {<action parameters>}}`. Example: `POST .../SalesOrder/ReopenSalesOrder`
  with `entity` = `OrderType` + `OrderNbr`; `POST .../BusinessAccount/ChangeBusinessAccountID` with
  `parameters.BusinessAccountID` = the new ID. (*Execute an Action That Is Present in an Endpoint*.)
- **Custom / workflow action not in the endpoint**: same URL pattern; parameters that the UI collects in a dialog
  go in `"parameters": {"custom": {"<View>": {"<Param>": {"type": "CustomStringField", "value": "..."}}}}`
  (view and parameter names from `$adHocSchema` or Inspect Element). Example: `POST .../Case/Close` with
  `FilterPreview.Reason`. (*Execute a Custom Action*.)
- **Response**: 204 = done, and in that case there is **no `Location` header**, so a client must not index it
  unconditionally; **202 = still running**, with `Location` =
  `<Base endpoint URL>/<Entity>/<Action>/status/<GUID>`. Poll that URL with GET, **with a delay between polls**;
  202 means in progress, 204 means completed. Then read the record to confirm its new status (for example a
  released invoice becomes Open). (*Execute an Action ...*, *Invoke Release of an Invoice*, *Retrieve the Status
  of the Release Operation*, *Check the Status of a Sales Invoice*.)
- While a long-running operation runs on a form in the current session, only the status request succeeds on
  that form; other requests in the session fail until it completes. (*Execute an Action ...*.)
- **Processing forms** (Process / Process All) take two requests **in the same session**: (1) `PUT .../<Entity>?$expand=<ResultEntity>`
  with the selection criteria in the body returns the filter plus the candidate rows, each with a `Selected`
  field; (2a) `POST .../<Entity>/<ProcessAction>` with body `{"Entity": <the whole response from step 1 with
  Selected set true/false per row>}`, or (2b) `POST .../<Entity>/<ProcessAllAction>` with body
  `{"Entity": {"id": "<id from step 1>"}}`. Example: `EmailProcessing` with `Result`, `ProcessEmailProcessing`,
  `ProcessAllEmailProcessing`. (*Narrow the List of Records on a Processing Form*, *Execute a Processing Action
  for Selected Records*, *... for All Filtered Records*.)
- **Generic inquiry entities** are always read with **PUT** (parameters in the body, even `{}`) and
  `$expand=<result detail entity>`: `PUT .../InventorySummaryInquiry?$expand=Results` with `InventoryID` and
  `WarehouseID`. A custom generic inquiry needs a custom endpoint or extension that maps it. (*Retrieve Data from
  an Inquiry Form*.)
- **Reports** need a **Report**-type entity in a custom endpoint: `POST <Base endpoint URL>/<Report entity>` with
  report parameters in the body (`{}` = defaults), `Accept` selecting PDF (default), HTML or Excel. Response 202
  with `Location` = `.../<Report entity>/report/<format>/<GUID>`; GET it until 200 returns the file. (*Request a
  Report*.)

## 7. Custom fields and user-defined fields

(*Custom Fields*, *Retrieve a Record with Custom Fields*, *Create a Record with Custom Fields*, *$custom Parameter*.)

- A **custom field** is any element not in the entity definition: a predefined form element the contract omits,
  an element added by a customization project, or a user-defined field (attribute). It is addressed as
  `<View name>.<Field name>`; a user-defined field is `<View name>.Attribute<AttributeID>`.
- **Read**: Contract Version 5 puts custom fields in `$select` (`$select=*,Document.AttributePRODUCT`;
  in a detail entity `$expand=Details($select=Transactions.UsrRepairItemType)`). Contract Version 4 uses
  `$custom=` (`$custom=ItemSettings.UsrRepairItemType`, `$custom=Details/Transactions.UsrRepairItemType&$expand=Details`).
- **Write**: the `custom` block of § 3 inside the entity that owns the view. The guide's create example also adds
  `$select=*,Document.AttributePRODUCT` to the PUT URL so the response shows the field.
- **Filter**: `cf.<Type>('<View>.<Field>')` (see `query-parameters.md` § 1).
- Custom fields can be added to a custom endpoint or extension and then used like contract fields; **user-defined
  fields cannot be added to custom endpoints or extensions**, they stay in the `custom` block.

## 8. Files

- **List** a record's attachments: `GET .../<Entity>/<keys>?$select=<fields>,files&$expand=files`; `files[]` items
  have `id`, `filename`, `href` (download path) and `comment`. For detail-line files use
  `$expand=Details($expand=files)` (Contract Version 5) or `$expand=Details/files` (Contract Version 4).
- **Download**: `GET <Base endpoint URL>/files/<File id>` with `Accept: application/octet-stream`.
- **Upload**: `PUT` to the record's `_links.files:put` template with `{filename}` replaced
  (`.../files/PX.Objects.IN.InventoryItemMaint/Item/<GUID>/<filename>`), body = raw bytes,
  `Content-Type: application/octet-stream`, optional `PX-CbFileComment`. Works for top-level and detail records of
  any nesting. Legacy form: `PUT .../<Entity>/<Key1>/<Key2>/files/<File name>`. Response 204 with `Location`.
  (*Retrieve a File Attached to a Record*, *Attach a File to a Record*, *Retrieve Comments for Attached Files*.)

## 9. Session hygiene (summary; details in `authentication.md`)

- Cookie sign-in: `POST /entity/auth/login` with `name`, `password`, `tenant`, `branch` (`locale` is reserved);
  204 and cookies. Always `POST /entity/auth/logout` when done: unclosed sessions count against the license's
  API session limit and are only reclaimed after a 10-minute timeout. Direct username/password sign-in is
  announced as **to be discontinued**; new work should use OAuth 2.0 / OIDC. Two-factor authentication is
  bypassed for API sign-in; give API users a dedicated user type with it turned off. (*Sign In to the Service*,
  *Sign Out from the Service*.)

## 10. Engineering pattern (practice, not Acumatica guidance)

Keep base URL, endpoint name and version, tenant and branch in configuration; wrap sign-in/sign-out (or token
acquisition and refresh) in one component with guaranteed sign-out in `finally`; put entity operations behind
small typed methods that always pass `$select`/`$expand`; treat 202 as "poll with back-off"; re-read after writes
that matter; log the `error` fields from 422 bodies, never credentials or cookies.

Three habits that follow from the guide facts above (practice, not Acumatica guidance):

- **Action result**: branch on the status code. 204 is complete (no `Location`); 202 gives the status URL. Poll it
  with a delay and a ceiling, tolerate a transient poll failure, and after completion GET the document with
  `$select=Status` and compare with the expected status before reporting success.
- **Idempotent creates**: a PUT without keys always creates, and a timed-out request may still have been saved.
  Put a deterministic reference of your own (document or transaction id) in a field such as `ExternalRef`,
  `VendorRef` or `Description`, and GET by `$filter` on it before creating; never stamp the reference with the
  current time.
- **Lookups that feed a write must fail loudly.** A helper that swallows an exception (including a 429 licence
  limit) and returns a default such as an order type produces a wrong document later with a misleading error.
