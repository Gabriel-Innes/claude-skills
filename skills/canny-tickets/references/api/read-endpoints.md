# Canny read endpoints (verified 2026-10-01)

Source: https://developers.canny.io/api-reference

## Auth & transport

- **Base URL:** `https://canny.io/api`
- Every request is **POST** with `Content-Type: application/x-www-form-urlencoded`.
- Every request includes `apiKey` (the company's **secret** key, from Canny → Settings → API).
  The skill reads it from `CANNY_API_KEY`; it is never printed or stored.
- Array params (e.g. `tagIDs`) are sent as JSON-encoded strings in a form field.

## Read endpoints used by this skill

| Endpoint | Purpose | Key params |
|---|---|---|
| `/v1/boards/list` | all boards | — |
| `/v1/boards/retrieve` | one board | `id` |
| `/v1/posts/list` | tickets on a board | `boardID`, `status`, `tagIDs`, `authorID`, `companyID`, `search`, `sort`, `limit`, `skip` |
| `/v1/posts/retrieve` | one ticket | `id` **or** `urlName` |
| `/v2/comments/list` | comments on a post | `postID`, `boardID`, `limit`, `cursor` |
| `/v1/comments/retrieve` | one comment | `id` |
| `/v1/votes/list` | votes on a post | `postID`, `boardID`, `limit`, `skip` |
| `/v1/votes/retrieve` | one vote | `id` |
| `/v1/status_changes/list` | status change history | `boardID`, `limit`, `skip` |
| `/v1/entries/list` | changelog entries | `labelIDs`, `type`, `sort`, `limit`, `skip` |
| `/v1/tags/list` | tags | `boardID` |
| `/v1/tags/retrieve` | one tag | `id` |
| `/v1/categories/list` | categories | `boardID` |
| `/v1/categories/retrieve` | one category | `id` |
| `/v2/users/list` | users | `limit`, `cursor` |

Write endpoints exist in the Canny API but are deliberately **excluded** from this skill and from
`scripts/canny.py` (its allowlist blocks anything that is not `list`/`retrieve`).

## posts/list parameters

- `boardID` — restrict to one board (resolve the id from `boards/list`).
- `status` — comma-separated list of statuses to include.
- `sort` — one of `newest`, `oldest`, `relevance`, `score`, `statusChanged`, `trending`.
- `search` — full-text query within the board.
- `tagIDs` — array of tag ids. `authorID`, `companyID` — filter by author / company.
- `limit` (default 10, max 100 per page), `skip` — pagination; response has `hasMore`.

## Valid post statuses

`open`, `under review`, `planned`, `in progress`, `complete`, `closed` — **plus any custom statuses**
the team defined in Canny settings. Treat the live values returned by the API as authoritative; don't
assume the set is only the six built-ins.

## Post object (key fields)

`id`, `title`, `details`, `created`, `url`, `score`, `commentCount`, `status`, `statusChangedAt`,
`eta`, `imageURLs[]`, `customFields[]`, and nested `author`, `board`, `by`, `category`, `owner`,
`tags[]`, `idea`. Integration links: `jira.linkedIssues`, `linear.linkedIssueIDs`,
`clickup.linkedTasks`. Also `roadmaps[]`, `mergeHistory[]`, `changeComment`.

## Board object

`id`, `created`, `name`, `postCount`, `isPrivate`, `privateComments`, `url`, `token` (list responses).

## Comment object

`id`, `author`, `board`, `post`, `created`, `value`, `imageURLs[]`, `internal`, `private`, `likeCount`,
`mentions[]`, `parentID`, `reactions`, `status`.

## Changelog Entry object (key fields)

`id`, `title`, `status` (`draft` / `published` / `scheduled`), `markdownDetails`, `plaintextDetails`,
`posts[]` (linked posts), `labels[]`, `types[]`, `url`, `created`, `lastSaved`, `publishedAt`,
`scheduledFor`, `reactions`.

**Quirk:** each post inside an entry's `posts[]` has a usable `id`, `title`, `board`, `status`, etc.,
but its `url` is a broken admin URL ending `/p/undefined`. Match entry posts to changelog links by
**post id** (resolve the link's urlName via `posts/retrieve`), not by url.

There is **no** `entries/update`, `entries/retrieve`, or endpoint to attach a post to an existing entry.
`entries/create` (a write, out of scope for this read-only skill) can set `postIDs` only at creation time.

## Pagination

- v1 endpoints: `skip` + `limit`, with `hasMore` in the response.
- v2 endpoints (`/v2/comments/list`, `/v2/users/list`): cursor-based (`cursor`).

## Rate limits

Per API key. Free: 5/s, 100/min, 1000/hr. Standard: 10/s, 300/min, 5000/hr. Business: 20/s, 600/min,
15000/hr. Responses carry `X-RateLimit-*` headers; a 429 returns `Retry-After`. The client honours
`Retry-After` and backs off automatically.
