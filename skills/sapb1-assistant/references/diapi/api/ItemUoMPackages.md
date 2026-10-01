<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ItemUoMPackages (Object)

The item UoM package. Source table: ITM4.

## Properties (23)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property Height1() As Double` [R/W] The height for the unit. Field name: Height1.
- `Public Property Height1Unit() As Long` [R/W] The height UoM. Field name: Hght1Unit.
- `Public Property Height2() As Double` [R/W] The height for the unit. Field name: Height2.
- `Public Property Height2Unit() As Long` [R/W] The height UoM. Field name: Hght2Unit.
- `Public Property Length1() As Double` [R/W] The length for the unit. Field name: Length1.
- `Public Property Length1Unit() As Long` [R/W] The length UoM. Field name: Len1Unit.
- `Public Property Length2() As Double` [R/W] The length for the unit. Field name: Length2.
- `Public Property Length2Unit() As Long` [R/W] The length UoM. Field name: Len2Unit.
- `Public Property PackageTypeEntry() As Long` [R/W] The internal key of the package type. Field name: PkgCode.
- `Public Property QuantityPerPackage() As Double` [R/W] The quantity of the package. Field name: QtyPerPack.
- `Public Property UoMEntry() As Long` [R/W] The internal key of the UoM. Field name: UomEntry.
- `Public Property UoMType() As ItemUoMTypeEnum` [R/W] The type of the UoM.
- `Public Property Volume() As Double` [R/W] The volume for the unit. Field name: Volume.
- `Public Property VolumeUnit() As Long` [R/W] The volume UoM. Field name: VolUnit.
- `Public Property Weight1() As Double` [R/W] The weight for the unit. Field name: Weight1.
- `Public Property Weight1Unit() As Long` [R/W] The weight UoM. Field name: Wght1Unit.
- `Public Property Weight2() As Double` [R/W] The weight for the unit. Field name: Weight2.
- `Public Property Weight2Unit() As Long` [R/W] The weight UoM. Field name: Wght2Unit.
- `Public Property Width1() As Double` [R/W] The width for the unit. Field name: Width1.
- `Public Property Width1Unit() As Long` [R/W] The width UoM. Field name: Wdth1Unit.
- `Public Property Width2() As Double` [R/W] The width for the unit. Field name: Width2.
- `Public Property Width2Unit() As Long` [R/W] The width UoM. Field name: Wdth2Unit.

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
