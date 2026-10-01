<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BatchNumbers (Object)

BatchNumbers is a business object that represents the batch numbers of an item in the Inventory and Production module. This object enables you to add batch numbers for a selected item row (one record per item). Source table: OBTN, OBTW, OBTQ, OITL, ITL1.

**Remarks:** Mandatory field in SAP Business One: BatchNumber. To display the form in the application: - Select Inventory --> Item Management --> Batches --> Define and Update Batch Numbers. - In the Batch No. for Receipt - Selection Criteria window, set your selection criteria and then click OK. Deallocate Batches To deallocate batches without actually remove them from the stock (based on a delivery document) is to update the Sales Order so that it has no batches defined. Note that batches allocated by Reserve Invoice cannot be deallocated. Batches allocated by Reserve Invoice can only be drawn to a Delivery or Invoice document.

## Properties (16)
- `Public Property AddmisionDate() As Date` [R/W] Sets or returns the admission date for the batch. Field name: InDate.
- `Public Property BaseLineNumber() As Long` [R/W] Sets or returns the row number in the current document. Field name: BaseNum.
- `Public Property BatchNumber() As String` [R/W] Sets or returns the batch number. The combination of the batchNumber, ItemCode, and WarehouseCode values must be unique. Field name: BatchNum. Mandatory property. Length: 32 characters.
- `Public Property Count() As Long` [R] Returns the number of records in the BatchNumbers object.
- `Public Property ExpiryDate() As Date` [R/W] Sets or returns the expiration date for the batch. Field name: ExpDate.
- `Public Property InternalSerialNumber() As String` [R/W] Sets or returns the internal serial number for the item. Length: 32 characters. Field name: IntrSerial.
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property Location() As String` [R/W] Sets or returns the location of the batch, for example, in the warehouse. Length: 100 characters. Field name: Located.
- `Public Property ManufacturerSerialNumber() As String` [R/W] Sets or returns the manufacturer's serial number for the selected item. Field name: SuppSerial. Length: 32 characters.
- `Public Property ManufacturingDate() As Date` [R/W] Sets or returns the manufacturing date for the batch. Field name: PrdDate.
- `Public Property Notes() As String` [R/W] Sets or returns a memo type string that specifies comments for the batch number. Length: 64,000 characters. Field name: Notes.
- `Public Property Quantity() As Double` [R/W] Sets or returns the quantity of items that are used to define or update batch numbers. Field name: Quantity.
- `Public Property SystemSerialNumber() As Long` [R/W] property SystemSerialNumber
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
