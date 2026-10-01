<!-- source: REFDI.chm (SAP Business One DI API 10.0 Objects Reference 10.00.190); items marked "practice" are engineering advice, not SAP statements | version: DI API 10.0 | verified: 2026-10-01 -->

# DI API common mistakes

Wrong pattern → the correct one. Each item names the reference file that backs it; "practice" marks advice SAP
doesn't state.

| # | Mistake | Do this instead | Backed by |
|---|---|---|---|
| 1 | Ignoring the return code of `Add()` / `Update()` / `Connect()` and carrying on | Check `!= 0` on every call and stop. Inside a transaction SAP has *already rolled back* when a call fails, so code that carries on runs outside it | `api/Company.md` (`StartTransaction` note) |
| 2 | Calling another API method before reading the error | Call `GetLastError(out code, out msg)` immediately after the failing call; the error is lost on the next call | `api/Company.md` (`GetLastError`) |
| 3 | Treating services like business objects (or the reverse) | Business objects return an error code; services throw `COMException` (read `ex.ErrorCode`, `ex.Message`) | `api/Company.md` (sample) |
| 4 | Forgetting `Marshal.ReleaseComObject` after creating a UDF, user table or UDO in .NET | Release the `UserFieldsMD` / `UserTablesMD` / `UserObjectsMD` object right after use; SAP marks it IMPORTANT | `api/UserFieldsMD.md`, `api/UserTablesMD.md`, `api/UserObjectsMD.md` |
| 5 | Leaving the connection open on an error path | `Disconnect()` in a `finally` / `Dispose()`. (practice) | `api/Company.md` (`Disconnect`) |
| 6 | Using `Recordset.DoQuery` to change Business One data | `DoQuery` runs any statement, so it is read-only by convention here; write through business objects or services so business logic runs | `api/Recordset.md` |
| 7 | Removing a document with `Remove()` | Not supported for documents (Purchase Quotation excepted). Cancel it, create a cancellation document, or close it | `api/Documents.md` |
| 8 | A document with no lines, or without the mandatory fields | At least one item line; `CardCode` on the header, `ItemCode` on lines | `api/Documents.md`, `api/Document_Lines.md` |
| 9 | Adding a line by calling `Lines.Add()` first | Set the first line's properties directly; call `Lines.Add()` before each *further* line | `api/Documents.md` (`Add` sample) |
| 10 | Pasting a VB sample into C# (including some that SAP labels "C#") | Translate it; `api/` tags such blocks `vb` | `api/` (the `vb` tags) |
| 11 | Mapping COM `Long` to C# `long` | `Long` is `int` in the interop (SAP's samples use `int errorCode`) | `api/Company.md` (sample) |
| 12 | Assuming `GetByKey` throws when nothing is found | It returns `false` and leaves the object unchanged; check it | `api/Documents.md` (`GetByKey`) |
| 13 | Setting `LicenseServer` | Deprecated since DI API 9.2 PL05; use `SLDServer` | `api/Company.md` |
| 14 | An old `DbServerType` (`dst_MSSQL`, `dst_DB_2`, `dst_SYBASE`, `dst_MAXDB`) | Those are "Not Supported from 8.8"; pick a current value and confirm it for the client's database | `enums/BoDataServerTypes.md` |
| 15 | Guessing an object-type number or enum value | Look it up in `enums/BoObjectTypes.md` and the other `enums/` files | `enums/` |
| 16 | Hard-coding connection details | Read them from configuration or a secret store. (practice) | |
| 17 | Assuming a 10.0 table or column exists on the client's database (or a 9.3 one on 10.0) | The reference and the default dictionary are 10.0 (a 9.3 dictionary is also bundled); compare against the client's database | `INDEX.md` |
