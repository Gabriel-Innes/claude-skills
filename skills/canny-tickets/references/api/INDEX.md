# Canny API reference — index

Source: official Canny API reference, https://developers.canny.io/api-reference
Verified: 2026-10-01

This folder documents **only the read endpoints** this skill uses. Canny also has write endpoints
(create/update/delete/change_status/merge/add_tag/…); they are intentionally **out of scope** — this
skill is read-only. See `MAINTENANCE.md` before ever adding them.

| File | Covers |
|---|---|
| `read-endpoints.md` | Auth, base URL, the read endpoints, object field lists, valid statuses, pagination, rate limits |

Read `read-endpoints.md` when you need an exact field name, a filter parameter, or the valid status
strings. For everyday asks the `scripts/canny.py` CLI already wraps all of this.
