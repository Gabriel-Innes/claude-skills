# Security & data-accuracy reporting

These skills generate SQL and C# that consultants may run against **production ERP databases**, so both
genuine security issues and **wrong reference data** are treated seriously here.

## What to report

- A skill that produces code which **writes to or could corrupt** vendor-owned tables (these skills are meant
  to be read-only against vendor data; a write path that isn't the vendor's API/SDK is a bug).
- A **factual error in a bundled reference** — a wrong field name, enum value, key, version requirement or SDK
  signature — that could cause a consultant to ship incorrect code or a bad query.
- Anything in `scripts/` that could be unsafe to run (shell/SQL injection, destructive file operations).
- Accidentally committed **secrets** or **vendor source material** that shouldn't be in the repo.

## How to report

- For a **non-sensitive** data error, open a normal GitHub issue with the file, the line, and your source.
- For anything **sensitive** (a security flaw, or a correctness bug whose exploitation you'd rather not post
  publicly), use **GitHub's private vulnerability reporting** on this repository
  (Security → *Report a vulnerability*) instead of a public issue.

Please include the skill, the file and line, what you observed, what you expected, and — for a data
correction — the vendor document or page (with its date) that supports the fix. There is no formal SLA on this
community project, but reports are reviewed as quickly as practical.

## Scope and expectations

- This repository ships **reference data and code generators**, not a running service, so the surface is the
  correctness and safety of what a skill tells Claude to do.
- The references are **point-in-time** and cover specific product versions (stated in each skill's `README`
  row and disclaimers). Always verify generated SQL/C# against the vendor's own documentation and against the
  client's actual database before running it in production — the skills are a lookup aid, not a substitute for
  that verification.
