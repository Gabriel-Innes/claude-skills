<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# VatGroups_Lines (Object)

VatGroups_Lines is a child object of the VatGroups_Lines object. It enables to define the tax percentage and the effective from date for the tax group. Source table: VTG1.

**Remarks:** Country-specific for Europe. Mandatory property: Effectivefrom. To display the form in the application: - Select Administration --> Setup --> Financials --> Tax --> Tax Groups. - Click the Tax Definition button.

## Properties (6)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DatevCode() As Long` [R/W] property DatevCode
- `Public Property Effectivefrom() As Date` [R/W] Sets or returns the date from which the tax group's percentage is effective. Mandatory property. Field name: EffecDate.
- `Public Property EqualizationTax() As Double` [R/W] Sets or returns the equalization tax percentage. Field name: EquVatPr.
  - remarks: Country-specific for Spain and Portugal.
- `Public Property Rate() As Double` [R/W] Sets or returns the percentage of the tax group. Field name: Rate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
