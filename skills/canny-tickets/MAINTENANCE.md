# Maintaining canny-tickets

## What this skill is

A **read-only** assistant for reviewing Canny tickets (bugs and RFCs, on separate boards). It wraps
Canny's `list`/`retrieve` endpoints in `scripts/canny.py` and documents them in `references/api/`.

## Capabilities

- Review: `boards`, `posts`, `post`, `comments`, `votes`, `status-changes`, `tags`, `categories`, `report`.
- Changelog review: `changelog --entry <title|id>` / `--file <path.md>` cross-checks the changelog body
  against the entry's linked posts (by **post id** — entry `posts[]` have a broken `url`) and each
  ticket's status. Enforces "every change documented AND attached". Read-only; the API cannot attach a
  post to an existing entry, so fixes happen in the Canny UI.

## Refresh the API reference

The endpoint catalog and object fields can drift. To refresh:

1. Re-read https://developers.canny.io/api-reference.
2. Update `references/api/read-endpoints.md` (endpoints, params, object fields, statuses, rate limits)
   and bump the "Verified" date in it and in `INDEX.md`.
3. If a read endpoint's params changed, update the matching subcommand in `scripts/canny.py`.
4. If Canny adds a new **read** endpoint worth exposing, add it to `ALLOWED_ENDPOINTS` and give it a
   subcommand.

## Pin board names (optional)

Board ids are account-specific. The CLI resolves boards by name at runtime (`resolve_board`), so no
config is needed. If name lookups ever get slow or ambiguous, add the bug/RFC board ids to this file as
a note for humans — do **not** hardcode a secret anywhere.

## Adding write capabilities later — read this first

The skill is read-only **on purpose** (the user asked for read-only developer review). The client
enforces it through `ALLOWED_ENDPOINTS`. Do **not** add write endpoints casually. If write support is
ever genuinely wanted:

- Treat it as a new, separately-scoped capability with its own review. Writing to Canny
  (change_status, create, merge, comment, delete) is user-visible and can notify voters.
- Every write must be confirmed with the user before it runs (per the action rules): changing status,
  posting a comment, merging or deleting are not to be done silently.
- Keep read and write in separate code paths and keep the read-only default.
- Update `SKILL.md` § 2 (which currently promises read-only) and this file together.

## Test

`evals/evals.json` holds prompts per capability. There is no live test harness bundled; to smoke-test,
set `CANNY_API_KEY` and run `python scripts/canny.py boards`.
