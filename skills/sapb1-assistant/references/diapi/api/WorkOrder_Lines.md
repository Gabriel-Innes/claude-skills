<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WorkOrder_Lines (Object)

WorkOrder_Lines is child object of the WorkOrders object that represents a collection of parent items in a work order. The parent item is connected to its bill of material. Source table: WKO1.

**Remarks:** Mandatory fields in SAP Business One: ItemCode. To display the form in the application: - Select Production --> Work Order. Note: The properties SerialNumbers and BatchNumbers were removed from this object because they are not supported. If you have an add-on from the previous version 6.5 that includes these properties, a compilation error will occur, therefore you must remove these properties from your add-on.

## Properties (11)
- `Public Property ActiveAccountCode() As String` [R/W] Sets or returns the active G/L account code to debit. Field name: ActWorkCod. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property Count() As Long` [R] Returns the total data rows in the WorkOrder_Lines object.
  - remarks: When you add a data row, the value of this property is incremented automatically.
- `Public Property ItemCode() As String` [R/W] Sets or returns the code of the item ordered for production. Mandatory in SAP Business One. Field name: ItemCode. Length: 20 characters. This is a foreign key to the ProductTrees object.
- `Public Property ItemDescription() As String` [R] Returns the item description/name. Field name: Descript. Length: 100 characters.
- `Public Property ItemPrice() As Double` [R/W] Sets or returns the item price. Field name: Price.
  - remarks: This is the price in the price list defined for the production bill of materials. The default price list proposed by the system is the purchasing price list.
- `Public Property ItemQuantity() As Double` [R/W] Sets or returns the quantity of items to be produced. Field name: Quantity.
- `Public Property ItemWarehouse() As String` [R/W] Sets or returns the warehouse where the finished product should be stored. Field name: WhsCode. Length: 8 characters. This is a foreign key to the Warehouses object.
  - remarks: In SAP Business One, if you do not set this property, the system automatically uses the default general storage location predefined in the system.
- `Public Property PriceCurrency() As String` [R/W] Returns the currency of the item price. Field name: Currency. Length: 3 characters.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (starts from 1). Field name: Line_ID.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WorkSum() As Double` [R/W] Sets or returns the labor price. SAP Business One adds this price to the total price (OrderTotal). Field name: ActWorkSum.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
