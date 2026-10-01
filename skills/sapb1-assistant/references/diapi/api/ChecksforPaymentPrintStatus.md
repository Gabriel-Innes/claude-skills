<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ChecksforPaymentPrintStatus (Object)

Represents the print status of Checks for Payment. Source table: CHO2.

**Remarks:** To display the form in the application: Select Banking --> Outgoing Payments --> Check Number Confirmation.

**Example:**
- C# example (from SAP's help):
  ```csharp
  ChecksforPayment.PrintStatus.PrintStatus = ""V"";
  ChecksforPayment.PrintStatus.CheckNumber = ""1"";
  ChecksforPayment.PrintStatus.DocEntry = ""1"";
  ChecksforPayment.PrintStatus.LineNumber = ""1"";
  ChecksforPayment.PrintStatus.PrintedBy = 0;
  ChecksforPayment.PrintStatus.Count;
  ```

## Properties (6)
- `Public Property CheckNumber() As Long` [R/W] The check number. Field name: ChkNum.
- `Public Property Count() As Long` [R] The count of rows. Field name: LogInstanc.
- `Public Property DocEntry() As Long` [R/W] The index (Primary Key). Field name: AbsEntry.
- `Public Property LineNumber() As Long` [R/W] The row number (Primary Key). Field name: LineNum.
- `Public Property PrintedBy() As Long` [R/W] The ID of a user. Field name: PrnBy.
- `Public Property PrintStatus() As String` [R/W] The print status of checks. Field name: Status. Length: 1 characte. Values: D=Details, N=Not Confirmed, O=Overflow, T=Not Printed, V=Void.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
