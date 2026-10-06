<!-- source: Acumatica Reporting Tools Guide and System Administration Guide on Acumatica Beacon, the I300 "Data Retrieval with OData" training course (2024 R1), and the DAC-based OData $metadata of a clean 2026 R2 instance (sources table below) | version: Acumatica ERP 2026 R2 (guide edition 2026-09-30); I300 is 2024 R1 | verified: 2026-10-06 -->

# OData references index

Curated facts for the two **read-only** OData interfaces: DAC-based (`/t/<TenantName>/api/odata/dac`, data access
classes straight from the metadata) and generic-inquiry-based (`/t/<TenantName>/api/odata/gi`, exposed inquiries).
Read `odata-guide.md` first; open the metadata snapshot only to look up a DAC, a field, a navigation property or an
entity-set name. The prose files are extractions (URL patterns, parameters, headers, rules and their exceptions),
not copies of the pages; every section names the topic it came from so it can be re-checked.

| Path | Covers | Version | Verified |
|---|---|---|---|
| `odata-guide.md` | **Start here.** The two interfaces, URLs and tenant names (2026 R2 and the 2024 R1 shapes), authentication / roles / licence, what `$metadata` contains, DAC-based requests (`$select`, `$expand`, `$filter` incl. navigation and lambda filters, paging, key access), headers (`PX-ApiArchive`, `PX-ApiDeleted`, `Accept-Language` / `locale`), `px.GetDeletedRecords()`, inquiry-based requests (`_WithParameters`, unsupported options, 200-without-body), CORS / `Web.config`, Excel and Power BI, OData versus REST | 2026 R2 (+ 2024 R1 where marked) | 2026-10-06 |
| `common-mistakes.md` | 22 review rules for OData consumers: the wrong pattern, why, and the topic with the rule | 2026 R2 | 2026-10-06 |
| `metadata/INDEX.md` | **Generated** snapshot of a clean 2026 R2 instance's DAC-based `$metadata`: how to read it, counts, Edm types, limits | 2026 R2 | 2026-10-06 |
| `metadata/entity-sets.md` | One row per DAC: URL names (`PX_Objects_SO_SOOrder`, `SalesOrder`, `SOOrder`), key, non-filterable fields, `Filterable=false`; singletons | 2026 R2 | 2026-10-06 |
| `metadata/api/INDEX.md` | One row per EntityType / ComplexType: label, key, field and navigation counts, base type, entity sets, bundle file and line range | 2026 R2 | 2026-10-06 |
| `metadata/api/members-01.md` ... `members-06.md` | The entries: `Type.Field : Edm.Type [key] [required] "Display name"` and `Type.Nav -> Target (LocalField=TargetField)`, one line each, grouped by type | 2026 R2 | 2026-10-06 |
| `metadata/enums.md` | The single EnumType the DAC metadata declares | 2026 R2 | 2026-10-06 |

## Sources

| ID | Source | Role | Verified |
|---|---|---|---|
| `rtg` | https://beacon.acumatica.com/r/Reporting-Tools-Guide/Reporting-Tools-Guide | Acumatica's Reporting Tools Guide (Fluid Topics map `4PtabvulGtJrxqfuktkFcw`, 229 topics, metadata version "2026 R2", last edition 2026-09-30). | 2026-10-06 |
| `rtg/dac` | https://beacon.acumatica.com/r/Reporting-Tools-Guide/Accessing-DACs-Through-OData | Chapter *Accessing DACs Through OData* (11 topics: general information, basic data retrieval, filtering, related data, localized and custom fields, archived and removed records, four activities) | 2026-10-06 |
| `rtg/gi-expose` | https://beacon.acumatica.com/r/Reporting-Tools-Guide/Managing-Generic-Inquiries/Exposing-Inquiry-Results-by-Using-OData | Chapter *Exposing Inquiry Results by Using OData* (4 topics) | 2026-10-06 |
| `rtg/gi-access` | https://beacon.acumatica.com/r/Reporting-Tools-Guide/Managing-Generic-Inquiries/Accessing-the-Exposed-Inquiry-Results-Through-OData | Chapter *Accessing the Exposed Inquiry Results Through OData* (10 topics: general information, data retrieval, Power BI, Excel, CORS, four activities) | 2026-10-06 |
| `rtg/dac-discovery` | https://beacon.acumatica.com/r/Reporting-Tools-Guide/Managing-Generic-Inquiries/Discovering-DACs/DAC-Discovery-General-Information | *DAC Discovery: General Information* and *Data from Multiple Data Sources: DAC Schema Browser* (finding the DAC and field behind a form element) | 2026-10-06 |
| `sag/roles` | https://beacon.acumatica.com/r/System-Administration-Guide/Configuring-User-Roles/User-Roles-Predefined-Roles | System Administration Guide, *User Roles: Predefined Roles* (the `BI` and `OData4 User` roles), 2026 R2 edition | 2026-10-06 |
| `i300` | Acumatica training course *I300 Data Retrieval with OData*, 2024 R1, revision 2024-03-21 (PDF; Postman collection in the `IntegrationDevelopment\I300` folder of Acumatica's Help-and-Training-Examples GitHub repository) | The 2024 R1 endpoint shapes (`/OData/<Tenant>` OData 3.0 for inquiries, `/ODatav4/<Tenant>` for DACs), OData 3.0 request syntax, Appendix A comparison of OData 3.0 / 4.0 / REST | 2026-10-06 |
| `metadata` | `GET <instance URL>/t/<TenantName>/api/odata/dac/$metadata` of a clean Acumatica ERP 2026 R2 instance, 20 MB CSDL, compiled by `scripts/build_odata_metadata_ref.py` (the raw XML is not committed) | `metadata/` | 2026-10-06 |

Any Reporting Tools Guide topic is reachable as
`https://beacon.acumatica.com/r/Reporting-Tools-Guide/<Chapter>/<Topic-Title-With-Hyphens>`.

## Known limits of these references

- **Two editions.** The guide is 2026 R2 and documents only the `/t/<TenantName>/api/odata/{dac,gi}` URLs and OData
  4.0 for both interfaces. The course is 2024 R1 and documents `/OData/` (OData 3.0) and `/ODatav4/`. Nothing here says
  in which release the URLs changed. The owner verified on a clean local 2026 R2 instance (Postman, 2026-10-06) that
  `/odatav4/<TenantName>/$metadata` and `/t/<TenantName>/api/odata/dac/$metadata` are interchangeable; the
  inquiry-based `/OData/<TenantName>` path was not tested, so probe `$metadata` on the client's instance and read the
  `edmx` version before relying on it.
- **One clean instance.** The metadata snapshot has every module of a clean 2026 R2 install (2,265 DACs, 5,108 entity
  sets) and no customization. A client's instance adds custom and user-defined fields and extension DACs and may lack
  modules; confirm names on the client's `$metadata`. No inquiry-based (`/api/odata/gi`) metadata is bundled, because
  it is tenant-specific.
- The guide's request examples are reproduced as URL patterns only; response bodies are summarised.
- Behaviour the pages do not state (status codes for refused fields, page-size caps, timeouts, `$search`,
  `$batch`, `$metadata` caching) is **not covered**; say so rather than guessing from the OData standard.
