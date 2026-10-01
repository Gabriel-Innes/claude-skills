<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PickLists_Lines (Object)

The PickLists_Lines is a child object of the PickLists object. Each line represents an order and its picking details in the pick list. Source table: PKL1.

**Remarks:** To display the form in the application: - Select Inventory --> Pick and Pack --> Pick List.

## Properties (14)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the pick list row as assinged by SAP Business One when adding a new enrty. Field name: AbsEntry. This is a foreign key to the PickLists object.
- `Public Property BaseObjectType() As String` [R/W] Sets or returns the type of object on which the pick lists entry is based. Field name: BaseObject.
  - remarks: A pick list can be based on one of the following values: 17 - Sales orders. oOrders. 13 - Reserve invoices. oInvoices that their ReserveInvoice value is tYES.
- `Public Property BatchNumbers() As BatchNumbers` [R] property BatchNumbers
- `Public Property BinAllocations() As DocumentLinesBinAllocations` [R] property BinAllocations
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
- `Public Property LineNumber() As Long` [R] Returns the current row number in the pick list. Field name: PickEntry.
- `Public Property OrderEntry() As Long` [R/W] Sets or returns the number of the sales order. Field name: OrderEntry.
  - remarks: DocEntry of Documents(oOrders).
- `Public Property OrderRowID() As Long` [R/W] Sets or returns the LineNum in the document. Field name: OrderLine.
- `Public Property PickedQuantity() As Double` [R/W] Sets or returns the quantity of the items that were picked. Field name: PickQtty.
- `Public Property PickStatus() As BoPickStatus` [R] Returns a valid value that specifies the status of the order row in the pick list. Field name: PickStatus.
- `Public Property PreviouslyReleasedQuantity() As Double` [R] Returns the quantity of the items that were released in the previous pick. Field name: PrevReleas.
- `Public Property ReleasedQuantity() As Double` [R/W] Sets or returns the quantity of the items that were released. Field name: RelQtty.
- `Public Property SerialNumbers() As SerialNumbers` [R] property SerialNumbers
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new record to the PKL1 table.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
