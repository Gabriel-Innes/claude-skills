<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ItemsDistributionRules (Object)

ItemsDistributionRules is a child object of the Items object. You can assign distribution rules to an asset to facilitate cost accounting. Source table: ITM6.

**Remarks:** For asset transactions that create journal entries, SAP Business One carries forward the relevant projects and distribution rules to the journal entries. To access the subtab, from the SAP Business One Main Menu, choose Financials --> Fixed Assets --> Asset Master Data. Select the Fixed Assets tab and then the Cost Accounting subtab.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for dimension 1 that you want to assign to the asset. Field name: OcrCode. Length: 8 characters.
- `Public Property DistributionRule2() As String` [R/W] The distribution rule for dimension 2 that you want to assign to the asset. Field name: OcrCode2. Length: 8 characters.
- `Public Property DistributionRule3() As String` [R/W] The distribution rule for dimension 3 that you want to assign to the asset. Field name: OcrCode3. Length: 8 characters.
- `Public Property DistributionRule4() As String` [R/W] The distribution rule for dimension 4 that you want to assign to the asset. Field name: OcrCode4. Length: 8 characters.
- `Public Property DistributionRule5() As String` [R/W] The distribution rule for dimension 5 that you want to assign to the asset. Field name: OcrCode5. Length: 8 characters.
- `Public Property LineNumber() As Long` [R] The current row number in the list. Field name: LineNum.
- `Public Property ValidFrom() As Date` [R/W] The start date of the period during which you want to assign a distribution rule to the asset. Field name: ValidFrom.
- `Public Property ValidTo() As Date` [R/W] The end date of the period during which you want to assign a distribution rule to the asset. Field name: ValidTo.

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
