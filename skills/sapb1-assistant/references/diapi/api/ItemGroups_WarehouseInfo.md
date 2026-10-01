<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ItemGroups_WarehouseInfo (Object)

ItemGroups_WarehouseInfo is a child object of the ItemGroups object that represents the items in the warehouse. Source table: OIGW.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DefaultBin() As Long` [R/W] The default bin location in the warehouse for receiving items. Field name: DftBinAbs.
- `Public Property DefaultBinEnforced() As BoYesNoEnum` [R/W] Indicates whether to enforce the use of the default bin location during receipt of items to the warehouse. That is, when you receive an item to the warehouse, you must place it in the default bin location. Field name: DftBinEnfd.
- `Public Property ItemGroupCode() As Long` [R] The item group code. Field name: ItmsGrpCod.
- `Public Property WarehouseCode() As String` [R/W] The warehouse code. Field name: WhsCode. Length: 8 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
