<!-- source: Acumatica Reporting Tools Guide on Acumatica Beacon, chapters "Accessing DACs Through OData", "Exposing Inquiry Results by Using OData", "Accessing the Exposed Inquiry Results Through OData", "Discovering DACs" (topic titles cited per section, URLs in INDEX.md); System Administration Guide "User Roles: Predefined Roles"; Acumatica training course I300 "Data Retrieval with OData" 2024 R1 (revision 2024-03-21) for the pre-2026 URL shapes and the interface comparison | version: Acumatica ERP 2026 R2 (guide edition 2026-09-30) unless a section says 2024 R1 | verified: 2026-10-06 -->

# OData access to Acumatica ERP

Acumatica exposes two **read-only** OData interfaces (*Accessing DACs Through OData*; the I300 course states "you
cannot edit the data in Acumatica ERP through the OData interface"):

| Interface | Reads | Protocol | Base URL (2026 R2) | Needs preparation in Acumatica |
|---|---|---|---|---|
| **DAC-based** | data access classes (the tables behind forms) and their relations, straight from the metadata | OData 4.0 (OData 4.01 URL conventions for `$filter`) | `<instance URL>/t/<TenantName>/api/odata/dac` | none; access rights and (optionally) the `OData4 User` role |
| **Generic-inquiry-based** | the results of generic inquiries that have **Expose via OData** selected | OData 4.0 with exceptions (§ 6) | `<instance URL>/t/<TenantName>/api/odata/gi` | a published inquiry with the check box selected and View Only rights |

Use the DAC-based interface when the data lives on a data entry form and no inquiry exists; use the inquiry-based
interface when the shape is already defined by an inquiry (joins, formulas, parameters) or the consumer is Excel /
Power BI. Neither writes data; writes go through the REST API (`references/rest/`).

## 1. URLs and tenant names

- `<TenantName>` is the tenant's **login name** (Login Name column on Tenant List (SM203530), also shown on the
  User menu). A space in the name is sent as `%20` (`/t/Calipso%20LLC/api/odata/dac`). (*DAC-Based OData: General
  Information*, *Generic Inquiry Access Through OData: General Information*.)
- `GET <base>` returns the service document: `{"@odata.context": "<base>/$metadata", "value": [{"name", "kind":
  "EntitySet", "url"}, ...]}`, listing every DAC (dac) or every exposed inquiry (gi). The inquiry list shows all exposed
  inquiries, but data comes back only for those the user has rights to. (Same topics.)
- `GET <base>/$metadata` returns the CSDL (§ 3). For the DAC interface the document is large and "the request can take a
  significant amount of time" (*DAC-Based OData: To Sign In to Acumatica ERP and Retrieve the Metadata*); the 2026 R2
  clean-instance document is 20 MB.
- Deploy with **HTTPS** so credentials are not sent in clear (*Generic Inquiry Access Through OData: General Information*).

### Older releases (I300 course, 2024 R1)

The 2024 R1 course documents different paths and a different protocol split; a client on an older release may still
use them. Probe `$metadata` on both shapes before assuming either.

| 2024 R1 | Path | Protocol | Notes |
|---|---|---|---|
| Inquiry-based | `<instance URL>/OData/<TenantName>/...` | **OData 3.0** (`edmx` 1.0, `DataServiceVersion 3.0`) | `$format=json`; response key `odata.metadata`; `datetime'2023-11-14T00:00:00.000'` literals; parameters of `<GI>_WithParameters` passed as query parameters (`?InventoryID=AALEGO500`) |
| DAC-based | `<instance URL>/ODatav4/<TenantName>/...` | OData 4.0 | same request shapes as § 4 |

On a **single-tenant** instance the course omits the tenant segment (`/OData/$metadata`, `/ODatav4/$metadata`); with
several tenants it is required. (I300 *Getting Started: OData Endpoints*, Examples 1.1.1 and 1.1.2.) The 2026 R2 guide
always writes the `/t/<TenantName>/api/odata/...` form.

**Both DAC-based shapes work on 2026 R2.** On a clean local 2026 R2 instance,
`<instance URL>/odatav4/<TenantName>/$metadata` and `<instance URL>/t/<TenantName>/api/odata/dac/$metadata` returned the
same metadata and are interchangeable (verified by the skill owner with Postman, 2026-10-06; not an Acumatica
statement). Prefer the documented `/t/<TenantName>/api/odata/dac` form in new work; treat `/odatav4/` as a working
legacy alias. Whether the inquiry-based `/OData/<TenantName>` path still answers on 2026 R2, and with which protocol
version, was **not** tested.

## 2. Authentication, roles and licence

- Both interfaces use **basic authentication** (username and password on every request; Postman "Basic Auth",
  browsers prompt). The username is the plain login, **without** the tenant appended (*... To Access an Exposed
  Inquiry in Microsoft Excel*).
- A basic-auth OData sign-in counts as a **conventional user**, not an API session: it is limited by the Concurrent
  Users figure on the License and Constraints tab of License Monitoring Console (SM604000), not by the API-user limit
  that REST sessions consume. (*DAC-Based OData: General Information*; I300 Appendix A: "Limit for the Number of
  API Users: No" for basic auth, "Yes" for OAuth.)
- **OAuth 2.0 / OIDC** is supported instead of basic auth (same topics); registration, flows and scopes are in
  `references/rest/authentication.md` (`api` scope covers OData). An OAuth session does count as an API session.
- **Access rights**: the DAC-based interface shows the user "the same data that's visible to them in the UI based on
  their access rights"; the inquiry-based interface needs at least **View Only** on the inquiry form (Access Rights by
  Screen (SM201020); an inquiry without a workspace sits under the **Hidden** node). (*DAC-Based OData: General
  Information*, *Generic Inquiries and OData: Preparation of an Inquiry for Exposure*, *... To Expose Inquiry Results
  Through OData*.)
- **Predefined roles** (System Administration Guide, *User Roles: Predefined Roles*): `BI` grants access to the
  inquiries exposed through OData (the predefined inquiries whose titles start with "BI"); `OData4 User` grants access
  to data exposed through the DAC-based interface, and without it the user still sees what their UI rights allow.
- No sign-out call exists for basic auth; each request authenticates itself.

## 3. Metadata: what `$metadata` tells you (DAC-based)

(*DAC-Based OData: General Information*, confirmed on the bundled 2026 R2 snapshot in `metadata/`.)

- One `EntityType` per DAC inside a `Schema` per namespace (`PX.Objects.SO.SOOrder`); `Property` elements are the
  fields with Edm types; the `Org.OData.Core.V1.Description` annotation on a type or property is its **display name**.
- **Navigation properties** are generated: `<RelatedType>By<LocalField>` for a lookup (`BAccountByCustomerID` links
  `SOOrder.CustomerID` to `BAccount.BAccountID`, the join being the `ReferentialConstraint`), and
  `<DetailType>Collection` for details (`SOLineCollection`).
- The container (`Schema Namespace="Default"`, `EntityContainer Name="Container"`) declares up to three **entity
  sets per DAC**: the generated `PX_Objects_SO_SOOrder`, a display-name alias `SalesOrder` and the class name
  `SOOrder`; a digit suffix (`Batch1`, `Vendor1`) marks an alias that collided. Setup DACs are `Singleton`s.
  `metadata/entity-sets.md` lists them.
- `Cap.FilterRestrictions` on an entity set: each field in `NonFilterableProperties` is treated as **non-filterable
  and non-selectable**; `<PropertyValue Property="Filterable" Bool="false"/>` means no field declared in that DAC
  (inherited ones excepted) may appear in `$filter` or `$select`. In the snapshot 1,074 DACs carry a list (`NoteText`
  and unbound calculated fields such as `CuryRate`, `DocBal`, `IsFullyPaid` are typical) and 56 derived DACs are
  `Filterable=false`.
- A derived DAC (`PX.Objects.AR.Customer : PX.Objects.CR.BAccount`) declares only the fields it adds; its key and the
  rest come from the base type (`metadata/api/INDEX.md` shows `BaseType`).
- **Aggregation** (`$apply`, the OData Data Aggregation extension) is **not supported** (same topic; I300 Example
  3.1.2 says the same for 2024 R1).
- Finding the DAC behind a form element: Ctrl+Alt+click (or Settings > Inspect Element) opens Element Properties with
  **Data Class** and **Data Field**; Drop-Down Values lists stored values versus captions; the DAC Schema Browser
  (Settings > DAC Schema Browser) shows keys, foreign references and incoming/outgoing references. (*DAC Discovery:
  General Information*, *Data from Multiple Data Sources: DAC Schema Browser*.)

## 4. DAC-based requests

All from *DAC-Based OData: Basic Data Retrieval*, *Filtering Records*, *Retrieving Related Data* unless noted. Base
`<base> = <instance URL>/t/<TenantName>/api/odata/dac`.

| Need | Request |
|---|---|
| All records | `GET <base>/SOOrder` or `GET <base>/PX_Objects_SO_SOOrder` (fully qualified or short name) |
| One record by key | `GET <base>/SOOrder(OrderType='SO',OrderNbr='000058')` (every key field, named) |
| Chosen fields | `GET <base>/PX_Objects_AR_Customer?$select=AcctCD,AcctName,CustomerClassID` |
| Related record with chosen fields | `$expand=AddressByDefAddressID($select=AddressLine1,City,State,PostalCode)` |
| Detail lines | `$expand=SOLineCollection`; several navigations comma-separated: `$expand=ContactByDefBillContactID($select=Email,Phone1),AddressByDefAddressID($select=City)` |
| Filter on own fields | `$filter=(OrderType eq 'IN')`; `$filter=StkItem eq true and ItemStatus eq 'AC' and LastModifiedDateTime eq 2025-12-01` (*To Filter the Requested Data*) |
| Filter on a related record | `$filter=SOAddressByBillAddressID ne null`; `$filter=SOAddressByBillAddressID/AddressID eq 37` |
| Filter on a collection | `$filter=SOLineCollection/Any()`; `$filter=SOLineCollection/Any(x: x/LineNbr eq 2)`; `$filter=SOLineCollection/All(x: x/LineNbr ne 2)`; `$filter=SOLineCollection/$count eq 3` |
| Pages | `$skip=50&$top=500&$orderby=InventoryID`; always add `$orderby` (without it the server sorts by key fields ascending) |
| Deleted-record list | `GET <base>/SOOrder/px.GetDeletedRecords()?$filter=DeleteDate ge 2024-11-01T00:00:00Z` (§ 5) |

Rules and limits:

- `$filter` follows **OData 4.01 URL conventions**: string literals in single quotes, numbers and booleans bare,
  date-times bare ISO 8601 (`2022-12-31T00:00:00%2b03:00`, `%2b` for a `+` offset; `Z` for UTC); the course adds
  "specify your timezone". Compare `ItemStatus eq 'AC'`: filter by the **stored value**, not the caption (Drop-Down
  Values in Element Inspector shows both).
- Foreign keys are integers in DACs: `INSiteStatus.InventoryID eq 41` filters by the internal `InventoryID`, while
  the user-facing code is `InventoryItem.InventoryCD` reached through `$expand=InventoryItemByInventoryID($select=InventoryCD)`
  (*... $expand, $select, and $filter Parameters*).
- Before putting a field in `$select` or `$filter`, check the entity set's `Cap.FilterRestrictions` (§ 3); a
  non-filterable field in either parameter is refused.
- `$expand` depth is limited to **3** by default; the `maxExpansionDepth` attribute of the `odata` element inside
  `px.core` in `Web.config` changes it.
- Password fields come back **encrypted**.
- Custom and user-defined fields are addressed **by their names**, nothing special needed (*Retrieving Localized and
  Custom Fields*).
- Response shape: `{"@odata.context": "<base>/$metadata#PX_Objects_AR_Customer(AcctCD,...,AddressByDefAddressID(City))",
  "value": [ {...}, ... ]}`; expanded single navigations are nested objects, collections are arrays; numbers are JSON
  numbers (`1999.000000`).

## 5. DAC-based headers and switches

(*DAC-Based OData: Retrieving Localized and Custom Fields*, *Retrieving Archived and Removed Records*.)

| Header / parameter | Effect |
|---|---|
| `Accept-Language: fr-FR` or `?locale=fr-FR` | multilingual fields in that locale; default language otherwise; the URL parameter wins when both are present |
| `PX-ApiArchive: SHOW` | include **archived** records |
| `PX-ApiDeleted: SHOW` | include **removed** records of tables that keep them (`DeletedDatabaseRecord` column); hidden by default |
| `GET <base>/<DAC>/px.GetDeletedRecords()` | list of records removed since tracking began for a DAC listed on Tables to Track Deleted Records (SM207010): the system stores only the record's `NoteID` and the deletion time; filter with `$filter=DeleteDate ge <datetime>`; result shape is the `DeletedRecordResult` complex type (`RefNoteID`, `DeleteDate`); the user needs DAC-based access to that DAC; the list of tracked DACs can be included in a customization project |

Delta synchronisation recommended by the guide: filter on `LastModifiedDateTime` for changes, and use
`px.GetDeletedRecords()` for removals, since modified-date filtering cannot see deletions.

## 6. Generic-inquiry-based requests

(*Generic Inquiries and OData: Preparation of an Inquiry for Exposure*, *Generic Inquiry Access Through OData: Data
Retrieval*, *... General Information*, *... To Sign In ...*, *... with Parameters*, *... To Filter the Results ...*.)

Exposing: the inquiry must be **published** (a Screen ID on Generic Inquiry (SM208000)); select **Expose via OData**
on the **Interface Options** tab (the Summary area in older releases); grant **View Only** to the roles that will read it.
Predefined `BI-*` inquiries exist for Power BI and the `BI` role reads them.

`$metadata` (namespace `GenericInquiry`, container `Default`): an `EntitySet` per exposed inquiry (name = the inquiry
title, spaces kept: `BI-Customers`, `Customer Contacts`), an `EntityType` whose `Property` elements are the result
columns plus the **key fields of the source tables even when they are not in the results grid**, and for an inquiry
with parameters a `Function` (the parameters) plus a `FunctionImport` named `<Title>_WithParameters`.

| Need | Request |
|---|---|
| Results | `GET <base>/BI-Customer`, `GET <base>/Customer%20Contacts` |
| Results with parameter values | `GET <base>/DBStorageDetailsByItemWarehouseLocation_WithParameters(Warehouse='WHOLESALE')`; or a parameter alias `..._WithParameters(Warehouse=@1)?@1='WHOLESALE'` when the value has URL-unsafe characters |
| Filter and order | `GET <base>/SO-BI-SalesOrdersForYear?$filter=Customer eq 'GOODFOOD' and OrderTotal ge 1000&$orderby=OrderTotal asc`; `$filter=ItemStatus eq 'Active' and LastModifiedOn gt 2025-10-14` |
| Pages | `$top`, `$skip` with `$orderby` |

Rules and limits:

- **Not supported**: `$expand`, `$count`, the `IsOf()` function. To read several kinds of detail lines, expose one
  inquiry per detail kind and call each.
- `$filter` becomes part of the SQL `WHERE` clause, like the inquiry's Conditions tab. **Fields calculated by a
  formula cannot be filtered or sorted**; such a request may return **200 OK with no body** instead of an error. A
  body with an empty `value` array means "no rows"; **no body means an unsupported query**, never an empty result.
- Requesting the `EntitySet` of an inquiry that has parameters does **not bind** them and can return an empty result
  without an error; use the `_WithParameters` function import.
- Field and parameter names are generated from the **English display names**: unchanged if valid; a leading digit gets
  an underscore (`2Update` to `_2Update`); invalid characters such as spaces are removed (`Account Name` to
  `AccountName`). Duplicate captions get `_2` suffixes in the examples (`InventoryID_2`).
- Inquiry values filter by the **displayed value** of a column (`ItemStatus eq 'Active'`), unlike DACs (`'AC'`).
- Custom and user-defined fields are read by adding them to the inquiry's results (2024 R1 names a user-defined field
  column `Attribute<AttributeID>`).
- Response shape in the 2026 R2 examples: `{"@odata.context": "<base>/$metadata#Customer%20Contacts", "value": [...]}`
  for a plain inquiry; the parameterised and filtered examples still print `odata.metadata` and decimal values as
  strings (`"QtyOnHand": "1999.000000"`), so parse numbers defensively.

## 7. CORS and server settings

(*DAC-Based OData: General Information*, *To Configure CORS*.) In `Web.config`, inside `px.core`:

```
<odata enableCompression="true" compressionThreshold="860">
    <cors enabled="true" origins="*" methods="*" headers="*"
          exposedHeaders="DataServiceVersion,MaxDataServiceVersion,OData-Version,OData-MaxVersion" />
</odata>
```

CORS is **on by default for all origins**; restrict `origins` (comma-separated), `methods`, `headers`, or add to
`exposedHeaders` after the four OData headers, which are needed to reach the endpoints from a browser. Saving
`Web.config` **restarts the site**. The same `odata` element carries `maxExpansionDepth` (§ 4).

## 8. OData clients

- **Excel** (newer than 2007): Data > Get Data > From Other Sources > From OData Feed, Basic, URL `<base gi>`,
  credentials = Acumatica username (no tenant suffix) and password; the Navigator lists the inquiries the account may
  read and takes parameter values; Refresh All reloads; Excel re-sorts after download. (*... in Microsoft Excel*.)
- **Power BI**: expose an inquiry, build the model (optionally through Excel / Power Pivot), upload; access follows
  the inquiry's rights, `BI` role for the predefined inquiries. (*... Connecting to Acumatica ERP from Power BI*.)

## 9. OData versus the contract-based REST API

From I300 Appendix A (2024 R1) and the 2026 R2 topics above:

| | DAC-based OData | Inquiry-based OData | REST API (`/entity/...`) |
|---|---|---|---|
| Writes | no | no | yes |
| Data of a data entry form | yes, through the form's DACs | yes, if an inquiry is built | yes, if mapped in an endpoint |
| Inquiry with parameters | conditions in `$filter` on the DACs | `_WithParameters(...)` | PUT to the mapped inquiry entity |
| Custom / user-defined fields | by name | add to the inquiry results | `$custom` (CV4) / `$select` with `type` (CV5) |
| Delta of records | `$filter` on `LastModifiedDateTime`, `px.GetDeletedRecords()` | `$filter` on a modified-date column | `$filter` on `LastModifiedDateTime` |
| Sign-in | basic auth (conventional-user licence) or OAuth | same | cookie session or OAuth (API-user licence) |
| Preparation | none (CORS optional) | expose the inquiry (CORS optional) | custom endpoint or extension if the default lacks it |
| Customization package | the inquiries, push definitions and other items used | the inquiries, access rights, push definitions | endpoints, inquiries, push definitions |

Real-time change notification is the same for all three: push notifications on an inquiry or built-in definition
(`references/rest/push-and-webhooks.md`; I300 Lesson 3.2 configures a webhook destination on Push Notifications
(SM302000) for an inquiry).
