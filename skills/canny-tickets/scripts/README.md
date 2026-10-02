# canny.py — quick reference

Read-only Canny client. Python 3.8+, standard library only. Needs `CANNY_API_KEY` in the environment.

```bash
# PowerShell
$env:CANNY_API_KEY = '<secret-key>'
# bash
export CANNY_API_KEY='<secret-key>'
```

## Commands

| Command | What it does |
|---|---|
| `canny.py boards` | list boards (name, post count, private, id) |
| `canny.py posts --board Bugs [--status …] [--tag …] [--search …] [--sort …] [--since …] [--limit N]` | list/filter tickets |
| `canny.py post <id>` / `post <slug> --by-url-name` | one ticket in full |
| `canny.py comments --post <id>` | comments on a ticket |
| `canny.py votes --post <id>` | votes on a ticket |
| `canny.py status-changes [--board …] [--limit N]` | recent status moves |
| `canny.py tags [--board …]` / `categories [--board …]` | tags / categories |
| `canny.py report --board Bugs [--since …]` | status roll-up + top by score |
| `canny.py changelog --entry "Release 7.3"` | review a changelog entry (links resolve, tickets complete & attached) |
| `canny.py changelog --file notes.md [--entry …]` | review a local changelog draft |

Add `--json` to any command for raw API JSON.

`--status` takes a comma list: `open`, `under review`, `planned`, `in progress`, `complete`, `closed`,
or the team's custom statuses. `--sort`: `newest`, `oldest`, `relevance`, `score`, `statusChanged`,
`trending`.

## Read-only guarantee

The client's `ALLOWED_ENDPOINTS` set contains only `/list` and `/retrieve` paths. There is no function
that calls a write endpoint. It cannot create, edit, close, merge, comment on, or re-tag anything.
