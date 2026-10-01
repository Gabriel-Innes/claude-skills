<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ChecksforPayment (Object)

Represents checks that are not tied to a document. SAP Business One updates the balances of vendor accounts each time you add a check for payment. This object is part of the Banking module. Checks tied to documents are represented by the Payments_Checks object. This object enables you to: - Add checks for payment. - Retrieve a check details by its key. - Update checks for payment. - Save the object in XML format. Source table: OCHO.

**Remarks:** Mandatory fields in SAP Business One: BankCode, CustomerAccountCode, CountryCode, and RowTotal (from ChecksforPaymentLines object). To display the form in the application: - Select Banking --> Outgoing Payments --> Checks for Payment.

## Properties (44)
- `Public Property AccountNumber() As String` [R/W] Sets or returns the bank account number of the check for payment. Field name: AcctNum. Length: 50 characters.
- `Public Property Address() As String` [R/W] Sets or returns the mailing address of the vendor. Field name: Address. Length: 254 characters.
- `Public Property AddressName() As String` [R/W] Sets or returns the name of the address (Bill To address, Main address, Ship To address, and so on). Field name: AddrName. Length: 50 characters.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code of the check. Field name: BankNum. Mandatory property. Length: 30 characters.
- `Public Property BankName() As String` [R] Returns the bank name of the payment check. Field name: BankName. Length: 15 characters.
- `Public Property Branch() As String` [R/W] Sets or returns the branch number of the payment check. Field name: Branch. Length: 50 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Canceled() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the check is canceled. Field name: Canceled.
- `Public Property CardOrAccount() As BoCpCardAcct` [R/W] Sets or returns a valid value of BoCpCardAcct type that specifies whether the payment check is to a vendor card or to a G/L account. Field name: CardOrAcct.
  - remarks: If Card, then you must set the value for the vendor code. If Account, then you must set the value for the account. SAP Business One validates the vendor code or the account.
- `Public Property CheckAmount() As Double` [R] Returns the total amount of the check. This number must be positive. Field name: CheckSum.
- `Public Property CheckCurrency() As String` [R] Returns the currency of the check. SAP Business One performs a validation check. Length: 3 characters. Field name: Currency.
- `Public Property CheckDate() As Date` [R/W] Sets or returns the due date for the check. Field name: CheckDate.
  - remarks: This date is also the value date, if a posting is created in accounting when the transaction is carried out. If you do not set the CheckDate property, the system sets the current date.
- `Public Property CheckKey() As Long` [R] Returns the sequence number of the check for payment. Field name: CheckKey. This number is assigned by SAP Business One automatically.
- `Public Property CheckNumber() As Long` [R/W] Sets or returns the check number for payment. Field name: CheckNum.
- `Public Property CountryCode() As String` [R/W] Sets or returns the country code of the bank. Field name: CountryCod. Mandatory property. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property CreateJournalEntry() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to create a journal entry when adding the current check. Field name: CreateJdt.
- `Public Property CreationDate() As Date` [R] Returns the date of creation of the check. Field name: CreateDate.
  - remarks: This property is internal in SAP Business One.
- `Public Property CustomerAccountCode() As String` [R/W] Sets or returns the credited G/L account code. Field name: CheckAcct. Mandatory property. Length: 210 characters.
  - remarks: SAP Business One validates this property with G/L account details.
- `Public Property DeductionRefundAmount() As Double` [R/W] Sets or returns the deduction refund amount. Field name: Deduction.
- `Public Property Details() As String` [R/W] Sets or returns the journal remarks of the check for payment. Field name: Details. Length: 50 characters.
  - remarks: SAP Business One automatically generates a remark that is copied to the accounting document. You can change or delete this text if necessary.
- `Public Property DocumentReferences() As ChecksforPaymentDocumentReferences` [R] Returns an instance of the document references of checks for payment.
- `Public Property ECheck() As BoYesNoEnum` [R/W] Specifies whether the account is relevant for e-check functionality or not. Field name: ECheck.
- `Public Property JournalEntryReference() As String` [R/W] Sets or returns the reference number for a payment to a vendor (outgoing payment) that is already created in SAP Business One. If the reference number does not exist, SAP Business One sets the transaction key. Field name: TransRef.
- `Public Property Lines() As ChecksforPaymentLines` [R] Returns ChecksforPaymentLines child object.
- `Public Property ManualCheck() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether or not to set the check number manually. Used in case the check is not printed through SAP Business One, but written manually. Relevant for outgoing payments only.
- `Public Property PaymentDate() As Date` [R/W] Sets or returns the posting date. If you do not set this date, SAP Business One sets the current date as the posting date for the transaction. Field name: PmntDate.
- `Public Property PaymentNo() As Long` [R] Returns the payment number of the check. Field name: PmntNum.
- `Public Property PrintConfirm() As BoYesNoEnum` [R/W] Confirms whether a check is printed or not. Field name: PrnConfrm.
- `Public Property Printed() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the check was printed. Field name: Printed.
- `Public Property PrintedBy() As Long` [R] Returns the ID of the user that prints the check. Field name: PrintedBy.
- `Public Property PrintStatus() As ChecksforPaymentPrintStatus` [R] The column Print Status in the Check Number Confirmation window.
- `Public Property Signature() As String` [R/W] Sets or returns the authorizing signature, such as the name of the responsible person, for approving the payment. Field name: Signature. Length: 30 characters.
- `Public Property TaxDate() As Date` [R] Returns the date for the tax payment. Field name: TaxDate.
- `Public Property TaxTotal() As Double` [R] Returns the total tax, such as VAT, added to the payment. Field name: VatTotal.
  - remarks: SAP Business One calculates the tax according to the tax group defined using the Document_LinesAdditionalExpenses object (source table: DRF3).
- `Public Property TotalinWords() As String` [R/W] Sets or returns the total amount is words. SAP Business One enters this value automatically according to the CheckAmount. Field name: TotalWords. Length: 100 characters.
- `Public Property TransactionNumber() As Long` [R] Returns the transaction code that SAP Business One creates for the payment check. Field name: TransNum.
- `Public Property Transferable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the check can be endorsed. If the value is set to No (not endorsable), SAP Business One includes the text "Non-negotiable" in the printout. Field name: Trnsfrable.
- `Public Property UpdateDate() As Date` [R] Returns the date when the check details were last updated. Field name: UpdateDate.
  - remarks: Internal property in SAP Business One.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VendorCode() As String` [R/W] Sets or returns the vendor number or G/L account for the payment. SAP Business One validates this number. Field name: VendorCode. Length: 15 characters.
- `Public Property VendorName() As String` [R] Returns the name of the vendor that appears in the "Pay to Order of" field of the check. Field name: VendorName. Length: 100 characters.
- `Public Property WithholdingTaxAmount() As Double` [R] property WithholdingTaxAmount
- `Public Property WithholdingTaxPercentage() As Double` [R/W] property WithholdingTaxPercentage

## Methods (9)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Not supported.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal CheckKey As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `CheckKey`: Specifies the sequence number of the check for payment (see CheckKey property).
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
