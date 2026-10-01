<!-- source: REFDI.chm (SAP Business One DI API 10.0 Objects Reference 10.00.190); code assembled from its signatures and SAP's own samples | version: DI API 10.0 | verified: 2026-10-01 -->

# DI API guide (C#)

How to program the SAP Business One **DI API** (`SAPbobsCOM`) correctly. Every statement below is taken from the
reference in `api/` and `enums/` (the CHM) unless it is marked **engineering practice** (not stated by SAP).
Look up exact signatures, parameters and enum values there; this file is the *how*, those files are the *what*.

Scope: the DI API object library only. Not the UI API (`SAPbouiCOM`), not the Service Layer (REST), not DI Server.
The reference is **DI API 10.0 (10.00.190)** and the default schema dictionary is **10.0** (`../dictionary/10.0/`),
so they line up; for a client on 9.3 use `../dictionary/9.3/` and say so (see `../dictionary/INDEX.md`).

## 1. The model in one paragraph

`Company` is the only DI API object you create directly; you create every other object through it
(`Company` class). Master-data and document **business objects** (`Documents`, `BusinessPartners`, `Items`, …)
come from `Company.GetBusinessObject(BoObjectTypes)`, are filled by property assignment and saved with `Add()` /
`Update()`, and report failure with a **return code**. **Services** (`GetCompanyService()` →
`GetBusinessService(ServiceTypes)` → `GetDataInterface(...)`) pass data structures and report failure by throwing
`COMException` (the pattern is visible in SAP's sample on `Company.StartTransaction`, `Company` class).
`Recordset` runs SQL for **reading** (§ 7). `1,378` classes in all; `api/INDEX.md` lists them with their source table.

## 2. Connect

Properties to set before `Connect()` (`Company` class, `Connect` remarks): `Server`, `CompanyDB`, `UserName`,
`Password`, `DbUserName`, `DbPassword`, `UseTrusted`, `AddonIdentifier`. SAP's sample marks `Server`, `DbServerType`
(from 8.8), `CompanyDB`, `UserName` and `Password` as mandatory and `DbUserName`, `DbPassword`, `UseTrusted`,
`language` as optional from 8.8 (database credentials then come from the System Landscape Directory).
`SLDServer` carries the SLD address; `LicenseServer` is **deprecated since DI API 9.2 PL05**, use `SLDServer`.

`DbServerType` takes a `BoDataServerTypes` value (`BoDataServerTypes` enum): `dst_MSSQL2019 = 15`,
`dst_HANADB = 9`, and so on; the older entries (SQL Server 2000, DB2, Sybase, MaxDB) are "Not Supported from 8.8".
The enum documents SQL Server up to 2019, so confirm the value for a newer SQL Server on the client's install.

```csharp
// Assembled from the Company property/method signatures and SAP's sample (the Company class, StartTransaction).
var company = new SAPbobsCOM.Company
{
    Server = cfg.Server,                                         // mandatory
    DbServerType = SAPbobsCOM.BoDataServerTypes.dst_MSSQL2019,   // mandatory from 8.8
    CompanyDB = cfg.CompanyDb,                                   // mandatory
    UserName = cfg.User,                                         // mandatory
    Password = cfg.Password,                                     // mandatory
    UseTrusted = false,                                          // optional from 8.8
    SLDServer = cfg.SldServer                                    // optional; default from the DI configuration file
};
int rc = company.Connect();                                      // Long -> int; 0 = success
if (rc != 0)
{
    company.GetLastError(out int code, out string message);      // call straight away, see § 3
    throw new InvalidOperationException($"DI API connect failed: {code} {message}");
}
// ... work ...
company.Disconnect();
```

`Connected` tells you whether the connection is active; `Version` returns the company database version and
`MinimalSupportedVersion` is the lowest database version your add-on accepts. Read credentials from configuration,
never from code.

## 3. Errors

- `Connect()`, `Add()`, `Update()` and most business-object methods **return `0` on success, otherwise an error
  code**. `GetByKey(...)` returns `bool` (found / not found).
- Fetch the detail with `Company.GetLastError(out int code, out string message)` — "**immediately** after the API
  call that caused the error; the error information is lost when you call other methods" (`Company` class).
  `GetLastErrorCode()` / `GetLastErrorDescription()` exist for technologies without `out` parameters.
- The message can carry an application error code (for example `10001090 - Posting period missing`); SAP points
  to the application's Message Documentation for those.
- DI API's own codes (`-103` connection to the company database failed, `-107` wrong username and/or password,
  `-1108` transaction already active, `-1109` no active transaction, `-2000` SQL native error, `-8007` license
  failure, and the rest) are tabulated in the `GetLastError` remarks in the `Company` class.
- Services throw `COMException`; read `ex.ErrorCode` and `ex.Message` (SAP's sample does this).

## 4. Create, read, update

1. `var inv = (SAPbobsCOM.Documents)company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oInvoices);` — returns an
   empty object holding only the company database's defaults (`Company` class, `GetBusinessObject`).
2. Set properties. **Mandatory** per the reference: `CardCode` on the document (`Documents` class) and `ItemCode`
   (with `AccountCode`) on the lines (`Document_Lines` class); a document must have at least one item line.
   The auto-complete feature fills the other defaults "the same way as in the SAP Business One application".
3. **Lines**: set the first line's properties directly on `inv.Lines`; call `inv.Lines.Add()` **before each further
   line**, then set that line's properties; `Lines.SetCurrentLine(i)` moves to an existing line (SAP's invoice
   sample, `Documents` class `Add`).
4. `int rc = inv.Add();` then check `rc`. The key of the new record is `company.GetNewObjectKey()` and its type
   `company.GetNewObjectType()` (use them after the `Add`).
5. Read: `GetByKey(DocEntry)`; if it returns `false` the object is left unchanged. Change properties, then
   `Update()`. Documents cannot be removed (`Remove` is "Not supported", except Purchase Quotation); use
   `Cancel()`, `CreateCancellationDocument()` or `Close()` as the requirement says.
6. Which document is which: `Documents` is every marketing document, chosen by `BoObjectTypes` (`oInvoices` →
   `OINV`, `oOrders` → `ORDR`, `oDrafts` → `ODRF`, and so on; the full list is in the `Documents` description in
   `Documents` class). Drafts also need `DocObjectCode`/`DocObjectCodeEx`.

```csharp
var inv = (SAPbobsCOM.Documents)company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oInvoices);
inv.CardCode = "BP234";                          // mandatory
inv.DocDate = DateTime.Today;
inv.Lines.ItemCode = "A00023";                   // first line: set directly, mandatory
inv.Lines.Quantity = 50;
inv.Lines.Price = 2.36;
inv.Lines.Add();                                 // before every further line
inv.Lines.ItemCode = "A00033";
inv.Lines.Quantity = 1;
inv.Lines.Price = 118;
int rc = inv.Add();
if (rc != 0)
{
    company.GetLastError(out int code, out string msg);
    throw new InvalidOperationException($"{code} {msg}");
}
string docEntry = company.GetNewObjectKey();
```

SAP's own VB invoice sample (`Documents` class, under `Add`) is the pattern this follows; the rest of the reference
carries C# and VB samples per member (`C# example` / `VB example` lines in each class's entry).

## 5. Transactions

`Company.StartTransaction()` … `Company.EndTransaction(BoWfTransOpt)`; `InTransaction` reports state.
`BoWfTransOpt` is `wf_Commit = 0` or `wf_RollBack = 1` (`BoWfTransOpt` enum). SAP's guidance (the example note on
`StartTransaction`, `Company` class):
- Check the return code of **every** call inside the transaction and leave immediately on failure.
- "If a call fails, SAP Business One **automatically ends the transaction with a rollback**; if you do not exit the
  transaction code, all subsequent code is still executed even though an error occurred."
- Only start/end while connected. If `EndTransaction` throws, the changes are not committed; fix the cause, start a
  new transaction and resubmit.
- Codes `-1108` / `-1109` are "transaction already active" / "no active transaction".

## 6. Release COM objects

SAP states one hard rule for .NET: after creating a user-defined **field**, **table** or **object**
(`UserFieldsMD`, `UserTablesMD`, `UserObjectsMD`) you **must** call
`System.Runtime.InteropServices.Marshal.ReleaseComObject(myObject)` on it (`UserFieldsMD` class,
`UserTablesMD` class, `UserObjectsMD` class). The reference gives no general rule for other objects.
**Engineering practice (not stated by SAP):** wrap the `Company` in an `IDisposable` that disconnects and releases it,
and release long-lived objects you create in loops, so a leaked connection doesn't hold a license.

## 7. Read data

- Prefer the business object (`GetByKey`) for one record.
- `Recordset` is the raw-read object: `rs.DoQuery(sql)`, then loop `while (!rs.EoF) { … rs.Fields.Item(0).Value … rs.MoveNext(); }`
  (SAP's sample on `Company.GetRegisteredServersList`, `Company` class). `RecordCount`, `MoveFirst`, `MoveLast`,
  `SaveXML` are on the `Recordset` class.
- **`DoQuery` will run any statement**, including data changes, and the reference says so. Use it for `SELECT` only.
  Changes to SAP Business One data go through the business objects or services so its business logic runs.
  Use table and column names from `../dictionary/10.0/` (or `9.3/` for a 9.3 client) and say which.
- A `Recordset` field's `Value` is `object`; convert it explicitly.

## 8. User-defined fields, tables and objects

- `UserFieldsMD` (UDF; source table `CUFD`), `UserTablesMD` (`OUTB`), `UserObjectsMD` (`OUDO`): create and change
  definitions; release each with `ReleaseComObject` (§ 6).
- `UserTable` reads and writes records of a user-defined table: `Add`, `GetByKey(string key)`, `Update`, `Remove`
  (`UserTable` class). The `Company.UserTables` property returns the collection.
- `GeneralService` is the entry point for UDOs: `GetDataInterface`, `Add`, `GetByParams`, `GetList`, `DoCommand`,
  `InvokeMethod` (`GeneralService` class).

## 9. Reading the signatures: VB → C#

The reference prints Visual Basic signatures only. COM types map as the SAP C# samples show:

| Reference (VB) | C# | Evidence in the reference |
|---|---|---|
| `Long` | `int` | `int errorCode = company.Connect();`, `company.GetLastError(out errorCode, …)` |
| `String` | `string` | C# samples declare `string` |
| `Double` | `double` | C# samples declare `double` |
| `Boolean` | `bool` | `bool findItem = item.GetByKey(...)` |
| `Date` | `DateTime` | `doc.DocDate = DateTime.Today;` |
| `ByRef x As T` | `out` / `ref` | `GetLastError(out errorCode, out errorMessage)` |
| `Variant`, `Object` | `object` | `GetBusinessObject` returns `Object`; cast it |
| enum parameters | `SAPbobsCOM.<Enum>.<member>` | `SAPbobsCOM.BoObjectTypes.oItems` |

`Integer` (16-bit in VB) is not exercised by the samples; confirm it in IntelliSense or the Object Browser on the
install before relying on `short`. Some samples that SAP labels "C#" are actually Visual Basic; `api/` tags those
`vb` so they aren't pasted as C#.

## 10. Where to look

| Need | File |
|---|---|
| a class's members | `api/INDEX.md` gives its file and line range in `api/classes-NN.md`; for a quick existence/type check grep `api/members.md` (`Class.Member : Type [R/W]`, one line each) |
| an enum value | `enums/members.md` (`Enum.Member = Value`, one line each); descriptions through `enums/INDEX.md` in `enums/enums-NN.md` |
| reviewing existing code | `review-checklist.md`: grep recipes per mistake, what not to flag, how to report |
| the object number for a type | `BoObjectTypes` enum and `../objects/object-types.md` |
| a table or column | `../dictionary/10.0/` (default) or `9.3/` for a 9.3 client |
| what goes wrong | `common-mistakes.md` |

## 11. Observed on a 10.0 install (practice, confirm on the client's)

Facts the CHM does not state or states differently from what the shipped interop and production code show.
Observed with `Interop.SAPbobsCOM.dll` 10.0 against SAP Business One 10.0 on SQL Server; re-check on other releases.

- **`BoDataServerTypes.dst_MSSQL2022 = 17`** exists in the 10.0 interop although the CHM table stops at
  `dst_MSSQL2019 = 15` (`enums/members.md` lists what the CHM has). Validate the setting with `Enum.TryParse` so a
  typo fails at connect time with the valid names instead of surfacing later as `-111`.
- **`Lines.Add()` after the last line is tolerated.** SAP's sample sets the first line and calls `Add` before each
  further line; most production code calls `Add` after every line, leaving a trailing empty line that the DI API
  ignores. Either order posts the same document. Don't report the second as a defect.
- **Assignment order that matters**: on drafts set `DocObjectCode` first; on a line set `BaseType`, `BaseEntry`,
  `BaseLine` before `ItemCode` (setting `ItemCode` triggers SAP's defaults, which would otherwise overwrite what came
  before); fill `SerialNumbers` / `BatchNumbers` / `BinAllocations` of a line before `Lines.Add()`; set `Series`
  on the header before adding lines. The sub-collections follow the same `SetCurrentLine(n)` ... `Add()` pattern as
  lines.
- **Base types are two different kinds**: `Document_Lines.BaseType` is the object number as `Long`;
  `StockTransfer_Lines.BaseType` is `InvBaseDocTypeEnum` with `InventoryTransferRequest = 5`.
- **`Document_LinesAdditionalExpenses.ExpenseCode` is `Long`** (the expense definition's code), not a string.
- **Header expenses are copied by reference** (`DocumentsAdditionalExpenses.BaseDocEntry` / `BaseDocLine` /
  `BaseDocType`), line expenses by value (`ExpenseCode`, `LineTotal`, `TaxCode`).
- **`GetNewObjectType()` + `GetNewObjectCode()` after a service `Add`** reflect the last business-object add, not the
  service call; the service returns its own params object (`InventoryPostingParams.DocumentEntry`). Code that builds
  a return key this way after a service call is reporting stale information.

## 12. A testable architecture for a .NET integration (practice)

The DI API is COM and order-sensitive, which makes integrations hard to unit test and tempting to copy per method.
This layout worked for a 45-method Granite WMS provider and generalises:

1. **One facade owns COM.** An `ISapSession : IDisposable` with the handful of operations the integration needs
   (`GetDocEntryByDocNum`, `GetItem`, `GetOnHand`, `ReadDocument`, `AddDocument`, `AddInventoryPosting`,
   `Begin/EndTransaction`), opened by an `ISapConnectionFactory`. Only its implementation references `SAPbobsCOM`.
   `Dispose` does `Disconnect` and one `ReleaseComObject`; every transient object is released in the method that
   created it.
2. **Build, then commit.** Posting logic reads a `SourceDocument` snapshot and produces a `TargetDocument` POCO
   (header, lines, allocations, expenses, user fields). One `DocumentWriter` replays it into `Documents` or
   `StockTransfer` in the canonical order from § 11. Tests assert on the POCO against a fake session; the writer is
   the only piece that needs a live smoke test. This beats wrapping each COM class in an interface: those wrappers
   have hundreds of members and tests degrade into call-sequence assertions.
3. **Declarative specs for document copies.** Most methods are "copy document A into B": source table and object,
   target object (or draft of), which header fields to copy, how incoming rows match SAP lines (single row / summed /
   summed and UOM-converted), where the warehouse comes from, batch/serial strategy, expenses, return-key format,
   plus hooks for client specials (numbering series, user fields). One handler executes every spec.
4. **A registry instead of a switch.** Method name → (how to group the incoming rows, which handler). Pin the full
   name list in a test: the names are configuration at every client, including any misspelled ones.
5. **Client profiles.** Numbering series per branch, user-field names and comment conventions live in one class per
   client, never in handlers.
6. **Errors**: a single exception type carrying `GetLastError`'s code and message, raised immediately after a
   non-zero return code; no `throw ex`, no re-wrapping; one catch at the provider boundary that turns the message
   into the host's return value.
7. **Characterise before you refactor.** For each legacy method write the expected `TargetDocument` from reading the
   old code first, then make the spec produce it. Behaviours that look wrong but may be intended (document copy
   direction, dropped second rows, dead series keys) are preserved and listed for the client to decide.
