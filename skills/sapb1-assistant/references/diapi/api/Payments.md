<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Payments (Object)

Payments is a business object that represents payment methods in the Banking module. This object defines the incoming payments from customers and outgoing payments to vendors. Available payment methods are cash, credit cards, checks, or bank transfers. Source tables: ORCT (incoming payments) and OVPM (outgoing payments).

**Remarks:** Mandatory fields in SAP Business One: CardCode, CashSum, TransferAccount, and TransferSum. To display the form in the application: - For the ORCT table, select Banking --> Incoming Payments --> Incoming Payments. - For the OVPM table, select Banking --> Outgoing Payments --> Payments to Vendors.

## Properties (101)
- `Public Property AccountPayments() As Payments_Accounts` [R] Returns the Payments_Accounts object that represents the payments through account transfers.
- `Public Property Address() As String` [R/W] Sets or returns the Bill To address of the business partner. Field name: Address. Length: 254 characters.
  - remarks: Default value: Bill To address from BusinessPartners object.
- `Public Property ApplyVAT() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to apply a tax to this payment. Field name: ApplyVAT.
  - remarks: Country specific field for Singapore only. If set to tYES, you must specify the VatGroup property in Payments_Accounts child object.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property AuthorizationStatus() As PaymentsAuthorizationStatusEnum` [R] Returns the status of the authorization for this payment. Field name: wddStatus.
- `Public Property BankAccount() As String` [R/W] Sets or returns the bank account number used for this payment. Field name: BankAcct. Length: 50 characters.
  - remarks: In SAP Business One, payments through accounts is used for payments to third-parties that are not part of your customers or vendors. Country-specific property for Poland.
- `Public Property BankChargeAmount() As Double` [R/W] Sets or returns the bank charge amount. Field name: BcgSum.
- `Public Property BankChargeAmountInFC() As Double` [R] Returns the bank charge amount in foreign currency. Field name: BcgSumFC.
- `Public Property BankChargeAmountInSC() As Double` [R] Returns the bank charge amount in system currency. Field name: BcgSumSy.
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code for bank transfer. Field name: BankCode. Length: 30 characters.
  - remarks: In SAP Business One, payments through accounts is used for payments to third-parties that are not part of your customers or vendors. Country-specific property for Poland.
- `Public Property BillOfExchange() As BillOfExchange` [R] Returns the BillOfExchange object.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillOfExchangeAgent() As String` [R/W] Sets or returns the code of the company employee responsible for the collection and management of bill of exchange transactions. Field name: BoeAgent. Length: 32 characters. This is a foreign key to the Agent Name table (OAGP), not exposed through the DI API).
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillOfExchangeAmount() As Double` [R/W] Sets or returns the total amount of payment using a Bill Of Exchange document in local currency. Field name: BoeSum.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillOfExchangeAmountFC() As Double` [R] Returns the total amount of payment using a Bill Of Exchange document in foreign currency. Field name: BoeSumFc.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillOfExchangeAmountSC() As Double` [R] Returns the total amount of payment using a Bill Of Exchange document in system currency. Field name: BoeSumSc.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BillofExchangeStatus() As BoBoeStatus` [R/W] Sets or returns a valid value of BoBoeStatus type that specifies the status of the Bill Of Exchange. Field name: BoeStatus.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BlanketAgreement() As Long` [R/W] property BlanketAgreement
- `Public Property BoeAccount() As String` [R/W] Sets or returns the control G/L account that is used in the Bill Of Exchange transactions. Field name: BoeAcc. Length: 15 characters.
  - remarks: Country-specific property for Italy, Spain, and Portugal.
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Cancelled() As BoYesNoEnum` [R] Indicates whether the payment was cancelled.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner code or the account code. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartnersService object.
  - remarks: Mandatory property. The card code is the primary key of business partners records in SAP Business One. Use this property to list, search, and display business partners records. When the payment is to/by an account, the property will contain the account number accordingly.
- `Public Property CardName() As String` [R/W] Sets or returns the business partner's full name. Field name: CardFName. Length: 100 characters.
  - remarks: You can use this property to represent company's name, organization name, person name, or any other entity that represents the business partner. Field name: CardName.
- `Public Property CashAccount() As String` [R/W] Sets or returns the cash G/L account used for this payment. Field name: CashAcct. Length: 15 characters.
- `Public Property CashSum() As Double` [R/W] Sets or returns the amount of cash in the current payment in local currency. Field name: CashSum. Mandatory property.
  - remarks: Use this property to record the payment amount in cash payments. The value must be positive or 0.
- `Public Property CashSumFC() As Double` [R] Returns the amount of cash in the current payment in foreign currency. Field name: CashSumFC.
- `Public Property CashSumSys() As Double` [R] Returns the amount of cash in the current payment in system currency. Field name: CheckSumSy.
- `Public Property CertificationNumber() As String` [R] property CertificationNumber
- `Public Property CheckAccount() As String` [R/W] Sets or returns the check G/L account used for this payment. Field name: CheckAcct. Length: 15 characters.
- `Public Property Checks() As Payments_Checks` [R] Returns the Payments_Checks child object that represents the payments through checks.
- `Public Property Cig() As Long` [R/W] property Cig
- `Public Property ContactPersonCode() As Long` [R/W] Sets or returns the contact person code of the specified business partner in this payment. Field name: CntctCode. This is a foreign key to the ContactEmployees object.
  - remarks: The default value is according to the value of ContactPerson property of the BusinessPartners object. You can choose only the contact person that belongs to the specified business partner.
- `Public Property ControlAccount() As String` [R/W] The control account for this document. Field name: BpAct This is a foreign key to the ChartOfAccounts object.
- `Public Property CounterReference() As String` [R/W] Sets or returns reference information about the payment. Field name: CounterRef. Length: 8 characters.
- `Public Property CreditCards() As Payments_CreditCards` [R] Returns the Payments_CreditCards child object that represents the payments through credit cards.
- `Public Property Cup() As Long` [R/W] property Cup
- `Public Property DeductionPercent() As Double` [R/W] Sets or returns the deduction percentage. Field name: DdctPrcnt.
  - remarks: Country-specific field for Israel.
- `Public Property DeductionSum() As Double` [R/W] Sets or returns the calculated deduction amount. Field name: DdctSum.
  - remarks: Country-specific field for Israel.
- `Public Property DocCurrency() As String` [R/W] Sets or returns the document code of the currency used in this payment. Field name: DocCurr. Length: 3 characters.
  - remarks: Valid values: local currency, system currency, card currency, or any other currency. For multi-currency the valid values are taken from the Currencies object.
- `Public Property DocDate() As Date` [R/W] Sets or returns the posting date of the payment document. Field name: VatDate.
  - remarks: Default date: system date. Valid values: not later than the system date.
- `Public Property DocEntry() As Long` [R] Returns the document entry key that uniquely identifies the payment document. Property type Read-only property " --> Field name: DocEntry.
- `Public Property DocNum() As Long` [R/W] Sets or returns the payment document number. Field name: DocNum.
  - remarks: This is a unique number (greater than 0) used as an entry key for identifying the payment document. Mandatory field in SAP Business One only in case the value of the HandWritten property is tYES. In case the value of HandWritten property is tNo, SAP Business One sets the next available number.
- `Public Property DocObjectCode() As BoPaymentsObjectType` [R/W] Sets or returns a valid value of BoPaymentsObjectType type that specifies the payments document type.
- `Public Property DocRate() As Double` [R/W] Sets or returns the exchange rate (greater than 0) related to the local currency. Field name: DocRate.
  - remarks: Mandatory in case the payment document does not use the local currency. You can get the recommended exchange rate using the GetCurrencyRate method.
- `Public Property DocType() As BoRcptTypes` [R/W] Sets or returns a valid value of BoRcptTypes type that specifies the payment recipient (replaces the DocTypte property). Field name: DocType.
- `Public Property DocTypte() As BoRcptTypes` [R/W] Sets or returns a valid value of BoRcptTypes type that specifies the payment recipient.
  - remarks: Note: This property is replaced by DocType, but remains in the collection due to backward compatibility.
- `Public Property DocumentReferences() As Payments_DocumentReferences` [R] property DocumentReferences
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date of the check. Field name: DueDate.
- `Public Property ElectronicProtocols() As ElectronicProtocols` [R] property ElectronicProtocols
- `Public Property HandWritten() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this payment is based on a handwritten document. Field name: Handwrtten.
- `Public Property Invoices() As Payments_Invoices` [R] Returns the Payments_Invoices child object that represents the invoice data for this payment.
- `Public Property IsPayToBank() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether to specify the bank details or only the PaytoCode for the outgoing payment. Field name: IsPaytoBnk.
- `Public Property JournalRemarks() As String` [R/W] Sets or returns the remarks to the journal entry of this payment. Field name: . Length: 50 characters.
  - remarks: Default value is auto-completed when setting the CardCode property.
- `Public Property LocalCurrency() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the payment uses local currency. Field name: DiffCurr.
- `Public Property LocationCode() As Long` [R/W] Sets or returns the location code in incoming and outgoing payments. Applicable for cluster B. Field name: LocCode.
- `Public Property PaymentByWTCertif() As BoYesNoEnum` [R/W] property PaymentByWTCertif
- `Public Property PaymentPriority() As BoPaymentPriorities` [R/W] Sets or returns a valid value of BoPaymentPriorities type that specifies the payment priority. Field name: PaPriority.
- `Public Property Payments_ApprovalRequests() As Payments_ApprovalRequests` [R] Returns the Payments_ApprovalRequests object.
- `Public Property PaymentType() As BoORCTPaymentTypeEnum` [R/W] Sets or returns a valid value of Payment Type (Object Type). Field name: ObjType.
- `Public Property PayToBankAccountNo() As String` [R/W] Sets or returns the bank account number for the outgoing payment. Field name: PBnkAccnt. Length: 50 characters.
  - remarks: Relevant only if IsPaytoBank property is set to tYES.
- `Public Property PayToBankBranch() As String` [R/W] Sets or returns the bank branch for the outgoing payment. Field name: PBnkBranch. Length: 50 characters.
  - remarks: Relevant only if IsPaytoBank property is set to tYES.
- `Public Property PayToBankCode() As String` [R/W] Sets or returns the bank code for the outgoing payment. Field name: PBnkCode. Length: 30 characters.
  - remarks: Relevant only if IsPaytoBank property is set to tYES.
- `Public Property PayToBankCountry() As String` [R/W] Sets or returns the bank country for the outgoing payment. Field name: PBnkCnt. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: Relevant only if IsPaytoBank property is set to tYES.
- `Public Property PayToCode() As String` [R/W] Sets or returns the destination code for the outgoing payment. Field name: PayToCode. Length: 50 characters.
  - remarks: Relevant only if IsPaytoBank property is set to tNO.
- `Public Property PrimaryFormItems() As CashFlowAssignments` [R] property PrimaryFormItems
- `Public Property Printed() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the payment document was printed. Field name: Printed.
- `Public Property PrivateKeyVersion() As Long` [R] property PrivateKeyVersion
- `Public Property Proforma() As BoYesNoEnum` [R/W] Returns a valid value of BoYesNoEnum type that specifies whether or not the payment refers to a Pro-Forma invoice. Field name: Proforma.
  - remarks: Country-specific field for Italy and Spain. Applies to outgoing payments to vendors only. A Pro-Forma invoice is a draft document sent to the company by a vendor who provides services, other than goods or items.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code that the payment refers to. Field name: PrjCode. Length: 8 characters. This is a foreign key to the Projects table (OPRJ - not exposed through the DI API).
  - remarks: Editing project code in the Journal Entry header does not affect the project code assigned to Journal Entry lines. To enforce the change on the lines, you must set JournalEntries_Lines.ProjectCode.
- `Public Property Reference1() As String` [R/W] Sets or returns the first reference code of the payment. Field name: Ref1. Length: 11 characters.
  - remarks: Default value from DocNum property.
- `Public Property Reference2() As String` [R/W] Sets or returns the second reference code of the payment. Field name: Ref2. Length: 8 characters.
- `Public Property Remarks() As String` [R/W] Sets or returns the remarks to this payment. Field name: Comments. Length: 254 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the auto-number series that generated the document number. Field name: Series. This is a foreign key to the Series object.
  - remarks: This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property SignatureDigest() As String` [R] property SignatureDigest
- `Public Property SignatureInputMessage() As String` [R] property SignatureInputMessage
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TaxGroup() As String` [R/W] Sets or returns the VAT group. Field name: VatGroup. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: The VAT groups are defined in SAP Business One and stored in the OVTG table, which is not exposed by the DI API. Country-specific for Europe. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property TransactionCode() As String` [R/W] Sets or returns the transaction code of incoming payment. Field name: TransCode. This is a foreign key to the Journal Entry Codes table (OTRC), not exposed through the DI API).
- `Public Property TransferAccount() As String` [R/W] Sets or returns the G/L account number for the payment Transfer Account. Field name: TrsfrAcct. Length: 15 characters.
  - remarks: When using payments through a bank transfer, you must set also the TransferDate, TransferReference, and TransferSum properties.
- `Public Property TransferDate() As Date` [R/W] Sets or returns the date of the payment transfer to the bank. Field name: TrsfrDate.
  - remarks: In payments through bank transfer, also set the TransferReference and TransferSum properties. The transfer date must be within the same period of the DocDate property.
- `Public Property TransferRealAmount() As Double` [R/W] Sets or returns the Transfer Real Amount in payment document. Field name: TfrRealAmt. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property TransferReference() As String` [R/W] Sets or returns the reference information for the payment transfer to the bank. Field name: PaymentRef. Length: 27 characters.
  - remarks: In payments via bank transfer, also set the TransferDate and TransferSum properties.
- `Public Property TransferSum() As Double` [R/W] Sets or returns the total payments Transfer Amount. Field name: TrsfrSum. Mandatory property.
  - remarks: When using payments through a bank transfer, you must set also the TransferDate and TransferReference properties. The value must be positive.
- `Public Property UnderOverpaymentdifference() As Double` [R] Sets or returns the Under / Over payment Difference. Field name: UndOvDiff.
- `Public Property UnderOverpaymentdiffFC() As Double` [R] property UnderOverpaymentdiffFC
- `Public Property UnderOverpaymentdiffSC() As Double` [R] Sets or returns the Under / Overpayment Difference in System Currency. Field name: UndOvDiffS.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatDate() As Date` [R/W] Sets or returns the Vat payment date (Document Date). Field name: TaxDate.
- `Public Property VATRegNum() As String` [R] property VATRegNum
- `Public Property WithholdingTaxCertificates() As WithholdingTaxCertificates` [R] property WithholdingCertificate
- `Public Property WithholdingTaxDataWTX() As WithholdingTaxDataWTX` [R] property WithholdingTaxDataWTX
- `Public Property WTAccount() As String` [R] Returns the withholding account. Field name: WtAccount. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, India, and Portugal. For India localizations, if this property is set to yes, then the TaxId0 property of the BPFiscalTaxID object is mandatory and must be set to a 10-character value.
- `Public Property WTAmount() As Double` [R/W] Sets or returns the total withholding tax amount (in local currency) related to the payment. Field name: WtSum.
  - remarks: Applies to payments to vendors only. To set this property you must first set the WTCode property as defined in the Withholding Tax Code definition in SAP Business One. WTAmount = WTTaxableAmount * tax rate as defined for the WTCode. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, and Portugal.
- `Public Property WTAmountFC() As Double` [R] Returns the total withholding tax amount (in foreign currency) related to the payment. Field name: WtSumFrgn.
- `Public Property WTAmountSC() As Double` [R] Returns the total withholding tax amount (in system currency) related to the payment. Field name: WtSumSys.
- `Public Property WtBaseSum() As Double` [R/W] Sets or returns the Base sum for vat calculation. Field name: WtBaseSum.
- `Public Property WtBaseSumFC() As Double` [R] Sets or returns the Withholding Tax Base Sum in Foreign Currency. Field name: WtBaseSumF.
- `Public Property WtBaseSumSC() As Double` [R] Sets or returns the Withholding Tax Base Sum in System Currency. Field name: WtSumSys.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code assigend to the payment. Length: 4 characters. This is a foreign key to WithholdingTaxCodes object. Field name: WtCode.
- `Public Property WTTaxableAmount() As Double` [R] Returns the withholding taxable amount of the payment. Field name: WtBaseAmnt.
  - remarks: Applies to payments to vendors only. The default value of WTTaxableAmount property depends on the Base Amount percentage as defined for the specified WTCode. Country-specific property for Germany, Switzerland, Netherlands, Norway, Finland, Denmark, Austria, UK, Sweden, Spain, Italy, and Portugal.

## Methods (13)
- `Public Function Add() As Long` Adds a new Payment object to SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Cancels a payment transaction. The cancellation date of the transaction is the original document date.
- `Public Function CancelbyCurrentSystemDate() As Long` method CancelbyCurrentSystemDate
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
- `Public Function GetApprovalTemplates() As Long` Gets the related approval template.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal RctEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `RctEntry`: Specifies the document entry key (DocEntry).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Function RequestApproveCancellation() As Long` method RequestApproveCancellation
- `Public Function SaveDraftToDocument() As Long` Converts an approved draft document to a valid document.
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
