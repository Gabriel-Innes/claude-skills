<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ChartOfAccounts (Object)

ChartOfAccounts is a business object that represents the General Ledger (G/L) accounts in the Finance module. This object enables you to: - Add a G/L account. - Retrieve a G/L account by its key. - Update a G/L account. - Remove a G/L account. - Save the object in XML format. Source table: OACT.

**Remarks:** The Chart of Accounts is an index of all G/L accounts that are used by one or more companies. For every G/L account there is an account number, an account description, and information that determines the function of the account. You have to assign a Chart of Accounts to every company. This Chart of Accounts becomes operative after you carry out posting for these businesses in your daily business. After choosing the most suitable Chart of Accounts, you can customize your choice by adding, adjusting, and changing. However, once posting were made to Chart of Accounts you cannot delete it. Mandatory fields in SAP Business One: Code or FormatCode (when working with account segmentation), and FatherAccountKey. To display the form in the application: - Select Financials --> Chart of Accounts (or Edit Chart of Accounts).

## Properties (78)
- `Public Property AccountLevel() As Long` [R] Returns the level of the account. Field name: Levels.
  - remarks: Level 1 is the drawer level. Levels 2 to 4 are for either titles or accounts. Only an active account can be defined in level 5.
- `Public Property AccountPurposeCode() As SPEDContabilAccountPurposeCode` [R/W] property AccountPurposeCode
- `Public Property AccountType() As BoAccountTypes` [R/W] Sets or returns a valid value of BoAccountTypes that specifies the account type (revenues, expenses, or other) for active accounts only. Field name: ActType.
- `Public Property AcctCurrency() As String` [R/W] Sets or returns the currency in which all the journal entries for that account are recorded. Field name: ActCurr. Length: 3 characters.
  - remarks: In case a journal entry is not connected to the current account, you can update this property to multi-currency only (value ##). In case a journal entry is connected to the current account, you cannot update this property (if you try to update this property, SAP Business One generates an error).
- `Public Property ActiveAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether the account is an active account or just a title. title is used to organize and display data in financial reports, and can summarize several active accounts or several active accounts and titles together. Field name: Postable.
  - remarks: Set tYES for active account. Set tNO for title. You can set up to two levels of titles. The third level must be an active account.
- `Public Property AllowChangeVatGroup() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to allow change of the VAT group. Field name: VatChange.
- `Public Property AllowMultipleLinking() As BoYesNoEnum` [R/W] Specify whether to link this account more than once within the same financial template. Field: MultiLink.
- `Public Property Balance() As Double` [R] Returns the account balance in local currency. Field name: CurrTotal.
  - remarks: The account balance is calculated after recording journal entries. The account balance is displayed in the currency defined for the account (local currency or any foreign currency).
- `Public Property Balance_FrgnCurr() As Double` [R] Returns the account balance in foreign currency. Field name: FcTotal.
- `Public Property Balance_syscurr() As Double` [R] Returns the account balance in system currency. Field name: SysTotal).
- `Public Property BlockManualPosting() As BoYesNoEnum` [R/W] property BlockManualPosting
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BudgetAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account (active account only) is relevant to budget management.
- `Public Property CashAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether the account is a monetary account or indexed account. Field name: CashBox.
  - remarks: Relevant to active accounts only and can be added only to the first two drawers in Chart of Accounts: Assets and Liabilities.
- `Public Property CashFlowRelevant() As BoYesNoEnum` [R/W] property CashFlowRelevant
- `Public Property Category() As Long` [R/W] Sets or returns this chart of account category. Field name: category. This is a foreign key to the OACG object.
- `Public Property Code() As String` [R/W] Sets or returns the G/L account code. Field name: AcctCode. Mandatory field in SAP Business One when not working with segmentation. Length: 15 characters.
- `Public Property CostAccountingOnly() As BoYesNoEnum` [R/W] property CostAccountingOnly
- `Public Property CostElementCode() As String` [R/W] property CostElementCode
- `Public Property CostElementRelevant() As BoYesNoEnum` [R/W] property CostElementRelevant
- `Public Property DataExportCode() As String` [R/W] Sets or returns an alternate code for identifying the account in data that is exported to other programs. Field name: ExportCode. Length: 10 characters.
- `Public Property DatevAccount() As String` [R/W] Property DatevAccount
- `Public Property DatevAutoAccount() As BoYesNoEnum` [R/W] Property DatevAutoAccount
- `Public Property DatevFirstDataEntry() As BoYesNoEnum` [R/W] Property DatevFirstDataEntry
- `Public Property DefaultVatGroup() As String` [R/W] Sets or returns the default VAT group. Field name: DfltVat. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: The VAT groups are defined in SAP Business One and stored in the OVTG table, which is not exposed by the DI API. Country-specific for Europe. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property Details() As String` [R/W] Sets or returns details about the account. Field name: Details. Length: 254 characters.
- `Public Property DistributionRule2Relevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim2Relvnt.
  - remarks: To use multiple distribution rules, from the SAP Business One Main Menu, choose Administration --> System Initialization --> General Settings, and on the Cost Accounting tab, select the Use Multidimensions checkbox.
- `Public Property DistributionRule3Relevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim3Relvnt.
  - remarks: To use multiple distribution rules, from the SAP Business One Main Menu, choose Administration --> System Initialization --> General Settings, and on the Cost Accounting tab, select the Use Multidimensions checkbox.
- `Public Property DistributionRule4Relevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim4Relvnt.
  - remarks: To use multiple distribution rules, from the SAP Business One Main Menu, choose Administration --> System Initialization --> General Settings, and on the Cost Accounting tab, select the Use Multidimensions checkbox.
- `Public Property DistributionRule5Relevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim5Relvnt.
  - remarks: To use multiple distribution rules, from the SAP Business One Main Menu, choose Administration --> System Initialization --> General Settings, and on the Cost Accounting tab, select the Use Multidimensions checkbox.
- `Public Property DistributionRuleRelevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to the distribution rules of corresponding dimensions. Field: Dim1Relvnt.
  - remarks: Distribution rule fields are for G/L accounts of Sales or Expenditure type only.
- `Public Property ExpenseClassificationCategory() As Long` [R/W] property ExpenseClassificationCategory
- `Public Property ExpenseClassificationType() As Long` [R/W] property ExpenseClassificationType
- `Public Property ExternalCode() As String` [R/W] Sets or returns an additional code that is used for information only. The external code allows you to refine queries when generating customized reports. Field name: AccntntCod. Length: 12 characters.
- `Public Property ExternalReconNo() As Long` [R] Returns the external reconciliation number. Field name: ExtrMatch.
  - remarks: SAP Business One provides this number when comparing business accounts with external data such as bank statements.
- `Public Property FatherAccountKey() As String` [R/W] Sets or returns the parent account key that is used to define the G/L account location in drawer. Field name: FatherNum. Mandatory property. Length: 15 characters.
- `Public Property ForeignName() As String` [R/W] Sets or returns an alternative account name (for example in foreign language). Field name: FrgnName. Length: 100 characters.
- `Public Property FormatCode() As String` [R/W] Sets or returns the account number when account segmentation is defined in SAP Business One. Field name: FormatCode. Length: 210 characters. Mandatory field in SAP Business One when working with account segmentation
  - remarks: Retrieving an account that operates with account segmentation When working with segmentation, SAP Business One ignores the account Code and uses only the FormatCode that its value represents the account number in Chart Of Accounts. To retrieve an account that operates with account segmentation: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010). 3. Call the method GetByKey with this value (for example, _SYS00000000010) to retrieve the account. FormatCode Structure The FormatCode can include up to 10 segments. The default account segmentation format in US databases includes four segments as follows: - Natural account - 8 numbers (for example: 11100000) - Division - 2 numbers (for example: 01) - Region - 3 numbers (for example: 001) - Department - 2 numbers (for example: 03) The complete FormatCode is in the example listed above is: 11100000-01-001-03.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim sStr As String

        Dim vRs As SAPbobsCOM.Recordset

        Dim vBOB As SAPbobsCOM.SBObob

        Dim vCH As SAPbobsCOM.ChartOfAccounts

        Set vCH = Vcmp.GetBusinessObject(oChartOfAccounts)

        Set vBOB = Vcmp.GetBusinessObject(BoBridge)

        Set vRs = Vcmp.GetBusinessObject(BoRecordset)

        Set vRs = vBOB.GetObjectKeyBySingleValue(oBusinessPartners, "CardName", "aaa", bqc_Equal)

        ' When working with segmentation use this function

        ' to find the account key in the ChartOfAccount object

        Set vRs = vBOB.GetObjectKeyBySingleValue(oChartOfAccounts, "FormatCode", "125100000100101", bqc_Equal)

        'The Recordset retrieves the value of the key (for example,  sStr = _SYS00000000010).

        sStr = vRs.Fields.Item(0).Value

        'Call the method GetByKey with this value (for example, sStr =_SYS00000000010) to 'retrieve the account

        vCH.GetByKey (sStr)
    ```
- `Public Property FrozenFor() As BoYesNoEnum` [R/W] property FrozenFor
- `Public Property FrozenFrom() As Date` [R/W] property FrozenFrom
- `Public Property FrozenRemarks() As String` [R/W] property FrozenRemarks
- `Public Property FrozenTo() As Date` [R/W] property FrozenTo
- `Public Property IncomeClassificationCategory() As Long` [R/W] property IncomeClassificationCategory
- `Public Property IncomeClassificationType() As Long` [R/W] property IncomeClassificationType
- `Public Property InternalReconNo() As Long` [R] Returns the internal reconciliation number (internal reconciliation are also known as financial statement analyses). Field name: IntrMatch.
  - remarks: SAP Business One provides this number when comparing the credit and debit sides of the accounts and adjust them according to the status of the invoices.
- `Public Property LiableForAdvances() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is liable for advances. Field name: Advance.
- `Public Property LoadingFactorCode() As String` [R/W] The distribution rule for dimension 1 for allocating this account to one or more profit centers. Field name: OverCode This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingFactorCode2() As String` [R/W] The distribution rule for dimension 2 for allocating this account to one or more profit centers. Field name: OverCode2 This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingFactorCode3() As String` [R/W] The distribution rule for dimension 3 for allocating this account to one or more profit centers. Field name: OverCode3 This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingFactorCode4() As String` [R/W] The distribution rule for dimension 4 for allocating this account to one or more profit centers. Field name: OverCode4 This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingFactorCode5() As String` [R/W] The distribution rule for dimension 5 for allocating this account to one or more profit centers. Field name: OverCode5 This is a foreign key to the DistributionRule object.
  - remarks: To set this field, LoadingType must be set to true.
- `Public Property LoadingType() As BoYesNoEnum` [R/W] Indicates whether the chart of accounts is associated with distribution rules, which are defined in the LoadFactorCode properties. Field name: OverType
- `Public Property LockManualTransaction() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account (active account only) can be added to the first two drawers in Chart of Accounts: Assets and Liabilities. Field name: LocManTran.
- `Public Property Name() As String` [R/W] Sets or returns the account name. Field name: AcctName. Length: 100 characters.
- `Public Property PCN874ReportRelevant() As BoYesNoEnum` [R/W] property PCN874ReportRelevant
- `Public Property PlanningLevel() As String` [R/W] The planning level that reflects the typical financial transactions and explains the origin of the data. Field name: PlngLevel. Length: 2 characters.
  - remarks: The property is for SAP Business One integration for SAP NetWeaver - Subsidiary Integration.
- `Public Property PrimaryAccount() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the account is a primary account (fixed). Field name: Fixed.
- `Public Property PrimaryClosingAccount() As String` [R/W] property PrimaryClosingAccount
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code related to the account. Field name: Project. Length: 8 characters. This is a foreign key to the Countries table OPRJ (not exposed through the DI API).
  - remarks: In SAP Business One, you can relate business transactions to projects. This can help you to create cost/income analyzes reports based on projects.
- `Public Property ProjectRelevant() As BoYesNoEnum` [R/W] Specify whether the G/L account is relevant to a project. Field: PrjRelvnt.
- `Public Property Protected() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is confidential. Field name: Protected.
  - remarks: Confidential accounts are protected so that unauthorized users cannot view or update these accounts.
- `Public Property RateConversion() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include the account (active account only) in the calculation of conversion rate differences. Field name: RateTrans.
  - remarks: Relevant to companies where the currency defined in the system is different than the local currency.
- `Public Property ReconciledAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is a reconciliation account. Field name: RealAcct.
  - remarks: Reconciliation accounts, such as tax accounts and goods receipt clearing accounts, cannot be posted manually. The total balance of the customers/vendors must be equal to the control accounts receivables/payables. Manual posting would lead to inconsistencies in the balance sheet/trial balance.
- `Public Property ReferentialAccountCode() As String` [R/W] property ReferentialAccountCode
- `Public Property RevaluationCoordinated() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is coordinated with revaluation. Field name: RevalMatch.
  - remarks: This property is relevant for companies where the defined currency is other than the local currency. Set to tYES, to adjust the balance of the account in the system currency to the balance in the account currency.
- `Public Property StandardAccountCode() As String` [R/W] property StandardAccountCode
- `Public Property TaxExemptAccount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is VAT exempted. Field name: ExmIncome.
- `Public Property TaxLiableAccount() As BoYesNoEnum` [R/W] Field name: . Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the account is liable to VAT. Field name: .
- `Public Property TaxonomyCode() As String` [R/W] property TaxonomyCode
- `Public Property TransactionCode() As String` [R/W] Sets or returns this ChartOfAccount transaction code. Field name: TransCode. Length: 4 characters. This is a foreign key to the OTRC object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ValidFor() As BoYesNoEnum` [R/W] property ValidFor
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidRemarks() As String` [R/W] property ValidRemarks
- `Public Property ValidTo() As Date` [R/W] property ValidTo
- `Public Property VATRegNum() As String` [R] property VATRegNum

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal AccountCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `AccountCode`: Specifies the account code (see Code property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
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
