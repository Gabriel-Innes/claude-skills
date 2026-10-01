<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxJurisdictions (Object)

Represents the tax amount of a document. Source table: PCH4. TaxJurisdictions is a child object of the following existing objects: - Document_Lines object (Source table: PCH1) - Document_LinesAdditionalExpenses object (Source table: PCH2) - DocumentsAdditionalExpenses object (Source table: PCH3)

**Example:**
- C# example (from SAP's help):
  ```csharp
  oc.CardCode = "C20000";
              doc.DocDate = DateTime.Today;
              doc.DocDueDate = DateTime.Today;
              doc.Lines.ItemCode = "A00001";
              doc.Lines.Quantity = 2;
              doc.Lines.UnitPrice = 100;
              doc.Lines.TaxCode = "1101-001";

             // Set Line Freight External Tax
              doc.Lines.Expenses.ExpenseCode = 2;
              doc.Lines.Expenses.LineTotal = 100;
              doc.Lines.Expenses.TaxCode = "1101-005";
              doc.Lines.Expenses.TaxJurisdictions.Add();
              doc.Lines.Expenses.TaxJurisdictions.SetCurrentLine(0);
              doc.Lines.Expenses.TaxJurisdictions.JurisdictionCode = "IC18BT01";
              doc.Lines.Expenses.TaxJurisdictions.JurisdictionType = 10;
              doc.Lines.Expenses.TaxJurisdictions.ExternalCalcTaxAmount = 20;
              doc.Lines.Expenses.TaxJurisdictions.ExternalCalcTaxRate = 6;

              doc.Lines.Expenses.TaxJurisdictions.Add();
              doc.Lines.Expenses.TaxJurisdictions.SetCurrentLine(1);
              doc.Lines.Expenses.TaxJurisdictions.JurisdictionCode = "IP15BT01";
              doc.Lines.Expenses.TaxJurisdictions.JurisdictionType = 16;
              doc.Lines.Expenses.TaxJurisdictions.ExternalCalcTaxAmount = 50;
              doc.Lines.Expenses.TaxJurisdictions.ExternalCalcTaxRate = 2;
              doc.Add();
  ```

## Properties (15)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalCalcTaxAmount() As Double` [R/W] The external calculated tax amount, in local currency. Field name: ExtTaxSum.
- `Public Property ExternalCalcTaxAmountFC() As Double` [R/W] Returns the external calculated tax amount, in foreign currency. Field name: ExtTaxSumF.
- `Public Property ExternalCalcTaxAmountSC() As Double` [R] Returns the external calculated tax amount, in system currency. Field name: ExtTaxSumS.
- `Public Property ExternalCalcTaxRate() As Double` [R/W] External calculated tax rate. Field: ExtTaxRate.
- `Public Property JurisdictionCode() As String` [R/W] The jurisdiction tax code. Field: StaCode. Length: 8 characters.
- `Public Property JurisdictionType() As Long` [R/W] The type of the jurisdiction tax code. Field: staType.
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property RowSequence() As Long` [R] property RowSequence
- `Public Property TaxAmount() As Double` [R/W] The tax amount, in local currency, calculated for the transaction. You can manually adjust the tax amount according to the business need. Field name: TaxSum.
- `Public Property TaxAmountFC() As Double` [R] Returns the tax amount, in foreign currency, calculated for the transaction. Field name: TaxSumFrgn.
- `Public Property TaxAmountSC() As Double` [R] Returns the total tax amount, in system currency, calculated for the transaction. Field name: TaxSumSys.
- `Public Property TaxRate() As Double` [R] The rate of the jurisdiction tax. Field: TaxRate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
