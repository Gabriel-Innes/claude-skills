<!-- source: SAP Help Portal sources listed below | version: SAP Business One 10.0, with feature-pack boundaries called out | verified: 2026-10-05 -->

# Service Layer index

Reference-backed guidance for the SAP Business One **Service Layer**. Read `service-layer-guide.md` first,
then open only the focused file the request needs. The prose files summarise SAP's guide; exact entity set,
property, enum and action names come from the generated `metadata/` snapshot (FP 2602).

| Path | Covers | Version | Verified |
|---|---|---|---|
| `service-layer-guide.md` | **Start here.** Protocol and versions, login/session, query options and their limits (incl. HANA-only features), paging, CRUD/actions, ETags (FP 2102, entity list), batch and transactions, UDF/UDT/UDO, attachments, SQL and Semantic Layer views, configuration/operations, limitations | B1 10.0; OData v4 primary from FP 2405 | 2026-10-04 |
| `di-api-vs-service-layer.md` | **Choosing between the DI API and Service Layer** and porting code between them: decision table with SAP's limitations, side-by-side operation mapping, naming differences (Appendix II), questions to ask | B1 10.0 | 2026-10-04 |
| `sql-queries.md` | `SQLQueries`: availability, CRUD and `List`, table/column allowlist, keyword and function subsets, normalization, parameters, permissions, audit table, error codes | B1 10.0 FP 2011+ (UDT/UDO from FP 2102) | 2026-10-04 |
| `fp2602.md` | Webhooks: enablement, event catalog, subscription properties, payload, company settings, delivery semantics (retry, duplicates, ordering, replay), FP 2608 additions | B1 10.0 FP 2602 / FP 2608 | 2026-10-04 |
| `metadata/INDEX.md` | **Exact names.** Generated from one OData v4 `/b1s/v2/$metadata` document: 298 entity types and 782 complex types with 11,054 properties (`api/`), 330 entity sets with navigation bindings (`entity-sets.md`), 667 actions/functions (`operations/`), 603 action/function imports (`operation-imports.md`), 473 enums with 2,827 members (`enums/`). Flat `members.md` indexes for grep; `INDEX.md` files give file/line ranges into the bundles. Customer UDFs and add-on objects were filtered out (counts recorded there) | B1 10.0 **FP 2602** only | 2026-10-05 |

## Sources

| ID | Source | Role | Verified |
|---|---|---|---|
| `guide-pdf` | *Working with SAP Business One Service Layer*, document version 1.29, 2026-07-27 (PDF export of `guide`). **Page numbers cited in these files refer to this document.** Kept as maintenance input outside the committed skill (SAP's notice forbids reproduction); do not package it. | Primary source for every file in this folder | 2026-10-04 |
| `guide` | https://help.sap.com/docs/SAP_BUSINESS_ONE/f110a154dd0f4c20bf7f3ebca9eeb794 | The same guide on SAP Help Portal (HTML); check its Document History for revisions after 1.29 | 2026-10-02 |
| `api-ref` | https://help.sap.com/doc/056f69366b5345a386bb8149f1700c19/10.0/en-US/Service%20Layer%20API%20Reference.html | Current OData v4 API reference; Login/Logout, exposed entities and actions, OData v3 deprecation statement | 2026-10-02 |
| `change-log` | https://help.sap.com/docs/SAP_BUSINESS_ONE/f0bf25fb678c405db749545310803c8b | Sequential Service Layer API change logs by feature pack/service pack | 2026-10-02 |
| `fp2011-change` | https://help.sap.com/doc/f99c5aaf48d245438a15623357172fb8/10.0/en-US/100140VS100130.html | Confirms SQL query API additions in FP 2011 | 2026-10-02 |
| `fp2602-change` | https://help.sap.com/doc/25b17ff712de4af99c129dd18da0f051/10.0/en-US/10.0_FP2602_VS_SP2511.html | Confirms FP 2602 webhook-related types, properties, entity sets and actions | 2026-10-02 |
| `diapi` | `references/diapi/` (DI API 10.0 reference compiled from SAP's `REFDI.chm`) | DI API side of `di-api-vs-service-layer.md` (members verified in `api/members.md`) | 2026-10-04 |
| `metadata-fp2602` | `GET /b1s/v2/$metadata` of a SAP Business One 10.0 FP 2602 company, compiled by `scripts/build_servicelayer_ref.py` (filters recorded in `metadata/INDEX.md`). The source was a **filtered production company**, not a clean demo company, and the raw document is not kept in the repository, so the snapshot cannot be rebuilt by others; re-capture from a demo company when one is available. Reviewed and merged 2026-10-05 (#11) | Every file under `metadata/` | 2026-10-05 |

## Scope and limits

- `metadata/` is a full extraction of one FP 2602 `$metadata`, not of SAP's API reference prose; it carries names,
  types, keys, bindings and signatures, no descriptions. For another feature pack, verify a name against the
  client's `/b1s/v2/$metadata` or SAP's change log for that pack before generating code, and say which you used.
- Absence from the snapshot is not proof of absence: `OpenType: true` types accept UDFs that are not listed, a
  `Filtered properties: N` line marks customer UDFs that were removed, and later feature packs add properties.
- Feature-pack boundaries matter: FP 2011 (`SQLQueries`), FP 2102 (ETags, UDT/UDO in SQLQueries), FP 2105
  (`$expand` with `$select`), FP 2202 (stream upload, log monitor), FP 2305 (domain login, access log default),
  FP 2405 (OData v3 deprecated), FP 2602 (webhooks), FP 2608 (webhook filters and payload properties, metadata
  annotations). Do not present a later feature as available on an earlier system.
- Several query features are documented for HANA only (aggregation, cross-join, row-level filter, Semantic
  Layer views); SQL views are SQL Server only. Ask which database before proposing them.
- Client-specific UDFs, UDTs and UDOs are not bundled.
- Known inconsistency in SAP's text: the webhook retry policy (3 × 2 s in the configuration table versus 5
  exponential retries in the FAQ). `fp2602.md` § 6 records both.
