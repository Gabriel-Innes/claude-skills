---
name: canny-tickets
description: "Read-only assistant for reviewing Canny tickets - bugs and RFCs / feature requests - so developers can see what's outstanding, what's in progress, and what needs attention. Use for anything about Canny: 'what bugs are open', 'show me the RFC board', 'what changed this week', 'summarise post X', 'how many in-progress items', vote/comment counts, triage review, and status/board reports. Triggers on 'Canny', a board name (Bugs, Feature Requests, RFC), a Canny post id or canny.io URL, or any ask to review/report on the team's tickets. Bugs and RFCs live on separate Canny boards. This skill only reads - it never creates, edits, closes, or comments on tickets."
compatibility: "Needs Python 3.8+ and outbound HTTPS to canny.io, plus the CANNY_API_KEY environment variable (a Canny secret API key). No third-party Python packages - standard library only. Read-only: the bundled client can only call Canny's list/retrieve endpoints."
metadata:
  author: Francois Taljaard
  version: "2026.10"
  domain: Canny - product feedback / ticket tracking
---

# Canny Tickets — read-only review & reporting

Helps developers review the team's Canny tickets without opening the Canny UI: list and filter
**bugs** and **RFCs** (which live on separate boards), read a post with its comments, and build quick
status reports. The rule that makes it safe: **this skill only reads Canny — never writes.** The
bundled client (`scripts/canny.py`) physically cannot create, edit, close, merge, comment on, or
re-tag anything; it only calls Canny's `list` and `retrieve` endpoints.

## 1. Route the request

| Request looks like | Go to |
|---|---|
| "what bugs are open", "show the RFC board", "in-progress items", filter/search tickets | § 4 List & filter |
| "summarise post X", a Canny URL or post id, "what are people saying on …" | § 5 Read one post |
| "how many open vs in progress", "what changed this week", a roll-up or weekly review | § 6 Report |
| "review the changelog / release notes", "are all the changes attached", "check the Release 7.3 draft" | § 7 Changelog review |
| "what boards / tags / categories exist" | `canny.py boards` / `tags` / `categories` |
| create a ticket, change a status, reply, close, merge, re-tag, add to changelog | **§ 2 — not supported.** |

## 2. Ground rules

- **Read-only, no exceptions.** This skill reviews and reports; it does not change Canny. If the user
  asks to create, edit, close, merge, comment, change status, or re-tag a ticket, say the skill is
  read-only by design and point them to the Canny UI (or note the skill could be extended — see
  `MAINTENANCE.md`). Do not try to do it with curl or another tool. The client enforces this: its
  endpoint allowlist is `list`/`retrieve` only.
- **Never print or echo the API key.** It lives only in `CANNY_API_KEY`. Don't put it in commands you
  show the user, in files, in URLs, or in output. If it's missing, the script says how to set it — relay
  that, don't ask the user to paste the key into the chat.
- **Report what Canny returns, don't invent.** Statuses, scores, vote and comment counts, ETAs — use the
  values from the API. If a field is empty (no ETA, no category, anonymous author), say so plainly rather
  than guessing.
- **Bugs and RFCs are separate boards.** Resolve the right board by name first (`canny.py boards`). If a
  request is ambiguous about which board, ask or run both and label each. Board names are account-specific —
  discover them, don't assume them.
- **Respect the data.** Comments marked internal/private are shown by the tool for the team's own review;
  don't surface them outside the team or paste them somewhere public.
- **Mind rate limits.** The client backs off on HTTP 429 automatically. For big sweeps prefer one
  `report`/`posts --limit N` call over many small ones.

## 3. Setup (once per environment)

The key is a **secret** Canny API key from **Canny → Settings → API**. It must be in the environment
before any command runs:

```bash
# PowerShell (this is a Windows box)
$env:CANNY_API_KEY = '<your-canny-secret-key>'
```

```bash
# bash / CI
export CANNY_API_KEY='<your-canny-secret-key>'
```

Never commit the key or write it into the repo. All commands below assume it is set.

## 4. List & filter

Run `scripts/canny.py posts` with the filters the request implies.

1. **Pin the board.** Bugs vs RFC → pass `--board "Bugs"` or `--board "Feature Requests"` (name match is
   case-insensitive and partial). Unsure of names? `python scripts/canny.py boards` first.
2. **Pin the filter.** Map the ask to flags:
   - status → `--status open` or a comma list `--status "in progress,planned"`
     (valid: `open`, `under review`, `planned`, `in progress`, `complete`, `closed`, or the team's custom statuses)
   - text → `--search "login"`; tag → `--tag "regression"`; author → `--author <userID>`
   - recency → `--since 2026-09-01` (filters on created date); ordering → `--sort score|trending|newest|statusChanged`
   - size → `--limit 50` (paginates automatically up to the limit)
3. **Deliver** the table the tool prints (score · status · comments · created · title), then a one-line
   read: how many, the notable ones, anything stale or high-score-but-still-open. Add `--json` when you
   need to post-process; otherwise the table is enough.

```bash
python scripts/canny.py posts --board Bugs --status open --sort score --limit 50
python scripts/canny.py posts --board "Feature Requests" --status "planned,in progress" --since 2026-09-01
```

## 5. Read one post

Given a post id or a `canny.io` URL (the `urlName` is the slug at the end of the URL):

```bash
python scripts/canny.py post <postID>
python scripts/canny.py post <url-slug> --by-url-name
python scripts/canny.py comments --post <postID>
```

`post` prints title, status, score, board, category, tags, author, dates, ETA, URL and the full details.
Add `comments` for the discussion. Summarise for the developer: what the issue/request is, where it
stands, and the gist of the comments — quote sparingly.

## 6. Report

For roll-ups and weekly reviews use `report` (counts by status + top items by score):

```bash
python scripts/canny.py report --board Bugs
python scripts/canny.py report --board "Feature Requests" --since 2026-09-01
python scripts/canny.py status-changes --board Bugs --limit 50   # what moved recently
```

Deliver the status breakdown, call out the backlog shape (e.g. how many open vs in progress), and list
the top few by score. For "what changed this week", combine `status-changes` with `--since`. Offer the
`--json` output if the user wants it in a doc or spreadsheet.

## 7. Changelog review

Reviews a release changelog against Canny — read-only. The team's changelog groups changes by component
(`# Database`, `# Process App`, …), one line each: `- ` + `` `type` `` + description + `([details](link))`
where the link is the Canny ticket and `type` is `new` / `change` / `fix` / `improvement`.

```bash
python scripts/canny.py changelog --entry "Release 7.3"      # pull body + linked posts from Canny
python scripts/canny.py changelog --file notes.md            # review a local draft
python scripts/canny.py changelog --file notes.md --entry "Release 7.3"   # draft + attach cross-check
```

The review checks, and the rule it enforces is **every change is documented AND attached**:

- **Attached ↔ documented** — every ticket in the body is in the entry's linked posts, and every linked
  post has a line in the body. A gap either way is an error (an undocumented attachment, or a line whose
  ticket won't show as attached).
- **Links resolve** — each `([details](…))` points to a real Canny post.
- **Status** — each linked ticket is `complete` (warns otherwise — don't ship notes for unfinished work).
- **Format** — valid `type` tag present; flags unknown tags, missing tags, and duplicate ticket links.
- **Type/board sanity** — a Bugs ticket tagged `new`/`change`, or a non-bug tagged `fix` (info only).

Deliver the findings grouped by severity (errors first), then tell the user plainly what to fix in Canny
(the API can't attach posts to an existing entry — see § 2 — so fixes to linked posts happen in the UI).

Note: Canny's API returns a broken `url` (`…/p/undefined`) for an entry's linked posts, so the review
matches tickets by **post id**, resolving each body link via `posts/retrieve`. Expect one retrieve call
per distinct link (cached), which the rate-limit backoff handles.

## 8. Layout

```
scripts/canny.py       read-only Canny API client (stdlib only); subcommands: boards, posts, post,
                       comments, votes, status-changes, tags, categories, report, changelog
scripts/README.md      quick command reference
references/api/        INDEX.md + read-endpoints.md (endpoint catalog, object fields, statuses, limits)
evals/evals.json       test prompts per capability
MAINTENANCE.md         refresh the API reference; how (and whether) to add write capabilities later
```

Read `references/api/INDEX.md` when you need exact field names or endpoint behaviour; the CLI covers the
day-to-day asks without it.
