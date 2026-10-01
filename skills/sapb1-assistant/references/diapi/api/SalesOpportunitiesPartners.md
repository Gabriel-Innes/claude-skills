<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesOpportunitiesPartners (Object)

SalesOpportunityPartner is a child object of the SalesOpportunities object that represents the partners of the sales opportunity. Source table: OPR2.

**Remarks:** To display the form in the application: - Select Sales Opportunities --> Sales Opportunity. - Select the Partners tab.

## Properties (7)
- `Public Property Count() As Long` [R] Returns the total rows in the SalesOpportunitiesPartners list.
  - remarks: When you add a partner to the sales opportunity, the Count value is incremented automatically.
- `Public Property Details() As String` [R/W] Sets or returns the details for the sales opportunity partner. Field name: Memo. Length: 50 characters.
- `Public Property Partners() As Long` [R/W] Sets or returns the partners table. Field name: ParterId. This is a foreign key to the Partners table (OPRT).
- `Public Property RelationshipCode() As Long` [R/W] Sets or returns the relationship ID number. Field name: OrlCode. This is a foreign key to the Relationships object.
- `Public Property RowNo() As Long` [R] Returns the current row number. Field name: Line.
- `Public Property SequenceNo() As Long` [R] Returns the sales opportunities partners, sequence no. Field name: OpportId. Returns the sales opportunity unique ID (primary key). Field name: OpportId.
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
