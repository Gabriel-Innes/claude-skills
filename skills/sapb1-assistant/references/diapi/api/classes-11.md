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

# DocumentsAdditionalExpenses (Object)

DocumentsAdditionalExpenses is a child object of Documents object and represents the documents of additional expenses in the Marketing Documents module. The source table for each document is according to the document type as follows: INV3, RIN3, DLN3, RDN3, RDR3, QUT3, PCH3, RPC3, PDN3, RPD3, POR3, and DRF3.

**Remarks:** Mandatory fields in SAP Business One: ExpenseCode and of Name of AdditionalExpenses object. For each type of additional expense you can add one row that summarizes all expenses of that type. To display the form in the application, first define expenses in documents as follows: - Select Administration --> System Initialization --> Document Settings. - In the General tab, select Manage Expenses In Documents. - Click Define Expenses. Then, - For INV3 table, select Sales - A/R --> A/R Invoice. Click Add. Expenses. - For RIN3 table, select Sales - A/R --> A/R Credit Memo. Click Add. Expenses. - For DLN3 table, select Sales - A/R --> Delivery. Click Add. Expenses. - For RDN3 table, select Sales - A/R --> Returns. Click Add. Expenses. - For RDR3 table, select Sales - A/R --> Order. Click Add. Expenses. - For QUT3 table, select Sales - A/R --> Quotation. Click Add. Expenses. - For PCH3 table, select Purchasing - A/P --> A/P Invoice. Click Add. Expenses. - For RPC3 table, select Purchasing - A/P --> A/P Credit Memo. Click Add. Expenses. - For PDN3 table, select Purchasing - A/P --> Goods Receipt PO. Click Add. Expenses. - For RPD3 table, select Purchasing - A/P --> Goods Returns. Click Add. Expenses. - For POR3 table, select Purchasing - A/P --> A/R Invoice. Click Add. Expenses. - For DRF3 table, select Sales - A/R (or Purchasing - A/P) --> Document Draft. Set your selection criteria, and click OK. Click Add. Expenses.

## Properties (60)
- `Public Property AquisitionTax() As BoYesNoEnum` [R] Specifies whether or not the additional expense is subject to acquisition tax. Relevant to input tax groups (A/P) only. Field name: IsAcquistn.
  - remarks: The acquisition tax is a procedure used when you record goods purchased from EU countries. In this case, tax is not calculated in the document but an appropriate amount is recorded in the journal entry and affects the tax report.
- `Public Property BaseDocEntry() As Long` [R/W] Sets or returns the source document ID. Field name: DocEntry.
  - remarks: Use the BaseDocEntry, BaseDocType, and BaseDocLine properties to extract data from one document to another. For example, to extract data from a Quotation to an Order.
- `Public Property BaseDocLine() As Long` [R/W] Sets or returns the line number of the source document. Field name: BaseLnNum.
  - remarks: Use the BaseDocLine, BaseDocEntry, and BaseDocType properties to extract data from one document to another. For example, to extract data from a Quotation to an Order.
- `Public Property BaseDocType() As Long` [R/W] Sets or returns the source document type. Field name: BaseType.
  - remarks: Use the BaseDocType, BaseDocEntry, and BaseDocLine properties to extract data from one document to another. For example, to extract data from a Quotation to an Order. To view the document type numbers, see BoAPARDocumentTypes.
- `Public Property BaseDocumentReference() As Long` [R] Returns this line number. Field name: LineNum.
- `Public Property Count() As Long` [R] Returns total rows in the additional expenses table.
- `Public Property CUSplit() As BoYesNoEnum` [R/W] If this flag is set to true, the amounts that are not subject to withholding tax and are not supplier income amounts are distinguished and split in a standalone report page.
  - remarks: Italy only, for the withholding tax single certification (Certificazione Unica).
- `Public Property DeductibleTaxSum() As Double` [R/W] Internal use only. Field name: DedVatSum.
- `Public Property DeductibleTaxSumFC() As Double` [R] Internal use only. Field name: DedVatSumF.
- `Public Property DeductibleTaxSumSys() As Double` [R] Internal use only. Field name: DedVatSumS.
- `Public Property DistributionMethod() As BoAdEpnsDistribMethods` [R/W] Sets or returns a valid value of BoAdEpnsDistribMethods type that specifies the distribution method of the additional expenses in documents. Field name: DistrbMthd.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property EBooksDetails() As EBooks_Doc_Details` [R] property EBooksDetails
- `Public Property EqualizationTaxFC() As Double` [R] Returns the equalization tax amount, in foreign currency, calculated for the additional expense. Field name: EquVatSumF.
- `Public Property EqualizationTaxPercent() As Double` [R] Returns the equalization tax percentage for the additional expense. Field name: EquVatPer.
- `Public Property EqualizationTaxSum() As Double` [R] Returns the equalization tax amount, in local currency, calculated for the additional expense. Field name: EquVatSum.
- `Public Property EqualizationTaxSys() As Double` [R] Returns the equalization tax amount, in system currency, calculated for the additional expense. Field name: EquVatSumS.
- `Public Property ExpenseCode() As Long` [R/W] Sets or returns the code of the additional expense as defined by SAP Business One. Field name: ExpnsCode. This is a foreign key to the AdditionalExpenses object.
  - remarks: Mandatory field in SAP Business One.
- `Public Property ExternalCalcTaxAmount() As Double` [R/W] property ExternalCalcTaxAmount
- `Public Property ExternalCalcTaxAmountFC() As Double` [R] property ExternalCalcTaxAmountFC
- `Public Property ExternalCalcTaxAmountSC() As Double` [R] property ExternalCalcTaxAmountSC
- `Public Property ExternalCalcTaxRate() As Double` [R/W] property ExternalCalcTaxRate
- `Public Property LastPurchasePrice() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not this is the Last Purchase Price. Field name: LstPchPrce.
- `Public Property LineGross() As Double` [R/W] property LineGross
- `Public Property LineGrossFC() As Double` [R] property LineGrossFC
- `Public Property LineGrossSys() As Double` [R] property LineGrossSys
- `Public Property LineNum() As Long` [R] Returns this document line number. Field name: LineNum.
- `Public Property LineTotal() As Double` [R/W] Sets or returns the total amount (in local currency) of the additional expense. Field name: LineTotal.
- `Public Property LineTotalFC() As Double` [R] Returns the total amount (in foreign currency) of the additional expense. Field name: TotalFrgn.
- `Public Property LineTotalSys() As Double` [R] Returns the total amount (in system currency) of the additional expense. Field name: TotalSumSy.
- `Public Property PaidToDate() As Double` [R] Returns the paid amount (in local currency) of the additional expense. Field name: PaidToDate. Not supported in DI API version 6.5.
- `Public Property PaidToDateFC() As Double` [R] Returns the paid amount (in foreign currency) of the additional expense. Field name: PaidFC. Not supported in DI API version 6.5.
- `Public Property PaidToDateSys() As Double` [R] Returns the paid amount (in system currency) of the additional expense. Field name: PaidSys. Not supported in DI API version 6.5.
- `Public Property Project() As String` [R/W] The project that relates to the freight. Field: Project. Length: 20 characters.
- `Public Property Remarks() As String` [R/W] Sets or returns comments regarding the additional expense. Field name: Comments. Length: 100 characters.
- `Public Property Status() As BoStatus` [R] Returns a valid value that determines this document Status, (open or Close). Field name: Status.
- `Public Property Stock() As BoYesNoEnum` [R/W] Sets or returns a valid value that Determines whether or not a Stock exists. Field name: Stock.
- `Public Property TargetAbsEntry() As Long` [R] Returns the Target Absolute Entry of this document. Field name: TrgAbsEnt.
- `Public Property TargetType() As Long` [R] Returns the Target Type for this document. Field name: TrgType.
- `Public Property TaxCode() As String` [R/W] Sets or returns the sales tax code for the item specified in the row. Field name: TaxCode. Length: 8 characters. This is a foreign key to the SalesTaxCodes object. Sets or returns the sales tax code for the item specified in the row. Field name: TaxCode. Length: 8 characters. This is a foreign key to the SalesTaxCodes object.
  - remarks: Country-specific property for USA. The tax code represents the sales tax related to specific locations where the business transaction occurs. Tax codes are defined in SAP Business One. Country-specific property for USA. The tax code represents the sales tax related to specific locations where the business transaction occurs. Tax codes are defined in SAP Business One.
- `Public Property TaxJurisdictions() As TaxJurisdictions` [R] Returns the TaxJurisdictions object.
- `Public Property TaxLiable() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the additional expense is VAT liable. Field name: TaxStatus.
- `Public Property TaxPaid() As Double` [R] Not used. Field name: LineVat.
- `Public Property TaxPaidFC() As Double` [R] Not used. Field name: LineVatF.
- `Public Property TaxPaidSys() As Double` [R] Not used. Field name: LineVatS.
- `Public Property TaxPercent() As Double` [R] Returns the tax percentage for the additional expense. Field name: VatPrcnt.
- `Public Property TaxSum() As Double` [R/W] The tax amount, in local currency, calculated for the additional expense. You can manually adjust the tax amount according to the business need. Field name: VatSum.
- `Public Property TaxSumFC() As Double` [R] Returns the tax amount, in foreign currency, calculated for the additional expense. Field name: VatSumFrgn.
- `Public Property TaxSumSys() As Double` [R] Returns the total tax amount, in system currency, calculated for the additional expense. Field name: VatSumSy.
- `Public Property TaxTotalSum() As Double` [R] Returns the total tax amount (TaxSum + EqualizationTaxSum) in local currency. Field name: EquVatSum.
- `Public Property TaxTotalSumFC() As Double` [R] Returns the total tax amount (TaxSumFC + EqualizationTaxFC) in foreign currency. Field name: EquVatSumF.
- `Public Property TaxTotalSumSys() As Double` [R] Returns the total tax amount ( TaxSumSys + EqualizationTaxSys) in system currency. Field name: EquVatSumS.
- `Public Property TaxType() As BoAdEpnsTaxTypes` [R] Returns a valid value of BoAdEpnsTaxTypes type that specifies tax type for the additional expense. Field name: TaxType.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatGroup() As String` [R/W] Sets or returns the VAT group for the additional expense. Field name: VatGroup. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: Country-specific property for EU.
- `Public Property WTLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not this document is subject to Withholding Tax. Field name: TaxStatus.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number. Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# DocumentSeriesParams (Object)

The DocumentSeriesParams specifies the identification key combination (Document and Series) for which the Documents is related. Source table: NNM1. DocumentSeries

**Remarks:** To display the form in the application: - Select a document type (for example: Sales A/R -- Sales Quotation). - Select Tools -- Print Layout Designer. - Choose a template name for the specified document type. - Click Set as default.

## Properties (3)
- `Public Property Document() As String` [R/W] Sets or returns the key of the document type for which the series relates. Field name: Document. Length: 20 characters.
- `Public Property DocumentSubType() As String` [R/W] Sets or returns the Document Sub-Type. Field name: DocSubType. Length: 2 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the Series a part of a document name. Field name: Series.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# DocumentSeriesUserParams (Object)

The DocumentSeriesUserParams specifies the identification key combination (Document, Series and Users) for which Documents is related. Source table: NNM2.

## Properties (4)
- `Public Property Document() As String` [R/W] Sets or returns the Document code. Field name: ObjectCode. For example: The Document property shall return 13 for A/R Invoice. Length: 20 Characters.
- `Public Property DocumentSubType() As String` [R/W] Sets or returns the Document Sub-Type. Field name: DocSubType. Length: 2 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the Series Object, part of the document name. Field name: Series.
- `Public Property User() As Long` [R/W] Sets or returns the User Id, This is a foreign key to the Users object. Field name: UserSign).

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# DocumentTypeParams (Object)

The DocumentTypeParams specifies the identification key combination (Document and DocumentSubType) for which the Documents object is related. Source table: NNM2.

## Properties (2)
- `Public Property Document() As String` [R/W] Sets or returns the Document code. Field name: ObjectCode. For example: The Document property shall return 13 for A/R Invoice. Length: 20 Characters.
- `Public Property DocumentSubType() As String` [R/W] Sets or returns the document sub-type. Field name: DocSubType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# DownPaymentsToDraw (Object)

Represents down payments drawn into A/R or A/P invoices. The Documents.DownPaymentAmount property is updated with the total amount to draw. Source tables: INV9, PCH9, RIN9, RPC9, DRF9

## Properties (21)
- `Public Property AmountToDraw() As Double` [R/W] The net amount (without tax) drawn to the invoice. Field name: DrawnSum
  - remarks: The amount to draw cannot exceed the open amount.
- `Public Property AmountToDrawFC() As Double` [R/W] The net amount (without tax) drawn to the invoice in foreign currency. Field name: DrawnSumFc
  - remarks: The amount to be drawn cannot be more than the open amount.
- `Public Property AmountToDrawSC() As Double` [R/W] The net amount (without tax) drawn to the invoice in system currency. Field name: DrawnSumSc
  - remarks: The amount to be drawn cannot be more than the open amount.
- `Public Property Count() As Long` [R] The number of downpayment lines in the collection.
- `Public Property Details() As String` [R] Set to the Remarks field in the down payment invoice. Field name: BsComments
- `Public Property DocEntry() As Long` [R/W] An internal key to the down payment document. Field name: BaseAbs
- `Public Property DocInternalID() As Long` [R] A key to the invoice for which the down payment is used. Field name: DocEntry
- `Public Property DocNumber() As Long` [R] The document number of the down payment document. Field name: BaseDocNum
- `Public Property DownPaymentsToDrawDetails() As DownPaymentsToDrawDetails` [R] The details for this drawn downpayment. A drawn downpayment can be applied to various tax groups and in different ways.
- `Public Property DownPaymentType() As DownPaymentTypeEnum` [R] Indicates whether the down payment document is an invoice or a request. Field name: Posted
- `Public Property DueDate() As Date` [R] Returns the due date of the down payment invoice. Field name: BsDueDate
- `Public Property GrossAmountToDraw() As Double` [R/W] The gross amount (with tax) drawn to the invoice. Field name: Gross
- `Public Property GrossAmountToDrawFC() As Double` [R/W] The gross amount (with tax) drawn to the invoice in foreign currency. Field name: GrossFc
- `Public Property GrossAmountToDrawSC() As Double` [R/W] The gross amount (with tax) drawn to the invoice in system currency. Field name: GrossSc
- `Public Property IsGrossLine() As BoYesNoEnum` [R] Indicates whether the gross amount was entered and all other fields were calculated based on the gross amount. Field name: IsGross
- `Public Property Name() As String` [R] The full name of the business partner. Field name: BsCardName
- `Public Property PostingDate() As Date` [R] The posting date of the down payment invoice. Field name: BsDocDate
- `Public Property RowNum() As Long` [R] The row number of the current drawn payment in the collection. Field name: LineNum
- `Public Property Tax() As Double` [R] The part of the drawn downpayment to be used for tax. Field name: Vat
- `Public Property TaxFC() As Double` [R] The part of the drawn downpayment to be used for tax in foreign currency. Field name: VatFc
- `Public Property TaxSC() As Double` [R] The part of the drawn downpayment to be used for tax in system currency. Field name: VatSc

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# DownPaymentsToDrawDetails (Object)

Represents detail lines for the DownPaymentsToDraw object. Source tables: INV11, PCH11, RIN11, RPC11, DRF11

**Example:**
- C# example (from SAP's help):
  ```csharp
  // Update PeriodCategory with SalesDownPaymentInterimAccount and PurchaseDownPaymentInterimAccount
  PeriodCategoryParamsCollection oPeriodCategoryColl;
  PeriodCategory oPerCategory;

  // Get Period Category Collection
  oPeriodCategoryColl = MainModule.oCmpSrv.GetPeriods();

  // Get the current period category, e.g. the first category
  oPerCategory = MainModule.oCmpSrv.GetPeriod(oPeriodCategoryColl.Item(0));

  // SalesDownPaymentInterimAccount is a new property, mandatory for DownPayment process
  oPerCategory.SalesDownPaymentInterimAccount = "2000";

  // PurchaseDownPaymentInterimAccount is a new property, mandatory for DownPayment process
  oPerCategory.PurchaseDownPaymentInterimAccount = "2000";
  MainModule.oCmpSrv.UpdatePeriod(oPerCategory);

  // Add a BP
  SAPbobsCOM.BusinessPartners oBP;
  oBP = (SAPbobsCOM.BusinessPartners)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oBusinessPartners);
  oBP.CardCode = "efrat";

  // DownPaymentClearAct is an existing property, mandatory for DownPayment process
  oBP.DownPaymentClearAct = "1000";
  //DownPaymentInterimAccount is a new property, mandatory for DownPayment process
  oBP.DownPaymentInterimAccount = "1000";
  oBP.Add();

  // Add two items
  SAPbobsCOM.Items oItem1, oItem2;
  oItem1 = (SAPbobsCOM.Items)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oItems);
  oItem1.ItemCode = "item1";
  oItem1.InventoryItem = BoYesNoEnum.tNO;
  oItem1.Add();
  oItem2 = (SAPbobsCOM.Items)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oItems);
  oItem2.ItemCode = "item2";
  oItem2.InventoryItem = BoYesNoEnum.tNO;
  oItem2.Add();

  // Add a DownPayment invoice
  SAPbobsCOM.Documents oDP;
  oDP = (SAPbobsCOM.Documents)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oDownPayments);
  // Set Down Payment Header Values
  oDP.CardCode = "efrat";
  oDP.DownPaymentType = DownPaymentTypeEnum.dptInvoice;

  // Set Down Payment Line Values
  // For VatGroup A1, the DownPayment has a line with 1 item1 of unit price $10.
  oDP.Lines.ItemCode = "item1";
  oDP.Lines.Quantity = 1;
  oDP.Lines.UnitPrice = 10;
  oDP.Lines.VatGroup = "A1";
  oDP.Lines.Add();

  //For VatGroup A2, the DownPayment has a line with 1 item2 of unit price $10.
  oDP.Lines.ItemCode = "item2";
  oDP.Lines.Quantity = 1;
  oDP.Lines.UnitPrice = 10;
  oDP.Lines.VatGroup = "A2";
  oDP.Add();

  string sNewObjCode = "";
  // Retrieve the key of the last added record, here the DocNum of DownPayment invoice created in the step
  MainModule.oCompany.GetNewObjectCode(out sNewObjCode);
  int tmpKey = Convert.ToInt32(sNewObjCode);

  // Pay the DownPayment invoice
  SAPbobsCOM.Payments oPay;
  oPay = (SAPbobsCOM.Payments)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oIncomingPayments);
  oPay.CardCode = "efrat";
  // Set the Downpayment we created to be paid
  oPay.Invoices.DocEntry = tmpKey;
  oPay.Invoices.InvoiceType = BoRcptInvTypes.it_DownPayment;
  oPay.CashAccount = "1000";
  oPay.CashSum = 30;
  oPay.Add();

  // Add invoice with down payment
  SAPbobsCOM.Documents oINV;
  oINV = (SAPbobsCOM.Documents)MainModule.oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oInvoices);
  oINV.CardCode = "efrat";
  oINV.DocType = SAPbobsCOM.BoDocumentTypes.dDocument_Items;

  // For VatGroup A1, the invoice has 1 item1 with unit price $10.
  oINV.Lines.ItemCode = "item1";
  oINV.Lines.Quantity = 1;
  oINV.Lines.UnitPrice = 10;
  oINV.Lines.VatGroup = "A1";
  oINV.Lines.Add();
  // For VatGroup A2, the invoice has 1 item2 with unit price $20.
  oINV.Lines.ItemCode = "item2";
  oINV.Lines.Quantity = 1;
  // ... (truncated)
  ```

## Properties (19)
- `Public Property AmountToDraw() As Double` [R/W] The net amount (without tax) drawn to the invoice for this line. Field name: LineTotal
- `Public Property AmountToDrawFC() As Double` [R/W] The net amount (without tax) drawn to the invoice for this line in foreign currency. Field name: TotalFrgn
- `Public Property AmountToDrawSC() As Double` [R/W] The net amount (without tax) drawn to the invoice for this line in system currency. Field name: TotalSumSy
- `Public Property Count() As Long` [R] The number of downpayment detail lines in the collection.
- `Public Property DocEntry() As Long` [R] An internal key to the down payment document. Field name: BaseAbs This is a foreign key to the Documents (down payments) object.
- `Public Property DocInternalID() As Long` [R] A key to the invoice for which the down payment is used. Field name: DocEntry This is a foreign key to the Documents (invoices) object.
- `Public Property GrossAmountToDraw() As Double` [R/W] The gross amount (with tax) drawn to the invoice for this line. Field name: Gross
- `Public Property GrossAmountToDrawFC() As Double` [R/W] The gross amount (with tax) drawn to the invoice for this line in foreign currency. Field name: GrossFc
- `Public Property GrossAmountToDrawSC() As Double` [R/W] The gross amount (with tax) drawn to the invoice for this line in system currency. Field name: GrossSc
- `Public Property IsGrossLine() As BoYesNoEnum` [R] Indicates whether the gross amount was entered and all other fields were calculated based on the gross amount. Field name: IsGross
- `Public Property LineType() As LineTypeEnum` [R/W] The type of detail line. Field name: LineType
- `Public Property RowNum() As Long` [R/W] The row number of the parent DownPaymentsToDraw object within its collection. Field name: LineNum
- `Public Property SeqNum() As Long` [R] The sequence number of the current drawn payment detail in the collection. Field name: LineSeq
- `Public Property Tax() As Double` [R/W] The part of the drawn downpayment in this line to be used for tax. Field name: VatSum
- `Public Property TaxAdjust() As BoYesNoEnum` [R] TaxAdjust
- `Public Property TaxFC() As Double` [R/W] The part of the drawn downpayment in this line to be used for tax in foreign currency. Field name: VatSumFrgn
- `Public Property TaxSC() As Double` [R/W] The part of the drawn downpayment in this line to be used for tax in system currency. Field name: VatSumSys
- `Public Property VatGroupCode() As String` [R/W] The tax code to which this downpayment line applied. Field name: VatGroup This is a foreign key to the VatGroups object.
- `Public Property VatPercent() As Double` [R] The tax rate for the tax code in the VatGroupCode property. Field name: VatPrcnt

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# DppChangeParams (Object)

DppChangeParams Class

## Properties (3)
- `Public Property FromDate() As Date` [R/W] property FromDate
- `Public Property FromTime() As Date` [R/W] property FromTime
- `Public Property HasChanged() As BoYesNoEnum` [R] property HasChanged

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# DunningLetters (Object)

Represents a list of dunning levels that is used as a template when creating a new dunning term. You can define up to 10 dunning levels, and relate each level to a dunning letter format. This object enables you to: - Add a dunning level. - Retrieve a dunning level by its key. - Update a dunning level. - Remove a dunning level. - Save the object in XML format. This object manages a list of dunning levels. This list is a template when creating a new dunning term, and the template list does not directly affect business partners or the dunning letters functionality. Dunning terms can be assigned to business partners and are managed by the DunningTermsService. Source table: ODUN.

**Remarks:** Mandatory fields: RowNumber, LetterFormat and Effectiveafter. To display the form in the application: - Select Administration --> Setup --> Business Partners --> Dunning Levels.

## Properties (10)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CalcInterest() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to calculate interest on a delinquent debt. Field name: CalcIntert.
- `Public Property Effectiveafter() As String` [R/W] Sets or returns the overdue number of days. Field name: EffctAftr. Mandatory in SAP Business One. Length: 3 characters.
  - remarks: The value of each level relates to the preceding level. For example, If you set this property to 30 days for level 1 and 40 days for level 2, then SAP Business One will send the first dunning letter 30 days after the payment due date, and then will send the second dunning letter 40 days after the first dunning letter date.
- `Public Property FeeCurrency() As String` [R/W] Sets or returns the currency of the dunning letter fee. Field name: FeeCurr. Length: 3 characters.
- `Public Property Feeperletter() As Double` [R/W] Sets or returns the fee for each dunning letter sent to the business partner. Field name: LetterFee.
- `Public Property LetterFormat() As String` [R/W] Sets or returns the letter format to relate to the dunning level. Field name: LetrFormat. Mandatory in SAP Business One. Length: 8 characters.
- `Public Property MinimumBalance() As Double` [R/W] Sets or returns the minimum balance of the debt. SAP Business One will send a dunning letter only for a debt balance higher than this minimum amount. Field name: MinBalance.
- `Public Property MinimumBalanceCurrency() As String` [R/W] Sets or returns the currency of MinimumBalance. Field name: MinBlnCurr. Length: 3 characters.
- `Public Property RowNumber() As Long` [R/W] Sets or returns the dunning level number, which is used as an identification key. Field name: LineNum. Mandatory in SAP Business One.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Dunning level number (RowNumber).
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

# DunningTerm (Object)

Represents a dunning term, which defines a set of dunning levels that determine when to send dunning letters for past-due balances. A dunning term can be assigned to a business partner. Source table: ODUT Mandatory properties: Code, Name; DunningTermLines must not be empty

## Properties (19)
- `Public Property ApplyHighestLetterTemplate() As BoYesNoEnum` [R/W] Indicates whether to use the template for the highest dunning level of all the documents included in the letter. The default is no. Field name: HiLtrFrmt
  - remarks: Relevant only if the GroupingMethod property is set to per business partner (gmPerBP) or set per dunning level (gmPerDunningLevel).
- `Public Property AutomaticPosting() As AutomaticPostingEnum` [R/W] property AutomaticPosting
- `Public Property BaseDateSelect() As BaseDateSelectEnum` [R/W] property BaseDateSelect
- `Public Property CalculateInterestMethod() As CalculateInterestMethodEnum` [R/W] Indicates whether to calculate the interest on the remaining amount or on the original total. Field name: RemIntrst
  - remarks: Relevant only if the IncludeInterest property is set to true.
- `Public Property Code() As String` [R/W] The key for a specific dunning term. Field name: TermCode
- `Public Property DaysInMonth() As Long` [R/W] The number of days in a month for calculating interest. The default is 30. Field name: MonthDays
- `Public Property DaysInYear() As Long` [R/W] The number of days in a year for calculating interest. The default is 360. Field name: YearDays
- `Public Property DunningTermLines() As DunningTermLines` [R] Defines the dunning levels for the current dunning term.
- `Public Property ExchangeRateSelect() As ExchangeRateSelectEnum` [R/W] Indicates whether to use the original exchange rate defined in the invoice, or to use the exchange rate defined for the day on which the dunning letters are created. This option is relevant when calculating interest in foreign currency. Field name: XchgOrig
- `Public Property FeeAccount() As String` [R/W] property FeeAccount
- `Public Property GroupingMethod() As GroupingMethodEnum` [R/W] Indicates whether to produce dunnings per invoice, per dunning level, or per business partner. The default is per business partner. Field name: GrpMethod
- `Public Property IncludeInterest() As BoYesNoEnum` [R/W] Indicates whether to charge interest for delinquent balances. The default is yes. Field name: CalcIntr
  - remarks: The method for calculating interest is specified in the CalculateInterestMethod property.
- `Public Property InterestAccount() As String` [R/W] property InterestAccount
- `Public Property LetterFee() As Double` [R/W] Specifies the fee to charge per dunning letter. Field name: TotalFee
  - remarks: Relevant only if the GroupingMethod property is set to per business partner (gmPerBP) and the ApplyHighestLetterTemplate property is set to false.
- `Public Property LetterFeeCurrency() As String` [R/W] The currency for the letter fee. Field name: FeeCurr
- `Public Property MinimumBalance() As Double` [R/W] Specifies the minimum balance for producing dunning letters. Field name: MinBalance
- `Public Property MinimumBalanceCurrency() As String` [R/W] The currency for the minimum balance. Field name: BalCurr
- `Public Property Name() As String` [R/W] The name for a specific dunning term. Field name: TermName
- `Public Property YearlyInterestRate() As Double` [R/W] Specifies the yearly interest rate. Field name: YearlyRate

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

# DunningTermLine (Object)

Represents a criterion for sending out a dunning letter. For example, a dunning term can define dunning letters for 30, 60, and 90-day delinquent balances. The term would, therefore, contain three lines, one for each dunning letter. Source table: DUT1 Mandatory properties: Effectiveafter, LetterFormat

## Properties (8)
- `Public Property CalculateInterest() As BoYesNoEnum` [R/W] Indicates whether to calculate interest for this dunning letter. The default is yes. Field name: CalcIntrst
- `Public Property Effectiveafter() As String` [R/W] The number of days following the due date of delinquent balances when this dunning letter is to be sent. Field name: EffctAftr
- `Public Property LetterFee() As Double` [R/W] The fee for sending this dunning letter. Field name: LetterFee
- `Public Property LetterFeeCurrency() As String` [R/W] The currency for the letter fee. Field name: FeeCurr
- `Public Property LetterFormat() As DunningLetterTypeEnum` [R/W] The letter format in the Print Layout Designer for use with this dunning letter. Field name: LetterFrmt
- `Public Property LevelNum() As Long` [R] The dunning level for this dunning letter. Field name: LevelNum
- `Public Property MininumBalance() As Double` [R/W] Specifies the minimum balance for producing this dunning letter. Field name: MinBalance
- `Public Property MininumBalanceCurrency() As String` [R/W] The currency for the minimum balance. Field name: MinBlnCurr

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

# DunningTermLines (Collection)

A collection of DunningTermLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As DunningTermLine` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DunningTermLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DunningTermParams (Object)

Holds the key and name of a dunning term. This object is used to pass keys to and retrieve keys from DunningTermsService methods.

## Properties (2)
- `Public Property Code() As String` [R/W] The key for a specific dunning term. Field name: TermCode
- `Public Property Name() As String` [R] The name for a specific dunning term. Field name: TermName

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

# DunningTermsParams (Collection)

A collection of DunningTermParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As DunningTermParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As DunningTermParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# DunningTermsService (Object)

The DunningTermsService service enables you to add, look up and remove dunning terms for defining when to send out dunning terms for delinquent balances. Each business partner can be assigned to one dunning term, which defines when to send dunning letters to that partner. Source table: ODUT

**Remarks:** SAP Business One maintains a template list of up to 10 dunning levels; in the DI API, this list is managed by the DunningLetters object. In the application, a new dunning term automatically contains this list of dunning levels, but the dunning levels in the dunning terms can be changed. In the DI API, if no lines are specified for a new dunning term in the AddDunningTerm method, then the template list of dunning levels is automatically added to the dunning term. To see the list of dunning terms, select Administration --> Setup --> Business partners --> Dunning Terms.

## Methods (8)
- `Public Function AddDunningTerm(ByVal pIDunningTerm As DunningTerm) As DunningTermParams` Adds a dunning term.
  - param `pIDunningTerm`: The data for the new dunning term.
  - returns: Contains the key (TermCode) of the new dunning term.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DunningTermsService dts = globals_Renamed.oCompany.GetCompanyService().GetBusinessService(ServiceTypes.DunningTermsService) as DunningTermsService;
    SAPbobsCOM.DunningTerm dt = dts.GetDataInterface(DunningTermsServiceDataInterfaces.dtsDunningTerm) as SAPbobsCOM.DunningTerm;

    string code = "Code" + DateTime.Now.Minute.ToString() + DateTime.Now.Second.ToString();
    dt.Code = code;
    dt.Name = "myName";
    dt.ApplyHighestLetterTemplate = BoYesNoEnum.tNO;
    dt.CalculateInterestMethod = CalculateInterestMethodEnum.cimOnRemainingAmount;
    dt.DaysInMonth = 28;
    dt.DaysInYear = 350;
    dt.GroupingMethod = GroupingMethodEnum.gmPerBP;
    dt.IncludeInterest = BoYesNoEnum.tYES;
    dt.ExchangeRateSelect = ExchangeRateSelectEnum.ierCurrentRate;
    dt.LetterFee = 12;
    dt.LetterFeeCurrency = "USD";
    dt.MinimumBalance = 13;
    dt.MinimumBalanceCurrency = "CAN";
    dt.YearlyInterestRate = 25;

    SAPbobsCOM.DunningTermLine dtl = dt.DunningTermLines.Add();
    dtl.CalculateInterest = BoYesNoEnum.tYES;
    dtl.Effectiveafter = "12";
    dtl.LetterFee = 20;
    dtl.LetterFeeCurrency = "USD";
    dtl.LetterFormat = dltDunningLetter2;
    dtl.MininumBalance = 14;
    dtl.MininumBalanceCurrency = "USD";

    dtl = dt.DunningTermLines.Add();
    dtl.CalculateInterest = BoYesNoEnum.tYES;
    dtl.Effectiveafter = "15";
    dtl.LetterFee = 20;
    dtl.LetterFeeCurrency = "CAN";
    dtl.LetterFormat = dltDunningLetter3;
    dtl.MininumBalance = 14;
    dtl.MininumBalanceCurrency = "USD";

    try
    {
        DunningTermParams dtp = dts.AddDunningTerm(dt);
    }
    catch(Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
    ```
- `Public Sub DeleteDunningTerm(ByVal pIDunningTermParams As DunningTermParams)` Deletes an existing dunning term. The dunning term is specified by its key (TermCode), which is contained in the DunningTermParams object passed to the method.
  - param `pIDunningTermParams`: The key of the dunning term to be deleted.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DunningTermsService dts = globals_Renamed.oCompany.GetCompanyService().GetBusinessService(ServiceTypes.DunningTermsService) as DunningTermsService;
    SAPbobsCOM.DunningTermParams dtp = dts.GetDataInterface(DunningTermsServiceDataInterfaces.dtsDunningTermParams) as DunningTermParams;
    dtp.Code = "Code5327";

    try
    {
        dts.DeleteDunningTerm(dtp);
    }
    catch (Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As DunningTermsServiceDataInterfaces) As Object` Creates an empty data structure for use with the DunningTermsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `DunningTermsServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetDunningTerm(ByVal pIDunningTermParams As DunningTermParams) As DunningTerm` Retrieves a dunning term. The dunning term is specified by its key (TermCode), which is contained in the DunningTermParams object passed to the method.
  - param `pIDunningTermParams`: The key of the dunning term to retrieve.
  - returns: The dunning term with the specified key.
- `Public Function GetDunningTermList() As DunningTermsParams` Retrieves the keys and names of all the dunning terms.
  - C# example (from SAP's help):
    ```csharp
    DunningTermsService dts = globals_Renamed.oCompany.GetCompanyService().GetBusinessService(ServiceTypes.DunningTermsService) as DunningTermsService;
    DunningTermsParams dtps = dts.GetDunningTermList();
    int length = dtps.Count;
    for (int i=0; i<length; i++)
    {
         Console.WriteLine(dtps.Item(i).Code);
    }
    ```
- `Public Sub UpdateDunningTerm(ByVal pIDunningTerm As DunningTerm)` Updates an existing dunning term. The data for the dunning term, including the key of the dunning term to be updated, is contained in the DunningTerm object passed to the method. To update a dunning term, you must first retrieve it using the GetDunningTerm method.
  - param `pIDunningTerm`: The data for the dunning term to be updated. The DunningTerm object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.DunningTermsService dts = globals_Renamed.oCompany.GetCompanyService().GetBusinessService(ServiceTypes.DunningTermsService) as DunningTermsService;
    SAPbobsCOM.DunningTermParams dtp = dts.GetDataInterface(DunningTermsServiceDataInterfaces.dtsDunningTermParams) as DunningTermParams;

    dtp.Code = "Code5327";
    SAPbobsCOM.DunningTerm dt = dts.GetDunningTerm(dtp);

    string code;
    string name;
    code = dt.Code;
    name = dt.Name;
    SAPbobsCOM.BoYesNoEnum applyHighestLetter = dt.ApplyHighestLetterTemplate;
    SAPbobsCOM.CalculateInterestMethodEnum calculateInterestMethod = dt.CalculateInterestMethod;
    dt.DaysInMonth = 28;
    dt.DaysInYear = 30;
    SAPbobsCOM.GroupingMethodEnum groupMethod = dt.GroupingMethod;
    SAPbobsCOM.BoYesNoEnum includeInterest = dt.IncludeInterest;
    SAPbobsCOM.ExchangeRateSelectEnum exchangeRateSelect = dt.ExchangeRateSelect;
    double letterFee = dt.LetterFee;
    string currency = dt.LetterFeeCurrency;
    double minBalance = dt.MinimumBalance;
    string minCurrency = dt.MinimumBalanceCurrency;
    double interestRate = dt.YearlyInterestRate;

    int count = dt.DunningTermLines.Count;
    SAPbobsCOM.DunningTermLine dtl = dt.DunningTermLines.Item(0);
    SAPbobsCOM.DunningTermLine dtl2 = dt.DunningTermLines.Item(1);
    dtl2.CalculateInterest = BoYesNoEnum.tNO;

    try
    {
        dts.UpdateDunningTerm(dt);
    }
    catch (Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
    ```

# DynamicSystemStrings (Object)

The DynamicSystemStrings object enables to modify the field name and format in the interface to match the terms used in your company. For example, in the Business Partners Master Data form, you can modify the field name 'Code' to 'BP Number' (format: bold). Source table: SDIS.

**Remarks:** Mandatory properties: FormID and ItemID. The combination of these properties specify the primary key of the required field for modification. In case the ItemID specifies a table, set also the ColumnID, otherwise the system sets the value -1. To display the form in the application: - Open a form, e.g. an A/R Invoice. - Hold down the Ctrl key and double-click the field name.

## Properties (8)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ColumnID() As String` [R/W] Sets or returns the column identification key. Field name: ColumnId. Mandatory property for Table fields. The default value is -1 (Title field). Length: 10 characters.
  - remarks: The entered value must be a valid column ID (the system does not validate the entered value). To display the column ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property FormID() As String` [R/W] Sets or returns the form identification key. Field name: FormID. Mandatory property. Length: 20 characters.
  - remarks: The entered value must be a valid form ID (the system does not validate the entered value). To display the form ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property IsBold() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not the new name of the field appears bold. Field name: IsBold.
- `Public Property IsItalics() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not the new name of the field appears italic. Field name: IsItalic.
- `Public Property ItemID() As String` [R/W] Sets or returns the ID of the field or the table in a form (primary key with FormID). Field name: ItemId. Mandatory property. Length: 10 characters.
  - remarks: The entered value must be a valid item ID (the system does not validate the entered value). In case the ItemID specifies a table, set also the ColumnID, otherwise the system sets the value -1. To display the item ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property ItemString() As String` [R/W] Sets or returns the new name for the specified field. Field name: ItemString. Length: 64 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Applies a new modification to a field name.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrFormId As String, ByVal bstrItemNum As String, ByVal bstrColNum As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrFormId`: 
  - param `bstrItemNum`: 
  - param `bstrColNum`: 
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

# EBooks (Object)

Source table: OEBK.

## Properties (19)
- `Public Property AA() As String` [R] property AA
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property CancelMARK() As String` [R] property CancelMARK
- `Public Property CPVATID() As String` [R] Counterpart VAT Number
- `Public Property Currency() As String` [R] property Currency
- `Public Property EBooksLines() As EBooksLines` [R] E-Books - Rows.
- `Public Property InvoiceType() As String` [R] property InvoiceType
- `Public Property IsNegativeMark() As BoYesNoEnum` [R/W] Is Negative MARK
- `Public Property IssueDate() As Date` [R] property IssueDate
- `Public Property IssuerVATID() As String` [R] property IssuerVATID
- `Public Property LinkedDocEntry() As Long` [R/W] property LinkedDocEntry
- `Public Property LinkedDocType() As Long` [R/W] property LinkedDocType
- `Public Property MARK() As String` [R] property MARK
- `Public Property Series() As String` [R] property Series
- `Public Property TotalGrossValue() As Double` [R] property TotalGrossValue
- `Public Property TotalNetValue() As Double` [R] property TotalNetValue
- `Public Property TotalVatAmount() As Double` [R] property TotalVatAmount
- `Public Property TotalWithheldAmount() As Double` [R] property TotalWithheldAmount
- `Public Property UID() As String` [R] Unique Identification.

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

# EBooks_Doc_Details (Object)

EBooks_Doc_Details Class

## Properties (15)
- `Public Property ExpensesClassificationCategory() As Long` [R/W] property ExpensesClassificationCategory
- `Public Property ExpensesClassificationType() As Long` [R/W] property ExpensesClassificationType
- `Public Property IncomeClassificationCategory() As Long` [R/W] property IncomeClassificationCategory
- `Public Property IncomeClassificationType() As Long` [R/W] property IncomeClassificationType
- `Public Property NetValueFC() As Double` [R] property NetValueFC
- `Public Property NetValueLC() As Double` [R] property NetValueLC
- `Public Property NetValueSC() As Double` [R] property NetValueSC
- `Public Property VatCategory() As Long` [R] property VatCategory
- `Public Property VatClassificationCategory() As Long` [R/W] property VatClassificationCategory
- `Public Property VatClassificationType() As Long` [R/W] property VatClassificationType
- `Public Property VATExemptionCause() As Long` [R/W] property VATExemptionCause
- `Public Property WithheldAmountFC() As Double` [R] property WithheldAmountFC
- `Public Property WithheldAmountLC() As Double` [R] property WithheldAmountLC
- `Public Property WithheldAmountSC() As Double` [R] property WithheldAmountSC
- `Public Property WithheldPercentCategory() As Long` [R] property WithheldPercentCategory

# EBooksLine (Object)

Source table: EBK1.

## Properties (10)
- `Public Property ExpenseClassificationCategory() As Long` [R/W] property ExpenseClassificationCategory
- `Public Property ExpenseClassificationType() As Long` [R/W] property ExpenseClassificationType
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property NetValue() As Double` [R] property NetValue
- `Public Property VatAmount() As Double` [R] property VatAmount
- `Public Property VatCategory() As Long` [R] property VatCategory
- `Public Property VatClassificationCategory() As Long` [R/W] property VATClassificationCategory
- `Public Property VatClassificationType() As Long` [R/W] property VATClassificationType
- `Public Property WithheldAmount() As Double` [R] property WithheldAmount
- `Public Property WithheldPercentCategory() As Long` [R] property WithheldPercentCategory

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

# EBooksLines (Collection)

EBooksLines Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As EBooksLine` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As EBooksLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EBooksParams (Object)

EBooksParams Class

## Properties (3)
- `Public Property LinkedDocEntry() As Long` [R/W] property LinkedDocEntry
- `Public Property LinkedDocType() As Long` [R/W] property LinkedDocType
- `Public Property MARK() As String` [R/W] property MARK

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

# EBooksParamsCollection (Collection)

EBooksParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As EBooksParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As EBooksParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# EBooksService (Object)

Source table: OEBK.

## Methods (7)
- `Public Function Get(ByVal pIEBooksParams As EBooksParams) As EBooks` Get
  - param `pIEBooksParams`: 
- `Public Function GetByDocKey(ByVal pIEBooksParams As EBooksParams) As EBooksParamsCollection` Return the object which is linked with a certain document.
  - param `pIEBooksParams`: 
- `Public Function GetByMark(ByVal pIEBooksParams As EBooksParams) As EBooks` Return the object by EBK.
  - param `pIEBooksParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As EBooksServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `EBooksServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pIEBooks As EBooks)` Update
  - param `pIEBooks`: 

# EcmAction (Object)

EcmAction Class

## Properties (25)
- `Public Property ActionID() As Long` [R] property ActionID
- `Public Property AssignedID() As String` [R/W] property AssignedID
- `Public Property BusinessPlace() As Long` [R/W] property BusinessPlace
- `Public Property Description() As String` [R/W] property Description
- `Public Property DocumentBatch() As String` [R/W] property DocumentBatch
- `Public Property DocumentBatchLine() As Long` [R/W] property DocumentBatchLine
- `Public Property Environment() As Long` [R/W] property Environment
- `Public Property GenerationType() As EcmActionGenerationTypeEnum` [R/W] property GenerationType
- `Public Property IsCanceled() As BoYesNoEnum` [R] property IsCanceled
- `Public Property IsRemoved() As BoYesNoEnum` [R] property IsRemoved
- `Public Property Message() As String` [R/W] property Message
- `Public Property ObjectID() As String` [R/W] property ObjectID
- `Public Property PeriodDateFrom() As Date` [R/W] property PeriodDateFrom
- `Public Property PeriodDateTo() As Date` [R/W] property PeriodDateTo
- `Public Property PeriodNumber() As Long` [R/W] property PeriodNumber
- `Public Property PeriodType() As EcmActionPeriodTypeEnum` [R/W] property PeriodType
- `Public Property PeriodYear() As Long` [R/W] property PeriodYear
- `Public Property Protocol() As String` [R/W] property Protocol
- `Public Property ReportID() As String` [R/W] property ReportID
- `Public Property SourceObject() As Long` [R/W] property SourceObject
- `Public Property SourceType() As String` [R/W] property SourceType
- `Public Property Status() As EcmActionStatusEnum` [R/W] property Status
- `Public Property Submits() As Long` [R/W] property Submits
- `Public Property Type() As EcmActionTypeEnum` [R/W] property Type
- `Public Property UserFields() As Fields` [R] property User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
