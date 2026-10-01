<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DocumentPackageItems (Object)

A data structure holding the properties of items in a package. Access this structure via DocumentPackages.Items. Source table: DLN8.

## Properties (7)
- `Public Property Count() As Long` [R] Returns the number of different items in the package.
- `Public Property ItemCode() As String` [R/W] Sets or returns the code of the item in the package.
- `Public Property MeasureUnit() As String` [R] The measure unit. Field name: UnitMsr.
- `Public Property Quantity() As Double` [R/W] Sets or returns the quantity of an item in the package.
- `Public Property UnitsOfMeasurement() As Double` [R/W] The quantity in the UoM. Field name: NumPerMsr.
- `Public Property UoMEntry() As Long` [R/W] The internal key of the UoM. Field name: UomEntry.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

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
