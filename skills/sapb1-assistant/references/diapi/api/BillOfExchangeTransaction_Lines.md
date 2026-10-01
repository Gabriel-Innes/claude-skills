<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BillOfExchangeTransaction_Lines (Object)

BillOfExchangeTransaction_Lines is a child object of the BillOfExchangeTransaction object, and represents the line entries of the Bill Of Exchange Transaction. This object enables you to add a line entry to the Bill Of Exchange Transaction table. Source table: BOT1.

**Remarks:** Mandatory fields in SAP Business One: BillOfExchangeNo and BillOfExchangeType.

## Properties (5)
- `Public Property BillOfExchangeDueDate() As Date` [R] Returns the due date of Bill Of Exchange on which the payment transaction will occur. Field name: DueDate.
- `Public Property BillOfExchangeNo() As Long` [R/W] Sets or returns the Bill Of Exchange number as defined in SAP Business One. Field name: BOENumber. Mandatory field is SAP Business One.
- `Public Property BillOfExchangeType() As BoBOETypes` [R/W] Sets or returns a valid value of BoBOETypes type that specifies the Bill Of Exchange type: incoming or outgoing. Mandatory field is SAP Business One.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
