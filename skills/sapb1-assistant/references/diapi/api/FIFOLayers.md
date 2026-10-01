<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FIFOLayers (Object)

Specifies the FIFO layers to be updated, and the new values for the quantity and price. Source table: MRV2

**Remarks:** A FIFO layer is identified by its LayerID and TransactionSequenceNum properties. For more information, see the Layer object.

## Properties (7)
- `Public Property BaseLine() As Long` [R/W] property BaseLine
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property LayerID() As Long` [R/W] A layer ID. Obtain the ID for a specific layer from the Layer object.
- `Public Property LineTotal() As Double` [R/W] The new total value for this FIFO layer. Only relevant when the revaluation method is inventory debit/credit (see RevalType property of the MaterialRevaluation object).
- `Public Property Price() As Double` [R/W] The new price for this FIFO layer. Only relevant when the revaluation method is price change (see RevalType property of the MaterialRevaluation object).
- `Public Property Quantity() As Double` [R/W] The quantity of this FIFO layer to be revalued. Only relevant when the revaluation method is inventory debit/credit (see RevalType property of the MaterialRevaluation object).
- `Public Property TransactionSequenceNum() As Long` [R/W] A layer transaction sequence number. Obtain the ID for a specific layer from the Layer object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
