<!-- source: Acumatica Integration Development Guide, "REST API Examples > Basic Requests > Sign In / Sign Out", "Authorizing Client Applications to Work with Acumatica ERP" (all flows), "Limiting Connections of Integrated Applications"; URLs in INDEX.md | version: Acumatica ERP 2026 R2 (guide edition 2026-09-30) | verified: 2026-10-03 -->

# Authentication, sessions and license limits

Three ways open an API session: the REST sign-in method (cookies), the screen-based SOAP `Login()` and OAuth 2.0 /
OIDC. All three count against the license's API session limit (§ 5). Acumatica states that direct
username/password sign-in **will be discontinued in a future version** and recommends OAuth 2.0 / OIDC for new
applications (*Sign In to the Service*).

## 1. Cookie-based sign-in and sign-out

- `POST <instance URL>/entity/auth/login`, `Content-Type: application/json` (or `application/x-www-form-urlencoded`),
  body `{"name": "...", "password": "...", "tenant": "<Login Name on Tenants SM203520>", "branch": "<Branch ID on Branches CS102000>", "locale": "EN-US"}`.
  `locale` is reserved for future use and need not be set. Response **204** with the session cookies; 400 bad
  data; 429 license limit; 500.
- Send the received cookies in the `Cookie` header on every later request.
- `POST <instance URL>/entity/auth/logout` (204) when finished, in **every** session. An unclosed session is
  reclaimed only after a **10-minute timeout**, and there is no way to force-close API users' sessions.
- Two-factor authentication is **bypassed** by the API sign-in; create a user type for API accounts with
  two-factor turned off (§ 6).
- Sign-out must also be called by OAuth clients that use the `api:concurrent_access` scope with cookie-managed
  sessions; it then takes the `Cookie` header, or the `Authorization` header for token sessions.
  (*Sign In to the Service*, *Sign Out from the Service*.)

## 2. OAuth 2.0 / OpenID Connect: registration and endpoints

- **HTTPS is mandatory** for the Acumatica site before OAuth/OIDC clients can work.
- Register the client on **Connected Applications (SM303010)** while signed in to the tenant the client will
  access: Client Name, **Flow** (Authorization Code, Implicit, Resource Owner Password Credentials, Hybrid),
  Secrets tab (shared secret shown **once**, or a JSON Web Key / JWKS URL for JWT bearer client authentication),
  Redirect URIs tab (code, implicit, hybrid), Claims tab and plug-in (OIDC), Refresh Tokens section (sliding
  expiration). The generated **client ID is `<GUID>@<Tenant>`**; the tenant in the ID is the one the token can
  access, and users must sign in to that tenant on the consent page.
- Endpoints (all under the instance URL): discovery `/identity/.well-known/openid-configuration` (recommended),
  authorize `/identity/connect/authorize`, token `/identity/connect/token`, userinfo `/identity/connect/userinfo`,
  JWKS `/identity/.well-known/openid-configuration/jwks` (key also shown on OpenID Connect Preferences SM303030).
- Revoke access on Connected Applications (all users) or User Profile (SM203010, own grants). Revocation removes
  tokens; shared secrets stay valid until they expire, so rotate secrets separately.
- To ship a registration to other instances, include the connected application in a customization project.
  (*OAuth 2.0 and OIDC: General Information*, *Registration ... General Information*, *... JWT Bearer Tokens*,
  *... Acumatica ERP as an Identity Provider via OIDC*, *Activity 1.1.1*.)

### Scopes

| Scope | Meaning |
|---|---|
| `api` | Access to the REST API, screen-based SOAP API and OData. Required for `token` / `id_token token` response types. |
| `offline_access` | Issue a refresh token (not supported by the Implicit flow). |
| `api:concurrent_access` | Allow several concurrent sessions for the application, managed through cookies. Request only when truly needed; each session counts against the license. |
| `openid` | Use OIDC and get an ID token; mandatory for the Hybrid flow. |
| `email`, `profile`, `phone` | Claims disclosed in the ID token / userinfo. |

With `api` and without `api:concurrent_access`, Acumatica issues the first access token together with one session
ID and **reuses that session** for tokens obtained with the refresh token: one session per grant.

### Flow comparison (from *OAuth 2.0 and OIDC: Comparison of the Flows*)

| Characteristic | Authorization Code | Implicit | Resource Owner Password | Hybrid |
|---|---|---|---|---|
| OAuth 2.0 available | yes | yes | yes | no |
| OIDC available | yes | yes | no | yes |
| Access token from the authorization endpoint | no | yes | no | yes |
| Access token from the token endpoint | yes | no | yes | yes |
| Refresh token can be issued | yes | no | yes | yes |
| Client sees the user's credentials | no | no | **yes** | no |
| User explicitly consents to scopes | yes | yes | no | yes |
| Client authenticates (secret or JWT) | yes | no | yes | yes |

Acumatica itself warns that Resource Owner Password Credentials has significant security drawbacks (credentials
pass through the client; no consent step) and that Authorization Code should be preferred whenever possible.

## 3. Token requests

All token requests: `POST /identity/connect/token`, `Content-Type: application/x-www-form-urlencoded`. Client
authentication is either `client_secret=<shared secret>` or
`client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer&client_assertion=<signed JWT>`.

| Flow | Step 1 | Step 2 |
|---|---|---|
| Authorization Code | `GET /identity/connect/authorize?response_type=code&client_id=<id>@<tenant>&redirect_uri=<registered URI>&scope=api%20offline_access` (+ `code_challenge_method=S256&code_challenge=...` for PKCE; only S256 is supported). User signs in and consents; redirect carries `code`. | token endpoint: `grant_type=authorization_code&code=...&client_id=...&client_secret=...&redirect_uri=...` (+ `code_verifier` for PKCE) |
| Resource Owner Password | token endpoint: `grant_type=password&client_id=...&client_secret=...&username=...&password=...&scope=api%20offline_access` | |
| Implicit | `GET /identity/connect/authorize?response_type=token` (or `id_token`, `id_token token`)`&client_id=...&redirect_uri=...&scope=...&nonce=...`; tokens arrive in the URL **fragment**; no refresh token | |
| Hybrid (OIDC) | `GET /identity/connect/authorize?response_type=code id_token` (or `code token`, `code id_token token`)`&client_id=...&redirect_uri=...&scope=openid ...&response_mode=fragment|form_post&nonce=...` | token endpoint: `grant_type=authorization_code&code=...&client_id=...&client_secret=...&redirect_uri=...` |
| Refresh | token endpoint: `grant_type=refresh_token&client_id=...&client_secret=...&refresh_token=...` | discard the old refresh token; always use the newest one issued |

Token response fields: `token_type` (`Bearer`), `access_token`, `expires_in` (seconds; **3600** in every guide
example), `scope`, `refresh_token` (only with `offline_access`), `id_token` (only with `openid`; validate it with
the JWKS key and read claims from it instead of calling userinfo).

Use the token: `Authorization: Bearer <access_token>` on every request, for example
`GET /AcumaticaDB/entity/Default/26.200.001/SalesOrder/SO/000001`.

Refresh-token lifetime: by default the refresh chain expires **30 days** after the initial authentication;
Sliding Expiration on Connected Applications extends it by *Sliding Lifetime (Days)* at each refresh up to
*Absolute Lifetime (Days)* (or Infinite). (*Sliding Expiration of Refresh Tokens*.)

## 4. OAuth session management and the API Login Limit error

(*OAuth 2.0 and OIDC: Session Management*.)

- `api` only: the access token lives one hour and its session closes automatically with it; Acumatica still
  recommends calling sign-out, because sessions count against the license's API user limit.
- `api` + `offline_access`: one session per grant, reused across refreshes; no sign-out needed.
- `api:concurrent_access`: multiple cookie-managed sessions; the application must sign out of **each**.
- **API Login Limit** error on a token request = the license's Maximum Number of API Sessions is reached by
  unclosed sessions. Fix the application to sign out; meanwhile sign out with the previous access token, wait
  up to an hour for OAuth sessions to expire, or restart the site (IIS or Apply Updates SM203510, Restart
  Application).

## 5. License limits on API usage

(*License Restrictions for API Sessions and Requests*; figures on License Monitoring Console SM604000, usage on
System Monitor SM201530, API Monitoring tab.)

- **Maximum Number of API Sessions**: an extra sign-in beyond the limit is rejected with an error. Trial
  licenses allow **two** API sessions and impose no other limits.
- **Maximum Number of Concurrent API Requests**: all requests except sign-out enter an internal queue served by
  that many "API processing cores"; extra requests wait.
- **Maximum Number of API Requests per Minute**: once the past minute reached **50 %** of the limit, each request
  is delayed by `(time left in the minute since its first request) / (requests remaining in the limit)`
  (guide example: 20 s / 25 = 0.8 s).
- A request is **declined** when the queue holds more than **20** requests or a request has waited more than
  **10 minutes**; the client gets no signal that it is queued and must stay connected. Data requests report
  the licence limit as **HTTP 429**.
- `$expand` does not consume these limits faster. Webhook requests (incoming) are summed with other API requests.

## 6. Limiting sessions per integration (admin side)

(*Limitation of API Connections for Integrated Applications*, *To Limit ... of Integrated Applications*, *To
Limit API Connections of a Particular Application*.)

- Create a role (User Roles SM201005) and a **user type** (User Types EP202500) for integrations: Allowed Sign-In
  Type **API** (login-method clients) or **Unrestricted** (OAuth/OIDC clients), **Allowed Concurrent Sign-Ins**
  = sessions per application, **Turn Off Two-Factor Authentication** selected. Give each integration its own
  user account (Users SM201010) of that type.
- A per-user **Max. Number of Concurrent Logins** on Users overrides the user type's value.
- License Monitoring Console, Warnings tab, lists applications holding more than three sessions at once (a
  predefined threshold), a sign of missing sign-outs.
