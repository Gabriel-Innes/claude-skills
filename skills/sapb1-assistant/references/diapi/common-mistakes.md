<!-- source: REFDI.chm (SAP Business One DI API 10.0 Objects Reference 10.00.190); items marked "practice" are engineering advice, not SAP statements | version: DI API 10.0 | verified: 2026-10-01 -->

# DI API common mistakes

Wrong pattern → the correct one. Each item names the reference file that backs it; "practice" marks advice SAP
doesn't state. Rows 18-24 were added after reviewing a production integration; `review-checklist.md` has the greps that find them.

| # | Mistake | Do this instead | Backed by |
|---|---|---|---|
| 1 | Ignoring the return code of `Add()` / `Update()` / `Connect()` and carrying on | Check `!= 0` on every call and stop. Inside a transaction SAP has *already rolled back* when a call fails, so code that carries on runs outside it | `Company` class (`StartTransaction` note) |
| 2 | Calling another API method before reading the error | Call `GetLastError(out code, out msg)` immediately after the failing call; the error is lost on the next call | `Company` class (`GetLastError`) |
| 3 | Treating services like business objects (or the reverse) | Business objects return an error code; services throw `COMException` (read `ex.ErrorCode`, `ex.Message`) | `Company` class (sample) |
| 4 | Forgetting `Marshal.ReleaseComObject` after creating a UDF, user table or UDO in .NET | Release the `UserFieldsMD` / `UserTablesMD` / `UserObjectsMD` object right after use; SAP marks it IMPORTANT | `UserFieldsMD` class, `UserTablesMD` class, `UserObjectsMD` class |
| 5 | Leaving the connection open on an error path | `Disconnect()` in a `finally` / `Dispose()`. (practice) | `Company` class (`Disconnect`) |
| 6 | Using `Recordset.DoQuery` to change Business One data | `DoQuery` runs any statement, so it is read-only by convention here; write through business objects or services so business logic runs | `Recordset` class |
| 7 | Removing a document with `Remove()` | Not supported for documents (Purchase Quotation excepted). Cancel it, create a cancellation document, or close it | `Documents` class |
| 8 | A document with no lines, or without the mandatory fields | At least one item line; `CardCode` on the header, `ItemCode` on lines | `Documents` class, `Document_Lines` class |
| 9 | Adding a line by calling `Lines.Add()` first | Set the first line's properties directly; call `Lines.Add()` before each *further* line | `Documents` class (`Add` sample) |
| 10 | Pasting a VB sample into C# (including some that SAP labels "C#") | Translate it; `api/` tags such blocks `vb` | `api/` (the `vb` tags) |
| 11 | Mapping COM `Long` to C# `long` | `Long` is `int` in the interop (SAP's samples use `int errorCode`) | `Company` class (sample) |
| 12 | Assuming `GetByKey` throws when nothing is found | It returns `false` and leaves the object unchanged; check it | `Documents` class (`GetByKey`) |
| 13 | Setting `LicenseServer` | Deprecated since DI API 9.2 PL05; use `SLDServer` | `Company` class |
| 14 | An old `DbServerType` (`dst_MSSQL`, `dst_DB_2`, `dst_SYBASE`, `dst_MAXDB`) | Those are "Not Supported from 8.8"; pick a current value and confirm it for the client's database | `BoDataServerTypes` enum |
| 15 | Guessing an object-type number or enum value | Look it up in the `BoObjectTypes` enum and the other `enums/` files | `enums/` |
| 16 | Hard-coding connection details | Read them from configuration or a secret store. (practice) | |
| 17 | Assuming a 10.0 table or column exists on the client's database (or a 9.3 one on 10.0) | The reference and the default dictionary are 10.0 (a 9.3 dictionary is also bundled); compare against the client's database | `INDEX.md` |
| 18 | Calling a service's `Add` inside the loop that builds the lines | `Add` posts the whole data interface each time, so N lines post N documents, each with the lines so far. Build every line, then call `Add` once | `InventoryPostingsService` class (`Add(pIInventoryPosting)`) |
| 19 | A lookup helper that catches everything and returns `0` / `null` / `""` | The caller cannot tell "not found" from "SQL failed"; `GetByKey(0)` then reports "not found", and a quantity computed from 0 writes stock off. Let the error propagate, or return a clear "not found" result | `Recordset` class (`-2052 No records found`, `MoveFirst` `-1002 Invalid row`); practice |
| 20 | Two owners releasing one `Company` (a module and a wrapper's finalizer), or `GC.Collect()` to "clean up" COM | One owner, `Disconnect` then one `ReleaseComObject`, in `Dispose`; never from a finalizer (the DI API is STA) and never via the GC. (practice) | `Company` class (`Disconnect`) |
| 21 | Connecting the same object twice (constructor and an explicit `Connect`) | One `Connect` per session; a second attempt returns `-116 Already connected to a company database` or leaks the first object | `Company` class (`GetLastError` code table) |
| 22 | Assigning a new `GetBusinessObject` result to the same variable inside a loop | The previous object is never released; release each iteration, or create once outside the loop. (practice) | `Company` class (`GetBusinessObject`) |
| 23 | Treating every `BaseType` as the object number | `Document_Lines.BaseType` is `Long` and takes the object number (`DocObjectCodeEx`); `StockTransfer_Lines.BaseType` is `InvBaseDocTypeEnum`, where `InventoryTransferRequest = 5`, not 1250000001 | `Document_Lines` class, `StockTransfer_Lines` class, `InvBaseDocTypeEnum` enum |
| 24 | Writing the serial number into `BatchNumbers.InternalSerialNumber` / `ManufacturerSerialNumber` and never setting `BatchNumber` | Those properties exist on `BatchNumbers` (so it compiles) but a batch allocation needs `BatchNumber`; this is a copy of the serial branch | `BatchNumbers` class |
