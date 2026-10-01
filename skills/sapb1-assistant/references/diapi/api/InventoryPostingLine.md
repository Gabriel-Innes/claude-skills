<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InventoryPostingLine (Object)

InventoryPostingLine is a child object of the InventoryPosting object and represents the line entries of the inventory posting transaction. Source table: IQR1. INC1V table is a virtual table to store the line data for inventory counting transaction.

## Properties (45)
- `Public Property ActualPrice() As Double` [R] property ActualPrice
- `Public Property AllowBinNegativeQuantity() As BoYesNoEnum` [R/W] Indicates whether negative quantity in the bin is allowed. Field name: BinNegQty.
- `Public Property BarCode() As String` [R/W] property BarCode
- `Public Property BaseEntry() As Long` [R/W] The base document internal ID. Field name: BaseEntry.
- `Public Property BaseLine() As Long` [R/W] The base document line. Field name: BaseLine.
- `Public Property BaseReference() As String` [R/W] The base document reference. Field name: BaseRef.
- `Public Property BaseType() As Long` [R/W] The base document type. Field name: BaseType.
- `Public Property BinEntry() As Long` [R/W] property BinEntry
- `Public Property CostingCode() As String` [R/W] property CostingCode
- `Public Property CostingCode2() As String` [R/W] property CostingCode2
- `Public Property CostingCode3() As String` [R/W] property CostingCode3
- `Public Property CostingCode4() As String` [R/W] property CostingCode4
- `Public Property CostingCode5() As String` [R/W] property CostingCode5
- `Public Property CountDate() As Date` [R/W] property CountDate
- `Public Property CountedQuantity() As Double` [R/W] property CountedQuantity
- `Public Property CountTime() As Date` [R/W] property CountTime
- `Public Property Currency() As String` [R/W] The price currency. Field name: Currency. Length: 3 characters.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory posting. Field name: DocEntry.
- `Public Property InventoryOffsetDecreaseAccount() As String` [R/W] The accounts in which the inventory decreasing movements are recorded. Field name: DOffDecAcc. Length: 15 characters.
  - remarks: This property is valid only if you use perpetual inventory.
- `Public Property InventoryOffsetIncreaseAccount() As String` [R/W] The accounts in which the inventory increasing movements are recorded. Field name: IOffIncAcc. Length: 15 characters.
  - remarks: This property is valid only if you use perpetual inventory.
- `Public Property InventoryPostingBatchNumbers() As InventoryPostingBatchNumbers` [R] The sub object for you to record the batch number information in inventory posting.
- `Public Property InventoryPostingCCDNumbers() As InventoryPostingCCDNumbers` [R] property InventoryPostingCCDNumbers
- `Public Property InventoryPostingLineUoMs() As InventoryPostingLineUoMs` [R] The sub object for you to specify the unit of measure information for the items you want to post.
- `Public Property InventoryPostingSerialNumbers() As InventoryPostingSerialNumbers` [R] The sub object for you to record the serial number information in inventory posting.
- `Public Property InWarehouseQuantity() As Double` [R] The quantities of the item in warehouses recorded by the system on the selected count date and time. Field name: Quantity.
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property ItemDescription() As String` [R/W] property ItemDescription
- `Public Property ItemsPerUnit() As Double` [R] property ItemsPerUnit
- `Public Property LineNumber() As Long` [R/W] The line number of the inventory posting document. Field name: LineNum.
- `Public Property Manufacturer() As Long` [R/W] property Manufacturer
- `Public Property PostedValueLC() As Double` [R] property PostedValueLC
- `Public Property PostedValueSC() As Double` [R] property PostedValueSC
- `Public Property PreferredVendor() As String` [R/W] property PreferredVendor
- `Public Property Price() As Double` [R/W] The price per unit of the item according to the price type you specified in the Price Source for Whse Inventory Posting field. Field name: Price.
- `Public Property ProjectCode() As String` [R/W] property ProjectCode
- `Public Property Remarks() As String` [R/W] The remarks of the inventory posting document line. Field name: Remark. Length: 254 characters.
- `Public Property SupplierCatalogNo() As String` [R/W] property SupplierCatalogNo
- `Public Property Total() As Double` [R] Total = Price × Variance The total value is displayed in local currency. Field name: DocTotal.
- `Public Property UoMCode() As String` [R/W] property UoMCode
- `Public Property UoMCountedQuantity() As Double` [R/W] property UoMCountedQuantity
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property Variance() As Double` [R/W] property Variance
- `Public Property VariancePercentage() As Double` [R] property VariancePercentage
- `Public Property VisualOrder() As Long` [R] property VisualOrder
- `Public Property WarehouseCode() As String` [R/W] property WarehouseCode

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
