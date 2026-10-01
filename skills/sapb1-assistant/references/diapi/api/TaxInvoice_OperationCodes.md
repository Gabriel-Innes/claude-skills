<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxInvoice_OperationCodes (Object)

TaxInvoice_OperationCodes is a child object of the TaxInvoices object that represents the operation codes of the tax invoice document.

## Properties (5)
- `Public Property BaseEntry() As Long` [R] Document key of tax invoice. Same as DocEntry of TaxInvoices object.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property LineNum() As Long` [R/W] Obsolete. Do not use anymore.
- `Public Property OpCode() As Long` [R/W] The operation code.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
