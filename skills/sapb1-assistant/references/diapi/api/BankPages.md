<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BankPages (Object)

BankPages is a business object that represents external bank statements in the Banking module. This object enables you to: - Add bank statements. - Retrieve a bank statement by its key. - Update bank statements. - Save the object in XML format. Source table: OBNK.

**Remarks:** Mandatory fields in SAP Business One: AccountCode, and CreditAmount or DebitAmount. To display the form in the application: - Select Banking --> Bank Statements and Reconciliations --> Process External Bank Statement.

## Properties (24)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code of the business partner as defined in Chart of Accounts. Field name: AcctCode. Mandatory property. Length: 15 characters.
  - remarks: To set the AccountCode value when working with segmentation, use the FormatCode to find its key value (for example, _SYS00000000010) as follows: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010).
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

        'Use the sStr value to set the AccountCode
    ```
- `Public Property AccountName() As String` [R] Returns the G/L account name of the business partner as defined in Chart of Accounts. Field name: AcctName. Length: 100 characters.
- `Public Property BankMatch() As Long` [R] Returns the status indicating whether or not the amount in the line of the bank statement is reconciled with amount in the line of the G/L account or business partner account. Field name: BankMatch.
- `Public Property BICSwiftCode() As String` [R/W] The BIC/SWIFT code of the business partner bank account as defined in the Business Partner Bank Accounts – Setup window. Field name: BPswift. Length: 50 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Length: 15 characters.
  - remarks: SAP Business One validates the CardCode, and if not valid, returns an error code. To create a receipt that matches to the invoice, set the following properties: CardCode, AccountCode, InvoiceNumber, CreditAmount or DebitAmount that must be equal to the invoice amount, and PaymentCreated.
- `Public Property CardName() As String` [R/W] Sets or returns the name of the existing business partner. Field name: CardName. Length: 100 characters.
  - remarks: SAP Business One validates this code, and if not valid, returns an error code.
- `Public Property CreditAmount() As Double` [R/W] Sets or returns the amount in foreign currency to credit the account. Field name: CredAmnt. Mandatory field in SAP Business One, if the amount is to credit the account.
- `Public Property DataSource() As String` [R] Not supported.
- `Public Property DebitAmount() As Double` [R/W] Sets or returns the amount in foreign currency to debit the account. Field name: DebAmount. Mandatory field in SAP Business One, if the amount is to debit the account.
- `Public Property DocNumberType() As BoBpsDocTypes` [R/W] Sets or returns a boolean value that specifies the document type for identifying an invoice document. Field name: DocNumType.
  - remarks: Default value is: bpdt_DocNum, which identifies the invoice by its number.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date in a bank statement row. Field name: DueDate.
- `Public Property ExternalCode() As String` [R/W] Sets or returns the external code. Field name: ExternCode. Length: 30 characters.
  - remarks: The ExternalCode property (together with CardName, CardCode, StatementNumber, InvoiceNumber, PaymentCreated, and VisualOrder) enable to create a receipt that matches to the invoice. If the value of PaymentCreated property is set to Yes and the payment creation succeeds, the property type is changed to Read Only.
- `Public Property InvoiceNumber() As Long` [R/W] Sets or returns the number of the invoice for payment. From release 2004, use the InvoiceNumberEx property, which is a string, instead of this property. Field name: DocNum. Length: 27 characters.
  - remarks: The InvoiceNumber property (together with CardCode, CardName, ExternalCode, PaymentCreated, and StatementNumber) enable to create a receipt that matches to the invoice. If the value of PaymentCreated property is set to Yes and the payment creation succeeds, the property type is changed to Read Only.
- `Public Property InvoiceNumberEx() As String` [R/W] Sets or returns a string that specifies the number of the invoice for payment. Field name: ExternCode. Length: 30 characters.
  - remarks: Use this property instead of InvoiceNumber (which remains the DI API to maintain backward compatibility).
- `Public Property Memo() As String` [R/W] Sets or returns the details of a line in the bank statement. Field name: Memo. Length: 255 characters.
- `Public Property PaymentCreated() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the payment was created. Field name: PaymCreat.
  - remarks: If the payment creation fails, the value of PaymentCreated property is changed to No.
- `Public Property PaymentReference() As String` [R/W] Sets or returns the payment reference that authorizes the payment process (according to the legal requirements). Field name: PaymentRef. Length: 27 characters.
- `Public Property Reference() As String` [R/W] Sets or returns the reference number in the bank statement row. Length: 8 characters. Field name: PaymentRef.
- `Public Property Sequence() As Long` [R] Returns the sequential number used, together with AccountCode, for identifying the bank account. Field name: Sequence.
- `Public Property StatementNumber() As Long` [R/W] Sets or returns the number of the bank statement. Field name: IdNumber.
  - remarks: The StatementNumber property (together with CardCode, CardName, ExternalCode, InvoiceNumber, and PaymentCreated) enable to create a receipt that matches to the invoice. If the value of PaymentCreated property is set to Yes and the payment creation succeeds, the property type is changed to Read Only.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the bank statement. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property VisualOrder() As Long` [R/W] Sets or returns the appearance order of the bank statement line. Field name: VisOrder.
  - remarks: By default, the visual order number equals to the Sequence number. To add a row between exiting rows, set the VisualOrder value to the required row number and call the Add method.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal AccountCode As String, ByVal Sequence As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `AccountCode`: Specifies the bank account code.
  - param `Sequence`: Specifies the sequential number used for identifying (together with the AccountCode) the bank account.
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
