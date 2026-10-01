<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Boxes1099 (Object)

Boxes1099 is a child object of the Forms1099 object. It enables to add 1099 reporting boxes to a specified 1099 Form type. Source table: TNN1.

**Remarks:** Country-specific for USA only. To display the form in the application: - Select Administration -->Setup -->Financials -->1099 Table. - Double-click the number on the left of the 1099 Form type for which you want to add 1099 Boxes.

## Properties (6)
- `Public Property Box1099() As String` [R/W] Sets or returns the name of the 1099 reporting box. Field name: Box1099. Length: 20 characters.
- `Public Property BoxDescription() As String` [R/W] Sets or returns the description of the 1099 reporting box. Field name: BoxDescr. Length: 100 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property FormCode() As Long` [R] Returns the identification key of the 1099 Form type as assigned by the system when adding a new 1099 Form type. Field name: FormCode.
- `Public Property Minimum1099Amount() As Double` [R/W] Sets or returns the minimum amount to include in the 1099 report.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
