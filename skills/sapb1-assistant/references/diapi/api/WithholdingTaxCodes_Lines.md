<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WithholdingTaxCodes_Lines (Object)

WithholdingTaxCodes_Lines is a child object of the WithholdingTaxCodes object. It enables to define the tax percentage and the effective from date for the withholding tax code. Source table: WHT1.

**Remarks:** Mandatory property: Effectivefrom Mandatory properties (for India): CessRate, HSCRate, SurchargeRate, TDSRate To display the form in the application: - Select Administration --> Setup --> Financials --> Tax --> Withholding Tax. - Choose the Tax Definition button.

## Properties (22)
- `Public Property CessGSTRate() As Double` [R/W] property CessGSTRate
- `Public Property CessRate() As Double` [R/W] The cess rate.
- `Public Property CGSTRate() As Double` [R/W] property CGSTRate
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property Currency() As String` [R/W] Fixed amount currency. Field name: Currency. Length: 3 characters.
- `Public Property Effectivefrom() As Date` [R/W] Sets or returns the date from which the withholding tax percentage is effective. Mandatory property. Field name: EffecDate.
- `Public Property FixedAmount() As Double` [R/W] Fixed amount. Field name: FixedAmnt.
- `Public Property HSCRate() As Double` [R/W] The HSC rate.
  - remarks: For India only.
- `Public Property IGSTRate() As Double` [R/W] property IGSTRate
- `Public Property ITRNonCompliantRate() As Double` [R/W] TDS ITR noncompliance rate. Field name: ItrNCRate.
  - remarks: For India only.
- `Public Property LineNum() As Long` [R] The ID (line number) of the withholding tax line. Field name: LineNum
- `Public Property PANNonCompliantRate() As Double` [R/W] TDS PAN noncompliance rate. Field name: PanNCRate.
  - remarks: For India only.
- `Public Property ProgressiveTaxLines() As WithholdingTaxCodes_ProgressiveTax_Lines` [R] property ProgressiveTaxLines
- `Public Property Rate() As Double` [R/W] Sets or returns the percentage of the withholding tax. Field name: Rate.
- `Public Property SGSTRate() As Double` [R/W] property SGSTRate
- `Public Property SurchargeRate() As Double` [R/W] The surcharge rate.
  - remarks: For India only.
- `Public Property TDSRate() As Double` [R/W] The TDS rate. Field name: TdsRate.
  - remarks: For India only.
- `Public Property UoMCode() As String` [R] UoM code. Field name: UoMCode. Length: 20 characters.
- `Public Property UoMEntry() As Long` [R/W] UoM entry. Field name: UomEntry.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UTGSTRate() As Double` [R/W] property UTGSTRate
- `Public Property ValueRangeLines() As WithholdingTaxCodes_ValueRange_Lines` [R] property ValueRangeLines

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
