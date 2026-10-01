<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SerialNumbers (Object)

SerialNumbers is a business object that represents the serial numbers and additional tracking information of items. This object is part of the Inventory and Production module. Source table: OSRN, OSRW, OSRQ, OITL, ITL1.

**Remarks:** This object helps you to track items using their serial number. A computer, for example, can be located by its serial number. The serial number can provide additional information regarding a specific item such as its manufacturing date, warranty data, location in warehouse, and so on. To display the form in the application: - Select Inventory --> Item Management --> Serial Number --> Serial Numbers Management. - Set your selection criteria and click OK. (The form will appear only if Serial Numbers are defined for the selected items.) To de-allocate batches without actually remove them from stock (based Delivery), update SO so that it has no batches defined - it works this way in the UI and should work in DI the same - if not it should be fixed. Please note that batches allocated by Reserve Invoice canNOT be deallocated this way since we do not support Reserve Invoice updating. Batches allocated by Reserve Invoice can only be drawn to the Delivery/Invoice.

## Properties (18)
- `Public Property BaseLineNumber() As Long` [R/W] Sets or returns the Row No. in thhDocument. Field name: BaseLinNum.
  - remarks: Sets or returns the row number in the current document.
- `Public Property BatchID() As String` [R/W] Sets or returns the unique batch number of an item. Field name: BatchId. Length: 32 characters. This is a foreign key to the SerialNumbers object.
- `Public Property Count() As Long` [R] Returns the total data rows in the SerialNumbers object.
  - remarks: When you add a data row, the Count value is incremented automatically.
- `Public Property ExpiryDate() As Date` [R/W] Sets or returns the expiration date for the item. Field name: ExpDate.
- `Public Property InternalSerialNumber() As String` [R/W] Sets or returns the internal serial number for the item. Field name: IntrSerial. Length: 32 characters. This is a foreign key to the SerialNumbers object.
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property Location() As String` [R/W] Sets or returns the location of the item, for example, in the warehouse. Field name: Located. Length: 100 characters.
- `Public Property ManufactureDate() As Date` [R/W] Sets or returns the manufacturing date for the batch. Field name: PrdDate.
- `Public Property ManufacturerSerialNumber() As String` [R/W] Sets or returns the manufacturer's serial number for the selected item. Field name: SuppSerial. Length: 32 characters. This is a foreign key to the SerialNumbers object.
- `Public Property Notes() As String` [R/W] Sets or returns a memo type string that specifies comments for the item. Field name: Notes. Length: 64,000 characters.
- `Public Property Quantity() As Double` [R/W] The total number of serial numbers for the item. Field name: Quantity.
- `Public Property ReceptionDate() As Date` [R/W] Sets or returns the reception date. Field name: InDate.
- `Public Property SystemSerialNumber() As Long` [R/W] Sets or returns the successive numerator starting from1 issued for each item with serial numbers management. This numerator progresses according to the creation of new units of the same sort (for the same item). This property is mandatory when using Serial Numbers for outgoing documents. Field name: SysSerial. This is a foreign key to the SerialNumbers object.
  - remarks: Using System Serial Number - This property is mandatory when using existing serial numbers through the DI API. - When you set this property it means that you want to use an existing serial number. If the system serial number does not exist, any action will fail. - When you do not set this properyt (empty) it means that you want to create a new serial number. You cannot provide a system number of your choice to create a new serial number.
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WarrantyEnd() As Date` [R/W] Sets or returns the warranty end date for the items. Field name: GrntExp.
- `Public Property WarrantyStart() As Date` [R/W] Sets or returns the warranty start date for the items. Field name: GrntStart.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
