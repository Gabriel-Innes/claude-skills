<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesForecast_Lines (Object)

SalesForecast_Lines is a child object of SalesForecast object and represents sales forecast of items and their quantity for a specified day. Source table: FCT1.

## Properties (6)
- `Public Property Count() As Long` [R] Returns the total rows in the SalesForecast_Lines list.
- `Public Property ForecastedDay() As Date` [R/W] Sets or returns the forecast date for the specified Quantity. Field name: Date.
  - remarks: If the forecast View property is weekly, the date must be the first day of a week. If the forecast View property is monthly, the date must be the first day of a month.
- `Public Property ItemNo() As String` [R/W] Sets or returns the item code in the inventory. Field name: ItemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property Quantity() As Double` [R/W] Sets or returns the sales forecast quantity of ItemNo for the ForecastedDay. Field name: Quantity.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Warehouse() As String` [R/W] property Warehouse

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
