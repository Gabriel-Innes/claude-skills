<!-- source: REFDI.chm (SAP Business One DI API 10.0 Objects Reference 10.00.190) for the API facts; the patterns come from reviewing a production Granite WMS integration (2026-10); items marked "practice" are engineering advice, not SAP statements | version: DI API 10.0 | verified: 2026-10-01 -->

# Reviewing existing DI API code

Use this when the request is "review / audit / clean up my DI API project" rather than "write me X". Run the greps
over the whole tree first, then read only the files they flag. Each item names the mistake it detects
(`common-mistakes.md` row) or the reference that backs it.

## 1. Inventory first

| Grep (ripgrep syntax) | What it tells you |
|---|---|
| `new SAPbobsCOM\.Company\(\)` | Every place a connection is created. More than one is a smell: connection code is duplicated and will drift (one copy here lacked `dst_MSSQL2022`). |
| `GetBusinessObject\(SAPbobsCOM\.BoObjectTypes\.(\w+)` with `-o`, piped to sort/uniq | Which business objects the code touches, so you can look each class up once in `api/INDEX.md`. |
| `GetCompanyService|GetBusinessService` | Which services are used; services throw `COMException` rather than returning codes (row 3). |
| `DoQuery\(` | Every raw SQL statement. Check each for reads only (row 6) and for string concatenation of user data. |
| `case "[A-Z_]+":` in a dispatcher | The method/route names the integration exposes; these are a deployment contract, keep them all. |

## 2. Correctness patterns

| Grep | Finding | Backed by |
|---|---|---|
| `^\s*\w+\.GetByKey\([^)]*\);\s*$` | `GetByKey` called as a statement: the `false` result is ignored and the empty object is used (blank header, item treated as non-batch) | `Documents`/`Items` class `GetByKey` returns Boolean; row 12 |
| `Service\.Add\(` inside a `foreach`/`for` | A service `Add` per line posts one document per iteration, each carrying the lines accumulated so far | `InventoryPostingsService.Add` takes the whole data interface; row 18 |
| `catch[^{]*\{[^}]*return (0|null|"");` (multiline) | Lookup helpers that swallow errors: `GetByKey(0)` then fails as "not found", or a quantity is computed from 0 | row 19 |
| `rs\.MoveFirst\(\)` without a nearby `EoF`/`RecordCount` check | Empty result sets throw -1002 "Invalid row" instead of a clear message | `Recordset.MoveFirst` returns -1002 |
| `\(int\)rs\.Fields\.Item|\(double\)rs\.Fields\.Item` | Unboxing casts on `Field.Value` (`object`): use `Convert.ToInt32`/`ToDouble` | guide § 7 |
| `GetLastError` not within a few lines after each `\.Add\(\)` / `\.Update\(\)` / `\.Connect\(\)` | Error read too late or not at all | `Company.GetLastError` remarks; rows 1, 2 |
| `\.Connect\(\)` appearing twice on one object's path (constructor and an explicit call) | Second connect returns -116 "Already connected" or leaks the first `Company` | `Company.GetLastError` code table; row 21 |
| `Lines\.BaseType = .*InvBaseDocTypeEnum|Lines\.BaseType = int\.Parse` | Mixed base-type kinds: `StockTransfer_Lines.BaseType` is `InvBaseDocTypeEnum` (InventoryTransferRequest = 5), `Document_Lines.BaseType` is the object number | row 23 |
| `BatchNumbers\.(InternalSerialNumber|ManufacturerSerialNumber)` | Serial fields on a batch allocation with no `BatchNumber` set: almost always a copy-paste from the serial branch | `BatchNumbers` class |
| `Lines\.Quantity = .*transactions\[0\]` | Loop body indexing the first element instead of the loop variable | practice |

## 3. COM lifetime

| Grep | Finding | Backed by |
|---|---|---|
| `Marshal\.ReleaseComObject\(\w*[cC]ompany` in more than one class, or alongside a wrapper with a finalizer | Two owners release the same `Company`; the second release hits a separated RCW | row 20 (practice) |
| `GC\.Collect\(\)` | Garbage collection used instead of deterministic release; a symptom of leaked objects | row 20 (practice) |
| `= \(SAPbobsCOM\.\w+\)\w+\.GetBusinessObject` inside a loop assigning to a variable declared outside it | Each iteration overwrites the reference without releasing the previous object | row 22 (practice) |
| `~\w+\(\)` (finalizer) in any class holding DI objects | COM released from the finalizer thread; the DI API is STA | row 20 (practice) |
| `UserFieldsMD|UserTablesMD|UserObjectsMD` without a matching `ReleaseComObject` | SAP's one explicit release requirement | row 4 |

## 4. Not defects (do not flag)

- `Lines.Add()` after every line, including the last. SAP's sample adds before each further line; the trailing
  empty line the other order leaves is ignored by the DI API, and it is the pattern most production code uses.
  Mention the documented form, don't call it a bug (guide § 11).
- `DocObjectCode` set on a draft before anything else: required, not redundant.
- `BaseType/BaseEntry/BaseLine` assigned before `ItemCode`: deliberate, `ItemCode` triggers SAP's defaults.
- Hard-coded numbering `Series` values: client-database specific by nature; recommend moving them to one place
  per client, not removing them.

## 5. Structural signals (practice)

- Dozens of classes that each connect, look up a DocEntry by DocNum, `GetByKey`, copy header, loop lines, add: the
  code is one pipeline copied per method. Recommend the build-then-commit design in guide § 12 rather than
  patching each copy.
- Method dispatch by a long `switch` on strings: replace with a registry keyed on the same strings, and pin the full
  name list in a test, since the names are configuration at every client.
- `throw ex;` and `throw new Exception(ex.Message)`: both destroy the stack trace; let `SapException`-style errors
  propagate and catch once at the provider boundary.

## 6. Deliver

Group findings as: data-affecting defects (wrong quantities, duplicate postings, silent failures), connection and
COM lifetime, then everything else. Cite the row or class for each. List separately the behaviours that look wrong
but may be intended for the client (direction of a document copy, dropped second rows, series keys that cannot match)
and ask rather than fix.
