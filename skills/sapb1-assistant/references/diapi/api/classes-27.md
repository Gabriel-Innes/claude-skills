<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# WithholdingTaxData (Object)

WithholdingTaxData is a child object of Documents object and represents the Withholding tax table related to the document. Source tables: INV5, RIN5, RDN5, RDN5, PCH5, RPC5, DPI5, DPO5, DRF5. The WithholdingTaxData object is relevant only to the following document types: - Documents(oInvoices), Documents(oCorrectionInvoice), Documents(oCorrectionInvoiceReversal) - OINV - Documents(oCreditNotes) - ORIN - Documents(oReturns) - ORDN - Documents(oPurchaseInvoices), Documents(oCorrectionPurchaseInvoice), Documents(oCorrectionPurchaseInvoiceReversal) - OPCH - Documents(oPurchaseCreditNotes) - ORPC - Documents(oDownPaymentsInput) - ODPI (not exposed through the DI API) - Documents(oDownPaymentsOutput) - ODPO (not exposed through the DI API) - Documents(oDrafts) - ODRF

**Remarks:** The data for the Withholding tax table consists on WithholdingTaxCodes definitions. To define withholding tax codes in the application: - Select Administration --> Setup --> Financials --> Tax --> Withholding Tax. To display the form in the application: - Select a document (for example, select Sales - A/R --> A/R Invoice). - From the main menu, select Go to --> WT Table.

## Properties (24)
- `Public Property BaseDocEntry() As Long` [R/W] Sets or returns the source document ID. Field name: BaseAbsEnt.
  - remarks: Use the BaseDocEntry, BaseDocType, and BaseDocLine properties to extract data from one document to another.
- `Public Property BaseDocLine() As Long` [R/W] Sets or returns the line number of the source document. Field name: BaseLine.
  - remarks: Use the BaseDocLine, BaseDocType, BaseDocEntry and properties to extract data from one document to another.
- `Public Property BaseDocType() As Long` [R/W] Sets or returns the source document type. Field name: BaseNum.
  - remarks: Use the BaseDocType, BaseDocEntry, and BaseDocLine properties to extract data from one document to another. To view the document type numbers, see BoAPARDocumentTypes.
- `Public Property BaseDocumentReference() As Long` [R] Returns the Base Document Reference number. Field name: BaseRef.
- `Public Property BaseType() As String` [R] Returns the amount type (Gross, Net, or VAT) on which the withholding tax calculation is based. Field name: BaseType. Length: 1 character.
  - remarks: The valid values are: - G - Gross. Total amount including VAT (country-specific for Europe only). - N - Net. Total amount without VAT (country-specific for Europe and Latin America). - V - VAT. VAT amount only (country-specific for Latin America only).
- `Public Property Category() As String` [R] Returns a valid value that indicates the cause for posting the withholding tax, either Payment (P) or Invoice (I). Field name: Category. Length: 1 character.
- `Public Property Count() As Long` [R] property Count
  - remarks: Returns the total withholding tax data lines.
- `Public Property Criteria() As String` [R] Returns the type of accounting under which the withholding tax is recorded. Length: 1 character. Field name: Criteria.
  - remarks: The valid values are: - Y - Accrual. - N - Cash.
- `Public Property GLAccount() As String` [R] Sets or returns the G/L account to which withholding tax is posted. Field name: Account. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property LineNum() As Long` [R] Returns the number of the withholding tax data line. Field name: LineNum.
- `Public Property Rate() As Double` [R] Returns the rate for calculating the withholding tax amount. Field name: Rate.
- `Public Property RoundingType() As String` [R] Returns the rounding method for calculating the withholding tax. Field name: RoundType. Length: 1 character.
  - remarks: Country-specific for Australia and New Zealand. The valid values are: - T - Truncated (known as Penalty Withholding Tax). Truncates the decimal value of both the base amount (TaxableAmount) and the calculated withholding tax amount (WTAmount). - C - Commercial rounding (known as Voluntary Withholding Tax). Round down 1 - 49 cents and round up 50 -99 cents of the calculated withholding tax amount (WTAmount).
- `Public Property Status() As BoStatus` [R] Determines whether the withholding tax status is Open or Close. Field name: status.
- `Public Property TargetAbsEntry() As Long` [R] Returns the target sum before the withholding tax calculations. Field name: TrgAbsEntr.
- `Public Property TargetDocumentType() As Long` [R] Returns the type of the target document. Field name: TrgType.
- `Public Property TaxableAmount() As Double` [R/W] Sets or returns the amount (in local currency) that is subject to withholding. Field name: TaxbleAmnt.
- `Public Property TaxableAmountFC() As Double` [R/W] Sets or returns the amount (in foreign currency) that is subject to withholding. Field name: TxblAmntFC.
- `Public Property TaxableAmountinSys() As Double` [R/W] Sets or returns the amount (in system currency) that is subject to withholding. Field name: TxblAmntSC.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WithholdingType() As String` [R] Returns the withholding tax type. Field name: Type. Length: 1 character.
  - remarks: Country-specific to Latin America. The valid values are: - I - Income withholding. This type is used when the supplier provides professional services and issues an invoice to the company. The company withholds the withholding tax amount, and then transfers this amount to the tax authority on behalf of the supplier. - V - VAT withholding. This type is used when the supplier cannot issue an invoice to the company, and therefore the company withholds the VAT amount (or part of it) and issues a purchase invoice.
- `Public Property WTAmount() As Double` [R/W] Sets or returns the withholding tax amount in local currency. Field name: ).
  - remarks: WTAmount is calculated as follows: WTAmount = TaxableAmount * Rate
- `Public Property WTAmountFC() As Double` [R/W] Sets or returns the withholding tax amount in foreign currency. Field name: WTAmntFC.
  - remarks: WTAmountFC is calculated as follows: WTAmountFC = TaxableAmountFC * Rate
- `Public Property WTAmountSys() As Double` [R/W] Sets or returns the withholding tax amount in system currency. Field name: WTAmntSC.
  - remarks: WTAmountSys is calculated as follows: WTAmountSys = TaxableAmountinSys * Rate
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code. Field name: WTCode. Length: 4 characters. This is a foreign key to the WithholdingTaxCodes Object.
  - remarks: You can set only WT codes that are relevant to the business partner as defined in BPWithholdingTax object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# WithholdingTaxDataWTX (Object)

WithholdingTaxDataWTX Class

## Properties (38)
- `Public Property AccumBaseAmount() As Double` [R] property AccumBaseAmount
- `Public Property AccumBaseAmountFC() As Double` [R] property AccumBaseAmountFC
- `Public Property AccumBaseAmountSys() As Double` [R] property AccumBaseAmountSys
- `Public Property AccumWTaxAmount() As Double` [R] property AccumWTaxAmount
- `Public Property AccumWTaxAmountFC() As Double` [R] property AccumWTaxAmountFC
- `Public Property AccumWTaxAmountSys() As Double` [R] property AccumWTaxAmountSys
- `Public Property BaseDocEntry() As Long` [R] property BaseDocEntry
- `Public Property BaseDocLine() As Long` [R] property BaseDocLine
- `Public Property BaseDocType() As Long` [R] property BaseDocType
- `Public Property BaseDocumentReference() As Long` [R] property BaseDocumentReference
- `Public Property BaseNetAmount() As Double` [R] property BaseNetAmount
- `Public Property BaseNetAmountFC() As Double` [R] property BaseNetAmountFC
- `Public Property BaseNetAmountSys() As Double` [R] property BaseNetAmountSys
- `Public Property BaseType() As String` [R] property BaseType
- `Public Property BaseVatAmount() As Double` [R] property BaseVatAmount
- `Public Property BaseVatAmountFC() As Double` [R] property BaseVatAmountFC
- `Public Property BaseVatAmountSys() As Double` [R] property BaseVatAmountSys
- `Public Property Category() As String` [R] property Category
- `Public Property Count() As Long` [R] property Count
- `Public Property Criteria() As String` [R] property Criteria
- `Public Property ExemptRate() As Double` [R/W] property ExemptRate
- `Public Property GLAccount() As String` [R] property GLAccount
- `Public Property LineNum() As Long` [R] property LineNum
- `Public Property Rate() As Double` [R/W] property Rate
- `Public Property RoundingType() As String` [R] property RoundingType
- `Public Property Status() As BoStatus` [R] property Status
- `Public Property TargetAbsEntry() As Long` [R] property TargetAbsEntry
- `Public Property TargetDocumentType() As Long` [R] property TargetDocumentType
- `Public Property TaxableAmount() As Double` [R/W] property TaxableAmount
- `Public Property TaxableAmountFC() As Double` [R/W] property TaxableAmountFC
- `Public Property TaxableAmountinSys() As Double` [R/W] property TaxableAmountinSys
- `Public Property UserFields() As UserFields` [R] property UserFields
- `Public Property WithholdingType() As String` [R] property WithholdingType
- `Public Property WTAbsId() As String` [R/W] property WTAbsId
- `Public Property WTAmount() As Double` [R/W] property WTAmount
- `Public Property WTAmountFC() As Double` [R/W] property WTAmountFC
- `Public Property WTAmountSys() As Double` [R/W] property WTAmountSys
- `Public Property WTCode() As String` [R] property WTCode

## Methods (2)
- `Public Sub Add()` method Add
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# WithholdingTaxLines (Object)

WithholdingTaxLines is a child object of Document_Lines object and supports Withholding Tax in a line level (as opposed to WithholdingTaxData object, which supports Withholding Tax in a document level). The WithholdingTaxLines object is applicable for cluster B only (country-specific for Brazil only). Source table: INV5. Relevant only for the following tables: OINV, ORIN, ODLN, ORDR, ORDN, OPCH, ORPC, OPDN, ORPD, OPOR, ODRF, OCSI, OCSV, OCPI, and OCPV.

**Remarks:** The data for the Withholding tax table consists on WithholdingTaxCodes definitions. To define withholding tax codes in the application: - Select Administration --> Setup --> Financials --> Tax --> Withholding Tax. To display the form in the application: - Select a document (for example, select Sales - A/R --> A/R Invoice). - Select a document line. - From the main menu, select Go to --> WT Table.

## Properties (22)
- `Public Property BaseDocEntry() As Long` [R/W] Sets or returns the source document ID.
- `Public Property BaseDocLine() As Long` [R/W] Sets or returns the line number of the source document.
- `Public Property BaseDocType() As Long` [R/W] Sets or returns the source document.
- `Public Property BaseType() As String` [R] Returns the amount type (Gross, Net, or VAT) on which the withholding tax calculation is based. Length: 1 character.
  - remarks: The valid values are: - G - Gross. Total amount including VAT (country-specific for Europe only). - N - Net. Total amount without VAT (country-specific for Europe and Latin America). - V - VAT. VAT amount only (country-specific for Latin America only).
- `Public Property Category() As String` [R] Returns a valid value that indicates the cause for posting the withholding tax, either Payment (P) or Invoice (I). Length: 1 character.
- `Public Property Count() As Long` [R] Returns the total withholding tax data lines.
- `Public Property Criteria() As String` [R] Returns the type of accounting under which the withholding tax is recorded. Length: 1 character.
- `Public Property CSTCodeIncoming() As String` [R/W] property CSTCodeIncoming
- `Public Property CSTCodeOutgoing() As String` [R/W] property CSTCodeOutgoing
- `Public Property GLAccount() As String` [R] Sets or returns the G/L account to which withholding tax is posted. Length: 15 characters.
- `Public Property LineNum() As Long` [R] Returns the number of the withholding tax line.
- `Public Property Rate() As Double` [R] Returns the percentage rate for calculating the withholding tax amount.
- `Public Property RoundingType() As String` [R] Returns the rounding method for calculating the withholding tax. Length: 1 character.
  - remarks: The valid values are: - T - Truncated (known as Penalty Withholding Tax). Truncates the decimal value of both the base amount (TaxableAmount) and the calculated withholding tax amount (WTAmount). - C - Commercial rounding (known as Voluntary Withholding Tax). Round down 1 - 49 cents and round up 50 -99 cents of the calculated withholding tax amount (WTAmount).
- `Public Property TaxableAmount() As Double` [R/W] Sets or returns the amount (in local currenxy) that is subject to withholding.
- `Public Property TaxableAmountFC() As Double` [R/W] Sets or returns the taxable amount (in foreign currency) that is subject to withholding.
- `Public Property TaxableAmountinSys() As Double` [R/W] Sets or returns the taxable amount (in system currency) that is subject to withholding.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WithholdingType() As String` [R] Returns the withholding tax type. Length: 1 character.
  - remarks: The valid values are: - I - Income withholding. This type is used when the supplier provides professional services and issues an invoice to the company. The company withholds the withholding tax amount, and then transfers this amount to the tax authority on behalf of the supplier. - V - VAT withholding. This type is used when the supplier cannot issue an invoice to the company and therefore the company withholds the VAT amount (or part of it) and issues a purchase invoice.
- `Public Property WTAmount() As Double` [R/W] Sets or returns the withholding tax amount in local currency.
- `Public Property WTAmountFC() As Double` [R/W] Sets or returns the withholding tax amount in foreign currency.
- `Public Property WTAmountSys() As Double` [R/W] Sets or returns the withholding tax amount in system currency.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code. Length: 4 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# WitholdingTaxDefinitionService (Object)

WitholdingTaxDefinitionService Class

## Methods (7)
- `Public Function AddWTDCode(ByVal pIWTDCode As WTDCode) As WTDCodeParamsCollection` AddWTDCode
  - param `pIWTDCode`: 
- `Public Sub Delete(ByVal pIWTDCodeParamsCollection As WTDCodeParamsCollection)` Delete
  - param `pIWTDCodeParamsCollection`: 
- `Public Function Get(ByVal pIWTDCodeParams As WTDCodeParams) As WTDCode` Get
  - param `pIWTDCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As WitholdingTaxDefinitionServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `WitholdingTaxDefinitionServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub UpdateWTDCode(ByVal pIWTDCode As WTDCode)` UpdateWTDCode
  - param `pIWTDCode`: 

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

# WorkflowApprovalTaskListParams (Object)

This object specifies the identification key of the GetApprovalTaskList method.

## Properties (1)
- `Public Property Status() As String` [R/W] Status is a string that represents a list of the task statuses. The statuses for workflow tasks are as follows: TaskStatus_To_Be_Picked W TaskStatus_Picking P TaskStatus_In_Process G TaskStatus_Completing D TaskStatus_Completed F TaskStatus_Canceled Q TaskStatus_Canceling C TaskStatus_Forwarding O TaskStatus_Error E TaskStatus_Terminated T A string may contain the vertical bar "|" as separators, such as "W", "W|G" or "W|G|F".

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTask (Object)

WorkflowTask is a data object holding properties for workflow tasks. Source table: OWLS.

## Properties (14)
- `Public Property Description() As String` [R] Returns the description of a workflow task. Field name: TaskDesc.
- `Public Property InstanceID() As Long` [R] Returns the ID of a workflow instance. Field name: WFInstID.
- `Public Property Name() As String` [R] Returns the name of the workflow task. Field name: TaskName.
- `Public Property Operation() As String` [R] Returns the operation type of the workflow task. Field name: Operation.
- `Public Property Owner() As String` [R] Returns the owner of the workflow task. Field name: Owner.
- `Public Property Priority() As Long` [R] Returns the priority of the workflow task. Field name: Priority.
- `Public Property Status() As String` [R] Returns the current status of the workflow task. Field name: Status.
- `Public Property TaskID() As Long` [R] Returns the ID of the workflow task. Field name: TaskID.
- `Public Property TemplateID() As String` [R] Returns the ID of a workflow template. Field name: WFID.
- `Public Property TemplateName() As String` [R] Returns the name of a workflow template. Field name: WFName.
- `Public Property Type() As String` [R] Returns the type of the workflow task. Field name: TaskType.
- `Public Property WorkflowTaskInputObjectCollection() As WorkflowTaskInputObjectCollection` [R] Returns the collection of the input objects for the workflow task.
- `Public Property WorkflowTaskNoteCollection() As WorkflowTaskNoteCollection` [R] Returns the collection of notes for the workflow task.
- `Public Property WorkflowTaskOutputObjectCollection() As WorkflowTaskOutputObjectCollection` [R] Returns the collection of output objects for the workflow task.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTaskCollection (Collection)

WorkflowTaskCollection is a collection of WorkflowTask objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As WorkflowTask` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As WorkflowTask` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTaskCompleteParams (Object)

This object specifies the identification key of the Complete method.

## Properties (3)
- `Public Property Note() As String` [R/W] The note that needs to be added to the task for processing.
- `Public Property TaskID() As Long` [R/W] The ID of the related workflow task.
- `Public Property TriggerParams() As String` [R/W] The trigger parameter that needs to be added to the task. The TriggerParams is a string in xml format.
  - remarks: The TriggerParams format is as follows: "<Params> <Param> <Key>%key1%</Key> <Value Type=\"type1\">%value1%</Value> </Param> <Param> <Key>%key2%</Key> <Value Type=\"type2\">%value2%</Value> </Param> … </Params>" The supported value types are: “integer”, “double”, “string”, “date” and “time”.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# WorkflowTaskInputObject (Object)

WorkflowTaskInputObject is a data object holding properties for workflow task input data objects. Source table: WLS2

## Properties (6)
- `Public Property Detail() As String` [R] Returns the detail information of the input data object if specified. Field name: ObjDetail.
- `Public Property Key() As String` [R] Returns the key of the input data object. Field name: ObjKey.
- `Public Property LineId() As Long` [R] Returns the line number of the input object. Field name: LineID.
- `Public Property SubType() As String` [R] Returns the sub-type of the input data object if specified. Field name: ObjSubType.
- `Public Property TaskID() As Long` [R] Returns the ID of the related workflow task. Field name: TaskID.
- `Public Property Type() As String` [R] Returns the type of the input data object. Field name: ObjectType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTaskInputObjectCollection (Collection)

WorkflowTaskInputObjectCollection is a collection of WorkflowTaskInputObject objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As WorkflowTaskInputObject` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As WorkflowTaskInputObject` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTaskNote (Object)

WorkflowTaskNote is a data object holding properties for the workflow task note. Source table: WLS3

## Properties (5)
- `Public Property Creator() As String` [R] Returns the creator of the note. Field name: Creator.
- `Public Property LineId() As Long` [R] Returns the line number of the output object. Field name: LineID.
- `Public Property Note() As String` [R] Returns the content of the note. Field name: Note.
- `Public Property NoteDate() As Date` [R] Returns the created date of the note. Field name: NoteDate.
- `Public Property TaskID() As Long` [R] Returns the ID of the related workflow task. Field name: TaskID.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTaskNoteCollection (Collection)

WorkflowTaskNoteCollection is a collection of the WorkflowTaskNote objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As WorkflowTaskNote` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As WorkflowTaskNote` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTaskOutputObject (Object)

WorkflowTaskOutputObject is a data object holding properties for the workflow task output data object. Source table: WLS4

## Properties (5)
- `Public Property Key() As String` [R] Returns the key of the output data object. Field name: ObjKey.
- `Public Property LineId() As String` [R] Returns the line number of the output object. Field name: LineID.
- `Public Property SubType() As String` [R] Returns the the sub-type of the output data object if specified. Field name: ObjSubType.
- `Public Property TaskID() As Long` [R] Returns the ID of the related workflow task. Field name: TaskID.
- `Public Property Type() As String` [R] Returns the type of the output data object. Field name: ObjectType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTaskOutputObjectCollection (Collection)

WorkflowTaskOutputObjectCollection is a collection of the WorkflowTaskOutputObject objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As WorkflowTaskOutputObject` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As WorkflowTaskOutputObject` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WorkflowTaskService (Object)

WorkflowTaskService is a business object that manages the tasks of the SAP Business One Workflow component. This object enables you to do the following: - Get workflow tasks owned by the current user and filter tasks by status. - Complete a workflow approval task of a given task ID and other parameters. Source table: OWLS.

**Remarks:** This service supports only the operations of approval tasks in this stage. To use the task service, proceed as follows: - Connect to a valid company. - Call CompanyService, which is the main DI service that you must call before using any other service. - Call the GetBusinessService method for the required service.

## Methods (5)
- `Public Sub Complete(ByVal pIWorkflowTaskCompleteParams As WorkflowTaskCompleteParams)` Completes a given approval task specified by WorkflowTaskCompleteParams (TaskID), adds notes, and triggers parameters for the task given in WorkflowTaskCompleteParams (Note, TriggerParams). This function, which is asynchronous, sends a signal to the workflow engine to complete the task specified by the "TaskID". You can check the task status to ensure that the task has been completed successfully. Note: This function is available only for the approval tasks that possess all the follwing features: - Type "U". - Operation "P". - Status "W" or "G".
  - param `pIWorkflowTaskCompleteParams`: The key of the approval task to be completed.
  - C# example (from SAP's help):
    ```csharp
    // using packages
    using SAPbobsCOM;
    using System.Runtime.InteropServices;

    // get Workflow Task Service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    SAPbobsCOM.WorkflowTaskService taskService = null;
    taskService = (SAPbobsCOM.WorkflowTaskService)oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.WorkflowTaskService);

    // get approval task
    SAPbobsCOM.WorkflowApprovalTaskListParams taskParam;
    taskParam = (SAPbobsCOM.WorkflowApprovalTaskListParams)taskService.GetDataInterface(WorkflowTaskServiceDataInterfaces.wtsWorkflowApprovalTaskListParams);
    taskParam.Status = "W|G";

    try
    {
                    SAPbobsCOM.WorkflowTaskCollection tasks = taskService.GetApprovalTaskList(taskParam);
    }
    catch (COMException ex)
    {
                    int code = ex.ErrorCode;
                    string msg = ex.Message;
                    //error handling
    }

    if(tasks.count>0)
    {
                    completeParam.TaskID = tasks.Item(0).TaskID;
                    completeParam.Note = "Default Comment";
                    completeParam.TriggerParams = "<Params><Param><Key>Result</Key><Value Type=\"string\">1</Value></Param></Params>";
                    try
                    {
                                    taskService.Complete(completeParam);
                    }
                    catch (COMException ex)
                    {
                                    int code = ex.ErrorCode;
                                    string msg = ex.Message;
                                    //error handling
                    }
    }
    ```
- `Public Function GetApprovalTaskList(ByVal pIWorkflowApprovalTaskListParams As WorkflowApprovalTaskListParams) As WorkflowTaskCollection` Returns the WorkflowTaskCollection object. Note: A task will be listed only for its owner or candidate.
  - param `pIWorkflowApprovalTaskListParams`: The key of the workflow task collection to retrieve.
  - C# example (from SAP's help):
    ```csharp
    // using packages
    using SAPbobsCOM;
    using System.Runtime.InteropServices;

    // get Workflow Task Service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    SAPbobsCOM.WorkflowTaskService taskService = null;
    taskService = (SAPbobsCOM.WorkflowTaskService)oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.WorkflowTaskService);

    // get approval tasks
    SAPbobsCOM.WorkflowApprovalTaskListParams taskParam = null;
    taskParam = (SAPbobsCOM.WorkflowApprovalTaskListParams)taskService.GetDataInterface(WorkflowTaskServiceDataInterfaces.wtsWorkflowApprovalTaskListParams);
    taskParam.Status = "W|G";

    try
    {
        SAPbobsCOM.WorkflowTaskCollection tasks = taskService.GetApprovalTaskList(taskParam);
        foreach (SAPbobsCOM.WorkflowTask task in tasks)
        {
            int TaskID = task.TaskID;
            foreach (SAPbobsCOM.WorkflowTaskInputObject inputObj in task.WorkflowTaskInputObjectCollection)
            {
                int id = inputObj.TaskID;
                string objType = inputObj.Type;
                string objKey = inputObj.Key;
            }
        }
    }
    catch (COMException ex)
    {
        int code = ex.ErrorCode;
        string msg = ex.Message;
        //error handling
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As WorkflowTaskServiceDataInterfaces) As Object` Creates an empty data structure for use with the GeneralService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `WorkflowTaskServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```

# WorkOrder_Lines (Object)

WorkOrder_Lines is child object of the WorkOrders object that represents a collection of parent items in a work order. The parent item is connected to its bill of material. Source table: WKO1.

**Remarks:** Mandatory fields in SAP Business One: ItemCode. To display the form in the application: - Select Production --> Work Order. Note: The properties SerialNumbers and BatchNumbers were removed from this object because they are not supported. If you have an add-on from the previous version 6.5 that includes these properties, a compilation error will occur, therefore you must remove these properties from your add-on.

## Properties (11)
- `Public Property ActiveAccountCode() As String` [R/W] Sets or returns the active G/L account code to debit. Field name: ActWorkCod. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property Count() As Long` [R] Returns the total data rows in the WorkOrder_Lines object.
  - remarks: When you add a data row, the value of this property is incremented automatically.
- `Public Property ItemCode() As String` [R/W] Sets or returns the code of the item ordered for production. Mandatory in SAP Business One. Field name: ItemCode. Length: 20 characters. This is a foreign key to the ProductTrees object.
- `Public Property ItemDescription() As String` [R] Returns the item description/name. Field name: Descript. Length: 100 characters.
- `Public Property ItemPrice() As Double` [R/W] Sets or returns the item price. Field name: Price.
  - remarks: This is the price in the price list defined for the production bill of materials. The default price list proposed by the system is the purchasing price list.
- `Public Property ItemQuantity() As Double` [R/W] Sets or returns the quantity of items to be produced. Field name: Quantity.
- `Public Property ItemWarehouse() As String` [R/W] Sets or returns the warehouse where the finished product should be stored. Field name: WhsCode. Length: 8 characters. This is a foreign key to the Warehouses object.
  - remarks: In SAP Business One, if you do not set this property, the system automatically uses the default general storage location predefined in the system.
- `Public Property PriceCurrency() As String` [R/W] Returns the currency of the item price. Field name: Currency. Length: 3 characters.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (starts from 1). Field name: Line_ID.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WorkSum() As Double` [R/W] Sets or returns the labor price. SAP Business One adds this price to the total price (OrderTotal). Field name: ActWorkSum.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# WorkOrders (Object)

WorkOrders is a business object that represents the work orders in the Inventory and Production module. This object is applicable only if work orders are already exist in the Company database. From release 2005, this object is replaced by the ProductionOrders object. Source table: OWKO.

**Remarks:** To display the form in the application (release 2004 only): - Select Production --> Work Order.

## Properties (26)
- `Public Property ActiveAccountCode() As String` [R/W] This property is not supported in this object. Supported only in WorkOrder_Lines.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Canceled() As BoYesNoEnum` [R] Determines whether or not the work order was canceled. Field name: Canceled.
- `Public Property Comment() As String` [R/W] Sets or returns remarks to the work order. Field name: Memo. Length: 254 characters.
- `Public Property ContactPerson() As Long` [R/W] Sets or returns the code of the contact person. Field name: CntctCode. This is a foreign key to the ContactEmployees object.
- `Public Property CustomerRefNo() As String` [R/W] Sets or returns the customer reference number related to the work order. Field name: NumInCustm. Length: 16 characters.
- `Public Property ExpectedCompletionDate() As Date` [R/W] Sets or returns the expected date for the product completion. Field name: ExpFinishD.
- `Public Property FinancialPeriod() As Long` [R] Returns the financial period. Field name: FinncPriod. This is a foreign key to the FinancePeriod object.
- `Public Property GenerationTime() As Date` [R/W] Sets or returns the generation time of the work order. Field name: DocTime.
- `Public Property InstructionNumber() As Long` [R] Returns the instruction number. That is the work order serial number, which is incremented automatically when adding a work order. Field name: SerialNum.
- `Public Property JournalRemarks() As String` [R/W] Sets or returns the journal remarks, of the G/L account, for the work order. Field name: JrnlMemo. Length: 50 characters.
  - remarks: The journal remark is copied to the accounting document when you set the work order Status to Work Completed.
- `Public Property Lines() As WorkOrder_Lines` [R] Returns the WorkOrder_Lines child object.
- `Public Property OrderDate() As Date` [R/W] Sets or returns the date for the work order. Field name: OrderDate.
  - remarks: SAP Business One suggest the current date as order date.
- `Public Property OrdererCode() As String` [R/W] Sets or returns the Contact code of the customer that ordered the work. Field name: CntctCode. Length: 11 characters.
- `Public Property OrdererName() As String` [R/W] Sets or returns the customer name as defined in the business partners master data. Field name: CustomName. Length: 100 characters.
- `Public Property OrderNum() As Long` [R] Returns the work order unique number (primary key) as assigned by SAP Business One. Field name: OrderNum.
- `Public Property OrderTotal() As Double` [R] Returns the total price of all the items specified in the work order. Field name: TotalOrder.
- `Public Property PriceListNum() As Long` [R/W] Sets or returns the number of the price list for a specified item. Field name: PriceList. This is a foreign key to the PriceLists object.
- `Public Property ReceiverName() As String` [R/W] Sets or returns the name of the employee that receives the production instructions. Field name: FinishUser. Length: 8 characters.
  - remarks: This property uses the internal key of the user. For Anonymous use the value -1.
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
- `Public Property Status() As BoWorkOrderStat` [R/W] Sets or returns a valid value of BoWorkOrderStat type that specifies the status of the work order. Field name: Status.
- `Public Property TotalCurrency() As String` [R] Returns the currency of the total price. Field name: TotalCurr. Length: 3 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WorkFinishDate() As Date` [R/W] Sets or returns the date for completing the product. Field name: FinishDate.
- `Public Property WorkStartDate() As Date` [R/W] Sets or returns the date for starting the production. Field name: ProdctDate.
- `Public Property WorkSum() As Double` [R/W] Not supported in this object. Supported only in WorkOrder_Lines. Field name: ActWorkSum.

## Methods (7)
- `Public Function Add() As Long` Adds a new workorder.
- `Public Function Cancel() As Long` Cancel a record from the object table. Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal WkoKey As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `WkoKey`: Specifies the work order identification key (OrderNum).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to an XML file.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# WTaxTypeCode (Object)

Source table: OWXT.

## Properties (2)
- `Public Property Code() As Long` [R/W] Field name: WtaxTCode.
- `Public Property Description() As String` [R/W] Field name: WtaxTDesc. Length: 100 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WTaxTypeCodeParams (Object)

WTaxTypeCodeParams Class

## Properties (1)
- `Public Property Code() As Long` [R/W] Field name: WtaxTCode.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WTaxTypeCodeService (Object)

Source table: OWXT.

**Remarks:** For the Italy localization only. Navigation path: Business Partner Master Data → Accounting → Tax, select the checkbox Subject to Withholding Tax, choose the browser button next to the Specific WTax Amounts Setup field, and go to the column WTax Type Code.

## Methods (8)
- `Public Function AddWTaxTypeCode(ByVal pIWTaxTypeCode As WTaxTypeCode) As WTaxTypeCodeParams` AddWTaxTypeCode
  - param `pIWTaxTypeCode`: 
- `Public Sub DeleteWTaxTypeCode(ByVal pIWTaxTypeCodeParams As WTaxTypeCodeParams)` DeleteWTaxTypeCode
  - param `pIWTaxTypeCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As WTaxTypeCodeServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `WTaxTypeCodeServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetWTaxTypeCode(ByVal pIWTaxTypeCodeParams As WTaxTypeCodeParams) As WTaxTypeCode` GetWTaxTypeCode
  - param `pIWTaxTypeCodeParams`: 
- `Public Function GetWTaxTypeCodeList() As WTaxTypeCodesParams` GetWTaxTypeCodeList
- `Public Sub UpdateWTaxTypeCode(ByVal pIWTaxTypeCode As WTaxTypeCode)` UpdateWTaxTypeCode
  - param `pIWTaxTypeCode`: 

# WTaxTypeCodesParams (Collection)

WTaxTypeCodesParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As WTaxTypeCodeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As WTaxTypeCodeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# WTDBP (Object)

WTDBP Class

## Properties (8)
- `Public Property BPKeyPart1() As String` [R/W] property BPKeyPart1
- `Public Property BPKeyPart2() As String` [R/W] property BPKeyPart2
- `Public Property DetailType() As WTDDetailType` [R/W] property DetailType
- `Public Property EffectiveDateFrom() As Date` [R/W] property EffectiveDateFrom
- `Public Property EffectiveDateTo() As Date` [R/W] property EffectiveDateTo
- `Public Property Rate() As Double` [R/W] property Rate
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property WTaxCode() As String` [R/W] property WTaxCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDBPCollection (Collection)

WTDBPCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As WTDBP` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As WTDBP` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDCode (Object)

WTDCode Class

## Properties (18)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property BaseAmountPrct() As Double` [R/W] property BaseAmountPrct
- `Public Property BaseType() As WithholdingTaxCodeBaseTypeEnum` [R/W] property BaseType
- `Public Property CalculateInAutomaticCM() As BoYesNoEnum` [R/W] property CalculateInAutomaticCM
- `Public Property Category() As WithholdingTaxCodeCategoryEnum` [R/W] property Category
- `Public Property FormulaId() As Long` [R/W] property FormulaID
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property MinAmount() As Double` [R/W] property MinAmount
- `Public Property OfficialCode() As String` [R/W] property OfficialCode
- `Public Property SlidingScaleProgressiveTax() As BoYesNoEnum` [R/W] property SlidingScaleProgressiveTax
- `Public Property Type() As Long` [R/W] property Type
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property WTaxCode() As String` [R/W] property WTaxCode
- `Public Property WTaxName() As String` [R/W] property WTaxName
- `Public Property WTDBPCollection() As WTDBPCollection` [R] property WTDBPCollection
- `Public Property WTDEffectiveDateCollection() As WTDEffectiveDateCollection` [R] property WTDEffectiveDateCollection
- `Public Property WTDFreightCollection() As WTDFreightCollection` [R] property WTDFreightCollection
- `Public Property WTDItemCollection() As WTDItemCollection` [R] property WTDItemCollection

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDCodeParams (Object)

WTDCodeParams Class

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property WTaxCode() As String` [R/W] property WTaxCode
- `Public Property WTaxName() As String` [R] property WTaxName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDCodeParamsCollection (Collection)

WTDCodeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As WTDCodeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As WTDCodeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDEffectiveDate (Object)

WTDEffectiveDate Class

## Properties (5)
- `Public Property Effectivefrom() As Date` [R/W] property EffectiveFrom
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property Rate() As Double` [R/W] property Rate
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property WTDValueRangeCollection() As WTDValueRangeCollection` [R] property WTDValueRangeCollection

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDEffectiveDateCollection (Collection)

WTDEffectiveDateCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As WTDEffectiveDate` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As WTDEffectiveDate` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDFreight (Object)

WTDFreight Class

## Properties (5)
- `Public Property EffectiveDateFrom() As Date` [R/W] property EffectiveDateFrom
- `Public Property EffectiveDateTo() As Date` [R/W] property EffectiveDateTo
- `Public Property FreightCode() As Long` [R/W] property FreightCode
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property WTaxCode() As String` [R/W] property WTaxCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDFreightCollection (Collection)

WTDFreightCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As WTDFreight` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As WTDFreight` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDItem (Object)

WTDItem Class

## Properties (5)
- `Public Property EffectiveDateFrom() As Date` [R/W] property EffectiveDateFrom
- `Public Property EffectiveDateTo() As Date` [R/W] property EffectiveDateTo
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property WTaxCode() As String` [R/W] property WTaxCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDItemCollection (Collection)

WTDItemCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As WTDItem` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As WTDItem` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDValueRange (Object)

WTDValueRange Class

## Properties (5)
- `Public Property Effectivefrom() As Date` [R/W] property EffectiveFrom
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property Rate() As Double` [R/W] property Rate
- `Public Property SeqNum() As Long` [R] property SeqNum
- `Public Property ValueFrom() As Double` [R/W] property ValueFrom

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTDValueRangeCollection (Collection)

WTDValueRangeCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As WTDValueRange` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As WTDValueRange` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# WTGroups (Object)

WTGroups Class

## Properties (9)
- `Public Property Count() As Long` [R] property Count
- `Public Property DocsInWTGroups() As DocsInWTGroups` [R] property WithholdingCertificateWTC2
- `Public Property Percent() As Double` [R] property Percent
- `Public Property SumAccumulatedAmount() As Double` [R] property SumAccumulatedAmount
- `Public Property SumBaseAmount() As Double` [R] property SumBaseAmount
- `Public Property SumDocTotal() As Double` [R] property SumDocTotal
- `Public Property SumPerceptAmount() As Double` [R] property SumPerceptAmount
- `Public Property SumVATAmount() As Double` [R] property SumVATAmount
- `Public Property WhtAbsId() As Long` [R] property WhtAbsId

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 
