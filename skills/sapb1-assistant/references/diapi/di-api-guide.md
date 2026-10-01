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
(`api/Company.md`). Master-data and document **business objects** (`Documents`, `BusinessPartners`, `Items`, …)
come from `Company.GetBusinessObject(BoObjectTypes)`, are filled by property assignment and saved with `Add()` /
`Update()`, and report failure with a **return code**. **Services** (`GetCompanyService()` →
`GetBusinessService(ServiceTypes)` → `GetDataInterface(...)`) pass data structures and report failure by throwing
`COMException` (the pattern is visible in SAP's sample on `Company.StartTransaction`, `api/Company.md`).
`Recordset` runs SQL for **reading** (§ 7). `1,378` classes in all; `api/INDEX.md` lists them with their source table.

## 2. Connect

Properties to set before `Connect()` (`api/Company.md`, `Connect` remarks): `Server`, `CompanyDB`, `UserName`,
`Password`, `DbUserName`, `DbPassword`, `UseTrusted`, `AddonIdentifier`. SAP's sample marks `Server`, `DbServerType`
(from 8.8), `CompanyDB`, `UserName` and `Password` as mandatory and `DbUserName`, `DbPassword`, `UseTrusted`,
`language` as optional from 8.8 (database credentials then come from the System Landscape Directory).
`SLDServer` carries the SLD address; `LicenseServer` is **deprecated since DI API 9.2 PL05**, use `SLDServer`.

`DbServerType` takes a `BoDataServerTypes` value (`enums/BoDataServerTypes.md`): `dst_MSSQL2019 = 15`,
`dst_HANADB = 9`, and so on; the older entries (SQL Server 2000, DB2, Sybase, MaxDB) are "Not Supported from 8.8".
The enum documents SQL Server up to 2019, so confirm the value for a newer SQL Server on the client's install.

```csharp
// Assembled from the Company property/method signatures and SAP's sample (api/Company.md, StartTransaction).
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
  call that caused the error; the error information is lost when you call other methods" (`api/Company.md`).
  `GetLastErrorCode()` / `GetLastErrorDescription()` exist for technologies without `out` parameters.
- The message can carry an application error code (for example `10001090 - Posting period missing`); SAP points
  to the application's Message Documentation for those.
- DI API's own codes (`-103` connection to the company database failed, `-107` wrong username and/or password,
  `-1108` transaction already active, `-1109` no active transaction, `-2000` SQL native error, `-8007` license
  failure, and the rest) are tabulated in the `GetLastError` remarks in `api/Company.md`.
- Services throw `COMException`; read `ex.ErrorCode` and `ex.Message` (SAP's sample does this).

## 4. Create, read, update

1. `var inv = (SAPbobsCOM.Documents)company.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oInvoices);` — returns an
   empty object holding only the company database's defaults (`api/Company.md`, `GetBusinessObject`).
2. Set properties. **Mandatory** per the reference: `CardCode` on the document (`api/Documents.md`) and `ItemCode`
   (with `AccountCode`) on the lines (`api/Document_Lines.md`); a document must have at least one item line.
   The auto-complete feature fills the other defaults "the same way as in the SAP Business One application".
3. **Lines**: set the first line's properties directly on `inv.Lines`; call `inv.Lines.Add()` **before each further
   line**, then set that line's properties; `Lines.SetCurrentLine(i)` moves to an existing line (SAP's invoice
   sample, `api/Documents.md` `Add`).
4. `int rc = inv.Add();` then check `rc`. The key of the new record is `company.GetNewObjectKey()` and its type
   `company.GetNewObjectType()` (use them after the `Add`).
5. Read: `GetByKey(DocEntry)`; if it returns `false` the object is left unchanged. Change properties, then
   `Update()`. Documents cannot be removed (`Remove` is "Not supported", except Purchase Quotation); use
   `Cancel()`, `CreateCancellationDocument()` or `Close()` as the requirement says.
6. Which document is which: `Documents` is every marketing document, chosen by `BoObjectTypes` (`oInvoices` →
   `OINV`, `oOrders` → `ORDR`, `oDrafts` → `ODRF`, and so on; the full list is in the `Documents` description in
   `api/Documents.md`). Drafts also need `DocObjectCode`/`DocObjectCodeEx`.

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

SAP's own VB invoice sample (`api/Documents.md`, under `Add`) is the pattern this follows; the rest of the reference
carries C# and VB samples per member (`C# example` / `VB example` lines in `api/<Class>.md`).

## 5. Transactions

`Company.StartTransaction()` … `Company.EndTransaction(BoWfTransOpt)`; `InTransaction` reports state.
`BoWfTransOpt` is `wf_Commit = 0` or `wf_RollBack = 1` (`enums/BoWfTransOpt.md`). SAP's guidance (the example note on
`StartTransaction`, `api/Company.md`):
- Check the return code of **every** call inside the transaction and leave immediately on failure.
- "If a call fails, SAP Business One **automatically ends the transaction with a rollback**; if you do not exit the
  transaction code, all subsequent code is still executed even though an error occurred."
- Only start/end while connected. If `EndTransaction` throws, the changes are not committed; fix the cause, start a
  new transaction and resubmit.
- Codes `-1108` / `-1109` are "transaction already active" / "no active transaction".

## 6. Release COM objects

SAP states one hard rule for .NET: after creating a user-defined **field**, **table** or **object**
(`UserFieldsMD`, `UserTablesMD`, `UserObjectsMD`) you **must** call
`System.Runtime.InteropServices.Marshal.ReleaseComObject(myObject)` on it (`api/UserFieldsMD.md`,
`api/UserTablesMD.md`, `api/UserObjectsMD.md`). The reference gives no general rule for other objects.
**Engineering practice (not stated by SAP):** wrap the `Company` in an `IDisposable` that disconnects and releases it,
and release long-lived objects you create in loops, so a leaked connection doesn't hold a license.

## 7. Read data

- Prefer the business object (`GetByKey`) for one record.
- `Recordset` is the raw-read object: `rs.DoQuery(sql)`, then loop `while (!rs.EoF) { … rs.Fields.Item(0).Value … rs.MoveNext(); }`
  (SAP's sample on `Company.GetRegisteredServersList`, `api/Company.md`). `RecordCount`, `MoveFirst`, `MoveLast`,
  `SaveXML` are on `api/Recordset.md`.
- **`DoQuery` will run any statement**, including data changes, and the reference says so. Use it for `SELECT` only.
  Changes to SAP Business One data go through the business objects or services so its business logic runs.
  Use table and column names from `../dictionary/10.0/` (or `9.3/` for a 9.3 client) and say which.
- A `Recordset` field's `Value` is `object`; convert it explicitly.

## 8. User-defined fields, tables and objects

- `UserFieldsMD` (UDF; source table `CUFD`), `UserTablesMD` (`OUTB`), `UserObjectsMD` (`OUDO`): create and change
  definitions; release each with `ReleaseComObject` (§ 6).
- `UserTable` reads and writes records of a user-defined table: `Add`, `GetByKey(string key)`, `Update`, `Remove`
  (`api/UserTable.md`). The `Company.UserTables` property returns the collection.
- `GeneralService` is the entry point for UDOs: `GetDataInterface`, `Add`, `GetByParams`, `GetList`, `DoCommand`,
  `InvokeMethod` (`api/GeneralService.md`).

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
| a class's members | `api/<Class>.md` (find the class in `api/INDEX.md`) |
| an enum value | `enums/<Enum>.md` (find it in `enums/INDEX.md`; or grep a member name across `enums/`) |
| the object number for a type | `enums/BoObjectTypes.md` and `../objects/object-types.md` |
| a table or column | `../dictionary/10.0/` (default) or `9.3/` for a 9.3 client |
| what goes wrong | `common-mistakes.md` |
