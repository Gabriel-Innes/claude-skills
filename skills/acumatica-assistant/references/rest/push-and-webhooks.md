<!-- source: Acumatica Integration Development Guide, "Configuring Push Notifications for Real-Time Monitoring" and "Configuring Webhooks"; URLs in INDEX.md | version: Acumatica ERP 2026 R2 (guide edition 2026-09-30) | verified: 2026-10-03 -->

# Push notifications (outbound) and webhooks (inbound)

Two different things in Acumatica's vocabulary:

- **Push notifications** are JSON messages **Acumatica sends** when the result set of a data query changes.
  Use them instead of polling the REST API for changes.
- **Webhooks** are URLs **Acumatica exposes** so an external application can push its own payload *into*
  Acumatica, handled by custom C# (`IWebhookHandler`).

## 1. Push notifications

(*Push Notifications: General Information*, *Recommendations for the Data Queries*, *Destinations*, *Format*,
*Failed Notifications*, *To Configure Push Notifications*, *To Connect to the SignalR Hub*, *To Include
Additional Information*.)

- Configured on **Push Notifications (SM302000)**: a destination (name, type, address, optional header name/value)
  plus one or more **data queries**: a generic inquiry (Generic Inquiries tab) or a built-in query definition
  (a class implementing `PX.PushNotifications.Sources.IInCodeNotificationDefinition`). Per query, either
  *Track All Fields* or an explicit Fields list; Acumatica recommends listing fields, since tracking everything
  can overflow the notification queue.
- Query rules: no aggregation or grouping; no joins of several detail tables (can hang the system); prefer left
  joins; keep it simple; no formulas on the Results Grid; no selector description fields (join the table and
  add its field instead).
- **Destination types**: *Webhook* (HTTP address; Acumatica POSTs the JSON and sets `Accept`/`Content-Type`
  itself; a configurable extra header for authentication), *Message Queue* (private MSMQ, most reliable),
  *SignalR Hub* (address `PushNotificationsHub`; clients connect by websocket or long polling; **not reliable**:
  a notification with no connected client is lost and cannot be resent), *Commerce* (MSMQ for commerce
  connectors), or a custom destination type.
- **Delivery**: at most **five** automatic attempts for webhook, MSMQ and commerce destinations. A non-success
  reply from your webhook triggers a resend, so **return success once you have accepted the message**, or you
  will receive duplicates. Failed notifications appear on **Process Push Notifications (SM502000)** for **two
  days** and can be resent (not when flagged Truncated); notifications that failed before sending are logged to
  `PushNotificationsErrors` only if `api:push-notifications:enable-dead-message-log` is `true` in web.config.
- **Format** (one JSON object per transaction):

| Element | Meaning |
|---|---|
| `Inserted` | rows now in the query result (new or updated state) |
| `Deleted` | rows that were in the result before the transaction (old state); compare with `Inserted` to see updates |
| `Query` | generic inquiry name or built-in definition class name |
| `CompanyId` | tenant name |
| `Id` | unique ID of the data transaction; use it to drop duplicate deliveries |
| `TimeStamp` | long value for ordering |
| `AdditionalInfo` | system extras (e.g. `PXPerformanceInfoStartTime`) plus anything an `ICommitEventEnricher` adds (the `Enrich()` method runs in `PXTransactionScope.Dispose()`) |

  When tracked fields are listed, untracked attribute values come back as `null`. A multilingual field changed
  under multilingual input can appear identical in `Inserted` and `Deleted`.
- **SignalR client** (.NET): `HubConnectionBuilder().WithUrl("<instance URL>/signalr/hubs/PushNotificationsHub", o => { o.Headers.Add("Authorization", "Basic <base64 user:password>"); o.Transports = HttpTransportType.WebSockets; o.SkipNegotiation = true; })`,
  then `InvokeAsync("Subscribe", "<Destination Name>")` and `On<object>("ReceiveNotification", ...)`. Multi-tenant
  login is `user@Tenant`.
- Definitions can be shipped in a customization project (Push Notifications item).

## 2. Webhooks

(*Webhooks: General Information*, *Webhooks: To Configure Webhooks*.)

- Implement `PX.Api.Webhooks.IWebhookHandler` (assembly `PX.Api.Webhooks.Abstractions.dll`) with
  `Task HandleAsync(WebhookContext context, CancellationToken cancellation)`: validate authentication from the
  request (`context.Request.Headers`), parse the body (`context.Request.CreateTextReader()`), run under a
  `PXLoginScope("user@Tenant")`, create a graph and save, write a reply with
  `context.Response.CreateTextWriter()` / `context.Response.StatusCode`.
- Build the DLL into the instance's `Bin` folder, then register on **Webhooks (SM304000)**: Webhook Name,
  Implementation Class; saving generates the URL, shaped like
  `https://<host>/<instance>/Webhooks/<tenant>/<GUID>`. Give that URL to the external system.
- Incoming requests must be **POST or GET**, body no larger than `webhook:maxrequestsize` (default **1 MB**,
  web.config). Errors are returned as JSON regardless of `Accept`. Webhook requests **count toward the license's
  API request limits**.
- Request History tab logs requests (body trimmed to `webhook:maxbodysizetolog`, default 10 KB; the amount kept
  is configurable). Ship the webhook (Webhooks AU210020 page) and the DLL (Files AU202500) in a customization
  project; *Predefined* makes the class read-only on target instances.
- The guide's sample handler checks `Authorization: Bearer token` literally and says real validation is
  required in production.
