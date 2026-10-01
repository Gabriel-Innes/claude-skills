<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WizardPaymentMethods (Object)

The WizardPaymentMethods object enables to define payment methods, such as check, bank transfer, or bill-of-exchange. Source table: OPYM.

**Remarks:** The payment method then can be assigned to each business partner. During the payment run process (Payment Wizard), the payment method selected for a business partner will affect the way the system clears invoices. To display the form in the application: - Select Administration --> Setup --> Banking --> Payment Methods.

## Properties (54)
- `Public Property Accepted() As String` [R/W] Sets or returns a string value that determines the BOE status, whether it is accepted or not. Field name: Accepted. Length: 1 character.
  - remarks: Applicable for cluster B. Country-specific for Brazil only (BOE in Brazil is called Boleto). This property is defined as BOE Property, used by different Boleto Barcode Algorithms to construct their own Algorithm Structure.
- `Public Property Active() As BoYesNoEnum` [R/W] Indicates whether or not the payment method is in use. Field: Active.
  - remarks: When the Active checkbox status is updated from selected to unselected, the following happens: If this payment method is selected in the Default Payment Method for Customer or Default Payment Method for Vendor dropdown list on the BP tab of the General Settings window (Administration --> System Initialization --> General Settings), the dropdown list is cleared to blank. The Include checkbox of this payment method on the Payment Run tab of the Business Partner Master Data window is treated as if it is unselected, even if it is selected. The Active checkbox of this payment method on the Payment Run tab of the Business Partner Master Data window is deselected. Accounting documents that use this payment method will be listed in the non-included transaction report when they are included in a payment run. When the Active checkbox status is updated from unselected to selected, the Active checkbox of this payment method on the Payment Run tab of the Business Partner Master Data window is selected. This means that, if the Include checkbox is also selected, this payment method will be available for use in business partner master data and accounting documents that will then be fully available when you run the payment wizard.
- `Public Property AgentCollection() As BoYesNoEnum` [R/W] Determines whether or not to display only invoices related to agents in the Payment Wizard. Relevant for Bill of Exchange, payment mean and incoming payments only. Field name: AgtCollect.
  - remarks: Country-specific for France, Italy, Spain and Portugal.
- `Public Property BankAccountKey() As Long` [R] Returns the bank account key. Field name: BnkActKey. This is a foreign key to the HouseBankAccounts object.
- `Public Property BankChargeRate() As Double` [R/W] Specify the bank charge rate as a percentage. For each payment in the payment wizard, the bank charge is calculated as the payment amount multiplied by the bank charge rate. Field: BcgPcnt.
  - remarks: This field is not available when the selected payment means is Bill of Exchange.
- `Public Property BankCountry() As String` [R/W] Sets or returns the house bank country. Field name: BankCountr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property BarcodeDll() As String` [R/W] Sets or returns the name and path of the BOE barcode reader DLL file. Field name: BoeDll. Length: 50 characters.
  - remarks: Applicable for cluster B. Country-specific for Brazil only (BOE in Brazil is called Boleto). This property is defined as BOE Property, used by different Boleto Barcode Algorithms to construct their own Algorithm Structure.
- `Public Property BlockForeignBank() As BoYesNoEnum` [R/W] Determines whether or not to block payment method for business partners for whom the BankCountry (BusinessPartners object) is different than the default country defined for the company BankCountry (AdminInfo). Field name: FrgnBnkBl.
- `Public Property BlockForeignPayment() As BoYesNoEnum` [R/W] Determines whether or not to block payment method for business partners for whom the Bill to Country is different than the country defined for your company CompanyName (AdminInfo). Field name: FrgnPmntBl.
  - remarks: Field name in the database: FrgnPmntBl. Field name in the application: Block Foreign Payment.
- `Public Property Branch() As String` [R] Returns the House Bank Branch no. Field name: Branch. Length: 50 characters.
  - remarks: Field name in the database: Branch. Field name in the application: Branch.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object. Returns the DataBrowser object.
  - remarks: Sample file available at DataBrowser Sample
- `Public Property CancelInstruction() As String` [R/W] property CancelInstruction
- `Public Property CheckAddress() As BoYesNoEnum` [R/W] Determines whether or not to check if the Bill to Address of the business partner is defined in full mode (Name, Street/ P.O. Box, City, Zip Code, Country). Field name: Address.
- `Public Property CheckBankDetails() As BoYesNoEnum` [R/W] Determines whether or not to check if the business partner's bank details: DefaultBankCode and DefaultAccount, are entered in full mode. (BusinessPartners Object ) Field name: BankDet.
- `Public Property CollectionAuthorizationCheck() As BoYesNoEnum` [R/W] Determines whether or not the customer authorizes an automatic files collection from their bank account. Relevant for the OPEX file (PaymentRunExport). Field name: CllctAutor.
- `Public Property CreationDate() As Date` [R] Returns the creation date of a specified check. Field name: CreateDate. Length: 8 characters.
- `Public Property CurCode() As String` [R/W] Sets or returns the BOE currency code. Field name: CurCode. Length: 2 characters.
  - remarks: Applicable for cluster B. Country-specific for Brazil only (BOE in Brazil is called Boleto). This property is defined as BOE Property, used by different Boleto Barcode Algorithms to construct their own Algorithm Structure.
- `Public Property CurrencyRestriction() As BoYesNoEnum` [R/W] Determines whether or not currency restriction exists for payment method. Field name: CurrRestr.
- `Public Property CurrencyRestrictions() As CurrencyRestrictions` [R] Returns the CurrencyRestrictions object. Applicable when the CurrencyRestriction property is set to tYES.
- `Public Property DebitMemo() As BoYesNoEnum` [R/W] Returns whether DebitMemo exists for Payment Method.Determines whether or not to create a corresponding indication in the Payment Run Export (OPEX) file. The Debit Memo indication is required for the Payment Engine add-on. Field name: DebitMemo.
  - remarks: Country-specific for Mexico.
- `Public Property DefaultAccount() As String` [R/W] Sets or returns the default bank account number of the business partner. Field name: DflAccount. Length: 50 characters.
- `Public Property DefaultBank() As String` [R/W] Sets or returns the default bank number. Field name: BnkDflt. Length: 30 characters.
- `Public Property DepositNorm() As String` [R/W] Sets or returns the Bill of Exchange file format for presentation as defined for the banks for each country. Displayed in the OPEX file only. Field name: DepNorm. Length: 8 characters.
- `Public Property Description() As String` [R/W] Sets and return the payment method description. Field name: Descript. Length: 100 Characters.
  - remarks: Field name in the database: Descript. Field name in the application: Description. To display the form in the application: - Select Administration -->Defentions-->Banking-->Payment Methods tab.
- `Public Property DirectDebit() As DirectDebitTypeEnum` [R/W] property DirectDebit
- `Public Property DocType() As String` [R/W] Sets or returns the BOE document type. Field name: DocType. Length: 2 characters.
  - remarks: Applicable for cluster B. Country-specific for Brazil only (BOE in Brazil is called Boleto). This property is defined as BOE Property, used by different Boleto Barcode Algorithms to construct their own Algorithm Structure.
- `Public Property DueDateSelection() As BoDueDateEnum` [R/W] Sets or returns a valid value that determines the due date type of the Bills of Exchange. Field name: ValDateSel.
- `Public Property Format() As String` [R/W] Sets and return the file format name of the payment. Field name: Format. Length: 100 Characters.
- `Public Property GLAccount() As String` [R] Sets or returns the G/L account assigned to the payment. Field name: GLAccount. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property GroupByDate() As BoYesNoEnum` [R/W] Determines whether or not to sort the Bills of Exchange payments by their due date. Field name: GrpByDate.
- `Public Property GroupByPaymentReference() As BoYesNoEnum` [R/W] Determines whether or not to sort the Bills of Exchange by their Payment Reference. Field name: GroupPmRef.
- `Public Property GroupInvoicesByCurrency() As BoYesNoEnum` [R/W] Determines whether or not to enable grouping invoices according to their currencies. Field name: GrpByCur.
- `Public Property GroupInvoicesbyPay() As BoYesNoEnum` [R/W] Determines whether or not to enable grouping invoices according to their target bank. Field name: GroupPmRef.
- `Public Property GroupInvoicesByPayToBank() As BoYesNoEnum` [R/W] Determines whether or not to enable grouping invoices for vendors by pay-to bank addresses. Field name: GrpByBank.
- `Public Property Instruction1() As String` [R/W] Sets or returns the first BOE instruction. Field name: Instruct1. Length: 2 characters.
  - remarks: Applicable for cluster B. Country-specific for Brazil only (BOE in Brazil is called Boleto). This property is defined as BOE Property, used by different Boleto Barcode Algorithms to construct their own Algorithm Structure.
- `Public Property Instruction2() As String` [R/W] Sets or returns the second BOE instruction. Field name: Instruct2. Length: 2 characters.
  - remarks: Applicable for cluster B. Country-specific for Brazil only (BOE in Brazil is called Boleto). This property is defined as BOE Property, used by different Boleto Barcode Algorithms to construct their own Algorithm Structure.
- `Public Property KeyCode() As String` [R/W] Sets and return the key of the payment method. Field name: KeyCode. Length: 6 Characters.
- `Public Property MaximumAmount() As Double` [R/W] Sets or returns the maximum amount of incoming or outgoing payments in a single check (Single Check Restrictions). Field name: MaxAmount.
- `Public Property MinimumAmount() As Double` [R/W] Sets or returns the minimum amount of incoming or outgoing payments in a single check (Single Check Restrictions). Field name: MinAmount.
- `Public Property MovementCode() As String` [R/W] property MovementCode
- `Public Property OccurenceCode() As String` [R/W] property OccurenceCode
- `Public Property PaymentMeans() As BoPaymentMeansEnum` [R/W] Sets or returns a valid value of BoPaymentMeansEnum that determines the payment means. Field name: BankTransf.
- `Public Property PaymentMethodCode() As String` [R/W] Sets or returns the payment method code. Field name: PayMethCod. Length:15 characters.
- `Public Property PaymentPlace() As String` [R/W] Sets or returns the BOE payment place. Field name: PaymntPlc. Length: 128 characters.
  - remarks: Applicable for cluster B. Country-specific for Brazil only (BOE in Brazil is called Boleto). This property is defined as BOE Property, used by different Boleto Barcode Algorithms to construct their own Algorithm Structure.
- `Public Property PaymentTermsCode() As Long` [R/W] Sets or returns the payment terms for incoming payments related to the business partner. Field name: PaymTerms. This is a foreign key to the PaymentTermsTypes object.
- `Public Property PortfolioID() As String` [R/W] Sets or returns the BOE internal portfolio ID. Field name: PtfID. Length: 3 characters.
  - remarks: Applicable for cluster B. Country-specific for Brazil only (BOE in Brazil is called Boleto). This property is defined as BOE Property, used by different Boleto Barcode Algorithms to construct their own Algorithm Structure.
- `Public Property PostOfficeBank() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not the payment method is related to a post office bank. Field name: PostOffBnk.
- `Public Property PosttoGLInterimAccount() As BoYesNoEnum` [R/W] Determines whether or not to enable posting payments to a G/L intermediate account. Field name: IntrimAcct.
- `Public Property ReportCode() As String` [R/W] property ReportCode
- `Public Property SendforAcceptance() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not Send for Acceptanceis required. Field name: SendAccept.
- `Public Property TransactionType() As String` [R/W] Sets or returns the Transaction type. Field name: TrnsType. Length: 2 Characters.
- `Public Property Type() As BoPaymentTypeEnum` [R/W] Sets or returns a valid value of BoPaymentTypeEnum that determines wether the payment is incoming or outgoing. Field name: Type.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the foreign key of the user who enters the payment method. Field name: UserSign. This is a foreign key to the Users object.

## Methods (7)
- `Public Function Add() As Long` Adds a payment method.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrCode`: 
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
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
