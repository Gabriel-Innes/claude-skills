# References index

One folder per domain; each has its own `INDEX.md` with sources, verified dates and known limits per file. Read
that index first, then open only what the request needs.

| Folder | Product | Covers | Verified |
|---|---|---|---|
| `core-api/` | **Cin7 Core** (formerly DEAR Inventory), API v2 | Extraction of the Cin7 Core developer portal: protocol basics (`api-basics.md`), a review checklist (`common-mistakes.md`), the endpoint catalogue (`endpoints.md`, 295 actions), the status and value lists (`enums.md`) and one generated file per portal group (`groups/`, 33 files with field tables, parameters, request and response bodies) | 2026-10-07 |

Nothing is bundled for **Cin7 Omni**.

Every file carries a provenance header:

```
<!-- source: <URL or document> | version: <Cin7 product and version, or "not stated"> | verified: YYYY-MM-DD -->
```

See `MAINTENANCE.md` for the conventions and how to regenerate `core-api/`.
