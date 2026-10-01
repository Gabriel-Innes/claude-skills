<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DeductionTaxHierarchies_Lines (Object)

The DeductionTaxHierarchies_Lines is a child object of DeductionTaxHierarchies object. It enables to define the deduction percentage and maximum amount for each taxation level. Source table: DDT1.

**Remarks:** Country-specific for Israel. To display the form in the application: - Select Business Partners -->Business Partner Master Data -->Accounting tab -->Tax tab. - Click the Hierarchies button. - Click the Withholding Tax Deduction Hierarchy button.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DeductionPercent() As Long` [R/W] Sets or returns the Deduction Percent . Field name: DdctPrcnt.
- `Public Property MaximumTotal() As Double` [R/W] Sets or returns the maximum amount for which the deduction percentage applies. Field name: MaxSum.
- `Public Property RowNumber() As Long` [R] Returns the row number of the taxation level. Field name: LineNum.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
