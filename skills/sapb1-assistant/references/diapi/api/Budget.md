<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Budget (Object)

Budget is a business object that represents the budget management in the Finance module. The budget management tracks company expenses and allows to block transactions when the budget exceeds. This object enables you to: - Add a budget object. - Retrieve a budget object by its key. - Update a budget object. - Save the object in XML format. Source table: OBGT.

**Remarks:** To initialize the budget management: - Select Administration --> System Initialization --> General Settings. - In the Budget tab, select Budget Initialization. - Set the budget initialization parameters and click OK. To display the form in the application: - Select Financials --> Budget --> Define Budget. - In the Define Budget dialog box, select a scenario and click OK. The budget management window opens.

## Properties (27)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code as defined in Chart of Accounts. Field name: AcctCode. Length: 15 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BudgetBalanceCreditLoc() As Double` [R] Returns the budget balance in local currency of the revenue account (credit side), based on the journal transactions. Field name: CrdRLTotal.
- `Public Property BudgetBalanceCreditSys() As Double` [R] Returns the budget balance in system currency of the revenue account (credit side), based on the journal transactions. Field name: CrdRSTotal.
- `Public Property BudgetBalanceDebitLoc() As Double` [R] Returns the budget balance in local currency of the account (debit side), based on the journal transactions. Field name: CrdRSTotal.
- `Public Property BudgetBalanceDebitSys() As Double` [R] Returns the budget balance in system currency of the account (debit side), based on the journal transactions. Field name: DebRSTotal.
- `Public Property BudgetScenario() As Long` [R/W] Sets or returns the budget scenario ID number. Field name: Instance. This is a foreign key to the BudgetScenarios object.
- `Public Property CostAccountingLines() As BudgetCostAccounting_Lines` [R] property CostAccountingLines
- `Public Property DivisionCode() As Long` [R/W] Sets or returns the code of the budget distribution method. Field name: BgdCode. This is a foreign key to the BudgetDistribution object.
- `Public Property FutureAnnualExpensesCreditLoc() As Double` [R] Returns the total annual amount (in local currency) of open purchase orders and purchase delivery notes related to the revenue account (credit side). Field name: FtrODRLSum.
- `Public Property FutureAnnualExpensesCreditSys() As Double` [R] Returns the total annual amount (in system currency) of open purchase orders and purchase delivery notes related to the revenue account (credit side). Field name: FtrODRSSum.
- `Public Property FutureAnnualExpensesDebitLoc() As Double` [R] Returns the total annual amount (in local currency) of open purchase orders and purchase delivery notes related to the account (debit side). Field name: FtrOCRLSum.
- `Public Property FutureAnnualExpensesDebitSys() As Double` [R] Returns the total annual amount (in system currency) of open purchase orders and purchase delivery notes related to the account (debit side). Field name: FtrOCRSSum.
- `Public Property FutureAnnualRevenuesCredit() As Double` [R] Returns the future annual income related to the revenue account (credit side). Field name: FtrIDRSSum.
- `Public Property FutureAnnualRevenuesDebit() As Double` [R] Returns the future annual revenue related to the account (debit side). Field name: FtrIDRLSum.
- `Public Property FutureRevenuesDebitLoc() As Double` [R] Returns the future revenue in local currency related to the account (debit side). Field name: FtrICRLSum.
- `Public Property FutureRevenuesDebitSys() As Double` [R] Returns the future revenue in system currency related to the account (debit side). Field name: FtrICRSSum.
- `Public Property Lines() As Budget_Lines` [R] Returns the Budget_Lines object.
- `Public Property Numerator() As Long` [R] Returns the identification key of the budget as assigned by SAP Business One. Field name: SCNCounter.
- `Public Property ParentAccountKey() As String` [R/W] Sets or returns the parent G/L account code as defined in Chart of Accounts. This property is used for automatic calculation of the budget for the account (AccountCode), as a percentage (ParentAccPercent) of the parent account budget. Field name: FatherCode. Length: 15 characters.
- `Public Property ParentAccPercent() As Double` [R/W] Sets or returns the percentage of the parent account budget. Field name: FthrPrcnt.
- `Public Property StartofFiscalYear() As Date` [R] Returns the start date of the fiscal year (financial year). Field name: FinancYear.
- `Public Property TotalAnnualBudgetCreditLoc() As Double` [R/W] Returns the total annual budget in local currency of the revenue account (credit side). Field name: CrdRLTotal.
  - remarks: You must define either the TotalAnnualBudgetCreditLoc Property or the TotalAnnualBudgetDebitLoc Property. The value must be: TotalAnnualBudgetCreditLoc = total values of 12 BudgetTotCredit budget lines
- `Public Property TotalAnnualBudgetCreditSys() As Double` [R/W] Returns the total annual budget in system currency of the revenue account (credit side). Field name: CrdRSTotal.
  - remarks: The value must be: TotalAnnualBudgetCreditSys = total values of 12 BudgetSysTotCredit budget lines
- `Public Property TotalAnnualBudgetDebitLoc() As Double` [R/W] Returns the total annual budget in local currency (debit side). Field name: CredSTotal.
  - remarks: You must define either the TotalAnnualBudgetDebitLoc Property or the TotalAnnualBudgetCreditLoc Property. The value must be: TotalAnnualBudgetDeditLoc = total values of 12 BudgetTotDebit budget lines
- `Public Property TotalAnnualBudgetDebitSys() As Double` [R/W] Returns the total annual budget in system currency (debit side). Field name: DebSTotal.
  - remarks: The value must be: TotalAnnualBudgetDeditSys = total values of 12 BudgetSysTotDebit budget lines
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Key As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Key`: Budget ID number (Numerator).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
