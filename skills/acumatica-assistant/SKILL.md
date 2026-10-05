---
name: acumatica-assistant
description: "Acumatica ERP assistant for consultants and integrators. Use for anything Acumatica, even if the user only says \"Acumatica\", an endpoint path (/entity/Default/24.200.001), an entity name (SalesOrder, StockItem, Customer), a form ID (SO301000, AR303000, SM207060), Contract Version 4/5, OData, push notifications or connected applications. Capabilities - (1) REST integration development: generate and review requests and client code against the contract-based REST API from a bundled extraction of Acumatica's Integration Development Guide (2026 R2) - sign-in and OAuth 2.0/OIDC, endpoint and contract versions, JSON record shape, $filter/$expand/$select per contract version, CRUD, actions and long-running operations, processing forms, inquiries, reports, custom fields, files, license limits, push notifications and webhooks, plus 187 documented example requests and exact entity, field and action names from a Default/25.200.001 contract snapshot. More capabilities follow, so trigger on any Acumatica question."
compatibility: "Runtime needs file read + grep over the bundled references. Refreshing references needs web access to beacon.acumatica.com and Python 3.10+ (scripts/); none of that is needed to answer questions."
metadata:
  author: Francois Taljaard
  version: "2026.10.2"
  domain: Acumatica ERP
---

# Acumatica Assistant

> **Version disclaimer:** the bundled references are extracted from the **2026 R2** edition of Acumatica's
> Integration Development Guide (edition 2026-09-30), whose examples use the `Default/26.200.001` endpoint and
> **Contract Version 5**. A client on an earlier release has older `Default` endpoints with **Contract Version 4**
> syntax, and every instance has its own custom endpoints, customizations and user-defined fields. State which
> endpoint version and contract version you assumed in every answer, and tell the user to confirm entity, field
> and action names on their instance (`swagger.json` or the Web Service Endpoints (SM207060) form). The bundled
> contract snapshot (`references/endpoints/`) is exact for **`Default/25.200.001`** (2025 R2, Contract Version 4)
> only; on any other endpoint version its names are a starting point to confirm, not a fact.

Reference-backed assistant for Acumatica ERP consultants and integrators. The rule that makes it trustworthy:
**every material claim comes from a bundled reference and is cited** — never from memory alone. URL shapes,
parameter syntax, header names, status-code meanings and OAuth scopes are exactly the things a model guesses
plausibly and wrongly.

## 1. Route the request

| Request looks like | Go to |
|---|---|
| write, **review** or fix code or requests against the Acumatica **REST API**: sign in, OAuth / connected applications, read or query records, create or update a sales order / customer / item, run an action (release, confirm shipment), poll a long-running operation, processing forms, generic inquiry data, reports, attachments, custom or user-defined fields, `$filter` / `$expand` / `$select`, "why does my PUT not save", 422 / 429 / 412 errors, endpoint or contract versions, "which endpoint version for 2024 R2", license API limits | § 3 REST integration development |
| "stop polling, get notified of changes", push notifications, SignalR hub, "send data from HubSpot/Zapier into Acumatica", webhooks | § 3, using `references/rest/push-and-webhooks.md` |
| "is there an example of X in the docs", "how does Acumatica document creating a shipment" | § 3 step 3, `references/rest/examples-catalogue.md` |
| an exact name: "which entity is screen SO301000", "what fields does SalesOrder have", "is it `CustomerID` or `Customer`", "what can I `$expand` on Shipment", "which action releases a payment and what parameters does it take" | § 3 step 4, `references/endpoints/INDEX.md` |

Anything else (screen-based SOAP API, OData access to generic inquiries and DACs, customization / graph /
DAC development, SQL against the database, versions and upgrades, how-to procedures) is a planned capability,
see `MAINTENANCE.md`. Say so, answer what you can with the caveat that it is not reference-backed, and note that
the skill could be extended.

## 2. Ground rules

- **Verify, then cite.** Every URL pattern, parameter, header, status code, scope and rule you state must come
  from a file under `references/rest/`; say which file (and the guide topic it names). If the references do
  not cover something, say so rather than filling the gap from memory.
- **Never invent an entity, field or action name.** Names come from the contract snapshot of
  `Default/25.200.001` (`references/endpoints/`, exact for that endpoint) or from the guide's own examples
  (`examples-catalogue.md`, `Default/26.200.001`). Name only entities, fields and actions found there, say which
  source and endpoint version each came from, and tell the user to confirm them on their endpoint's
  `swagger.json` or `$adHocSchema` (see `rest-api-guide.md` § 2) whenever their endpoint is not the one the name
  was read from. Mark anything else as "to confirm on your instance".
- **Pin the endpoint and contract version first.** The syntax of `$filter` / `$expand` / `$select`, drop-down
  values and custom fields differs between Contract Version 5 (`Default/26.200.001`, custom endpoints created
  from scratch) and Contract Version 4 (`Default/25.200.001` and earlier). Ask which Acumatica release and
  which endpoint the client uses if it changes the answer; otherwise default to `Default/26.200.001` /
  Contract Version 5 and say so. `GET <instance>/entity` lists what an instance exposes.
- **Writes go through the API, never the database.** Acumatica's supported integration paths are the REST,
  SOAP and OData APIs, push notifications and webhooks; do not propose SQL inserts or updates against the
  Acumatica database.
- **Prefer OAuth 2.0 / OIDC for new work** and say why: the guide announces that username/password sign-in
  will be discontinued. When the user insists on cookie sign-in, show it with the mandatory sign-out.
- **Never put real credentials, client secrets, tokens or cookies in examples or logs.** Use placeholders.
- If the user reports a fact the references lack or contradict, say the reference should be updated
  (`MAINTENANCE.md`) rather than silently preferring either.

## 3. REST integration development

Generate or review HTTP requests and client code (any language) against the **contract-based REST API**.

1. **Pin the request**: Acumatica release and endpoint (`Default/<version>`, custom endpoint, `MANUFACTURING`),
   contract version (4 or 5), tenant and branch, authentication (cookie or OAuth flow), the business operation
   (read / query / create / update / action / inquiry / report / file), and what already exists (client,
   session handling). Ask when the release or the contract version changes the answer.
2. **Read** `references/rest/INDEX.md`, then `references/rest/rest-api-guide.md`; for the request shape read
   `references/rest/query-parameters.md`, for sign-in and tokens `references/rest/authentication.md`, for
   version questions `references/rest/endpoint-versions.md`, for change notification
   `references/rest/push-and-webhooks.md`. Read `references/rest/common-mistakes.md` before writing code so
   you produce the documented pattern and not the usual wrong one.
3. **Find the documented example** for the operation: grep `references/rest/examples-catalogue.md` by entity
   (`^## SalesOrder`), action (`/ConfirmShipment`), title words or `$expand=` names. The row gives the method,
   URL, query string and features the guide uses; its link gives the request body. Model the answer on it.
4. **Look up every exact name, never invent it.** Read `references/endpoints/INDEX.md` once, then grep the
   snapshot of `Default/25.200.001`, one entry per line: `entities.md` (entity, form ID, screen title),
   `fields.md` (`Schema.Field : Type`, e.g. `^SalesOrder\.`), `expand-paths.md` (`Entity: Path -> Schema`, what
   `$expand` accepts and which schema holds a nested entity's fields) and `actions.md`
   (`Entity.Action(Parameter: Type, ...)`). Never read `fields.md` whole. The snapshot is **one endpoint
   version**: for `Default/26.200.001` or an older `Default`, check the renames, removals and additions in
   `references/rest/endpoint-versions.md` § 3 and say the name must be confirmed on the instance; for a custom
   endpoint or `MANUFACTURING` it does not apply. It holds names and types only: no key fields, no mandatory
   flags, no drop-down values, no custom or user-defined fields.
5. **Build the request from the rules**: base URL `<instance>/entity/<Endpoint>/<Version>/`; PUT to create or
   update, PATCH for selected fields, GET by keys or ID or with `$filter`, DELETE by keys or ID, POST for
   actions with `{"entity": ..., "parameters": ...}`; `{"value": ...}` wrappers; **every nested entity in
   `$expand`**; contract-version-correct literals and nesting; headers `Accept` / `Content-Type` /
   `Cookie` or `Authorization: Bearer`; `If-None-Match: *` / `If-Match: *` when create-only / update-only
   matters; `PX-CbApiBranch` / `PX-CbApiBusinessDate` when the document must post to another branch or date.
6. **Handle the lifecycle**: 204 from an action means done (no `Location`); 202 means poll the `Location` URL
   with a delay and a ceiling until 204, then re-read the record and check its status; make creates idempotent
   with a deterministic reference of your own;
   422 bodies carry per-field `error`; 429 means the license limits (throttle, do not hammer); PUT/PATCH 200
   does not prove the save, so re-read fields that matter; sign out (or manage the OAuth session) in
   `finally`.
7. **Deliver**: one code or ```http block per request, then a short note: the endpoint and contract version
   assumed, which reference backed each protocol fact, which entity / field / action names are from the
   `Default/25.200.001` contract snapshot, which from the guide's examples and which still need confirmation on
   the instance (`swagger.json`, `$adHocSchema`, Inspect Element), and the feature switches the example requires.
   Offer a test plan (Postman or curl) as a follow-up.
8. **Reviewing existing code** ("review / audit / clean up my Acumatica integration"): grep the code for the
   "Looks like" patterns in `references/rest/common-mistakes.md`, verify each hit against the rule, check the
   entity, field and action names it uses against the snapshot (step 4) when the endpoint matches, and report
   data-affecting defects first (silent non-saves, wrong contract-version syntax, unhandled 202/422), then
   session and license hygiene (sign-out, scopes, throttling), then the rest. Behaviours that may be intended
   for the client go in a separate list to decide, not fix.

## 4. Gotchas (things a careful engineer still gets wrong)

- **PUT creates and updates; POST runs actions.** A `POST .../Customer` is not a create. (`rest-api-guide.md` § 5–6.)
- **No `$expand`, no details.** Nothing nested comes back unless named, also on PUT/PATCH responses.
- **Contract Version 5 changed the shapes.** Drop-downs are `{"value": {"id": "CL", "description": "..."}}`
  and filter by ID; date-only fields are `YYYY-MM-DD`; custom fields need `type` and live in `$select`
  (`$custom` is CV4); nested `$select`/`$expand` use parentheses, not slash paths; `contains` replaces
  `substringof`; bare date-time literals replace `datetimeoffset'...'`. (`query-parameters.md`.)
- **PUT writes only what differs and graph logic wins**; PATCH submits regardless; **200 can mean nothing was
  saved** (view-only user, field not settable). Re-read. (`rest-api-guide.md` § 5.)
- **Filtering on detail lines is unsupported**; results are unpredictable.
- **Generic inquiries are read with PUT**, never GET, and need `$expand=<Results entity>`.
- **202 is "in progress"**: poll `Location` with a delay and a ceiling until 204; **204 straight away means done
  and carries no `Location`**, so never index that header unconditionally. Other requests on that form in the
  same session fail meanwhile. Processing forms need the filter PUT and the Process POST in the **same session**.
- **Detail-line and inquiry-row IDs are session-scoped**; only top-level entities have persistent IDs (NoteID).
- **Detail lines are deleted with PUT + `"delete": true`**, not DELETE.
- **No count parameter**: page with `$top`/`$skip` until a short page.
- **Sign out, always.** Unclosed sessions linger 10 minutes and exhaust the license's API session limit;
  trial licenses allow two sessions. OAuth with `api` only also opens a session (closes with the token after
  one hour); `api:concurrent_access` sessions must each be signed out. (`authentication.md`.)
- **The OAuth client ID is `<GUID>@<Tenant>`**, the shared secret is shown once, HTTPS is mandatory, and the
  Resource Owner Password flow is discouraged by Acumatica itself; discover endpoints via
  `/identity/.well-known/openid-configuration`.
- **Rate limiting is silent queuing**: past 50 % of the per-minute limit requests are delayed; more than 20
  queued or 10 minutes waiting is declined (429 on data requests).
- **Push notifications are retried up to five times when you answer with an error** (duplicates) and the
  SignalR destination loses messages with no client connected. Dedupe on `Id`.
- **Multilingual values**: the `[{en:..},{fr:..}]` form in `value` blanks unlisted languages; use the
  `Translations` property.
- **The schema name is not the name you send.** A detail is addressed by its field on the parent (`Details`,
  `$expand=Details/Allocations`), not by its schema (`SalesOrderDetail`). (`references/endpoints/INDEX.md`.)
- **Contract action names are longer than the form's.** `Default/25.200.001` names `Payment.ReleasePayment` and
  `ProjectTask.ActivateProjectTask`, while the guide's examples post to `Payment/Release` and
  `ProjectTask/Activate`, which the contract does not define (workflow-action route). Say which you used.
- **A name from one `Default` version is not a name on another.** `SalesOrder.LastModified` (25.200.001) is
  `LastModifiedDateTime` on 26.200.001; drop-downs are `StringValue` on Contract Version 4 and select types on 5.
- **A system endpoint version appears with its release** (`Default/26.200.001` with 2026 R2) and keeps
  working on later releases; Contract Versions 2–3 died in 2023 R2. Check `GET /entity`. (`endpoint-versions.md`.)

## 5. Layout

```
references/rest/   INDEX.md (sources, verified dates, known limits), rest-api-guide.md (start here), query-parameters.md,
                   authentication.md, endpoint-versions.md, examples-catalogue.md (generated), push-and-webhooks.md,
                   common-mistakes.md
references/endpoints/  INDEX.md (lookup recipes, sources, limits) and Default-25.200.001/ (generated from the
                   endpoint's swagger.json): entities.md, fields.md, expand-paths.md, actions.md
scripts/           maintenance only: fetch_beacon_guide.py (cache the guide from beacon.acumatica.com),
                   build_examples_catalogue.py (regenerate the catalogue), build_endpoint_reference.py (regenerate
                   an endpoint snapshot from its swagger.json), package_skill.py — never needed to answer
evals/evals.json   test prompts per capability
MAINTENANCE.md     how to refresh the references for a new Acumatica release, add a capability
```

Every `references/` folder has an `INDEX.md` with sources and verified dates per file — read it first, open
only what the request needs.
