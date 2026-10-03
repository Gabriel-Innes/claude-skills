<!-- source: Pastel.Evolution.chm + Pastel.Evolution.xml, SDK 11.0.0.10 | verified: 2026-10-02 -->

# Pastel Evolution SDK — common mistakes

Anti-patterns from real Evolution SDK integrations, each with the correct alternative. Read before writing
code so you produce the right pattern, not the plausible-but-wrong one.

### Writing to Evolution tables with raw SQL
`INSERT`/`UPDATE`/`DELETE` straight into the company database skips every bit of Evolution's posting,
validation and GL logic and silently corrupts the books. **The SDK is the supported write path** — construct
the record/transaction object, set properties, `Save()`/post. Raw SQL is read-only (reports, diagnostics)
only, and even then prefer the SDK's `List(criteria)` where it exists.

### Opening only the accounting connection
The SDK needs **both** the accounting DB and the **common** DB (`EvolutionCommon`). Forgetting the common
connection fails later in confusing ways. Use `DatabaseContext.Initialise(...)` (opens both) or pair
`CreateConnection(...)` with `CreateCommonDBConnection(...)`, then check `IsConnectionOpen` **and**
`IsCommonConnectionOpen`.

### Guessing a property, method or enum value
The surface is large (152 types, ~1,800 properties, 41 enums) and names are not guessable — property names
don't always match the database column, and enum members carry specific integer values. **Verify in `api/`
and `enums/` and cite the file.** Use the named enum constant in code, never the raw int.

### Not wrapping multi-record writes in a transaction
A header that saves and a line that then throws leaves a half-written document. Wrap the unit of work in
`DatabaseContext.BeginTran()` / `CommitTran()` with `RollbackTran()` in the `catch`. Check
`IsTransactionPending` and don't double-manage operations that begin their own transaction implicitly.

### Managing your own SqlConnection to Evolution
Opening a separate `SqlConnection` to write Evolution tables (or to run your own transaction alongside the
SDK's) fights the SDK's transaction scope. Let `DatabaseContext` own `DBConnection`/`DBTransaction`; read
through the SDK or a *separate* read-only reporting connection, never a parallel writer.

### Treating `ID == 0` as a real record
`ID`/`LongID` is `0` for a new, unsaved record. Branch on it to tell "create" from "update", and read it back
after `Save()` to get the assigned ID.

### Version / registration mismatch
Referencing a different `Pastel.Evolution.dll` version than the installed Evolution runtime, or pointing at a
company database of an incompatible version, fails at connect/registration. Reference the DLLs that match the
install, and guard on `CompatibleDatabaseVersion` / `CurrentDatabaseVersion`.

### Swallowing the real error
Catching and discarding the SDK's exception hides the actual posting/validation reason. Surface the exception
message (and inner exception), and roll the transaction back on failure rather than leaving it pending.

### Building a posting document from memory of its shape
Order/invoice/batch documents each have their own line object, collection property and post method — don't
assume they're uniform. Look the specific type up in `api/` (its `## Properties` / `## Methods` / `## Events`)
before wiring it, and leave a `// TODO(verify): confirm against the installed SDK` marker for anything the
reference doesn't pin down.
