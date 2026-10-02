#!/usr/bin/env python3
"""
canny.py - READ-ONLY command-line client for the Canny API.

Purpose: let developers review Canny tickets (bugs and RFCs) and build reports
without touching the Canny UI. This client is deliberately read-only: it can
ONLY call Canny's /list and /retrieve endpoints. There is no code path that
creates, updates, deletes, merges, changes status, or posts comments. Even if
asked to, it cannot modify anything in Canny.

Auth: reads the secret key from the CANNY_API_KEY environment variable. The key
is never printed, logged, or written to disk.

API docs: https://developers.canny.io/api-reference

Usage examples:
    python canny.py boards
    python canny.py posts --board "Bugs" --status open --sort score --limit 50
    python canny.py posts --board "Feature Requests" --status "in progress,planned"
    python canny.py posts --board Bugs --since 2026-09-01 --json
    python canny.py post 553c3ef8b8cdcd1501ba1234
    python canny.py comments --post 553c3ef8b8cdcd1501ba1234
    python canny.py report --board Bugs
    python canny.py tags --board Bugs
    python canny.py categories --board Bugs

Every subcommand supports --json to emit raw API JSON for further processing.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_BASE = "https://canny.io/api"

# The ONLY endpoints this client is allowed to call. All are read-only.
# This allowlist is the enforcement point for the read-only guarantee:
# the request helper refuses any path not listed here.
ALLOWED_ENDPOINTS = {
    "/v1/boards/list",
    "/v1/boards/retrieve",
    "/v1/posts/list",
    "/v1/posts/retrieve",
    "/v2/comments/list",
    "/v1/comments/retrieve",
    "/v1/votes/list",
    "/v1/votes/retrieve",
    "/v1/status_changes/list",
    "/v1/entries/list",
    "/v1/categories/list",
    "/v1/categories/retrieve",
    "/v1/tags/list",
    "/v1/tags/retrieve",
    "/v2/users/list",
}


class CannyError(Exception):
    pass


def get_api_key():
    key = os.environ.get("CANNY_API_KEY", "").strip()
    if not key:
        raise CannyError(
            "CANNY_API_KEY is not set. Export your Canny secret API key first, e.g.\n"
            "  PowerShell:  $env:CANNY_API_KEY = '<your-key>'\n"
            "  bash:        export CANNY_API_KEY='<your-key>'\n"
            "Find the key in Canny: Settings -> API. Keep it secret; never commit it."
        )
    return key


def call(endpoint, params=None, max_retries=4):
    """POST to a read-only Canny endpoint and return parsed JSON.

    Refuses any endpoint not in ALLOWED_ENDPOINTS. Handles rate limiting (429)
    with Retry-After backoff.
    """
    if endpoint not in ALLOWED_ENDPOINTS:
        raise CannyError(
            f"Refusing to call '{endpoint}': this client is read-only and only "
            f"permits {sorted(ALLOWED_ENDPOINTS)}."
        )

    body = dict(params or {})
    body["apiKey"] = get_api_key()

    # Arrays (e.g. tagIDs) must be sent as repeated/encoded fields; Canny accepts
    # JSON-encoded array values in form fields, so encode lists as JSON strings.
    encoded = {}
    for k, v in body.items():
        if isinstance(v, (list, tuple)):
            encoded[k] = json.dumps(list(v))
        elif isinstance(v, bool):
            encoded[k] = "true" if v else "false"
        elif v is None:
            continue
        else:
            encoded[k] = str(v)

    data = urllib.parse.urlencode(encoded).encode("utf-8")
    url = API_BASE + endpoint

    attempt = 0
    while True:
        attempt += 1
        req = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt <= max_retries:
                retry_after = e.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else min(2 ** attempt, 30)
                time.sleep(wait)
                continue
            detail = ""
            try:
                detail = e.read().decode("utf-8")
            except Exception:
                pass
            # Never surface the API key in errors.
            raise CannyError(f"HTTP {e.code} from {endpoint}: {detail[:500]}")
        except urllib.error.URLError as e:
            if attempt <= max_retries:
                time.sleep(min(2 ** attempt, 15))
                continue
            raise CannyError(f"Network error calling {endpoint}: {e.reason}")


def paginate_posts(params, hard_limit):
    """Fetch posts across pages (v1 skip/limit) up to hard_limit rows."""
    out = []
    skip = 0
    page = 100  # Canny max page size for posts
    while len(out) < hard_limit:
        want = min(page, hard_limit - len(out))
        resp = call("/v1/posts/list", {**params, "limit": want, "skip": skip})
        posts = resp.get("posts", [])
        out.extend(posts)
        if not resp.get("hasMore") or not posts:
            break
        skip += len(posts)
    return out[:hard_limit]


def resolve_board(name_or_id):
    """Return a board dict matching a board id or (case-insensitive) name."""
    resp = call("/v1/boards/list")
    boards = resp.get("boards", [])
    for b in boards:
        if b.get("id") == name_or_id:
            return b
    lowered = name_or_id.lower()
    matches = [b for b in boards if b.get("name", "").lower() == lowered]
    if not matches:
        matches = [b for b in boards if lowered in b.get("name", "").lower()]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        names = ", ".join(repr(b.get("name")) for b in boards) or "(none)"
        raise CannyError(f"No board matching {name_or_id!r}. Available boards: {names}")
    names = ", ".join(repr(b.get("name")) for b in matches)
    raise CannyError(f"Board {name_or_id!r} is ambiguous; matches: {names}")


def parse_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        raise CannyError(f"Bad date {s!r}; use YYYY-MM-DD.")


def post_created(p):
    v = p.get("created")
    if not v:
        return None
    try:
        return datetime.fromisoformat(v.replace("Z", "+00:00"))
    except ValueError:
        return None


def short_date(iso):
    return (iso or "")[:10]


def emit(obj, as_json):
    if as_json:
        print(json.dumps(obj, indent=2, ensure_ascii=False))
        return True
    return False


# ---- subcommands -----------------------------------------------------------

def cmd_boards(args):
    resp = call("/v1/boards/list")
    if emit(resp, args.json):
        return
    boards = resp.get("boards", [])
    if not boards:
        print("No boards found.")
        return
    width = max(len(b.get("name", "")) for b in boards)
    print(f"{'NAME':<{width}}  {'POSTS':>6}  PRIVATE  ID")
    for b in sorted(boards, key=lambda x: x.get("name", "")):
        print(
            f"{b.get('name',''):<{width}}  {b.get('postCount',0):>6}  "
            f"{str(b.get('isPrivate', False)):<7}  {b.get('id','')}"
        )


def cmd_posts(args):
    params = {}
    board = None
    if args.board:
        board = resolve_board(args.board)
        params["boardID"] = board["id"]
    if args.status:
        params["status"] = args.status
    if args.search:
        params["search"] = args.search
    if args.sort:
        params["sort"] = args.sort
    if args.author:
        params["authorID"] = args.author
    if args.tag:
        # resolve tag names to IDs on the board when possible
        params["tagIDs"] = _resolve_tag_ids(args.tag, board["id"] if board else None)

    posts = paginate_posts(params, args.limit)

    if args.since:
        cutoff = parse_date(args.since)
        posts = [p for p in posts if (post_created(p) or cutoff) >= cutoff]

    if args.exclude_tag:
        drop = {t.strip().lower() for t in args.exclude_tag.split(",") if t.strip()}
        posts = [p for p in posts
                 if not ({(t.get("name") or "").lower() for t in p.get("tags", [])} & drop)]

    if emit({"posts": posts, "count": len(posts)}, args.json):
        return
    _print_post_table(posts)


def _resolve_tag_ids(names, board_id):
    params = {"boardID": board_id} if board_id else {}
    resp = call("/v1/tags/list", params)
    tags = resp.get("tags", [])
    wanted = [n.strip().lower() for n in names.split(",") if n.strip()]
    ids = []
    for w in wanted:
        hit = next((t for t in tags if t.get("name", "").lower() == w), None)
        if not hit:
            raise CannyError(f"No tag named {w!r} on this board.")
        ids.append(hit["id"])
    return ids


def _print_post_table(posts):
    if not posts:
        print("No matching posts.")
        return
    print(f"{'SCORE':>5}  {'STATUS':<12}  {'CMTS':>4}  {'CREATED':<10}  TITLE")
    for p in posts:
        title = (p.get("title") or "").replace("\n", " ")
        if len(title) > 70:
            title = title[:67] + "..."
        print(
            f"{p.get('score',0):>5}  {(p.get('status') or ''):<12}  "
            f"{p.get('commentCount',0):>4}  {short_date(p.get('created')):<10}  {title}"
        )
    print(f"\n{len(posts)} post(s).")


def cmd_post(args):
    key = "urlName" if args.by_url_name else "id"
    resp = call("/v1/posts/retrieve", {key: args.id})
    if emit(resp, args.json):
        return
    p = resp
    print(f"Title:   {p.get('title')}")
    print(f"Status:  {p.get('status')}   Score: {p.get('score')}   "
          f"Comments: {p.get('commentCount')}")
    board = p.get("board") or {}
    cat = p.get("category") or {}
    print(f"Board:   {board.get('name')}   Category: {cat.get('name') or '-'}")
    tags = ", ".join(t.get("name", "") for t in p.get("tags", [])) or "-"
    print(f"Tags:    {tags}")
    author = p.get("author") or {}
    print(f"Author:  {author.get('name') or 'anonymous'}")
    print(f"Created: {short_date(p.get('created'))}   "
          f"ETA: {p.get('eta') or '-'}")
    print(f"URL:     {p.get('url')}")
    print("\nDetails:\n" + (p.get("details") or "(none)"))


def cmd_comments(args):
    resp = call("/v2/comments/list", {"postID": args.post, "limit": args.limit})
    if emit(resp, args.json):
        return
    comments = resp.get("comments", [])
    if not comments:
        print("No comments.")
        return
    for c in comments:
        who = (c.get("author") or {}).get("name", "?")
        flag = " [internal]" if c.get("internal") or c.get("private") else ""
        print(f"- {short_date(c.get('created'))} {who}{flag}: "
              f"{(c.get('value') or '').strip()}")


def cmd_votes(args):
    resp = call("/v1/votes/list", {"postID": args.post, "limit": args.limit})
    if emit(resp, args.json):
        return
    votes = resp.get("votes", [])
    print(f"{len(votes)} vote(s) on post {args.post}.")
    for v in votes:
        voter = (v.get("voter") or {}).get("name", "?")
        print(f"- {short_date(v.get('created'))}  {voter}")


def cmd_status_changes(args):
    params = {"limit": args.limit}
    if args.board:
        params["boardID"] = resolve_board(args.board)["id"]
    resp = call("/v1/status_changes/list", params)
    if emit(resp, args.json):
        return
    changes = resp.get("statusChanges", [])
    if not changes:
        print("No status changes.")
        return
    for ch in changes:
        post = (ch.get("post") or {}).get("title", "?")
        print(f"- {short_date(ch.get('created'))}  -> {ch.get('status'):<12}  {post}")


def cmd_tags(args):
    params = {}
    if args.board:
        params["boardID"] = resolve_board(args.board)["id"]
    resp = call("/v1/tags/list", params)
    if emit(resp, args.json):
        return
    tags = resp.get("tags", [])
    for t in sorted(tags, key=lambda x: x.get("name", "")):
        print(f"{t.get('postCount',0):>5}  {t.get('name','')}  ({t.get('id')})")


def cmd_categories(args):
    params = {}
    if args.board:
        params["boardID"] = resolve_board(args.board)["id"]
    resp = call("/v1/categories/list", params)
    if emit(resp, args.json):
        return
    cats = resp.get("categories", [])
    for c in sorted(cats, key=lambda x: x.get("name", "")):
        print(f"{c.get('postCount',0):>5}  {c.get('name','')}  ({c.get('id')})")


def cmd_report(args):
    """Roll-up of a board: post counts by status, plus the top items by score."""
    board = resolve_board(args.board) if args.board else None
    params = {"boardID": board["id"]} if board else {}
    posts = paginate_posts(params, args.limit)

    if args.since:
        cutoff = parse_date(args.since)
        posts = [p for p in posts if (post_created(p) or cutoff) >= cutoff]

    by_status = {}
    for p in posts:
        by_status.setdefault(p.get("status") or "unknown", []).append(p)

    report = {
        "board": board["name"] if board else "(all boards)",
        "total": len(posts),
        "since": args.since,
        "byStatus": {k: len(v) for k, v in sorted(by_status.items())},
    }
    if emit(report, args.json):
        return

    print(f"Report: {report['board']}"
          + (f"  (since {args.since})" if args.since else ""))
    print(f"Total posts: {report['total']}\n")
    print("By status:")
    for status, items in sorted(by_status.items(), key=lambda kv: -len(kv[1])):
        print(f"  {len(items):>4}  {status}")
    print("\nTop by score:")
    for p in sorted(posts, key=lambda x: x.get("score", 0), reverse=True)[:args.top]:
        title = (p.get("title") or "")[:60]
        print(f"  {p.get('score',0):>5}  [{p.get('status','')}]  {title}")


# ---- changelog review ------------------------------------------------------

KNOWN_TYPES = {"new", "change", "fix", "improvement", "deprecate", "remove"}
LINK_RE = re.compile(r"\(\[[^\]]*\]\((?P<url>[^)]+)\)\)")
# a canny post URL: https://<co>.canny.io/<boardSlug>/p/<urlName>
POST_URL_RE = re.compile(r"https?://[^/]+/(?P<slug>[^/]+)/p/(?P<urlname>[^/?#)]+)", re.I)
BULLET_RE = re.compile(r"^\s*[-*]\s+(?:`(?P<type>[^`]+)`\s+)?(?P<rest>.*)$")
HEADER_RE = re.compile(r"^\s*#{1,6}\s+(?P<title>.+?)\s*$")


def url_name_from_url(url):
    m = POST_URL_RE.search(url or "")
    return (m.group("urlname").lower(), m.group("slug").lower()) if m else (None, None)


def resolve_entry(name_or_id, limit=200):
    """Find a changelog entry by id or (case-insensitive) title via entries/list."""
    skip = 0
    found = []
    while True:
        resp = call("/v1/entries/list", {"limit": 100, "skip": skip})
        entries = resp.get("entries", [])
        found.extend(entries)
        if not resp.get("hasMore") or not entries or len(found) >= limit:
            break
        skip += len(entries)
    for e in found:
        if e.get("id") == name_or_id:
            return e
    lowered = name_or_id.lower()
    exact = [e for e in found if (e.get("title") or "").lower() == lowered]
    if len(exact) == 1:
        return exact[0]
    partial = [e for e in found if lowered in (e.get("title") or "").lower()]
    if len(partial) == 1:
        return partial[0]
    titles = ", ".join(repr(e.get("title")) for e in (exact or partial or found))
    if not (exact or partial):
        raise CannyError(f"No changelog entry matching {name_or_id!r}. Entries: {titles}")
    raise CannyError(f"Entry {name_or_id!r} is ambiguous; matches: {titles}")


def parse_changelog_body(markdown):
    """Return list of change lines: {group, type, desc, url, urlname, line_no, has_link}."""
    lines = []
    group = None
    for i, raw in enumerate(markdown.splitlines(), start=1):
        h = HEADER_RE.match(raw)
        if h:
            group = h.group("title")
            continue
        b = BULLET_RE.match(raw)
        if not b:
            continue
        rest = b.group("rest")
        link = LINK_RE.search(rest)
        url = link.group("url") if link else None
        urlname, slug = url_name_from_url(url) if url else (None, None)
        desc = LINK_RE.sub("", rest).strip() if link else rest.strip()
        lines.append({
            "group": group,
            "type": (b.group("type") or "").strip().lower() or None,
            "desc": desc,
            "url": url,
            "urlname": urlname,
            "slug": slug,
            "line_no": i,
            "has_link": bool(url),
        })
    return lines


def board_slug_map():
    """Map a board's URL slug -> board dict, for resolving links by board."""
    resp = call("/v1/boards/list")
    out = {}
    for b in resp.get("boards", []):
        slug = (b.get("url") or "").rstrip("/").rsplit("/", 1)[-1].lower()
        if slug:
            out[slug] = b
    return out


def cmd_changelog(args):
    # 1. Get the body and (optionally) the entry's linked posts.
    entry = None
    if args.entry:
        entry = resolve_entry(args.entry)
    if args.file:
        with open(args.file, "r", encoding="utf-8") as fh:
            body = fh.read()
    elif entry:
        body = entry.get("markdownDetails") or entry.get("plaintextDetails") or ""
    else:
        raise CannyError("Provide --entry <title|id> and/or --file <path.md>.")

    change_lines = parse_changelog_body(body)

    # The entry's linked posts, keyed by post id. (Canny returns a broken url
    # for linked posts, so id is the only reliable cross-check key.)
    attached_by_id = {}
    if entry:
        for p in entry.get("posts", []):
            if p.get("id"):
                attached_by_id[p["id"]] = p

    findings = []

    def add(sev, msg, line_no=None):
        findings.append({"severity": sev, "message": msg, "line": line_no})

    # 2. Per-line checks. Resolve each body link to a post id so we can compare
    #    against the entry's attached ids.
    seen = {}               # urlName -> [line numbers]
    resolved_ids = set()    # post ids documented in the body
    resolve_cache = {}      # urlName -> resolved post (or None)
    slugs = None            # lazy board slug map
    for cl in change_lines:
        ln = cl["line_no"]
        if not cl["has_link"]:
            add("error", f"Change line has no ([details](...)) link: {cl['desc'][:70]!r}", ln)
            continue
        if cl["type"] and cl["type"] not in KNOWN_TYPES:
            add("warn", f"Unknown type tag `{cl['type']}` (expected {sorted(KNOWN_TYPES)})", ln)
        if not cl["type"]:
            add("warn", f"Change line has no `type` tag: {cl['desc'][:60]!r}", ln)
        un = cl["urlname"]
        if not un:
            add("error", f"Link is not a recognizable Canny post URL: {cl['url']}", ln)
            continue
        seen.setdefault(un, []).append(ln)

        if un in resolve_cache:
            resolved = resolve_cache[un]
        else:
            try:
                if slugs is None:
                    slugs = board_slug_map()
                params = {"urlName": un}
                board = slugs.get(cl["slug"])
                if board:
                    params["boardID"] = board["id"]
                resolved = call("/v1/posts/retrieve", params)
            except CannyError:
                resolved = None
            resolve_cache[un] = resolved

        if resolved is None:
            add("error", f"Ticket link does not resolve to a real post: {cl['url']}", ln)
            continue

        pid = resolved.get("id")
        if pid:
            resolved_ids.add(pid)

        if entry is not None and pid not in attached_by_id:
            add("error",
                f"Ticket '{resolved.get('title','?')}' is in the changelog text but "
                f"NOT attached to the entry (add it to the entry's linked posts)", ln)

        status = resolved.get("status")
        if status and status != "complete":
            add("warn",
                f"Linked ticket '{resolved.get('title','?')}' status is "
                f"'{status}', not 'complete'", ln)

        # type vs board sanity
        board_name = (resolved.get("board") or {}).get("name", "").lower()
        if cl["type"] == "fix" and board_name and "bug" not in board_name:
            add("info", f"'{resolved.get('title','?')}' tagged `fix` but is on "
                        f"board '{board_name}'", ln)
        if cl["type"] in ("new", "change", "improvement") and "bug" in board_name:
            add("info", f"'{resolved.get('title','?')}' tagged `{cl['type']}` but is "
                        f"on the Bugs board", ln)

    # 3. Duplicates (same ticket on multiple lines).
    for un, lns in seen.items():
        if len(lns) > 1:
            add("warn", f"Ticket {un} linked on multiple lines: {lns}")

    # 4. Attached but undocumented (entry has a linked post with no body line).
    if entry:
        for pid, p in attached_by_id.items():
            if pid not in resolved_ids:
                add("error",
                    f"Post '{p.get('title','?')}' is attached to the entry but has NO line "
                    f"in the changelog text")

    summary = {
        "entry": entry.get("title") if entry else None,
        "status": entry.get("status") if entry else None,
        "source": args.file or f"entry:{args.entry}",
        "changeLines": len(change_lines),
        "linkedPosts": len(attached_by_id) if entry else None,
        "errors": sum(1 for f in findings if f["severity"] == "error"),
        "warnings": sum(1 for f in findings if f["severity"] == "warn"),
        "info": sum(1 for f in findings if f["severity"] == "info"),
    }

    if emit({"summary": summary, "findings": findings}, args.json):
        return

    title = entry.get("title") if entry else args.file
    print(f"Changelog review: {title}"
          + (f"  [{entry.get('status')}]" if entry else ""))
    print(f"Change lines: {summary['changeLines']}"
          + (f"   Linked posts on entry: {summary['linkedPosts']}" if entry else ""))
    print(f"Errors: {summary['errors']}   Warnings: {summary['warnings']}   "
          f"Info: {summary['info']}")
    if not entry:
        print("Note: no --entry given, so attachment to a changelog entry was NOT checked.")
    print()
    if not findings:
        print("Clean — every change line links to a complete, attached ticket.")
        return
    marks = {"error": "[X]", "warn": "[!]", "info": "[i]"}
    for f in sorted(findings, key=lambda x: {"error": 0, "warn": 1, "info": 2}[x["severity"]]):
        loc = f"L{f['line']}: " if f.get("line") else ""
        print(f"  {marks[f['severity']]} {loc}{f['message']}")


def build_parser():
    p = argparse.ArgumentParser(
        description="Read-only Canny API client for reviewing tickets (bugs & RFCs).",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_json(sp):
        sp.add_argument("--json", action="store_true", help="emit raw JSON")

    sp = sub.add_parser("boards", help="list all boards")
    add_json(sp)
    sp.set_defaults(func=cmd_boards)

    sp = sub.add_parser("posts", help="list/filter posts on a board")
    sp.add_argument("--board", help="board name or id")
    sp.add_argument("--status", help="comma-separated: open,under review,planned,"
                                     "in progress,complete,closed, or custom")
    sp.add_argument("--tag", help="comma-separated tag names to include")
    sp.add_argument("--exclude-tag", help="comma-separated tag names to exclude")
    sp.add_argument("--author", help="authorID")
    sp.add_argument("--search", help="full-text search within the board")
    sp.add_argument("--sort", choices=["newest", "oldest", "relevance", "score",
                                       "statusChanged", "trending"], default="newest")
    sp.add_argument("--since", help="only posts created on/after YYYY-MM-DD")
    sp.add_argument("--limit", type=int, default=50, help="max posts (default 50)")
    add_json(sp)
    sp.set_defaults(func=cmd_posts)

    sp = sub.add_parser("post", help="retrieve one post by id (or --by-url-name)")
    sp.add_argument("id")
    sp.add_argument("--by-url-name", action="store_true",
                    help="treat the argument as a urlName instead of an id")
    add_json(sp)
    sp.set_defaults(func=cmd_post)

    sp = sub.add_parser("comments", help="list comments on a post")
    sp.add_argument("--post", required=True, help="postID")
    sp.add_argument("--limit", type=int, default=50)
    add_json(sp)
    sp.set_defaults(func=cmd_comments)

    sp = sub.add_parser("votes", help="list votes on a post")
    sp.add_argument("--post", required=True, help="postID")
    sp.add_argument("--limit", type=int, default=100)
    add_json(sp)
    sp.set_defaults(func=cmd_votes)

    sp = sub.add_parser("status-changes", help="list recent status changes")
    sp.add_argument("--board", help="board name or id")
    sp.add_argument("--limit", type=int, default=50)
    add_json(sp)
    sp.set_defaults(func=cmd_status_changes)

    sp = sub.add_parser("tags", help="list tags (optionally on a board)")
    sp.add_argument("--board", help="board name or id")
    add_json(sp)
    sp.set_defaults(func=cmd_tags)

    sp = sub.add_parser("categories", help="list categories (optionally on a board)")
    sp.add_argument("--board", help="board name or id")
    add_json(sp)
    sp.set_defaults(func=cmd_categories)

    sp = sub.add_parser("report", help="status roll-up + top posts for a board")
    sp.add_argument("--board", help="board name or id")
    sp.add_argument("--since", help="only posts created on/after YYYY-MM-DD")
    sp.add_argument("--limit", type=int, default=500, help="max posts to scan")
    sp.add_argument("--top", type=int, default=10, help="top-N by score to show")
    add_json(sp)
    sp.set_defaults(func=cmd_report)

    sp = sub.add_parser("changelog", help="review a changelog entry or .md draft: "
                                          "links resolve, tickets complete & attached")
    sp.add_argument("--entry", help="changelog entry title or id (pulls body + linked posts)")
    sp.add_argument("--file", help="path to a .md changelog draft to review")
    add_json(sp)
    sp.set_defaults(func=cmd_changelog)

    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        args.func(args)
    except CannyError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
