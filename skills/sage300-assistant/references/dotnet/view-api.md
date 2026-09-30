<!-- source: smist08.wordpress.com (Stephen Smith) Sage 300 .NET API series + Sage community R&D | version: API idioms are version-independent; defaults target Sage 300 2026 (7.3A) | verified: 2026-09-25 -->

# Sage 300 .NET View API (ACCPAC.Advantage) — how to write correct C#

Everything here is the **Business Logic / Views layer** reached from C# through the `ACCPAC.Advantage`
assembly (`Session` → `DBLink` → `View`). This is the only "Sage 300 .NET library" this capability covers.
It is **not** the Web UI SDK, the Web API / web services, macros/VBA or Python — those are different
integration methods and out of scope.

The API idioms below are **version-independent**; only the `Init` version string and the exact view
rotoIDs/fields vary by installed version. Verify field names and single-table rotoIDs against
`references/dictionary/<version>/` (see § 8). Never invent a rotoID, a field name or a compose order.

Sources are cited per section; extract and cite, do not paste blog text.

## 1. Environment & build (state this with any generated code)

- `ACCPAC.Advantage` is a **.NET Framework** interop assembly over Sage's native/COM business logic. It is
  **not** .NET Core / .NET 5+, and **not** cross-platform. Target .NET Framework 4.x.
- It is **32-bit**. Build **x86** (or "Any CPU" with *Prefer 32-bit*), or the API throws at load/`Init`.
- The machine that runs the code needs a **Sage 300 workstation install** (the runtime/ADMIN share) and a
  licensed **API / Lanpak seat**; `Open` consumes a seat until the session is disposed.
- Reference `ACCPAC.Advantage.dll` (and its interop) from the Sage 300 program folder. Match the referenced
  assembly to the installed Sage version.
- Runs under the identity/DSNs configured for that Sage install; a service account still needs Sage rights.

## 2. Session lifecycle

Order is **Init → Open → OpenDBLink**, and `Init` **must be first** — calling anything before it yields
obscure errors ([opening-sessions](https://smist08.wordpress.com/2012/12/15/opening-sage-300-erp-sessions/),
[intro](https://smist08.wordpress.com/2013/10/12/an-introduction-to-the-sage-300-erp-net-api/)).

```csharp
using ACCPAC.Advantage;

var session = new Session();
session.Init("", "XY", "XY1000", "72A");   // see arg notes + version caveat below
session.Open("ADMIN", "ADMIN", "SAMINC", DateTime.Today, 0);
DBLink db = session.OpenDBLink(DBLinkType.Company, DBLinkFlags.ReadWrite);
```

**`Init(orgArg, appID, program, version)`**
- `orgArg` — empty string `""` for a standalone third-party app (only set when launched from the Sage desktop).
- `appID` — two-char app/object ID. `"XY"` is the reserved ID for non-SDK / third-party apps; use it unless you
  have a registered SDK app ID.
- `program` — program identifier (e.g. `"XY1000"`).
- `version` — System Manager version string, e.g. `"72A"`. **Do not guess this** — it tracks the installed
  version, not the marketing year, and a wrong value fails obscurely. Make it a **config value**, and confirm it
  against the install (macro-record the desktop sign-on, or read the installed System Manager version). Older
  code in the wild hard-codes values like `"65A"`; treat any literal as unverified until confirmed.

**`Open(user, password, company, date, flags)`**
- `user`, `password` — **case-sensitive at the API level** even though the desktop dialog upper-cases them; pass
  the exact case. Never hard-code — read from secure config.
- `company` — company/organization (database) ID.
- `date` — session date (defaults, aging, etc. key off this).
- `flags` — security flags; `0` is typical. (Trailing-arg shapes differ slightly between the old VB/COM and the
  .NET signatures; if the overload differs on your reference, match what IntelliSense shows.)

**`OpenDBLink(DBLinkType, DBLinkFlags)`** — `DBLinkType.Company` (company data) or `.System`;
`DBLinkFlags.ReadWrite` or `.ReadOnly`. Use `.ReadOnly` for pure reporting/reads.

**Disposal** — dispose in **reverse creation order: views → DBLink → session**, via `using` or `try/finally`.
The objects wrap unmanaged/COM resources and hold a licence seat, so leaking them exhausts seats. The blog does
not publish this as a single quoted rule (cleanup otherwise happens in the finalizer) — treat the order as
**best-practice convention**, but always release deterministically. See the § 6 scaffold.

## 3. Opening & composing views

- `db.OpenView("XX####")` opens one business view by its **rotoID** — a 2-letter module code + 4-digit number
  (e.g. `OE0520` OE Order header, `OE0500` OE Order detail). One document normally needs **several** views
  (header, details, optional fields, tax, …), each opened from the DBLink.
- `header.Compose(new View[]{ ... })` wires the views together so they operate on the **same instances** (header
  and its details cooperate, keys flow, posting cascades). You call `Compose` on each participating view with the
  array of its related views.
- **The array order is fixed per view and is NOT derivable from the dictionary.** Getting a slot wrong silently
  corrupts documents. The reliable way to get the exact open+compose sequence is to **macro-record the real Sage
  desktop UI** performing the operation and translate the recorded view IDs/order to C#
  ([composing-views](https://smist08.wordpress.com/2013/10/27/composing-views-in-the-sage-300-erp-net-api/); Sage
  R&D: "Composing Views in the Sage 300 .Net API"). See § 7 for the recipe. When you cannot confirm the order,
  emit a clearly-marked placeholder — do not guess.

## 4. View verbs & field access

Sources: [starting-to-program](https://smist08.wordpress.com/2013/10/20/starting-to-program-the-sage-300-erp-views-in-net/),
[view-protocols](https://smist08.wordpress.com/2013/11/02/using-the-sage-300-erp-view-protocols-with-net/),
[performance-2](https://smist08.wordpress.com/2015/03/14/performance-and-the-sage-300-views-part-2/).

| Verb | Meaning / correct use |
|---|---|
| `RecordClear()` | Blank the record buffer — start of a read loop, or before setting a user-supplied key. |
| `RecordCreate(ViewRecordCreate mode)` | Prepare a new record. `Insert` (normal new), `NoInsert` (build in memory, e.g. a detail line staged into the revision list), `DelayKey` (defer key generation to insert — headers whose key the view generates). |
| `RecordGenerate(bool)` | Generate/default a new record — used for optional-field records. |
| `Read(bool lock)` | Read the record for the current key. Pass **`false`** normally. `Read(true)` **locks and throws** unless inside `TransactionBegin/Commit`. |
| `GoTop()` / `GoNext()` | Forward navigation; return `bool` (`true` = a record was returned). |
| `Browse(filter, ascending)` + `Fetch(bool lock)` | Set a filter, then loop `Fetch` until it returns `false`. `RecordClear()` first. Preferred for filtered iteration. |
| `Exists` | Property — does the current record exist. |
| `Insert()` | Persist a new record. For composed header/detail, a **detail** `Insert()` only stages into the in-memory **revision list**; the **header** `Insert()` commits the whole document in one transaction and cascades the post. |
| `Update()` | Save changes to the **current** record — you must `Read`/`Fetch` it first. |
| `Delete()` / `FilterDelete(filter)` | Remove current record; `FilterDelete` bulk-deletes matching rows far faster than a loop. |
| `Process()` | Run a view's processing command (workflow step) after setting a `PROCESSCMD`/`FUNCTION` field. |
| `Order` | Integer property selecting the active **index/key** for navigation (which key `Read`/`GoNext` follow). Set it before reading by an alternate key. |

**Fields**
```csharp
view.Fields.FieldByName("IDCUST").SetValue("1200", false);      // set, defer verify
string cust = (string) view.Fields.FieldByName("IDCUST").Value; // native stored value
```
- `SetValue(value, verify)` — the **second boolean is "verify now"**: `true` fires the field's edit/validation
  logic immediately; `false` defers it to insert/update/process. Setting many fields with `false` then letting
  `Insert`/`Process` validate is normal; verify (`true`) key/business fields you want checked at once.
- `.Value` is the native stored value. Field-name lookups hit a dictionary, so **cache** `FieldByName` results
  (or field indexes) in hot loops rather than re-resolving per row.

## 5. Standard header/detail create-and-post pattern

From [view-protocols](https://smist08.wordpress.com/2013/11/02/using-the-sage-300-erp-view-protocols-with-net/)
(shape generalised; verify the exact rotoIDs/fields/compose for your document):

1. If the doc lives in a batch: `batch.RecordCreate(ViewRecordCreate.Insert)`, set batch fields, `batch.Update()`.
2. `header.RecordCreate(ViewRecordCreate.DelayKey)` (key derived on insert), set header fields (e.g. `IDCUST`).
3. Per line: `detail.RecordCreate(ViewRecordCreate.NoInsert)`, set the **line-sequence key** field, set line
   fields (item, qty, …), then `detail.Insert()` (stages into the revision list).
   - **Line-order gotcha:** setting the sequence key to `0` for every line inserts them **in reverse** — each new
     line goes to the front. Increment the sequence, or use the last sequence number, so lines keep their order.
4. Repeat per line (optional fields: see § 6a).
5. `header.Insert()` — commits the document in one DB transaction and posts the composed details.

Read-then-update an existing document: set the key field(s), set `Order` to the matching index, `Read(false)`,
check `Exists`, modify fields, `Update()` the record, then `header.Insert()`/`Update()` as the protocol requires.

### 5a. Reading / querying (reports, lookups)
Open the view `ReadOnly`, `RecordClear()`, `Browse(filter, true)`, loop `while (view.Fetch(false)) { read
Fields… }`. For a single record, set the key + `Order` and `Read(false)`. Prefer `Browse`/`Fetch` over `GoNext`
for filtered scans.

## 6. Optional fields, revision lists, transactions

Sources: [optional-fields](https://smist08.wordpress.com/2014/01/04/sage-300-erp-optional-fields/),
[performance-2](https://smist08.wordpress.com/2015/03/14/performance-and-the-sage-300-views-part-2/).

- **Revision lists** stage details/optional-fields in memory; nothing hits the DB until the header `Insert()`
  fires the single transaction.
- **Optional fields fail at customer sites, not on sample data.** A view that works on SAMINC breaks where the
  customer has **required** optional fields configured. Handle them. An optional-field view is itself an ordered
  header/detail whose "header" is the entity it belongs to.
- Order: insert the parent **detail first**, then add its optional-field sub-records, then `Update()` the detail,
  finally `Insert()` the header:
  ```csharp
  detail.Insert();
  detailOptFields.RecordClear();
  detailOptFields.RecordGenerate(false);
  detailOptFields.Fields.FieldByName("OPTFIELD").SetValue("EXTWARRANTY", false);
  detailOptFields.Insert();
  detail.Update();
  header.Insert();
  ```
- Optional-field values store into one `VALUE` field; read/write typed values via the `VALIF…` fields
  (`VALIFTEXT`, `VALIFBOOL`, …). Validate against the CS optional-fields setup (`CSOPTFD` / CS0012) where lookups
  are required. Many views expose `PROCESSCMD` commands ("Insert Optional Fields", "Default and Transfer Optional
  Fields") to auto-populate/flow them.
- **Bulk performance:** wrap many writes in `db.TransactionBegin() … db.TransactionCommit()` (measured ~2× faster),
  but **commit periodically** (~every 1000 records) — an open transaction locks touched records. Use
  `FilterDelete` over a manual delete loop.

## 6b. Reference scaffold (greenfield-correct)

Shape generated code like this: a disposable session wrapper (deterministic reverse-order cleanup, one seat),
and a per-document class that opens/composes its own views. Fill `TODO(verify)` from § 7/§ 8; do not guess.

```csharp
public sealed class Sage300Session : IDisposable
{
    private readonly Session _session;
    public DBLink Db { get; }

    public Sage300Session(string user, string password, string company, string version)
    {
        _session = new Session();
        _session.Init("", "XY", "XY1000", version); // version from config, confirmed on the install
        _session.Open(user, password, company, DateTime.Today, 0); // case-sensitive creds
        Db = _session.OpenDBLink(DBLinkType.Company, DBLinkFlags.ReadWrite);
    }

    /// <summary>Drain the business-logic error stack (see § 9) and clear it.</summary>
    public IReadOnlyList<string> DrainErrors()
    {
        var msgs = new List<string>();
        if (_session.Errors != null)
        {
            for (int i = 0; i < _session.Errors.Count; i++)
                msgs.Add($"{_session.Errors[i].Priority}: {_session.Errors[i].Message}");
            _session.Errors.Clear();
        }
        return msgs;
    }

    public void Dispose()   // views are disposed by their owning document class; then link, then session
    {
        Db?.Dispose();
        _session?.Dispose();
    }
}
```

## 7. Finding the right rotoIDs and compose order (do this, don't guess)

1. **Core transaction documents** (OE order/invoice/credit-debit/shipment; PO purchase-order/receipt/invoice/
   return/credit-debit; IC adjustment/transfer/shipment/receipt/internal-usage; AR invoice & receipt batches;
   AP invoice & payment batches; GL journal entry): use **`references/dotnet/compose-graphs.md`** — it lists the
   exact views to open and, per view, the exact `Compose()` **slot order** (extracted and verified from the 7.3A
   AOM). `-` = a GENSTUB slot → pass `null`; a `rotoID*` slot = a view not opened by the integration → `null`.
   These are the authoritative wiring; don't restate them from memory.
2. **Single-table rotoID + field names**: look them up in the bundled dictionary (§ 8). That confirms field names
   for `FieldByName(...)` and the primary view per table.
3. **A document NOT in `compose-graphs.md`** (or when in doubt on a specific install): get the compose graph by
   **macro-recording** the operation in the Sage desktop — Tools/Macro → Record, perform the entry once, stop,
   open the recorded macro (VBA). The recorded `OpenView`/`Compose` calls and their order translate directly to
   C#. Cross-check the recorded view IDs and fields against the dictionary.
4. If none of the above is available at authoring time, emit the code with the composition marked
   `// TODO(verify): confirm rotoIDs and Compose() order by macro-recording <operation>` rather than a plausible guess.

Composition of the core OE/IC/AR/AP/PO/GL documents is stable across 7.0A–7.3A, so `compose-graphs.md` (built for
7.3A) also applies to 2023–2025; confirm on the client's install only if something looks off.

## 8. Verify against the bundled dictionary

- `references/dictionary/<version>/table-index.md` — one line per table with its **primary view rotoID** in
  parentheses, e.g. `` `OEORDD` - Order Details (OE0500) ``. Grep it to map a table → its view.
- `references/dictionary/<version>/dict/<MODULE>.md` — every **field name**, type, key and enum for the table
  (module = first two letters: `OEORDH` → `dict/OE.md`; header shows `## OEORDH - Orders (view OE0520)`).
- Rule: **never emit a `FieldByName("…")` you have not seen** in the dict for the target version, and cite which
  file confirmed it. Default version is 7.3A (2026); use the folder matching the client and say so.

## 9. Error handling — read the error stack, don't trust exceptions alone

Source: [error-reporting](https://smist08.wordpress.com/2013/12/06/error-reporting-in-sage-300-erp/).
- Business logic accumulates messages on **`session.Errors`**. A thrown exception may carry **no** entry on the
  stack, and a verb that returns a failure code may leave the **real, human-readable reason** on the stack. So on
  any failure, read `session.Errors` for the message, surface it, then **`session.Errors.Clear()`** so stale
  messages don't leak into the next operation.
```csharp
for (int i = 0; i < session.Errors.Count; i++)
{
    var e = session.Errors[i];
    switch (e.Priority)   // SevereError, Error, Security, Warning, Message
    {
        case ErrorPriority.SevereError:
        case ErrorPriority.Error:
        case ErrorPriority.Security:
            // log/raise e.Message
            break;
        case ErrorPriority.Warning:
        case ErrorPriority.Message:
            // informational
            break;
    }
}
session.Errors.Clear();
```
- Simple verbs (e.g. reads) return a `bool`; abnormal conditions throw. Handle both, and always consult the stack.

## Primary sources (verified 2026-09-25)
- Intro to the .NET API — https://smist08.wordpress.com/2013/10/12/an-introduction-to-the-sage-300-erp-net-api/
- Opening sessions — https://smist08.wordpress.com/2012/12/15/opening-sage-300-erp-sessions/
- Starting to program the views — https://smist08.wordpress.com/2013/10/20/starting-to-program-the-sage-300-erp-views-in-net/
- Composing views — https://smist08.wordpress.com/2013/10/27/composing-views-in-the-sage-300-erp-net-api/
- View protocols — https://smist08.wordpress.com/2013/11/02/using-the-sage-300-erp-view-protocols-with-net/
- Error reporting — https://smist08.wordpress.com/2013/12/06/error-reporting-in-sage-300-erp/
- Optional fields — https://smist08.wordpress.com/2014/01/04/sage-300-erp-optional-fields/
- Performance part 2 (transactions, Browse/Fetch, FilterDelete) — https://smist08.wordpress.com/2015/03/14/performance-and-the-sage-300-views-part-2/
- Helper APIs — https://smist08.wordpress.com/2014/07/19/using-the-sage-300-net-helper-apis/
- Sage R&D, Composing Views in the Sage 300 .Net API — https://communityhub.sage.com/us/sage300/b/sage_300_erp_r_and_d/posts/composing-views-in-the-sage-300-erp-net-api

Gaps to be honest about: the blog never publishes a single ordered Dispose recipe (the reverse order is
best-practice convention); `Init`/`Open` trailing-arg shapes vary between the old VB/COM and .NET signatures.
