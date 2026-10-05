<!-- source: swagger.json (OpenAPI 3.0) of the system endpoints listed below; cross-checked against Acumatica's Integration Development Guide | version: per snapshot (Default/25.200.001 = Acumatica ERP 2025 R2, build 25.201.0213) | verified: 2026-10-05 -->

# Endpoint contract references index

**Exact entity, field and action names** of a system endpoint, generated from that endpoint's OpenAPI document
by `scripts/build_endpoint_reference.py`. One folder per endpoint version. Use it to name things; the protocol
rules (URLs, `$expand` syntax, PUT/POST, status codes) stay in `references/rest/`.

| Path | Covers | Version | Verified |
|---|---|---|---|
| `Default-25.200.001/entities.md` | **Start here.** The 119 top-level entities with form ID, screen title and counts of fields, nested entities and actions; the system members every entity carries | 2025 R2, Contract Version 4 | 2026-10-05 |
| `Default-25.200.001/fields.md` | Every field of all 428 entity schemas (119 top-level, 309 nested), one line each: `Schema.Field : Type` (5,338 lines) | 2025 R2, Contract Version 4 | 2026-10-05 |
| `Default-25.200.001/expand-paths.md` | The 575 linked/detail paths reachable from the top-level entities, one line each: `Entity: Path -> Schema` | 2025 R2, Contract Version 4 | 2026-10-05 |
| `Default-25.200.001/actions.md` | The 163 actions the contract names on 50 entities, with parameter names and types: `Entity.Action(Parameter: Type, ...)` | 2025 R2, Contract Version 4 | 2026-10-05 |

No snapshot of `Default/26.200.001` (Contract Version 5) or of `MANUFACTURING` is bundled yet.

## Looking a name up

Grep; never read `fields.md` whole.

| Question | Grep |
|---|---|
| Does the entity exist, which form is it | `^\| SalesOrder \|` or the form ID (`SO301000`) in `entities.md` |
| An entity's fields | `^SalesOrder\.` in `fields.md` |
| Is it `CustomerID` or `Customer` on this entity | `^SalesOrder\.Customer` in `fields.md` |
| Which entities carry a field | `\.InventoryID ` in `fields.md` |
| What can be expanded, and the schema behind it | `^SalesOrder: ` in `expand-paths.md`, then `^SalesOrderDetail\.` in `fields.md` |
| Where a nested schema is used | `-> Address` in `expand-paths.md` |
| An entity's actions and their parameters | `^Shipment\.` in `actions.md` |
| Which action does X | the verb (`Release`, `Confirm`, `Hold`) in `actions.md` |

A nested schema's name is not the name you send: requests use the **field** name on the parent (`Details`), the
schema name (`SalesOrderDetail`) only tells you where its fields are listed.

## Using the snapshot for another endpoint version

The snapshot is exact for `Default/25.200.001` only.

- **`Default/26.200.001` (Contract Version 5):** most names carry over, but check
  `references/rest/endpoint-versions.md` § 3 first: it lists the entities added, the fields renamed or removed
  (for example `SalesOrder.LastModified` became `LastModifiedDateTime`, every `Subitem` field went, and
  `SalesOrder.UsrExternalOrderOriginal` became `ExternalOrderOriginal`) and the retyping of drop-down and date-only
  fields. Say the name was taken from the 25.200.001 contract and must be confirmed on the instance.
- **`Default/24.200.001` and earlier:** a name here may not exist yet; `endpoint-versions.md` § 3 lists what each
  later version added. Same caveat.
- **Custom endpoints, endpoint extensions and `MANUFACTURING`:** not covered. Use the instance's `swagger.json`.

## Sources

| ID | Source | Role | Verified |
|---|---|---|---|
| `swagger-25.200.001` | `GET <instance URL>/entity/Default/25.200.001/swagger.json` (OpenAPI 3.0.1, `info.version` 4) from an Acumatica ERP 2025 R2 instance, build 25.201.0213. The instance was a **sandbox of a live site, not a clean demo instance**; its name is withheld. The raw document is not in the repository; a scrubbed copy (`servers` removed) belongs at `sources/acumatica-assistant/Default-25.200.001.swagger.json` so the snapshot can be rebuilt. **Pending:** that copy has not been added yet, so until it is the snapshot cannot be rebuilt by others (`sources/acumatica-assistant/README.md`). | Every file under `Default-25.200.001/` | 2026-10-05 |
| `guide-2025r2` | Acumatica ERP *Integration Development* developer guide, 2025 R2 (PDF, last updated 2025-12-15), topic *Comparison of System Endpoints*. Maintenance input, not in the repository. | Cross-check of the snapshot (below) | 2026-10-05 |
| `guide` | `references/rest/endpoint-versions.md` and `references/rest/examples-catalogue.md` (2026 R2 guide) | Cross-check of the snapshot (below) | 2026-10-05 |

## Why a sandbox's swagger is safe to bundle, and how it was checked

- A system endpoint's contract cannot be changed, and the endpoint version fixes its entities, fields and actions
  (`references/rest/rest-api-guide.md` § 1, guide topic *Endpoints and Contracts*), so the `Default` contract does
  not carry a site's customizations. Custom fields and user-defined fields are outside the contract and are not
  in the swagger.
- The only site-specific value in the document is the instance URL in `servers`; the generator never writes it
  and writes nothing if any part of the host name (generic words such as `erp` or `sandbox` excepted) appears in
  its output.
- One name has the `Usr` prefix customizations use: `SalesOrder.UsrExternalOrderOriginal`. It is Acumatica's own:
  the 2025 R2 guide lists it for Sales Orders, and the 2026 R2 guide records its removal in `Default/26.200.001`
  in favour of `ExternalOrderOriginal`.
- Cross-checks run on 2026-10-05, all passing: none of the 14 entities the guide says are new in 26.200.001 is
  present; both entities and the 50 field and action names the 2025 R2 guide lists as new in 25.200.001 are
  present; the eight fields it lists as removed in 25.200.001 are absent; all 49 `Default` entities used by the
  guide's examples are present.

## Scope and limits

- **Names and types only.** The swagger has no field descriptions, no mandatory flags, no key fields and, in
  Contract Version 4, no drop-down values (a drop-down is a `StringValue`). Find allowed values on the form, and
  key fields from the form (`rest-api-guide.md` § 5).
- **The contract, not the instance.** The snapshot says what the contract defines, not which features the
  client's instance has enabled: the guide's examples name the features each needs (`examples-catalogue.md`,
  "Features required") and `GET /entity` returns `features[]`. A name that is absent here is absent from
  `Default/25.200.001`, not necessarily from the form: an element outside the contract is reached as a custom
  field (`rest-api-guide.md` § 7).
- **Contract actions are not all the actions.** Any workflow action of the form can be posted to
  `<Entity>/<action name>` and is discovered with `$adHocSchema` (`rest-api-guide.md` § 2 and § 6). The guide's own
  examples post to four names that this contract does not define: `Case/Close` (its custom-action example),
  `Bill/Approve`, `Payment/Release` and `ProjectTask/Activate`; the contract's names for the last two are
  `Payment.ReleasePayment` and `ProjectTask.ActivateProjectTask`. Prefer the contract name when one exists and say
  which you used.
- Four entity schemas are defined but not referenced by any top-level entity (`EmployeePaycheckEarningDetail`,
  `ItemPriceClassesDetails`, `ItemsDetails`, `PurchaseSettings`); they are in `fields.md` and cannot be reached
  through this endpoint.
- Build 25.201.0213 is one build of 2025 R2. The guide states the endpoint version fixes the contract, so other
  2025 R2 builds should expose the same `Default/25.200.001`; this was not tested against a second build.
