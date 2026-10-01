<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Document_SpecialLines (Object)

This object represents text and subtotal lines in marketing documents. Source table: INV10 and IN10V (a virtual table for storing calculated values).

**Remarks:** In text line, you can add remarks. In subtotal line, you can calculate subtotal of previous lines. Text and subtotal lines cannot be drawn from the base document.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Sub AddSpecialLine()

          'Adding special line

          'Assume Qut is an existing Quotation Document Object

          'Setting the type of special line to be sub total

          Qut.SpecialLines.LineType = SAPbobsCOM.BoDocSpecialLineType.dslt_Subtotal

          'Setting the after line number

          'A number that says after which line the special line will appear

          Qut.SpecialLines.AfterLineNumber = 2

          'Check for errors

          lRetCode = Qut.Update()

          If lRetCode <> 0 Then

              oCompany.GetLastError(lErrCode, sErrMsg)

              MsgBox(lErrCode & " " & sErrMsg) ' Display error message

          Else

              MsgBox("Special Lines Added")

          End If

  End Sub
  ```

## Properties (24)
- `Public Property AfterLineNumber() As Long` [R/W] Returns or sets the line number after which the text or subtotal line will appear. This property is mandatory. You must set this property in incremental order. Table: INV10. Field name: AftLineNum.
- `Public Property Count() As Long` [R] Returns the number of special lines in the document.
- `Public Property Freight1() As Double` [R] Returns a calculated value of the 1st freight expense in local currency. Source table: IN10V (virtual table).
- `Public Property Freight1FC() As Double` [R] Returns a calculated value of the 1st freight expense in foreign currency. Source table: IN10V (virtual table).
- `Public Property Freight1SC() As Double` [R] Returns a calculated value of the 1st freight expense in system currency. Source table: IN10V (virtual table).
- `Public Property Freight2() As Double` [R] Returns a calculated value of the 2nd freight expense in local currency. Source table: IN10V (virtual table).
- `Public Property Freight2FC() As Double` [R] Returns a calculated value of the 2nd freight expense in foreign currency. Source table: IN10V (virtual table).
- `Public Property Freight2SC() As Double` [R] Returns a calculated value of the 2nd freight expense in system currency. Source table: IN10V (virtual table).
- `Public Property Freight3() As Double` [R] Returns a calculated value of the 3rd freight expense in local currency. Source table: IN10V (virtual table).
- `Public Property Freight3FC() As Double` [R] Returns a calculated value of the 3rd freight expense in foreign currency. Source table: IN10V (virtual table).
- `Public Property Freight3SC() As Double` [R] Returns a calculated value of the 3rd freight expense in system currency. Source table: IN10V (virtual table).
- `Public Property GrossTotal() As Double` [R] Returns a calculated value of the gross total in local currency. Source table: IN10V (virtual table).
- `Public Property GrossTotalFC() As Double` [R] Returns a calculated value of the gross total in foreign currency. Source table: IN10V (virtual table).
- `Public Property GrossTotalSC() As Double` [R] Returns a calculated value of the gross total in system currency. Source table: IN10V (virtual table).
- `Public Property LineNum() As Long` [R] Returns the text or subtotal line number.
- `Public Property LineText() As String` [R/W] Returns or sets the string for text line.
- `Public Property LineType() As BoDocSpecialLineType` [R/W] Sets or returns a value specifying the type of the special line (text line or subtotal line).
  - remarks: Default is text.
- `Public Property OrderNumber() As Long` [R] Returns the order of the text or subtotal line. The order of the line is specified by the order you have added the line in the DI API.
  - remarks: This property is mandatory. In update, or delete, the line order is auto-completed by the application.
- `Public Property Subtotal() As Double` [R] Returns a calculated value of the sub total in local currency. Source table: IN10V (virtual table).
- `Public Property SubtotalFC() As Double` [R] Returns a calculated value of the sub total in foreign currency. Source table: IN10V (virtual table).
- `Public Property SubtotalSC() As Double` [R] Returns a calculated value of the sub total in system currency. Source table: IN10V (virtual table).
- `Public Property TaxAmount() As Double` [R] Returns a calculated value of the tax amount in local currency. Source table: IN10V (virtual table).
- `Public Property TaxAmountFC() As Double` [R] Returns a calculated value of the tax amount in foreign currency. Source table: IN10V (virtual table).
- `Public Property TaxAmountSC() As Double` [R] Returns a calculated value of the tax amount in system currency. Source table: IN10V (virtual table).

## Methods (3)
- `Public Sub Add()` Adds a new text or subtotal line to the document.
- `Public Sub Delete()` Deletes an existing text or subtotal line in the document.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
