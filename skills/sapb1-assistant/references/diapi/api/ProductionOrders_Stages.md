<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProductionOrders_Stages (Object)

The ProductionOrders_Stages is a child object of the ProductionOrders object. You can set the route stages to which to link the production order. Source table: WOR4.

## Properties (11)
- `Public Property CalculationProportion() As Double` [R/W] The percentage of resource capacity that will be consumed in a particular route stage. Field name: RtCalcProp.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DocEntry() As Long` [R] The internal ID of the production order. Field name: DocEntry.
- `Public Property EndDate() As Date` [R/W] The latest date by which a component needs to be used in the production process. Field name: EndDate.
- `Public Property Name() As String` [R/W] The stage name. Field name: Name. Length: 100 characters.
- `Public Property RequiredDays() As Double` [R] The number of days required for a specific Resource to complete the Planned Qty. of a particular route stage. Field name: ReqDays.
- `Public Property SequenceNumber() As Long` [R/W] The sequence number that is assigned to each route stage. The sequence indicates the precise order in which the routing stages must be performed during the production process. Field name: SeqNum.
- `Public Property StageEntry() As Long` [R/W] property StageEntry
- `Public Property StageID() As Long` [R] The stage ID. Field name: StageId.
- `Public Property StartDate() As Date` [R/W] The earliest date on which the component is needed in the production process. For a production order that has route stages, the Start Date for the first Route Stage type line (included in the calculation) is set to the production order header Start Date. And by default, the Start Date for the next Route Stage type line is the same as the calculated End Date of the previous route stage. You can manually change the Route Stage type line Start Date to any date that falls between or is equal to the production order header Start Date and Due Date. Field name: StartDate.
- `Public Property WaitingDays() As Double` [R/W] The number of days to wait after the completion of the route stage. This field will not be visible by default. As soon as a Route Stage type line is created, you can manually enter the number of waiting days. Field name: WaitDays.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
