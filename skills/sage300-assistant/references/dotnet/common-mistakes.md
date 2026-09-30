<!-- source: distilled from real Sage 300 .NET integrations + the correct idioms in view-api.md | version: version-independent | verified: 2026-09-25 -->

# Sage 300 .NET (ACCPAC.Advantage) — common mistakes and the correct way

Recurring anti-patterns seen in real ACCPAC.Advantage integrations, each with the fix. When generating or
reviewing C#, avoid the left column and produce the right. These are the things that make an integration leak
seats, hide the real Sage error, or silently corrupt documents.

## Lifecycle & resources

- **SignOn in a constructor.** `new SomeModule()` opening a Sage session as a construction side effect couples
  object creation to a live connection, surfaces failures from `new`, and makes testing/DI impossible.
  → Open the session **explicitly** (a factory method or the disposable `Sage300Session` wrapper in
  `view-api.md` § 6b). Construction should not connect.

- **No deterministic disposal.** A manual `Close()` that nothing calls in a `finally`, and no `IDisposable`,
  leaks views, the DBLink, the session **and a licence seat** on every success and every exception path.
  → Implement `IDisposable`; wrap usage in `using`/`try-finally`; dispose in **reverse order: views → DBLink →
  session**. Never rely on the finalizer to release seats.

- **Opening the same document's views in two places.** A shared "base" that composes a document one way and a
  module that re-composes it another way = two sources of truth that drift.
  → One owner per document composes its own views once. Delete dead/duplicate compose variants (e.g. left-over
  version-specific copies) — they rot and hide bugs (wrong rotoIDs, unopened views referenced in `Compose`).

- **Hard-coded `Init` version string** (`"65A"`, `"72A"`, …). It tracks the installed System Manager and breaks
  on upgrade. → Read it from **config**, confirmed against the install (§ 7 of `view-api.md`).

- **Hard-coded credentials/company.** → From secure config; remember API creds are **case-sensitive**.

## Correctness against the View API

- **Guessing rotoIDs or `Compose()` order.** The compose array order is fixed per view and not in the data
  dictionary; a wrong slot silently corrupts documents. A plausible guess reads as fact.
  → **Macro-record** the operation in the Sage desktop and translate it (`view-api.md` § 7); verify field names
  and single-table rotoIDs against the dictionary; mark anything unconfirmed as `TODO(verify)`.

- **Unverified view-role assumptions.** Assuming "detail-view slot 3 is lots, slot 4 is serials" because another
  document happened to be wired that way. → Confirm each composed view's role from the recorded macro / that
  view's own definition, not by analogy.

- **`Update()` without reading first**, or branching on `Exists` without checking the `Read` return. → Set key +
  `Order`, `Read(false)`, check the return/`Exists`, then modify and `Update()`.

- **Detail lines keyed to sequence `0` in a loop** — inserts them in reverse. → Increment the line-sequence key.

- **`Read(true)` outside a transaction** — throws. → Use `Read(false)` unless inside `TransactionBegin/Commit`.

- **Magic numbers** for status / function / process-command / line-type (`STATUS=2`, `FUNCTION=10`,
  `PROCESSCMD=1`, `SLITEM=1/2/3`, `OECOMMAND=4`). → Named `const`/`enum` with the meaning; don't reuse the same
  literal for two concepts.

- **Ignoring optional fields.** Works on sample data, fails where the customer configured required optional
  fields. → Handle them (`view-api.md` § 6).

## Error handling

- **Lossy catch-and-rethrow:** `catch (Exception ex) { throw new Exception(ex.Message); }` discards the type,
  stack and inner exception. → `throw;` to rethrow, or `throw new SomeException(msg, ex)` preserving the inner.

- **Trusting the exception over the error stack.** The real Sage reason often sits on `session.Errors` while the
  exception says little (or a failed verb throws nothing). → Read `session.Errors` (`view-api.md` § 9), surface
  the messages, then `session.Errors.Clear()`.

- **Swallowing errors / returning null or defaults on catch.** A caught DB/view failure that returns `null` or
  leaves `out` params at their defaults makes an error indistinguishable from "no data" / "not lot-controlled".
  → Let it propagate (wrapped), or return an explicit result that distinguishes failure from empty.

- **"Retry" branches that don't retry.** A catch that re-sets a field but never re-runs `Process()`/`Insert()`
  does nothing. → Make the retry actually re-execute, or remove it.

## SQL alongside the View API

- **Raw `System.Data.SqlClient` into Sage physical tables** (`ICITEM`, `OEORDH`, `POPORH1`, …) to read or, worse,
  write. It bypasses business logic and security, couples you to internal schema, and misses uncommitted view
  state. → Use composed **Advantage views** for reads and all writes. This capability, like the SQL one, **never**
  writes Sage tables via SQL — writes go through the View API.

- **String-concatenated SQL** where read-only SQL is genuinely unavoidable (e.g. a separate reporting query).
  → **Parameterize** every value; concatenation is an injection and a correctness bug.
