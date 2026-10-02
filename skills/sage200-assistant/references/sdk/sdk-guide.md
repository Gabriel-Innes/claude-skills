<!-- source: Pastel.Evolution.chm + Pastel.Evolution.xml, SDK 11.0.0.10 | verified: 2026-10-02 -->

# Pastel Evolution SDK — how to drive it

The correct way to program the **Pastel Evolution .NET SDK** (`Pastel.Evolution.dll`, namespace
`Pastel.Evolution`) — the managed object layer Sage 200 Evolution / Pastel Evolution ships for reading and
writing accounting data through its own business logic. Idioms below are taken from the shipped CHM and XML
doc (SDK 11.0.0.10). Signatures, members and enum values are **authoritative in `api/` and `enums/`** — this
file is the *how-to*; `api/INDEX.md` is the *what*.

**Scope:** this is the `Pastel.Evolution` object SDK only — not the Evolution ODBC/SQL layer, the Evolution
Connector/API web service, or direct SQL against the company database. The SDK *is* the supported write path;
it runs the same validation and posting logic the Evolution desktop uses.

## 1. Environment & build

- The SDK is **.NET Framework** and references `Pastel.Evolution.dll` + `Pastel.Evolution.Common.dll` (both
  shipped in `docs/Pastel.Evolution.11.0.0.10/`). It must run on a machine with a **licensed Evolution
  install** of a **matching version** — the DLLs bind to the installed Evolution runtime and registration;
  a version mismatch between your referenced DLLs and the installed Evolution fails at connect/registration.
- Match the process bitness and target framework to the installed Evolution runtime; confirm on the install
  rather than assuming. Reference the DLLs from the install folder (or ship the exact matching version).
- The SDK talks to **two SQL Server databases**: the **company/accounting** database and a shared **common**
  database (default name `EvolutionCommon`, typically on the same server). Both connections must be opened.

## 2. Connect (DatabaseContext)

`DatabaseContext` is a **static** class — the entry point. Open the accounting connection and the common
connection, then work through record objects. See `api/` → `DatabaseContext` for every overload.

- `DatabaseContext.Initialise(...)` — opens the connections the SDK needs in one call; overloads let you give
  the common DB connection string explicitly, assume it is `EvolutionCommon` on the same server, or assume
  defaults. Prefer `Initialise` for a normal startup.
- Lower-level: `CreateConnection(connectionString)` / `CreateConnection(server, database)` /
  `CreateConnection(server, database, login, password, trustedAuth)` for the accounting DB, plus the matching
  `CreateCommonDBConnection(...)` for the common DB.
- State to check: `IsConnectionOpen`, `IsCommonConnectionOpen`, `CompanyName`, `CompanyID`,
  `CurrentDatabaseVersion` / `CompatibleDatabaseVersion` (guard against an incompatible company DB),
  `CurrentAgent` (the logged-in agent/user), `RegisteredUsers`.
- `DBConnection` exposes the underlying `SqlConnection` the SDK uses; `DBTransaction` the current
  `SqlTransaction`. Let the SDK own them — don't open your own parallel connection to write Evolution tables.

## 3. The record pattern (RecordBase)

Almost every master/account object derives from `RecordBase` (via `AccountBase`, `BranchedRecordBase`, etc.).
The pattern is the same for `Customer`, `Supplier`, `Inventory`, `GLAccount`, `Agent`, `Project`, …:

1. **Load or create** with a constructor:
   - `new Customer()` → a new, unsaved record (`ID == 0`).
   - `new Customer(code)` → loads the existing account by its code.
   - `new Customer(id)` → loads by internal ID.
2. **Read/set properties** — strongly-typed (`Description`, `Active`, address fields, control accounts, …).
   Every property is in `api/` with its C# type and read/write accessors; never guess a property name.
3. **`Save()`** — persists through Evolution's business logic (the public method on `RecordBase`;
   concrete types override the internal `OnSave`). `Delete()` removes the record *if* nothing references it.
4. **Find by criteria** — static helpers return an ID: `Customer.Find(criteria)`,
   `Customer.FindByCode(code)`; many types also expose `List(criteria)` returning a `DataTable`. The
   `criteria` is raw SQL `WHERE`-clause text (e.g. `Description like '%ABC%'`), so quote string literals.

`ID == 0` means "new / unsaved"; a non-zero `ID`/`LongID` means it is persisted.

## 4. Transactional (posting) objects

Posting objects — `InventoryTransaction`, `GLTransaction`, `CashbookBatch`, order/invoice documents and their
`*Detail`/`*Collection` line objects — build a document in memory, then **post** it. They expose:

- **Collections** for lines (`...Detail` + `...Collection`) you add to before posting; collections raise
  change events.
- **`Post()`-style** commit (concrete types override `OnPost`), with hook **events** such as
  `BeforePost` and GL-posting events (e.g. `GLCostVarianceCreditPosting`) to adjust or veto.
- Static `Find(criteria)` / `List(criteria)` to locate posted documents.

Look the exact type up in `api/` before coding — the line object, the collection property, and the post
method differ per document, and the summaries there are the SDK's own.

## 5. Transactions (atomic multi-record writes)

Wrap any multi-record operation in an explicit transaction so a mid-way failure rolls everything back:

- `DatabaseContext.BeginTran()` — starts a global transaction (returns false if one was already pending).
- `DatabaseContext.CommitTran()` — commits (quietly no-ops if none pending).
- `DatabaseContext.RollBackTran()` — roll back on failure.
- `DatabaseContext.IsTransactionPending` — check before begin/commit.

Put the work in `try`/`catch`: commit at the end of the `try`, roll back in the `catch`. Some SDK operations
begin/commit their own transaction implicitly when none is pending — don't double-manage. While a transaction
is open other readers may block (isolation is read-committed by default), so keep them short.

## 6. Generating correct C#

- Verify **every** class, property, method and enum member against `api/` and `enums/` — the SDK surface is
  large (152 types, 41 enums) and names are exactly what a model guesses wrongly. Cite the file.
- Use the **named enum constant** (from `enums/`), never a magic int — even though the enum's integer value is
  listed, pass the constant in code.
- Open both connections (accounting + common) via `DatabaseContext` before touching any record.
- Use the record pattern: construct → set typed properties → `Save()`; wrap multi-record writes in
  `BeginTran`/`CommitTran`/`RollBackTran` with rollback on exception.
- Never bypass the SDK with raw `INSERT`/`UPDATE` to Evolution tables — it skips all posting/validation logic
  and corrupts integrity. The SDK is the write path.
- Dispose/close: let `DatabaseContext` own connections; close them on shutdown. Don't leak a connection or
  leave a transaction pending.
- For any document whose post/compose shape you can't confirm in `api/`, say so and leave a
  `// TODO(verify): confirm against the installed SDK` marker rather than inventing a member.

## 7. Lookup recipes

- A property/method by name across the API: grep `FieldName` in `api/classes-*.md`.
- Which type owns a member: grep the member name, then read that type's heading (`^# <Type> (`).
- An enum's integer values: grep the enum name in `enums/enums-*.md` (table is Member | Value | Description).
- Exact signature / params / returns of a method: find the type in `api/INDEX.md`, read its line range.
