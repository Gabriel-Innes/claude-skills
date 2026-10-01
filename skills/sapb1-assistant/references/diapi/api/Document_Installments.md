<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Document_Installments (Object)

A child object of Documents object representing the installments feature in marketing documents. Source tables: INV6, OPCH6.

**Remarks:** To access installments in the application: Sales-A/R > A/R invoice > Accounting tab > Installments.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Sub Installments

          Try

              Dim oInv As SAPbobsCOM.Documents

              Dim oIns As SAPbobsCOM.Document_Installments

              'Create Invoice Object

              oInv = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oInvoices)

              'Set Invoice Header Values

              oInv.CardCode = Some Card Code

              oInv.DocDueDate = Doc Date

              If optApplyTaxFirst.Checked = True Then

                  oInv.ApplyTaxOnFirstInstallment = SAPbobsCOM.BoYesNoEnum.tYES

              End If

              'Set Invoice Line Values

              oInv.Lines.ItemCode = Some Item Code

              oInv.Lines.Quantity = Quantity

              oInv.Lines.Price = Price

              'Set Installments

              oIns = oInv.Installments

              'Installment #1

              oIns.DueDate = Installment #1 Date

              oIns.Percentage = Percentage

              oIns.Add()

              'Installment #2, completes #1 to 100%

              oIns.DueDate = Installment #2 Date

              oIns.Percentage = Percentage

              lRetCode = oInv.Add ' Try to add the invoice to the database

              If lRetCode <> 0 Then

                  oCompany.GetLastError(lErrCode, sErrMsg)

                  MsgBox(lErrCode & " " & sErrMsg) ' Display error message

              Else

                  MsgBox("Invoice Added to DataBase", MsgBoxStyle.Information, "Invoice Added")

              End If

          Catch ex As Exception

              MsgBox(ex.Message)

          End Try

  End Sub
  ```

## Properties (10)
- `Public Property Count() As Long` [R] Returns a value specifying the number of installments.
- `Public Property DueDate() As Date` [R/W] Returns or sets the due date of the installment. Field name: DueDate
- `Public Property DunningLevel() As Long` [R/W] Returns the dunning level. Field name: DunnLevel. This is a foreign key to the DunningLetters object.
  - remarks: Dunning is the process of methodically communicating with customers to insure the collection of accounts receivable. It follows the process that progresses from gentle reminders (low level) to almost threatening letters (high level) as accounts become more past due.
- `Public Property InstallmentId() As Long` [R] The ID of the installment. The value, which is a sequence number, is unique for the installments for a specific invoice. Field name: InstlmntID
- `Public Property LastDunningDate() As Date` [R] Returns the date, in which the last dunning letter was sent.
- `Public Property PaymentOrdered() As BoYesNoEnum` [R] property PaymentOrdered
- `Public Property Percentage() As Double` [R/W] Sets or returns the installments percentage within the total payment amount. Field name: InstPrcnt
  - remarks: Set either the Percentage or Total property, but not both.
- `Public Property Total() As Double` [R/W] Sets or returns the total payment amount based on the specified percentage. Field name: InsTotal
  - remarks: Set either the Percentage or Total property, but not both.
- `Public Property TotalFC() As Double` [R/W] Total amount in foreign currency. Field name: InsTotalFC
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: Installments can be applied to draft documents as well (ODRF and DRF6). You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes a specific installments before added to the document.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
