<!-- source: Acumatica Integration Development Guide on Acumatica Beacon (sources table below) | version: Acumatica ERP 2026 R2, guide edition 2026-09-30 | verified: 2026-10-03 -->

# REST API references index

Curated facts from Acumatica's **Integration Development Guide** for the contract-based REST API, authorization,
license limits, push notifications and webhooks. Read `rest-api-guide.md` first, then open only the file the
request needs. The files are extractions (URL patterns, parameters, headers, status codes, JSON shapes, rules
and their exceptions), not copies of the pages; every section names the topic it came from so it can be
re-checked.

| Path | Covers | Version | Verified |
|---|---|---|---|
| `rest-api-guide.md` | **Start here.** Endpoint URLs and versions, contract discovery (`swagger.json`, `$adHocSchema`, `GET /entity`), JSON record representation, headers and status codes, CRUD rules, actions and long-running operations, processing forms, generic inquiries, reports, custom fields, files, session hygiene, engineering habits | 2026 R2 | 2026-10-03 |
| `query-parameters.md` | `$filter`, `$expand`, `$select`, `$custom`, `$top`, `$skip`: syntax per contract version (5 = OData 4.01, 4 = OData 3.0), custom-field filter functions, where each parameter is accepted | 2026 R2 | 2026-10-03 |
| `authentication.md` | Cookie sign-in/sign-out, OAuth 2.0 / OIDC registration (Connected Applications), scopes, flow comparison, token requests per flow, refresh and session management, license limits on sessions/requests, user types for integrations | 2026 R2 | 2026-10-03 |
| `endpoint-versions.md` | Contract Versions 4 vs 5; the `Default` system endpoint versions compared by the guide (20.200.001 to 26.200.001) with new, renamed and removed entities/fields per step | 2026 R2 | 2026-10-03 |
| `examples-catalogue.md` | Generated: one row per example topic in the guide (187 topics, 54 groups) with the documented request lines (method, URL, query string), features required and a link to the page | 2026 R2 | 2026-10-03 |
| `push-and-webhooks.md` | Push notifications (queries, destinations, delivery, JSON format, SignalR client) and inbound webhooks (`IWebhookHandler`, registration, limits) | 2026 R2 | 2026-10-03 |
| `common-mistakes.md` | 36 review rules: the wrong pattern, why, and the guide topic with the rule | 2026 R2 | 2026-10-03 |

## Sources

| ID | Source | Role | Verified |
|---|---|---|---|
| `guide` | https://beacon.acumatica.com/r/Integration-Development-Guide/Integration-Development-Guide | Acumatica's Integration Development Guide (Fluid Topics map `UpQu337K_38feMdsBg0ruQ`, 346 topics, metadata version "2026 R2", last edition 2026-09-30). Every file here derives from it. | 2026-10-03 |
| `guide/rest` | https://beacon.acumatica.com/r/Integration-Development-Guide/Configuring-the-REST-API | Chapter *Configuring the REST API* (18 topics: contract concepts, custom fields, custom endpoints, naming rules, contract versions, system endpoint comparison, OpenAPI, JSON representation, SM207060 procedures) | 2026-10-03 |
| `guide/examples` | https://beacon.acumatica.com/r/Integration-Development-Guide/REST-API-Examples | Chapter *REST API Examples* (Basic Requests 33 topics, Parameters 9 topics, 145 per-entity examples) | 2026-10-03 |
| `guide/auth` | https://beacon.acumatica.com/r/Integration-Development-Guide/Authorizing-Client-Applications-to-Work-with-Acumatica-ERP | Chapter *Authorizing Client Applications* (OAuth 2.0 / OIDC, 30 topics) | 2026-10-03 |
| `guide/limits` | https://beacon.acumatica.com/r/Integration-Development-Guide/Limiting-Connections-of-Integrated-Applications | Chapter *Limiting Connections of Integrated Applications* (5 topics) | 2026-10-03 |
| `guide/push` | https://beacon.acumatica.com/r/Integration-Development-Guide/Configuring-Push-Notifications-for-Real-Time-Monitoring | Chapter *Configuring Push Notifications* (13 topics) | 2026-10-03 |
| `guide/webhooks` | https://beacon.acumatica.com/r/Integration-Development-Guide/Configuring-Webhooks | Chapter *Configuring Webhooks* (3 topics) | 2026-10-03 |

Any topic is reachable as `https://beacon.acumatica.com/r/Integration-Development-Guide/<Chapter>/<Topic-Title-With-Hyphens>`;
`examples-catalogue.md` links every example page directly. The chapter *Working with the SOAP API* (36 topics,
screen-based SOAP API) was fetched but is **not** curated here: the skill's first capability is REST.

## Known limits of these references

- **One version.** The guide is the 2026 R2 edition and its examples use `Default/26.200.001` (Contract Version 5).
  Older instances expose older `Default` versions with Contract Version 4 syntax; `endpoint-versions.md` records
  what the guide says changed, but exact entity and field names on a client's instance must come from that
  instance's `swagger.json` or Web Service Endpoints (SM207060) form.
- **No entity/field reference is bundled.** Acumatica publishes the contract as OpenAPI per endpoint and tenant;
  it is not reproduced here. `examples-catalogue.md` shows which entities, actions and `$expand` names the guide
  uses, which is evidence that they exist on `Default/26.200.001`, not a schema.
- The per-field change lists in *Comparison of System Endpoints* are summarised, not copied: when a field is
  missing on an older endpoint, open the page.
- The guide's request bodies are not reproduced; the catalogue links to them.
- Facts about Contract Version 4 come from the 2026 R2 guide's CV4 parameter topics, which describe CV4 as it
  behaves in 2026 R2.
