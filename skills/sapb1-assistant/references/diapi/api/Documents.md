<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Documents (Object)

Documents is a business object that represents the header data of documents in the Marketing Documents and Receipts module and the Inventory and Production module of SAP Business One application. The source table for each document is according to the document type as follows: - Documents(oInvoices) - OINV - Documents(oCorrectionInvoice) - OCSI - Documents(oCorrectionInvoiceReversal) - OCSV - Documents(oCreditNotes) - ORIN - Documents(oDeliveryNotes) - ODLN - Documents(oReturns) - ORDN - Documents(oOrders) - ORDR - Documents(oQuotations) - OQUT - Documents(oPurchaseInvoices) - OPCH - Documents(oCorrectionPurchaseInvoice) - OCPI - Documents(oCorrectionPurchaseInvoiceReversal) - OCPV - Documents(oPurchaseCreditNotes) - ORPC - Documents(oPurchaseDeliveryNotes) - OPDN - Documents(oPurchaseReturns) - ORPD - Documents(oPurchaseOrders) - OPOR - Documents(oPurchaseQuotations) - OPQT - Documents(oPurchaseRequests) - OPRQ - Documents(oInventoryGenEntry) - OIGN - Documents(oInventoryGenExit) - OIGE - Documents(oDrafts) - ODRF - Documents(oDownPaymentAP) - ODPO - Documents(oDownPaymentAR) - ODPI

**Remarks:** Mandatory fields in SAP Business One: CardCode and ItemCode (from Document_Lines object). To create a draft document (oDraft) also set the document object type (DocObjectCode). To display the form in the application: - For OINV table, select Sales - A/R --> A/R Invoice. - For ORIN table, select Sales - A/R --> A/R Credit Memo. - For ODLN table, select Sales - A/R --> Delivery. - For ORDN table, select Sales - A/R --> Returns. - For ORDR table, select Sales - A/R --> Order. - For OQUT table, select Sales - A/R --> Quotation. - For OPCH table, select Purchasing - A/P --> A/P Invoice. - For ORPC table, select Purchasing - A/P --> A/P Credit Memo. - For OPDN table, select Purchasing - A/P --> Goods Receipt PO. - For ORPD table, select Purchasing - A/P --> Goods Returns. - For OPOR table, select Purchasing - A/P --> A/R Invoice. - For OPQT table, select Purchasing - A/P --> Purchase Quotation. - For OIGN table, select Inventory --> Inventory Transactions --> Goods Receipt. Or, in case of receipt from production, select Production --> Receipt from Production (see ProductionOrders). - For OIGE table, select Inventory --> Inventory Transactions --> Goods Issue. Or, in case of issue for production, select Production --> Issue for Production (see ProductionOrders). - For ODRF table, select Sales - A/R (or Purchasing - A/P) --> Document Draft. Set your selection criteria, and click OK.

## Properties (290)
- `Public Property AdditionalLegalInformation() As String` [R/W] Additional legal information text. Field name: AddLegIn. Length: 100 characters.
- `Public Property Address() As String` [R/W] The business partner's Bill To address (sales documents) or the warehouse address (purchase documents). If the AddressExtension property contains values for its BillTo subproperties, then the Address property value is replaced with a formatted address string based on the values in the AddressExtension property. Field name: Address Length: 254 characters
  - remarks: You can update the value of the Address property only in sales quotations, sales orders, purchase quotations, and purchase orders. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Address2() As String` [R/W] The business partner's Ship To address. If the AddressExtension property contains values for its ShipTo subproperties, then the Address2 property value is replaced with a formatted address string based on these values in the AddressExtension property. Field name: Address2 Length: 254 characters
- `Public Property AddressExtension() As AddressExtension` [R] The Bill To and Ship To addresses for the document. This property enables you to specify the BillTo and ShipTo addresses by defining their component parts -- for example, the street name, city name, and country -- instead of specifying the address as free-text strings. After setting the AddressExtension property, the system does the following: - Clears the Address and Address2 properties. - Creates BillTo and ShipTo addresses based on the values in the AddressExtension property. The address format is determined by the country's address format, which is specified at Administration --> Setup --> Business Partner --> Countries. The format used is either the format for the country specified in […]
  - remarks: - If both the AddressExtension BillTo properties and and the Address property are modified, the AddressExtension properties are cleared and the Address property is stored. The same is true for the AddressExtension ShipTo properties and Address2 property. - If only the AddressExtension BillTo properties are changed, then the Address property is updated, but the AddressExtension ShipTo properties and the Address2 property are not affected (and vice versa).
- `Public Property AgentCode() As String` [R/W] Sets or returns the code of the company employee responsible for the collection and management of bill of exchange transactions related to the business partner. Field name: AgentCode. Length: 32 characters. This is a foreign key to the OAGP object.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property AnnualInvoiceDeclarationReference() As Long` [R/W] property AnnualInvoiceDeclarationReference
- `Public Property ApplyCurrentVATRatesForDownPaymentsToDraw() As BoYesNoEnum` [R/W] property ApplyCurrentVATRatesForDownPaymentsToDraw
- `Public Property ApplyTaxOnFirstInstallment() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to add the tax amount calculated in the invoice to the amount of the first installment. Field name: VATFirst.
  - remarks: For example, if the total amount of the invoice before tax is $1000, and the tax amount is $100, and the first installment percentage is 50% (of $1000) than the first installment amount is $600. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property ArchiveNonremovableSalesQuotation() As BoYesNoEnum` [R/W] Indicates whether to archive the document even when it is linked to other documents that cannot be archived. The document must still be in the archive date range and conform to all the other rules for being archived. Applies to sales quotations only. Field name: IgnRelDoc
- `Public Property AssetValueDate() As Date` [R/W] property AssetValueDate
- `Public Property ATDocumentType() As String` [R/W] property ATDocumentType
- `Public Property AttachmentEntry() As Long` [R/W] The attachment for marketing documents. Field name: AtcEntry
  - remarks: Foreign key to OATC.
- `Public Property AuthorizationCode() As String` [R/W] property AuthorizationCode
- `Public Property AuthorizationStatus() As DocumentAuthorizationStatusEnum` [R] Returns the status of the authorization for this payment. Field name: wddStatus.
- `Public Property BaseAmount() As Double` [R] Returns the net amount (amount excluding tax, including expenses) of the document, in local currency. Field name: BaseAmnt.
- `Public Property BaseAmountFC() As Double` [R] Returns the net amount (amount excluding tax, including expenses) of the document, in foreign currency. Field name: BaseAmntFC.
- `Public Property BaseAmountSC() As Double` [R] Returns the net amount (amount excluding tax, including expenses) of the document, in system currency. Field name: BaseAmntSC.
- `Public Property BaseEntry() As Long` [R/W] The base document internal key for inventory transfer in India localization. Field name: BaseEntry.
- `Public Property BaseType() As Long` [R/W] The base document type for inventory transfer in India localization. The object code for WTR is 67. Field name: BaseType.
  - C# example (from SAP's help):
    ```csharp
    Documents oInv = (Documents)oCompany.GetBusinessObject(BoObjectTypes.oInvoices);
    oInv.BaseType = 67;
    oInv.BaseEntry = baseEntry;
    ```
- `Public Property BillOfExchangeReserved() As BoYesNoEnum` [R] Not used. Field name: BoeReserev.
- `Public Property BlanketAgreementNumber() As Long` [R/W] property BlanketAgreementNumber
- `Public Property BlockDunning() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to block dunning. Field name: BlockDunn. Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to block dunning letters to the business partner. Field name: BlockDunn. Length: 1 character.
  - remarks: This property is relevant only for sales invoice documents.
- `Public Property Box1099() As String` [R/W] Default value is retrieved from Box1099 property of the BusinessPartners object. Field name: Box1099. Country-specific property for USA. Sets or returns the number of Box 1099 on the Form 1099 where the payment should be entered. Field name: Box1099. Length: 20 characters.
  - remarks: Set this property only if you set Form1099 property. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property BPChannelCode() As String` [R/W] Sets or returns the distribution channel for the business partner (the distribution channel is also a business partner). Relevant to business partners of customer type only. Field name: BPChCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property BPChannelContact() As Long` [R/W] Sets or returns the contact person of the business partner channel. Field name: BPChCntc. This is a foreign key to the ContactEmployees object.
- `Public Property BPL_IDAssignedToInvoice() As Long` [R/W] Sets or returns the business place ID assigned to a marketing document (such as, invoice). Field name: BPLId.
  - remarks: Country-specific for Korea. In Korea, Business Place is a mandatory field in all marketing documents. Any purchase or sales transaction should be linked to a business place (with valid VAT registration number), the value of BPL_IDAssignedToInvoice should be the foreign key pointing to OBPL table (i.e. business place master data).
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CancelDate() As Date` [R/W] Sets or returns the cancel date of the sales order or purchase order. After this date, shipping the goods to the customer or from the vendor is not allowed. Field name: CancelDate.
  - remarks: Relevant to sales orders and purchase orders only. The default date is the Delivery Date (DocDueDate) of the document + 30 days. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Cancelled() As BoYesNoEnum` [R] Indicates whether the document was cancelled.
- `Public Property CancelStatus() As CancelStatusEnum` [R] Indicates the document cancel status.
- `Public Property CardCode() As String` [R/W] Sets or returns the customer or vendor code. Field name: CardCode. This is a foreign key to the BusinessPartners object. Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners Object
  - remarks: For oInventoryGenEntry and oInventoryGenExit document types, DI API versions 6.2 and 6.5, the value of this property specifies the G/L Account number. From DI API version 2004, this property is not relevant for oInventoryGenEntry and oInventoryGenExit document types. The G/L account for these document types is based on AccountCode property in Document_Lines object (which its default value is taken from the G/L account associated with the item).
- `Public Property CardName() As String` [R/W] Sets or returns the customer or vendor name. Field name: CardName. Length: 100 characters. Sets or returns the business partner's full name. Field name: CardFName. Length: 100 characters.
  - remarks: The default value is retrieved from CardName property of the BusinessPartners object. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property CashDiscountDateOffset() As Long` [R/W] property CashDiscountDateOffset
- `Public Property CentralBankIndicator() As String` [R/W] Sets or returns the central bank indicator for foreign documents as defined in SAP Business One. Field name: CntrlBnk. Length: 15 characters. This is a foreign key to the Central Bank Ind. object (OCBI), not exposed through the DI API)
  - remarks: Relevant to sales and purchase invoices only.
- `Public Property CertificationNumber() As String` [R] property CertificationNumber
- `Public Property Cig() As Long` [R/W] property Cig
- `Public Property ClosingDate() As Date` [R/W] Set or retrieves Document closing date. Field name: ClsDate.
- `Public Property ClosingOption() As ClosingOptionEnum` [R/W] To close a goods receipt PO or a goods return, specify a posting date to be used in the clearing journal entry. Field: ClosingOpt.
  - C# example (from SAP's help):
    ```csharp
    //Close by current system date
    Documents doc = (Documents)oCompany.GetBusinessObject(BoObjectTypes.oPurchaseReturns);
    doc.GetByKey(1);
    doc.ClosingOption = ClosingOptionEnum.coByCurrentSystemDate;
    doc.Close();
    //Close by original document date
    Documents doc = (Documents)oCompany.GetBusinessObject(BoObjectTypes.oPurchaseReturns);
    doc.GetByKey(1);
    doc.ClosingOption = ClosingOptionEnum.coByOriginalDocumentDate;
    doc.Close();
    //Close by specified date
    Documents doc = (Documents)oCompany.GetBusinessObject(BoObjectTypes.oPurchaseReturns);
    doc.GetByKey(1);
    doc.ClosingOption = ClosingOptionEnum.coBySpecifiedDate;
    DateTime date = DateTime.Parse("2010/6/26");
    doc.SpecifiedClosingDate = date;
    doc.Close();
    ```
- `Public Property ClosingRemarks() As String` [R/W] Sets or returns the Footer text of the sales or purchasing document. Field name: Footer. Length: 64000 characters.
  - remarks: To access the Opening and Closing Remarks window in the application: - Create a sales or purchasing document and choose Goto > Opening and Closing Remarks.
- `Public Property Comments() As String` [R/W] Sets or returns comments for the document. Field name: Comments. Length: 254 characters.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property CommissionTrade() As CommissionTradeTypeEnum` [R/W] property CommissionTrade
- `Public Property CommissionTradeReturn() As BoYesNoEnum` [R/W] property CommissionTradeReturn
- `Public Property Confirmed() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this document is confirmed. The information of confirmed documents can be used as a basis for creating other documents (such as invoices). Field name: Confirmed.
  - remarks: This property is used for sales orders only. Unconfirmed documents do not change real data such as, storage, account, and so on. After confirmation, the document information cannot be changed and relative information is updated accordingly. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property ContactPersonCode() As Long` [R/W] Sets or returns the Contact Person code. Field name: CntctCode. This is a foreign key to the ContactEmployees object.
  - remarks: The default value is according to ContactPerson property of the BusinessPartners object. You can update the value of the ContactPersonCode property only in sales quotations, sales orders, purchase quotations, and purchase orders. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property ControlAccount() As String` [R/W] The control account for this document. Field name: CtlAccount This is a foreign key to the ChartOfAccounts object.
- `Public Property CreateOnlineQuotation() As BoYesNoEnum` [R/W] property CreateOnlineQuotation
- `Public Property CreateQRCodeFrom() As String` [R/W] property CreateQRCodeFrom
- `Public Property CreationDate() As Date` [R] Returns the creation date of the document. Field name: CreateDate.
  - remarks: This property is internal in SAP Business One.
- `Public Property Cup() As Long` [R/W] property Cup
- `Public Property CustOffice() As String` [R/W] Enter Customs Office Name. It is mandatory if Export Process form is filled in.. Field name: CustOffice. Length: 60 characters.
- `Public Property DANFELegalText() As String` [R] DANFE Legal Text. Field name: DANFELgTxt.
- `Public Property DateOfReportingControlStatementVAT() As Date` [R/W] property DateOfReportingControlStatementVAT
- `Public Property DeferredTax() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the business partner applies deferred tax. Field name: DeferrTax. Length: 1 characters.
  - remarks: Country-specific for Spain, Italy, Portugal, and France.
- `Public Property DiscountPercent() As Double` [R/W] Sets or returns the discount percentage you specify for a customer, or the discount percentage a supplier specifies for you. Field name: Discount.
  - remarks: The default value is retrieved from DiscountPercent property of the BusinessPartners object. You can update the value of the DiscountPercent property only in sales quotations, sales orders, purchase quotations, and purchase orders. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types. This property is not relevant when using Down Payment.
- `Public Property DocCurrency() As String` [R/W] Sets or returns the currency used in the document. Field name: DocCur. Length: 3 characters. This is a foreign key to the Currencies object.
  - remarks: The default value is retrieved from the Currency property of the BusinessPartners object. However, in case: - the the business partner uses multi-currency, and - the document is either purchase order, sales order, or quotation, and - the document is not used as a base document, then the system, by default, retrieves the local currency. If a different currency is required, you can specify it by the DocCurrency property. Then the system updates the DocRate from the Currency Rates Table according to the specified document currency. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocDate() As Date` [R/W] Sets or returns the document posting date. Field name: DocDate.
  - remarks: The default is the current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocDueDate() As Date` [R/W] Sets or returns the document due date (for example, Delivery Date in sales orders, Value Date in invoices, Valid To in quotations, and so on). Field name: DocDueDate.
  - remarks: The document due date must be within the financial period and later than posting date (DocDate). This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocEntry() As Long` [R] Returns the document entry key that uniquely identifies the document. Field name: DocEntry.
- `Public Property DocNum() As Long` [R/W] Sets or returns the number of the document. Mandatory field in SAP Business One only in case the value of the HandWritten property is tYES. Field name: DocNum. and also verify Relevant to sales documents only. In case the value of the HandWritten property is tNO and you add a sales document, SAP Business One automatically assigns the next available number to the document, in accordance with the document numbering system defined during system configuration. When saving the document as a draft, this number is stored for the document draft only. So that the number of the draft is still available in the system for other new documents. The system may assign this number to a new document of the […]
  - remarks: and also verify Relevant to sales documents only. In case the value of the HandWritten property is tNO and you add a sales document, SAP Business One automatically assigns the next available number to the document, in accordance with the document numbering system defined during system configuration. When saving the document as a draft, this number is stored for the document draft only. So that the number of the draft is still available in the system for other new documents. The system may assign this number to a new document of the same type. When saving the draft as a document, SAP Business One assigns a new available number. In case the value of the HandWritten property is tYES, set a value (greater than 0) to the DocNum property and also set the Series property to -1.
- `Public Property DocObjectCode() As BoObjectTypes` [R/W] Sets or returns a valid value of BoObjectTypes type that specifies the object type related to a draft document. Note: This property is replaced by DocObjectCodeEx property (string), but remains in the collection due to backward compatibility.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocObjectCodeEx() As String` [R/W] Sets or returns the a valid value of BoObjectTypes that defines the document object code (replaces the valid values of DocObjectCode property).
  - remarks: For the object's codes, see the numbers in the BoObjectTypes table.
- `Public Property DocRate() As Double` [R/W] Sets or returns the exchange rate with local currency for the document. Field name: DocRate.
  - remarks: Not relevant for documents that use local currency. If the document does not use local currency, you must specify an exchange rate for this document. To get a recommended exchange rate, use the GetCurrencyRate method. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocTime() As Date` [R/W] Sets or returns the document creation time. Field name: DocTime.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocTotal() As Double` [R/W] Sets or returns the total amount in the document. Field name: DocTotal.
  - remarks: Do not use this property for oInventoryGenEntry and oInventoryGenExit document types. In case you set this property for these documents, an error occur and the document will not be added.
- `Public Property DocTotalFc() As Double` [R/W] Sets or returns the total amount, in foreign currency, in the document. Field name: DocTotalFC.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocTotalSys() As Double` [R] Sets or returns the total amount, in system currency, in the document. Field name: DocTotalSy.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property DocType() As BoDocumentTypes` [R/W] Sets or returns a valid value of BoDocumentTypes type that specifies the business transaction content type: Items Transaction or Service Transaction. Field name: DocType.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Document_ApprovalRequests() As Document_ApprovalRequests` [R] Returns the Document_ApprovalRequests object.
- `Public Property DocumentDelivery() As DocumentDeliveryTypeEnum` [R/W] Property DocumentDelivery
- `Public Property DocumentReferences() As Document_DocumentReferences` [R] property DocumentReferences
- `Public Property DocumentsOwner() As Long` [R/W] Sets or returns the document owner. Field name: OwnerCode. This is a foreign key to the EmployeesInfo object.
- `Public Property DocumentStatus() As BoStatus` [R] Returns a valid value of BoStatus type that specifies document status (closed or open). Field name: DocStatus.
- `Public Property DocumentSubType() As BoDocumentSubType` [R/W] Sets or returns a valid value of BoDocumentSubType type that specifies document sub-type. Field name: DocSubType.
  - remarks: This enables to create a sub document with a separate series number. For example, creating an exempt invoice. Country-specific field for Mexico and Chile.
- `Public Property DocumentTaxID() As String` [R/W] property DocumentTaxID
- `Public Property DownPayment() As Double` [R/W] Deprecated in Release 2006 A. Instead, use the properties DownPaymentAmount, DownPaymentAmountFC, DownPaymentAmountSC.
- `Public Property DownPaymentAmount() As Double` [R/W] Returns the total down payment amount in local currency. Field name: DpmAmnt.
- `Public Property DownPaymentAmountFC() As Double` [R/W] Returns the total down payment amount in foreign currency. Field name: DpmAmntFC.
- `Public Property DownPaymentAmountSC() As Double` [R/W] Returns the total down payment amount in system currency. Field name: DpmAmntSC.
- `Public Property DownPaymentPercentage() As Double` [R/W] Sets or returns percentage of down payment. Field name: DpmPrcnt.
- `Public Property DownPaymentStatus() As BoSoStatus` [R/W] property DownPaymentStatus
- `Public Property DownPaymentsToDraw() As DownPaymentsToDraw` [R] Returns an instance of DownPaymentsToDraw object holding properties of available down payments (sales and purchase) that can be drawn to A/R or A/P invoice.
- `Public Property DownPaymentTrasactionID() As String` [R/W] property DownPaymentTrasactionID
- `Public Property DownPaymentType() As DownPaymentTypeEnum` [R/W] Returns or sets a value specifying whether the down payment document is invoice or request. Field name: Posted.
  - remarks: Relevant for Czech, Slovak, Hungary, and Poland localizations.
- `Public Property ECommerceGSTIN() As String` [R/W] property ECommerceGSTIN
- `Public Property ECommerceOperator() As String` [R/W] property ECommerceOperator
- `Public Property EDocErrorCode() As String` [R/W] property EDocErrorCode
- `Public Property EDocErrorMessage() As String` [R/W] property EDocErrorMessage
- `Public Property EDocExportFormat() As Long` [R/W] property EDocExportFormat
- `Public Property EDocGenerationType() As EDocGenerationTypeEnum` [R/W] property EDocGenerationType
- `Public Property EDocNum() As String` [R/W] property EDocNum
- `Public Property EDocSeries() As Long` [R/W] property EDocSeries
- `Public Property EDocStatus() As EDocStatusEnum` [R/W] property EDocStatus
- `Public Property EDocType() As EDocTypeEnum` [R/W] property EDocType
- `Public Property ElecCommMessage() As String` [R] property ElecCommMessage
- `Public Property ElecCommStatus() As ElecCommStatusEnum` [R/W] property ElecCommStatus
- `Public Property ElectronicProtocols() As ElectronicProtocols` [R] property ElectronicProtocols
- `Public Property EndDeliveryDate() As Date` [R/W] property EndDeliveryDate
- `Public Property EndDeliveryTime() As Date` [R/W] property EndDeliveryTime
- `Public Property ETaxNumber() As String` [R/W] property ETaxNumber
- `Public Property ETaxWebSite() As Long` [R/W] property ETaxWebSite
- `Public Property EWayBillDetails() As Document_EWayBillDetails` [R] property EWayBillDetails
- `Public Property ExcludeFromTaxReportControlStatementVAT() As BoYesNoEnum` [R/W] property ExcludeFromTaxReportControlStatementVAT
- `Public Property ExemptionValidityDateFrom() As Date` [R/W] Sets or returns the Exemption Validity Date From. This property is linked to the ExemptionValidityDateFrom property of the BusinessPartners object. Relevant to invoice documents only. Field name: FromDate.
- `Public Property ExemptionValidityDateTo() As Date` [R/W] Sets or returns the Exemption Validity Date To. This property is linked to the ExemptionValidityDateTo property of the BusinessPartners object. Relevant to invoice documents only. Field name: ToDate.
- `Public Property Expenses() As DocumentsAdditionalExpenses` [R] Returns the DocumentsAdditionalExpenses child object.
- `Public Property ExternalCorrectedDocNum() As String` [R/W] Not used. Field name: CorrExt.
  - remarks: Country-specific property for Poland.
- `Public Property ExtraDays() As Long` [R/W] property ExtraDays
- `Public Property ExtraMonth() As Long` [R/W] property ExtraMonth
- `Public Property FatherCard() As String` [R/W] Sets or returns the card code of the parent business partner (for example, card code of the head office related to the current business partner). Field name: FatherCard. Length: 15 characters.
  - remarks: The property is exposed for the following documents: - A/R Invoice (OINV) - A/R Credit Memo (ORIN) - A/R Reserve Invoices (OINV) - A/P Invoice (OPCH) - A/P Credit Memo (ORPC) - A/P Reserve Invoices (OPCH) - Delivery (ODLN) - Returns (ORDN) - Goods Receipt PO (OPDN) - Goods Returns (ORPD) In SAP Business One, you can organize business partners in hierarchical structure. Use this property to specify the parent business partner. Organizing business partners hierarchically is useful when you create separate business partner cards for branches of the same business partner. This allows you to consolidate all business activities for the head office. You can either send delivery notes together in one invoice to the head office or balance the invoices sent to the various branches by means of a payment from the head office.
- `Public Property FatherType() As BoFatherCardTypes` [R/W] Sets or returns a valid value of BoFatherCardTypes that specifies the method of handling deliveries and payments used by the parent business partner. Field name: FatherType.
  - remarks: The property is exposed for the following documents: - A/R Invoice (OINV) - A/R Credit Memo (ORIN) - A/R Reserve Invoices (OINV) - A/P Invoice (OPCH) - A/P Credit Memo (ORPC) - A/P Reserve Invoices (OPCH) - Delivery (ODLN) - Returns (ORDN) - Goods Receipt PO (OPDN) - Goods Returns (ORPD) Set to cDelivery_sum to send delivery notes in one invoice to the head office. Set to cPayments_sum to balance invoices sent to branches using payments from the head office.
- `Public Property FCEAsPaymentMeans() As BoYesNoEnum` [R/W] property FCEAsPaymentMeans
- `Public Property FCI() As String` [R/W] Enter the FCI Number. Field name: FCI. Length: 36 characters.
- `Public Property FederalTaxID() As String` [R/W] Sets or returns the federal tax ID of the business partner. Field name: LicTradNum. Length: 32 characters.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property FinancialPeriod() As Long` [R] Returns the financial period. Field name: FinncPriod. This is a foreign key to the CompanyService object.
- `Public Property FiscalDocNum() As String` [R/W] property FiscalDocNum
- `Public Property FolioNumber() As Long` [R/W] Sets or returns the additional number for a printed document. Field name: FolioNum.
  - remarks: Country-specific field for Mexico and Chile.
- `Public Property FolioNumberFrom() As Long` [R/W] property FolioNumberFrom
- `Public Property FolioNumberTo() As Long` [R/W] property FolioNumberTo
- `Public Property FolioPrefixString() As String` [R/W] Sets or returns the prefix for the FolioNumber. Field name: FolioPref. Length: 2 characters.
  - remarks: Country-specific field for Mexico and Chile.
- `Public Property Form1099() As Long` [R/W] Sets or returns the 1099 form. Field name: Form1099. This is a foreign key to the Forms1099 object. Sets or returns the code of the Form 1099. Field name: FormCode. This is a foreign key to the Forms1099 object.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property GroupHandWritten() As BoYesNoEnum` [R/W] Specify whether to have the manual number of the purchase quotation group. Field name: PQTGrpHW.
- `Public Property GroupNumber() As Long` [R/W] Number of the purchase quotation group. That is, all items that are contained in one purchase quotation share the same group number. Field: PQTGrpNum.
- `Public Property GroupSeries() As Long` [R/W] Sets or returns the auto-number series that are generated for the purchase quotation group. Field name: PQTGrpSer.
- `Public Property GSTTransactionType() As GSTTransactionTypeEnum` [R/W] property GSTTransactionType
- `Public Property GTSChecker() As Long` [R/W] property GTSChecker
- `Public Property GTSPayee() As Long` [R/W] property GTSPayee
- `Public Property HandWritten() As BoYesNoEnum` [R/W] Determines whether or not this document is based on a handwritten document. Field name: Handwrtten.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types. Field name: .
- `Public Property ImportFileNum() As Long` [R/W] Sets or returns the landed costs key (import file number). The import file is used as a basis for purchase documents (purchase order and goods receipt). Field name: LndCstNum.
  - remarks: This property is related to Import Data Document in Purchase menu. It represents the number of the import as defined by the customs agency. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types. Field name: .
- `Public Property Indicator() As String` [R/W] Sets or returns the factoring indicator . Field name: Indicator. This is a foreign key to the FactoringIndicators object. The Factoring Indicators object enables to define a key that can be used as a selection criterion in various reports. Sets or returns the Factoring Indicator for the business partner master record. Field name: Indicator. Length: 2 characters. This is a foreign key to the FactoringIndicators object.
  - remarks: This indicator is automatically inserted as default value in outgoing invoices and may be displayed in the account statements. Can be used later for sorting invoices related to this business partner. You can set only an indicator that is already defined in SAP Business One. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property IndicatorForFinalConsumer() As BoYesNoEnum` [R/W] The checkbox Final Consumer on the header of an A/R invoice, A/R sales order, A/R sales quotation, delivery, return or credit note. Field name: IndFinal.
- `Public Property Installments() As Document_Installments` [R] Returns an instance of Document_Installments object holding installments properties.
- `Public Property InsuranceOperation347() As BoYesNoEnum` [R/W] Indicates if this document is reported with the insurance operation type in 347 reports. Field name: InsurOp347
- `Public Property InterimType() As BoInterimDocTypes` [R/W] property InterimType
- `Public Property InternalCorrectedDocNum() As Long` [R/W] Not used.
  - remarks: Country-specific property for Poland.
- `Public Property InventoryStatus() As BoStatus` [R] property InventoryStatus
- `Public Property InvoicePayment() As BoYesNoEnum` [R] property InvoicePayment
- `Public Property IsAlteration() As BoYesNoEnum` [R/W] property IsAlteration
- `Public Property IsPayToBank() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether to specify the bank details or only the PayToCode for the outgoing payment. Field name: IsPaytoBnk.
- `Public Property IssuingReason() As Long` [R/W] property IssuingReason
- `Public Property JournalMemo() As String` [R/W] Sets or returns the journal entry remarks that is copied later to the accounting document. Field name: JrnlMemo. Length: 50 characters.
  - remarks: SAP Business One, by default, automatically enters the document type and the business partner number. When using the system's default template for printing, the remark is not printed on the associated document. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property LanguageCode() As Long` [R/W] Sets or returns the Language Code of the document. Field name: LangCode. Field name: LangCode. This is the foreign key of the UserLanguages object.
- `Public Property LastPageFolioNumber() As Long` [R] Folio number of the last page of the marketing document in the Chile localization. Field name: LPgFolioN.
- `Public Property LegalTextFormat() As Long` [R/W] Legal text format template. Field name: LegTextF.
- `Public Property Letter() As FolioLetterEnum` [R/W] property Letter
- `Public Property Lines() As Document_Lines` [R] Returns the Document_Lines child object.
- `Public Property ManualNumber() As String` [R/W] Sets or returns the manual number of the document. Field name: ExpAnSys. Length: 20 characters.
- `Public Property MaximumCashDiscount() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to calculate the discount in a payment run even if its due date is expired. Field name: MaxDscn.
  - remarks: Relevant to Sales and Purchasing documents.
- `Public Property NetProcedure() As BoYesNoEnum` [R] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to calculate a cash discount in A/P invoices according the payment terms with the vendor. Field name: NetProc.
  - remarks: Country-specific property for EU.
- `Public Property NextCorrectingDocument() As Long` [R] Not used.
  - remarks: Country-specific property for Poland.
- `Public Property NTSApproved() As BoYesNoEnum` [R/W] property NTSApproved
- `Public Property NTSApprovedNumber() As String` [R/W] property NTSApprovedNumber
- `Public Property NumAtCard() As String` [R/W] Sets or returns a unique code by which your vendor/customer identifies your company. Field name: NumAtCard. Length: 100 characters.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property NumberOfInstallments() As Long` [R/W] Sets or returns the number of installments for the payment. Field name: Installmnt.
  - remarks: In SAP Business One, each installment appears as an exclusive record in payments, journal entries, reconciliations, and reports. Relevant for sales and purchase invoices only.
- `Public Property OpenForLandedCosts() As BoYesNoEnum` [R/W] Enables the landed costs feature. Field name: OpenForLaC.
- `Public Property OpeningRemarks() As String` [R/W] Sets or returns the Header text of the sales or purchasing document. Field name: Header. Length: 64000 characters.
  - remarks: To access the Opening and Closing Remarks window in the application: - Create a sales or purchasing document and choose Goto > Opening and Closing Remarks.
- `Public Property OriginalCreditOrDebitDate() As Date` [R/W] property OriginalCreditOrDebitDate
- `Public Property OriginalCreditOrDebitNo() As String` [R/W] property OriginalCreditOrDebitNo
- `Public Property OriginalRefDate() As Date` [R/W] property OriginalRefDate
- `Public Property OriginalRefNo() As String` [R/W] property OriginalRefNo
- `Public Property Packages() As DocumentPackages` [R] Returns the DocumentPackages object, which is a child object of Documents holding package details for items in Delivery and A/R Invoice documents.
- `Public Property PaidToDate() As Double` [R] property PaidToDate
- `Public Property PaidToDateFC() As Double` [R] property PaidToDateFC
- `Public Property PaidToDateSys() As Double` [R] property PaidToDateSys
- `Public Property PartialSupply() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not only some of the items were supplied to the customer. Field name: PartSupply.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property PaymentBlock() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to block a payment due to a reason specified in PaymentBlockEntry property. Field name: PayBlock.
- `Public Property PaymentBlockEntry() As Long` [R/W] Sets or returns a description of the payment block reason as defined in SAP Business One in 'Define Payment Block' table. Field name: PayBlckRef. This is a foreign key to the OPYB object.
- `Public Property PaymentGroupCode() As Long` [R/W] Sets or returns the payment terms used in the document . Field name: GroupNum. This is a foreign key to the PaymentTermsTypes object.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property PaymentMethod() As String` [R/W] Sets or returns the payment method for outgoing payments (for example: check, bank transfer, and so on). Field name: PeyMethod. Length: 15 characters. This is a foreign key to the WizardPaymentMethods object.
  - remarks: The valid values are defined in SAP Business One in the Payment Methods table (OPYM table, which is not exposed through the DI API).
- `Public Property PaymentReference() As String` [R/W] Returns the payment reference that authorizes the payment process (according to the legal requirements). Field name: PaymentRef. Length: 27 characters.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property PayToBankAccountNo() As String` [R/W] Sets or returns the bank account number for the outgoing payment. Field name: BnkAccount. Length: 50 characters.
  - remarks: Relevant only if IsPayToBank property is set to tYES. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property PayToBankBranch() As String` [R/W] Sets or returns the bank branch for the outgoing payment. Field name: BnkBranch. Length: 50 characters.
  - remarks: Relevant only if IsPayToBank property is set to tYES. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property PayToBankCode() As String` [R/W] Sets or returns the bank code for the outgoing payment. Field name: BankCode. Length: 30 characters.
  - remarks: Relevant only if IsPayToBank property is set to tYES.
- `Public Property PayToBankCountry() As String` [R/W] Sets or returns the bank country for the outgoing payment. Field name: BnkCntry. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: Relevant only if IsPayToBank property is set to tYES.
- `Public Property PayToCode() As String` [R/W] Sets or returns the destination code for the outgoing payment. Field name: PayToCode. Length: 50 characters.
  - remarks: Relevant only if IsPayToBank property is set to tYES.
- `Public Property PeriodIndicator() As String` [R] Returns the period indicator of the document. Field name: PIndicator. Length: 10 characters. This is a foreign key to the Period Indicator table (OPID - not exposed through the DI API).
  - remarks: Period indicator is used in documents series to enable document numbering starting with 1 for each fiscal year.
- `Public Property Pick() As BoYesNoEnum` [R/W] Returns a valid value of BoYesNoEnum type that specifies whether or not to create a pick list document. Field name: pick.
  - remarks: The Pick List document lists the items to pick from the warehouse. The end-user uses the pick list to track the items released from the warehouse and manage their status and actual quantities.
- `Public Property PickRemark() As String` [R/W] Sets or returns the Pick Remarks, the remarks related to the pick process . Field name: PickRmrk. Length: 254 characters.
- `Public Property PickStatus() As BoYesNoEnum` [R] Returns a valid value that specifies the picking status of the items specified in the document: picked, not picked, released for picking, or partially picked from the warehouse. Field name: PickStatus.
- `Public Property PlasticPackagingTaxRelevant() As BoYesNoEnum` [R/W] Document relevant for plastic packaging tax in UK localization. Field name: Rel4PPTax.
- `Public Property PointOfIssueCode() As String` [R/W] property PointOfIssueCode
- `Public Property POS_CashRegister() As Long` [R/W] property POS_CashRegister
- `Public Property POSCashierNumber() As Long` [R/W] property POSCashierNumber
- `Public Property POSDailySummaryNo() As Long` [R/W] property POSDailySummaryNo
- `Public Property POSEquipmentNumber() As String` [R/W] property POSEquipmentNumber
- `Public Property POSManufacturerSerialNumber() As String` [R/W] property POSManufacturerSerialNumber
- `Public Property POSReceiptNo() As Long` [R/W] property POSReceiptNo
- `Public Property PriceMode() As PriceModeDocumentEnum` [R/W] property PriceMode
- `Public Property Printed() As PrintStatusEnum` [R/W] Sets or returns a valid value of PrintStatusEnum type that specifies whether or not this document was printed. Field name: Printed.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property PrintSEPADirect() As BoYesNoEnum` [R/W] property PrintSEPADirect
- `Public Property PrivateKeyVersion() As Long` [R] property PrivateKeyVersion
- `Public Property Project() As String` [R/W] Sets or returns the project code related to the document. Field name: Project. Length: 8 characters This is a foreign key to Project Codes table - OPRJ. You can work with this table using the ProjectsService.
  - remarks: In SAP Business One, you can relate business transactions to projects. This can help you to create cost/income analyzes reports based on projects.
- `Public Property Receiver() As Long` [R/W] property Receiver
- `Public Property Reference1() As String` [R/W] Sets or returns the first reference code of the document. Field name: Ref1. Length: 11 characters.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Reference2() As String` [R/W] Sets or returns the second reference code of the document. Field name: Ref2. Length: 11 characters. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property RelatedEntry() As Long` [R/W] property RelatedEntry
- `Public Property RelatedType() As Long` [R/W] property RelatedType
- `Public Property Releaser() As Long` [R/W] property Releaser
- `Public Property RelevantToGTS() As BoYesNoEnum` [R/W] property RelevantToGTS
- `Public Property ReopenManuallyClosedOrCanceledDocument() As BoYesNoEnum` [R/W] Specifies whether to reopen an original document that was manually closed or cancelled. Field: ReopManCls.
  - remarks: Available for document type: return, A/R credit memo, goods return and A/P credit memo.
- `Public Property ReopenOriginalDocument() As BoYesNoEnum` [R/W] Specifies whether to reopen a sales or purchasing order when you create a return or goods return document that is based on the sales or purchasing order, or when you create a credit memo based on an invoice. Field: ReopOriDoc.
  - remarks: Available for document type: return, A/R credit memo, goods return and A/P credit memo.
- `Public Property ReportingSectionControlStatementVAT() As String` [R/W] property ReportingSectionControlStatementVAT
- `Public Property ReqCode() As String` [R/W] Requester code. Field name: ReqCode. Length: 50 characters.
- `Public Property ReqType() As Long` [R/W] property ReqType
- `Public Property Requester() As String` [R/W] property Requester
- `Public Property RequesterBranch() As Long` [R/W] property RequesterBranch
- `Public Property RequesterDepartment() As Long` [R/W] property RequesterDepartment
- `Public Property RequesterEmail() As String` [R/W] property RequesterEmail
- `Public Property RequesterName() As String` [R/W] property RequesterName
- `Public Property RequriedDate() As Date` [R/W] Sets or returns the date in which the customer expects the goods. Field name: ReqDate.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Reserve() As BoYesNoEnum` [R] Returns a valid value that specifies whether or not this document was saved by the payment wizard. Field name: Reserve.
- `Public Property ReserveInvoice() As BoYesNoEnum` [R/W] Determines whether or not this document is a Reserve Invoice, invoice that can be drawn to a delivery. Field name: isIns.
  - remarks: Reserve Invoices allow issuing invoices for warehouse items without deducting the items from the inventory (SAP Business One creates a journal entry without creating an inventory entry). Reserve Invoices refer only to item invoices.
- `Public Property ReuseDocumentNum() As BoYesNoEnum` [R/W] property ReuseDocumentNum
- `Public Property ReuseNotaFiscalNum() As BoYesNoEnum` [R/W] property ReuseNotaFiscalNum
- `Public Property Revision() As BoYesNoEnum` [R/W] property Revision
- `Public Property RevisionPo() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to split a purchase order to different warehouses in different locations. Field name: RevisionPo.
  - remarks: Relevant to purchase orders only. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Rounding() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to round the total amount in sales or purchase documents. Field name: Rounding.
  - remarks: Relevant to sales and purchase documents only.
- `Public Property RoundingDiffAmount() As Double` [R/W] The difference between the original amount and the rounded amount. Field name: RoundDif
- `Public Property RoundingDiffAmountFC() As Double` [R] The difference between the original amount and the rounded amount in foreign currency. Field name: RoundDifFC
- `Public Property RoundingDiffAmountSC() As Double` [R] The difference between the original amount and the rounded amount in system currency. Field name: RoundDifSy
- `Public Property SalesPersonCode() As Long` [R/W] Sets or returns the code of the sales employee who has created this document. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: Can be updated in open sales quotations and open purchase orders only. If a sales employee is defined for the selected business partner, the value for this property is retrieved from the SalesPersonCode property (BusinessPartners object), else the value is retrieved from the SalesEmployeeCode property (SalesPersons object). This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property Segment() As Long` [R] Returns the segment number of a child document related to a parent document (parent document number is the value of DocNum property). Field name: Segment.
  - remarks: Relevant to split purchase orders only.
- `Public Property SendNotification() As BoYesNoEnum` [R/W] property SendNotification
- `Public Property SequenceCode() As Long` [R/W] Sets or returns the Sequence Code. Field name: SeqCode.
- `Public Property SequenceModel() As String` [R/W] Sets or returns the Nota Fiscal Model. Field name: Model.
  - remarks: This property is applicable for cluster B only (country-specific for Brazil only).
- `Public Property SequenceSerial() As Long` [R/W] Sets or returns the Nota Fiscal Sequence Serial . Field name: Serial.
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
- `Public Property SeriesString() As String` [R/W] Sets or returns the Series String. Field name: SeriesStr. Length: 3 characters.
- `Public Property ServiceGrossProfitPercent() As Double` [R/W] The gross profit percent for a service document. Field name: SrvGpPrcnt
- `Public Property ShipFrom() As String` [R/W] property ShipFrom
- `Public Property ShipPlace() As String` [R/W] Enter Shipment Place Name. It is mandatory if Export Process form is filled in.. Field name: ShipPlace. Length: 60 characters.
- `Public Property ShipState() As String` [R/W] Enter Shipment State Code. It is mandatory if Export Process form is filled in.. Field name: ShipState. Length: 3 characters.
- `Public Property ShipToCode() As String` [R/W] Sets or returns the Ship To address name. Field name: ShipToCode. Length: 50 characters.
  - remarks: For sales documents, the value is retrieved from the business partner record. This address name can be updated only for open sales documents except for delivery notes. For purchase documents, the value is retrieved from the company record. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property ShowSCN() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to show the BP catalog number instead of item code. Field name: ShowSCN.
  - remarks: The SCN field is used for information only. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property SignatureDigest() As String` [R] property SignatureDigest
- `Public Property SignatureInputMessage() As String` [R] property SignatureInputMessage
- `Public Property SOIWizardId() As Long` [R] property SOIWizardId
- `Public Property SpecialLines() As Document_SpecialLines` [R] Returns an instance of Document_SpecialLines object holding properties for text or subtotal lines in documents.
- `Public Property SpecifiedClosingDate() As Date` [R/W] To close a goods receipt PO or a goods return, specify a date other than the current system date and the original posting date. Field: SpecDate.
  - remarks: If you specified a date which is earlier than or the same as the original posting date of this document, you receive a message: Enter a specified date that is later than original document posting date. If you specified a date which is in a locked period, you receive a message: Period is locked for new data.
- `Public Property StartDeliveryDate() As Date` [R/W] property StartDeliveryDate
- `Public Property StartDeliveryTime() As Date` [R/W] property StartDeliveryTime
- `Public Property StartFrom() As BoPayTermDueTypes` [R/W] property StartFrom
- `Public Property Submitted() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the document was submitted. Field name: submitted.
- `Public Property SubSeriesString() As String` [R/W] Sets or returns the document's Subseries String. Field name: SubStr. Length: 3 characters.
- `Public Property SummeryType() As BoDocSummaryTypes` [R/W] Sets or returns a valid value of BoDocSummaryTypes type that specifies the summary method to be used for table rows in a document. Field name: SummryType.
  - remarks: This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property Supplier() As String` [R/W] property Supplier
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TaxExemptionLetterNum() As String` [R/W] Sets or returns the tax exemption letter number. Field name: LetterNum. Length: 20 characters.
  - remarks: Relevant to invoice documents only.
- `Public Property TaxExtension() As TaxExtension` [R] Sets or returns the Tracking Number. Field name: TrackNo. Length: 30 characters.
- `Public Property TaxInvoiceDate() As Date` [R/W] property TaxInvoiceDate
- `Public Property TaxInvoiceNo() As String` [R/W] property TaxInvoiceNo
- `Public Property TotalDiscount() As Double` [R] Returns the Total Discount for current document. Field name: DiscSum.
- `Public Property TotalDiscountFC() As Double` [R] property TotalDiscountFC
- `Public Property TotalDiscountSC() As Double` [R] property TotalDiscountSC
- `Public Property TotalEqualizationTax() As Double` [R] Returns the total equalization tax amount, in local currency, calculated for the document. Field name: EquVatSum.
  - remarks: Relevant only for Output tax groups. Country-specific property for Spain, Italy, Portugal, and France.
- `Public Property TotalEqualizationTaxFC() As Double` [R] Returns the total equalization tax amount, in foreign currency, calculated for the document. Field name: EquVatSumF.
- `Public Property TotalEqualizationTaxSC() As Double` [R] Returns the total equalization tax amount, in system currency, calculated for the document. Field name: EquVatSumS.
- `Public Property TrackingNumber() As String` [R/W] property TrackingNumber
  - remarks: Sets or returns the tracking number. Field name: TrackNo.
- `Public Property TransNum() As Long` [R] Returns the transaction number that SAP Business One creates for the document. Field name: TransId. This is a foreign key to the JournalEntries object.
- `Public Property TransportationCode() As Long` [R/W] Sets or returns the shipping type. Field name: TrnspCode. This is a foreign key to the ShippingTypes object. Sets or returns the code of the shipping type (such as, Courier or Air Cargo). Field name: ShipType. This is a foreign key to the ShippingTypes object.
  - remarks: The shipping type defines how the goods will be transported to the customer, and how the expenses will be calculated. This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property UpdateDate() As Date` [R] Returns the date when the document was last updated. Field name: UpdateDate.
  - remarks: Internal property in SAP Business One.
- `Public Property UpdateTime() As Date` [R] property UpdateTime
- `Public Property UseBillToAddrToDetermineTax() As BoYesNoEnum` [R/W] property UseBillToAddrToDetermineTax
- `Public Property UseCorrectionVATGroup() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to use the correction vat group. Field name: UseCorrVat.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSign() As Long` [R] Returns the ID of the user who enters the object's details. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property UseShpdGoodsAct() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the document uses Shipped Goods account. Field name: UseShpdGd.
- `Public Property VatDate() As Date` [R/W] Sets or returns the date from which the tax rate for this VAT Group code applies. Field name: vatdate.
  - remarks: If the DocDate value (posting date) is later than the VatDate value,SAP Business One applies the latest tax rate, else it applies the tax rate defined for the period before the VatDate value. Relevant to sales and purchase documents only.
- `Public Property VatPercent() As Double` [R/W] The tax rate for the document. Field name: VatPercent
- `Public Property VATRegNum() As String` [R] property VATRegNum
- `Public Property VatSum() As Double` [R] Returns the total tax amount, in local currency, calculated for the document. Field name: VatSum.
  - remarks: Relevant to sales and purchase documents only.
- `Public Property VatSumFc() As Double` [R] Returns the total tax amount, in foreign currency, calculated for the document. Field name: VatSumFC.
  - remarks: Relevant to sales and purchase documents only.
- `Public Property VatSumSys() As Double` [R] Returns the total tax amount, in system currency, calculated for the document. Field name: VatSumSy.
  - remarks: Relevant to sales and purchase documents only.
- `Public Property VehiclePlate() As String` [R/W] property VehiclePlate
- `Public Property WareHouseUpdateType() As BoDocWhsUpdateTypes` [R/W] Not Used. Field name: InvntSttus.
- `Public Property WithholdingTaxData() As WithholdingTaxData` [R] Returns the WithholdingTaxData object.
- `Public Property WithholdingTaxDataWTX() As WithholdingTaxDataWTX` [R] property WithholdingTaxDataWTX
- `Public Property WTAmount() As Double` [R] Returns the total withholding tax amount in the document, in local currency. Field name: WTSum.
  - remarks: Relevant to sales and purchase documents only. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, and Portugal.
- `Public Property WTAmountFC() As Double` [R] Returns the total withholding tax amount in the document, in local currency. Field name: WTSumSC.
- `Public Property WTAmountSC() As Double` [R] Returns the total withholding tax amount in the document, in system currency. Field name: WTSumSC.
- `Public Property WTApplied() As Double` [R] Returns the total withholding tax applied, in local currency. Field name: WTApplied.
- `Public Property WTAppliedFC() As Double` [R] Returns the total withholding tax applied, in foreign currency. Field name: WTAppliedF. Returns the total withholding tax amount in the document, in local currency. Field name: WTSumSC.
- `Public Property WTAppliedSC() As Double` [R] Returns the total withholding tax applied, in system currency. Field name: WTAppliedS.
- `Public Property WTExemptedAmount() As Double` [R] Returns the exempted amount, in local currency, from the document. Field name: ExepAmnt.
  - remarks: Relevant to sales and purchase documents only. Country-specific property for Italy.
- `Public Property WTExemptedAmountFC() As Double` [R] Returns the exempted amount, in foreign currency, from the document. Field name: ExepAmntFC.
  - remarks: Relevant to sales and purchase documents only. Country-specific property for Italy.
- `Public Property WTExemptedAmountSC() As Double` [R] Returns the exempted amount, in system currency, from the document. Field name: ExepAmntSC.
  - remarks: Relevant to sales and purchase documents only. Country-specific property for Italy.
- `Public Property WTNonSubjectAmount() As Double` [R] Returns the amount, in local currency, that is not subject to withholding tax in the document. Field name: NnSbAmnt.
  - remarks: The amount of the document that is not included in the withholding tax calculation. For example, if the Base Amount (BaseAmount) is $100 and Base Amount, defined in the Define Withholding Tax Codes table, is 60, then the Non-Subject Amount is $40. Relevant for sales and purchase documents only. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, and Portugal.
- `Public Property WTNonSubjectAmountFC() As Double` [R] Returns the amount, in foreign currency, that is not subject to withholding tax in the document. Field name: NbSbAmntFC.
  - remarks: The amount of the document that is not included in the withholding tax calculation. Relevant for sales and purchase documents only. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, and Portugal.
- `Public Property WTNonSubjectAmountSC() As Double` [R] Returns the amount, in system currency, that is not subject to withholding tax in the document. Field name: NnSbAmntSC.
  - remarks: The amount of the document that is not included in the withholding tax calculation. Relevant for sales and purchase documents only. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, and Portugal.

## Methods (17)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
  - example note: The following sample shows how to add an invoice (with lines) document to the database. Use this sample as a basis for all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub AddInvoice_Click()

        Dim RetVal As Long

        Dim ErrCode As Long

        Dim ErrMsg As String

        'Create the Documents object

        Dim vInvoice    As SAPbobsCOM.Documents

        Set vInvoice = vCmp.GetBusinessObject(oInvoices)

        'Set values to the fields

        vInvoice.Series = 0

        vInvoice.CardCode = "BP234"

        vInvoice.HandWritten = tNO

        vInvoice.PaymentGroupCode = "-1"

        vInvoice.DocDate = "21/8/2003"

        vInvoice.DocTotal = 264.6

        'Invoice Lines - Set values to the first line

        vInvoice.Lines.ItemCode = "A00023"

        vInvoice.Lines.ItemDescription = "Banana"

        vInvoice.Lines.PriceAfterVAT = 2.36

        vInvoice.Lines.Quantity = 50

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Invoice Lines - Set values to the second line

        vInvoice.Lines.Add

        vInvoice.Lines.ItemCode = " A00033"

        vInvoice.Lines.ItemDescription = "Orange"

        vInvoice.Lines.PriceAfterVAT = 118

        vInvoice.Lines.Quantity = 1

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Add the Invoice

        RetVal = vInvoice.Add

       'Check the result

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox ErrCode & " " & ErrMsg

        End If

     End Sub
    ```
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function Close() As Long` Closes a record of the object in SAP Business One database.
  - example note: The following sample shows how to close a document record. Use this sample as a basis to all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Sub CloseDocument()

        Dim RetVal    As Long

        Dim ErrCode   As Long

        Dim ErrMsg    As String

        Dim vOrder As SAPbobsCOM.Documents

        Set vOrder = vCmp.GetBusinessObject(oOrders)

        'Retrieve the document record to close from the database

        RetVal = vOrder.GetByKey("55")

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

                Exit Sub

        End If

        'Close the record

        RetVal = vOrder.Close

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox "Failed to Close the record " & ErrCode & " " & ErrMsg

        End If

    End Sub
    ```
- `Public Function CreateCancellationDocument() As Documents` Creates a cancellation document when a marketing document is added in error, has become invalid, or has no concrete transactions associated with it.
  - C# example (from SAP's help):
    ```csharp
    //Create a new Documents object
    Documents doc = comp.GetBusinessObject(BoObjectTypes.oDeliveryNotes);

    //Get a the document by key which will be cancelled
    doc.GetByKey(19);

    //Create an object which represent to a new cancellation document based on doc
    Documents cancelDoc = doc.CreateCancellationDocument();

    //We can modify some values in the cancellation document
    cancelDoc.DocDate = new DateTime(2012, 4, 8);

    //Then we can add this cancellation document, and at the same time the status of the base document will be changed into ‘canceled’
    cancelDoc.Add();
    ```
- `Public Function ExportEWayBill() As Long` method ExportEWayBill
- `Public Function GetApprovalTemplates() As Long` Gets the related approval template.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal AbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database. If serial numbers and batch numbers are set to the specified Document object lines, the returned object will contain references to these child objects.
  - param `AbsEntry`: For all types of documents, use the document entry key (DocEntry property). Note: For Receipt for Production and Issue from Production documents (based on production orders) prior to release 2007, use the document number (DocNum property). Starting from release 2007 use the document entry key (DocEntry property).
  - returns: If the specified object is found, the method returns True and the properties of the object will be filled with object's data. If the specified object is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function HandleApprovalRequest() As Long` method HandleApprovalRequest
- `Public Function Remove() As Long` Not supported. SAP Business One does not allow to remove a document object from the database. Note: The remove feature is supported for Purchase Quotation.
- `Public Function Reopen() As Long` Reopens a closed document. The method is only relevant for China, Japan, Korea, India, Brazil and Singapore.
  - remarks: You can only reopen a document if all of the following conditions are met: - The document is an A/R, A/P, or reserve invoice. - The document status is closed. - The document total is 0. - There are no target documents related to the invoice. - There is no reconciliation related to the invoice. - There is no related freight in the header or lines. - For item invoices, there is a quantity greater than 0 for each line. For all countries except Brazil, the following conditions for lines must also be met: - For item invoices, the unit price and line total is 0 for all lines. - For service invoices, the line total is 0 for all lines. For Brazil, all lines must meet the above conditions or must meet all of the following conditions: - The Tax Only checkbox is selected for all rows. - The VAT Code is set to Included in Price for all rows.
- `Public Function RequestApproveCancellation() As Long` method RequestApproveCancellation
- `Public Function SaveDraftToDocument() As Long` Converts an approved draft document to a valid document.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
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
- `Public Function UpdateFromXML(ByVal FileName As String) As Long` Receives and processes the XML content. You can remove sub-object lines from the Document object via the XML file.
  - param `FileName`: Specifies the path and file name of the XML data.
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    'Set import export model first
    vComp.XmlExportType = BoXmlExportTypes.xet_ExportImportMode

    'Delete line from the Documents object
    Dim vvdoc As Documents = vComp.GetBusinessObject(BoObjectTypes.oOrders)

    'Get object
    vvdoc.GetByKey(1)
    vvdoc.SaveToFile("C:\testdoc.xml")

    'Delete sub line directly from C:\testdoc.xml

    'Update object
    vvdoc.UpdateFromXML("C:\testdoc.xml")
    ```
