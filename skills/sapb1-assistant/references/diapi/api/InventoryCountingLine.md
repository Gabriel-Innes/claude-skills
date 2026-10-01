<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InventoryCountingLine (Object)

InventoryCountingLine is a child object of the InventoryCounting object and represents the line entries of the inventory counting transaction. Source table: INC1V, INC1. INC1V table is a virtual table to store the line data for inventory counting transaction.

## Properties (39)
- `Public Property BarCode() As String` [R/W] The barcode of the item. Field name: BarCode. Length: 16 characters.
  - remarks: If you use multiple UoMs (sub object InventoryCountingLineUoM), the value in this property will be ignored.
- `Public Property BinEntry() As Long` [R/W] The bin location for the item you want to count. Mandatory property if you use bin. Field name: BinEntry.
- `Public Property CostingCode() As String` [R/W] The distribution rule for dimension 1 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode. Length: 8 characters.
- `Public Property CostingCode2() As String` [R/W] The distribution rule for dimension 2 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode2. Length: 8 characters.
- `Public Property CostingCode3() As String` [R/W] The distribution rule for dimension 3 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode3. Length: 8 characters.
- `Public Property CostingCode4() As String` [R/W] The distribution rule for dimension 4 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode4. Length: 8 characters.
- `Public Property CostingCode5() As String` [R/W] The distribution rule for dimension 5 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode5. Length: 8 characters.
- `Public Property Counted() As BoYesNoEnum` [R/W] Indicates whether the item was counted, and vice versa. Field name: Counted.
- `Public Property CountedQuantity() As Double` [R/W] The quantity of the item as counted in actual warehouses. Field name: CountQty.
  - remarks: If you use multiple UoM (sub object InventoryCountingLineUoM), the value in this property will be ignored.
- `Public Property CounterID() As Long` [R/W] The ID of the counter. Field name: CounterId.
- `Public Property CounterType() As CounterTypeEnum` [R/W] The type of the counter. Field name: CounteType.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory counting. Field name: DocEntry.
- `Public Property Freeze() As BoYesNoEnum` [R/W] Specify whether you want to freeze an item, that is, prevent any transaction (except inventory posting) that affects the in-warehouse quantity of the item in the selected warehouse and bin. Field name: Freeze.
- `Public Property InventoryCountingBatchNumbers() As InventoryCountingBatchNumbers` [R] The sub object to count inventory by batch number.
- `Public Property InventoryCountingLineUoMs() As InventoryCountingLineUoMs` [R] The sub object to count inventory by unit of measure.
- `Public Property InventoryCountingSerialNumbers() As InventoryCountingSerialNumbers` [R] The sub object to count inventory by serial number.
- `Public Property InWarehouseQuantity() As Double` [R] The quantities of an item in warehouses as recorded by the system on the selected count date and time. Field name: InWhsQty.
- `Public Property ItemCode() As String` [R/W] The code of the item that you specified for the inventory. Mandatory property. Not mandatory only if BarCode is specified and is unique. Field name: ItemCode. Length: 20 characters.
- `Public Property ItemDescription() As String` [R/W] The description of the item that you specified for the inventory. Field name: ItemDesc. Length: 100 characters.
- `Public Property ItemsPerUnit() As Double` [R] The calculated value from the group UoM definition of the item. Inventory Items per Unit = Base Qty ÷ Alt. QQty Field name: ItmsPerUnt.
- `Public Property LineNumber() As Long` [R/W] The line number of the inventory counting document. Field name: LineNum.
- `Public Property LineStatus() As CountingLineStatusEnum` [R/W] Determines this document is open or close. Field name: LineStatus.
- `Public Property Manufacturer() As Long` [R/W] The manufacturer code of the item (foreign key of the Manufacturers object). Field name: FirmCode.
- `Public Property MultipleCounterRole() As MultipleCounterRoleEnum` [R/W] The role of the multiple counters, that is, the multiple counters conduct the inventory counting individually or as a team. Field name: CounteRole.
- `Public Property PreferredVendor() As String` [R/W] The preferred vendor for the item. Field name: PrefVendor. Length: 15 characters.
- `Public Property ProjectCode() As String` [R/W] The project code related to the document. Field name: ProjCode. Length: 20 characters.
- `Public Property Remarks() As String` [R/W] The remarks of the inventory counting document line. Field name: Remark. Length: 254 characters.
- `Public Property SupplierCatalogNo() As String` [R/W] The vendor catalog number. Field name: SuppCatNum. Length: 17 characters.
- `Public Property TargetEntry() As Long` [R] The target document internal ID. Field name: TargetEntr.
- `Public Property TargetLine() As Long` [R] The target document line. Field name: TargetLine.
- `Public Property TargetReference() As String` [R] The target document reference. Field name: TargetRef.
- `Public Property TargetType() As Long` [R] The target document type. Field name: TargetType.
- `Public Property UoMCode() As String` [R/W] The UoM code. Field name: UomCode. Length: 20 characters.
  - remarks: If you use multiple UoM (sub object InventoryCountingLineUoM), the value in this property will be ignored.
- `Public Property UoMCountedQuantity() As Double` [R/W] The counted quantity in the specified UoM. Field name: UomQty.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property Variance() As Double` [R] Displays the difference between the in-warehouse quantity on the count date and the counted quantity. Field name: Difference.
- `Public Property VariancePercentage() As Double` [R] Displays the absolute variance percentage between the in-warehouse quantity on the count date and the counted quantity. Field name: DiffPercen.
- `Public Property VisualOrder() As Long` [R] The visual order number. The value for the first row is null, and from the second row the number starts from 1. Field name: VisOrder.
- `Public Property WarehouseCode() As String` [R/W] The code of the warehouse where the item locates. Mandatory property. Field name: WhsCode. Length: 8 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
