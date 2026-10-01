<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Items_PreferredVendors (Object)

Items_PreferredVendors is a child object of the Items object that represents the preferred vendor for the item. Source table: ITM2

## Properties (3)
- `Public Property BPCode() As String` [R/W] The code of the vendor. Field name: VendorCode. Length: 15 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property UserFields() As UserFields` [R] Get User Fields

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
