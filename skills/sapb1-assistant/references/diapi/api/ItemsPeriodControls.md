<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ItemsPeriodControls (Object)

ItemsPeriodControls is a child object of the Items object. You can define the depreciation calculation factors for different periods when you depreciate an asset using the straight line period control method with individual period control. Source table: ITM11.

**Remarks:** To access the Depreciation Period Control window, do the following: From the SAP Business One Main Menu, choose Financials --> Fixed Assets --> Asset Master Data, and select the Fixed Assets tab. On the Overview subtab of the Fixed Assets tab, select the row with the intended depreciation type in the Depreciation Parameters table and choose the Period Control pushbutton.

## Properties (7)
- `Public Property ActualUnits() As Long` [R/W] property ActualUnits
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DepreciationArea() As String` [R/W] The depreciation area in which the asset's depreciation takes effect. Field name: DprArea. Length: 15 characters.
- `Public Property DepreciationStatus() As BoYesNoEnum` [R/W] Indicates whether to depreciate the asset in the period. Field name: DprSt.
- `Public Property Factor() As Double` [R/W] The factor for the calculation of depreciation in the period. Field name: factor.
- `Public Property FiscalYear() As String` [R/W] The fiscal year you have selected in the Fiscal Year field in the Asset Master Data window. Field name: PeriodCat. Length: 10 characters.
- `Public Property SubPeriod() As Long` [R/W] The sub period. Field name: VisOrder.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
