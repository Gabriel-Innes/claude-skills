<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ItemsDepreciationParameters (Object)

ItemsDepreciationParameters is a child object of the Items object. You can specify depreciation parameters for a fixed asset. Source table: ITM7.

**Remarks:** To access the subtab, from the SAP Business One Main Menu, choose Financials --> Fixed Assets --> Asset Master Data. Select the Fixed Assets tab and then the Overview subtab.

## Properties (11)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DepreciationArea() As String` [R/W] The depreciation area in which the asset's depreciation takes effect. Field name: DprArea. Length: 15 characters.
- `Public Property DepreciationEndDate() As Date` [R] The depreciation end date, which is calculated based on the depreciation start date and the useful life. Field name: DprEnd.
- `Public Property DepreciationStartDate() As Date` [R/W] The asset's depreciation start date. Once you change the date, the system automatically recalculates the depreciation and updates the asset-relevant values. Field name: DprStart.
- `Public Property DepreciationType() As String` [R/W] The depreciation type in the depreciation area. Field name: DprType. Length: 15 characters.
- `Public Property FiscalYear() As String` [R/W] The fiscal year you have selected in the Fiscal Year field in the Asset Master Data window. Field name: PeriodCat. Length: 10 characters.
- `Public Property RemainingLife() As Double` [R] The asset's remaining life, which is calculated based on the useful life and the depreciation start date. Field name: RemainLife.
- `Public Property RemainingUnits() As Long` [R] property RemainingUnits
- `Public Property StandardUnits() As Long` [R] property StandardUnits
- `Public Property TotalUnitsInUsefulLife() As Long` [R/W] property TotalUnitsInUsefulLife
- `Public Property UsefulLife() As Long` [R/W] The asset's useful life, in months. Field name: UsefulLife.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
