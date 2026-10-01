<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CompanyInfo (Object)

The CompanyInfo is a data structure related to the CompanyService. It includes initial parameters related to the company. The default values of part of the properties vary according to the country localization. Source table: CINF.

## Properties (35)
- `Public Property AutoCreateCustomerEqCard() As BoYesNoEnum` [R/W] Determines whether or not to create automatically customer equipment card when assigning a unique serial number. Field name: AutoCrIns.
  - remarks: Field name in the application: Auto. Create Customer Equipment Card. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Items tab.
- `Public Property AutoSRICreationOnReceipt() As BoYesNoEnum` [R/W] Determines whether or not to create automatically consecutive serial numbers on receipt of items to the inventory (system numerartor). This flag is applicable only if the inventory management method is On Release Only. Field name: SriCreatIn.
  - remarks: Field name in the application: Automatic Serial Number Creation on Receipt. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Inventory tab -->Items tab.
- `Public Property B1iTimeOut() As Long` [R/W] property B1iTimeOut
- `Public Property BaseDateForExchangeRate() As BoBaseDateRateEnum` [R/W] Determines whether the exchange rate is based on the Posting Date (P) or the Tax Date (T). Field name: RateBase.
  - remarks: Field name in the application: Base Date for Exchange Rate. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Inventory tab -->Items TAB.
- `Public Property BISRBankAccount() As String` [R] BISRBnkAcDetermines whether the exchange rate is based on the Posting Date (P) or the Tax Date (T). Field name: BISRBnkAc.
  - remarks: Field name in the application: BISR Bank Account. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property BISRBankActKey() As Long` [R/W] Set or returns the BISR bank account key. Field name: BisBnkAcKy. This is a foreign key to the HouseBankAccounts object (AbsoluteEntry).
- `Public Property BISRBankCountry() As String` [R] Sets the country code (3 characters) of the company house bank (BISR bank in Switzerland companies). This flag is valid only when EnbPayRef is set to Y. Field name: BISBnkCnt.
  - remarks: Field name in the application: BISR Bank Country. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property BISRBankNo() As String` [R] Sets the code of the of the company house bank (BISR bank in Switzerland companies). This flag is valid only when EnbPayRef is set to Y. Field name: BISRBnkCd.
  - remarks: Field name in the application: BISR Bank No. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property BISRBranch() As String` [R] Sets the branch number of the of the company house bank (BISR bank - applicable for Switzerland). This flag is valid only when EnbPayRef is set to Y. Field name: BISRBranch.
  - remarks: Field name in the application: BISR Branch. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property BlockStockNegativeQuantity() As BoYesNoEnum` [R/W] Determines whether or not to block documents that would cause negative inventory level. Field name: BlockZeroQ.
  - remarks: Field name in the application: Block Below Negative Quantity. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->General tab.
- `Public Property CompanyName() As String` [R] Returns this company name . Field name: CompnyName. Length: 100 characters.
- `Public Property DataOwnershipIndication() As BoYesNoEnum` [R/W] Determines whether or not to block documents that would cause negative inventory level. Field name: BlockZeroQ.
  - remarks: Field name in the application: Block Below Negative Quantity. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->General tab.
- `Public Property DefaultDaysForOrdCanc() As Long` [R/W] Sets the default number of days before cancelling a sales order. After this date the goods are not to be eccepted by the customer. The default value is 30 days after the Delivery Date. Field name: DaysOrdCnc.
  - remarks: Field name in the application: Default Days for Order Cancellation. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property DefaultStampTax() As String` [R/W] Sets the default stamp tax code for incoming payments. Applicable for Portugal. Field name: stampTax.
  - remarks: Field name in the application: Default Stamp Tax Code. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property DisplayTransactionsByDflt() As BoYesNoEnum` [R/W] Determines whether or not to display all transactions by default for incoming and outgoing payments. Field name: DispTrByDf.
  - remarks: Field name in the application: Display All Transactions by Default. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property EnableAccountSegmentation() As BoYesNoEnum` [R/W] Determines whether or not to enable account segmentation. Field name: EnbSgmnAct.
  - remarks: Field name in the application: Enable Accounts Segmentation. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Basic Initialization tab.
- `Public Property EnableBillOfExchange() As BoYesNoEnum` [R/W] Determines whether or not to enable bill-of-exchange payment method. Applicable for Spain, Italy, France, and Portugal. Field name: EnableBOE.
  - remarks: Field name in the application:Use Bill of Exchange. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Basic Initialization tab.
- `Public Property EnableCheckQuantityInRDR() As BoYesNoEnum` [R/W] Determines whether or not to check automatically the availabllity of item quantities before adding the quantity in sales orders. The default setting is Y. In case the available quantity is less than the quantity specified in the sales order, the system displays several options. Field name: ChkQunty.
  - remarks: Field name in the application: Activate Automatic Availability Check (in Sales Orders). To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property EnableConversionDifferentAcct() As BoYesNoEnum` [R] Determines whether or not to enable the conversion different accounts. Field name: ConvDifAct.
- `Public Property EnableExpensesManagement() As BoYesNoEnum` [R/W] Determines whether or not to enable additional expenses management Field name: EnblExpns.
  - remarks: Field name in the application: Enable Expenses Management. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->General tab.
- `Public Property EnableStockRelNoCostPrice() As BoYesNoEnum` [R/W] Determines whether or not to allow stock release without the item cost price. Field name: RelStkNoPr.
  - remarks: Field name in the application: Max. Number Of Documents In Payment. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property EnableTransactionNotification() As BoYesNoEnum` [R/W] property EnableTransactionNotification
- `Public Property GroupLinesInVATCalculation() As BoYesNoEnum` [R] Returns a valid value that determines whether or not the Tax Engine System groups the lines when calculating the tax. Field name: CalcVatGrp.
- `Public Property IEPSPayer() As BoYesNoEnum` [R/W] Determines whether or not the company is liable to IEPS Payer (indirect tax). Applicable for Mexico, Costa Rica, and Guatemala. Companies defined as liable for IEPS Payer must maintain special IEPS posting, printing forms and declaration for authorities in all A/R documents. Note: For Mexico only, when this filed is set to Y, the IEPS Payer option is available also in the Item Master Data -->General tab. Field name: IepsPayer.
  - remarks: Field name in the application: IEPS Payer. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property LanguageCode() As BoSuppLangs` [R/W] property LanguageCode
- `Public Property Localization() As String` [R] property Localization
  - remarks: Administration --> Choose Company --> Find your DB: localization column.
- `Public Property MaxNumberOfDocumentsInPmt() As Long` [R/W] Sets the maximum number of invoices for outgoing payments by check. Field name: MxDcsInPmt.
  - remarks: Field name in the application: Max. Number Of Documents In Payment. To display the form in the application: - Select Administration -->System Initialization -->Document Setting -->Per Document tab.
- `Public Property MaxRecordsInChooseFromList() As Long` [R/W] Sets the maximum number of records to display in the Choose From List form. Field name: MaxChoose.
  - remarks: Field name in the application: No. of Choose from list Rows. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Display tab.
- `Public Property MinimumAmountForAnnualList() As Double` [R/W] Sets the minimum amount above which a document is included in the annual sales report. This report is used for VAT declaration regarding customers only. The report covers all the customers who have federal tax ID that starts with a Belgium ISO code, and all the sales transactions that are VAT liable such as A/R invoices, A/R credit memos, down payments and manual journal entries created for sales purposes. Applicable for Belgium. Field name: MinAmntAL.
  - remarks: Field name in the application: Minimum Amount for Annual Sales List. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property MinimumAmountForAppndixOP() As Double` [R/W] Sets the minimum amount above which a document is included in the annual sales report. This report is used for VAT declaration regarding customers only. The report covers all the customers who have federal tax ID that starts with a Belgium ISO code, and all the sales transactions that are VAT liable such as A/R invoices, A/R credit memos, down payments and manual journal entries created for sales purposes. Applicable for Belgium. Field name: MinAmntAL.
  - remarks: Field name in the application: Minimum Amount for Annual Sales List. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property MinimumBaseAmountPerDoc() As Double` [R/W] Determines whether or not to enable generatiion of reports that include only documents with minimum base amount. Applicable for Portugal. Field name: MinBaseDoc.
  - remarks: Field name in the application: Minimum Base Amount per Document. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property PercentOfTotalAcquisition() As Double` [R/W] Determines whether or not to enable generatiion of reports that include only documents with minimum base amount. Applicable for Portugal. Field name: MinBaseDoc.
  - remarks: Field name in the application: Minimum Base Amount per Document. To display the form in the application: - Select Administration -->System Initialization -->Company Details -->Accounting Data tab.
- `Public Property SRIManagementSystem() As BoManageMethod` [R/W] Determines the default management method for serial numbers and batches. The options are: A - On Every Transaction. The user must assign serial or batch numbers on every inventory transaction. R - On Release Only. The user must assign serial or batch numbers only on release (it is optional for other transactions). Field name: SriMngSys.
  - remarks: Field name in the application: SRI Management System. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Inventory tab -->Items tab.
- `Public Property TaxCalculationSystem() As TaxCalcSysEnum` [R] Returns a valid value that determines the type of tax calculation system to be used by the Tax Calculation Engine. Field name: TaxSysType).
- `Public Property Version() As Long` [R] Returns the version of SAP Business One application used by the company. Field name: Version.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
