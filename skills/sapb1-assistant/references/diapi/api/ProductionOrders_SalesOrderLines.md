<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProductionOrders_SalesOrderLines (Object)

The ProductionOrders_SalesOrderLines is a child object of the ProductionOrders object. You can set the sales order to which to link the production order. Source table: WOR2.

**Remarks:** To display the form in the application, choose Production --> Production Orders. And click the link button of the Sales Order field.

## Properties (5)
- `Public Property BaseAbsEntry() As Long` [R] The production order base entry. Field name: BaseEntry.
- `Public Property BaseLine() As Long` [R] The production order base line. Field name: BaseLine.
- `Public Property BaseNumber() As Long` [R] The production order base number. Field name: BaseNum.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DocEntry() As Long` [R] The internal ID of the production order. Field name: DocEntry.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
