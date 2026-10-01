<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesOpportunitiesInterests (Object)

SalesOpportunitiesInterests is a child object of the SalesOpportunities object and represents the interests range of sales opportunity. Source table: OPR4.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - Select the Potential tab (the Interset Range table is enabled only when the sales opportunity status is Open).

## Properties (6)
- `Public Property Count() As Long` [R] Returns the total rows in the SalesOpportunitiesInterests list.
- `Public Property InterestId() As Long` [R/W] Sets or returns the interest ID. This is a foreign key to the Interest table (OOIN), which is exposed via the SalesOpportunityInterestsSetupService object. Field name: IntId.
- `Public Property PrimaryInterest() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the sales opportunity interset is primary. Field name: Prmry.
- `Public Property RowNo() As Long` [R] Returns the current available row number (starts from 1). Field name: Line. Returns the current available row number (starts from 1). Field name: Line_ID.
- `Public Property SequenceNo() As Long` [R] Returns the sales opportunity unique ID (primary key). Field name: OpportId.
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
