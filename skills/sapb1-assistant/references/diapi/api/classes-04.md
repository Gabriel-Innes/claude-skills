<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# Banks (Object)

The Banks object enables to define banks, which can be used by the HouseBankAccounts and BPBankAccounts objects. Source table: ODSC.

**Remarks:** Mandatory fields in SAP Business One: BankCode and CountryCode. To display the form in the application: - Select Administration -->Setup -->Banking -->Banks.

## Properties (13)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the bank as assigned by the system when adding a new entry. Field name: AbsoluteEntry.
- `Public Property AccountforOutgoingChecks() As String` [R] Returns the bank account number for outgoing checks. Field name: DfltAcct. Length: 50 characters.
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code. Field name: BankCode. Mandatory property. Length: 30 characters.
- `Public Property BankName() As String` [R/W] Sets or returns bank name. Field name: BankName. Length: 32 characters.
- `Public Property BranchforOutgoingChecks() As String` [R] Returns the bank branch for outgoing checks. Field name: DfltBranch. Length: 50 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CountryCode() As String` [R/W] Sets or returns the country code of the bank (for example: DE). Field name: CountryCod. Length: 3 characters. Mandatory property.
  - remarks: You can set only the country codes that are defined in the Countries table (OCRY - not exposed through the DI API).
- `Public Property DefaultBankAccountKey() As Long` [R/W] Sets or returns the identification key of the default house bank account. Field name: DfltActKey. This is a foreign key to the HouseBankAccounts object.
  - remarks: Bank accounts are defined through the HouseBankAccounts object. The bank account is identified by the AbsoluteEntry.
- `Public Property IBAN() As String` [R/W] Sets or returns the International Bank Account Number (IBAN). Field name: IBAN. Length: 50 characters.
- `Public Property NextCheckNumber() As Long` [R] Returns the number of the next check for payment as specified in the NextCheckNo property of the HouseBankAccounts object. Field name: NextNum.
- `Public Property PostOffice() As BoYesNoEnum` [R/W] Determines whether or not the bank is also a post office. Field name: PostOffice.
- `Public Property SwiftNo() As String` [R/W] Sets or returns the swift number for international payments by wire transfer. Field name: SwiftNum. Length: 50 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a new record of banks table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: 
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

# BankStatement (Object)

A data structure related with the BankStatementService holding the bank statement header properties. Source table: OBNH.

## Properties (14)
- `Public Property BankAccountKey() As Long` [R/W] Sets or returns the bank account code. Field name: ActKey.
- `Public Property BankStatementFileHash() As String` [R/W] Sets or returns the bank statement file hash. Field name: FileCRC.
- `Public Property BankStatementGUID() As String` [R/W] Sets or returns the bank statement GUID. Field name: StmtGuid.
- `Public Property BankStatementRows() As BankStatementRows` [R] Returns a reference to a data collection holding properties of bank statement lines.
- `Public Property Currency() As String` [R/W] Sets or returns the statement currency. Field name: Currency.
- `Public Property EndingBalanceF() As Double` [R/W] Sets or returns the statement end balance in foreign currency. Field name: EndBlncF.
- `Public Property EndingBalanceL() As Double` [R/W] Sets or returns the statement end balance in local currency. Field name: EndBlncL.
- `Public Property Imported() As BoYesNoEnum` [R] Returns a valid value specifying whether or not the statement created manually or imported from file.
- `Public Property InternalNumber() As Long` [R] Returns the unique ID of the statement in the system. Field name: IdNumber.
- `Public Property StartingBalanceF() As Double` [R/W] Sets or returns the statement start balance in foreign currency. Field name: StrtBlncF.
- `Public Property StartingBalanceL() As Double` [R/W] Sets or returns the statement start balance in local currency. Field name: StrtBlncL.
- `Public Property StatementDate() As Date` [R/W] Sets or returns the statement creation date. Field name: BSDate.
- `Public Property StatementNumber() As String` [R/W] Sets or returns the statement sequential number. Field name: BSFileNum.
- `Public Property Status() As BankStatementStatusEnum` [R] Returns a value specifying the statement status. Field name: Status.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BankStatementParams (Object)

A data structure holding idnetification properties for the BankStatementService.

## Properties (11)
- `Public Property BankAccountKey() As Long` [R] Returns the bank account code. Field name: ActKey.
- `Public Property Currency() As String` [R] Returns the statement currency. Field name: Currency.
- `Public Property EndingBalanceF() As Double` [R] Returns the statement end balance in foreign currency. Field name: EndBlncF.
- `Public Property EndingBalanceL() As Double` [R] Returns the statement end balance in local currency. Field name: EndBlncL.
- `Public Property Imported() As BoYesNoEnum` [R] Returns a valid value specifying whether or not the statement created manually or imported from file.
- `Public Property InternalNumber() As Long` [R/W] Sets or returns the unique ID of the statement in the system. Field name: IdNumber.
- `Public Property StartingBalanceF() As Double` [R] Returns the statement start balance in foreign currency. Field name: StrtBlncF.
- `Public Property StartingBalanceL() As Double` [R] Returns the statement start balance in local currency. Field name: StrtBlncL.
- `Public Property StatementDate() As Date` [R] Returns the statement creation date. Field name: BSDate.
- `Public Property StatementNumber() As String` [R] Returns the satatement sequential number. Field name: BSNum.
- `Public Property Status() As BankStatementStatusEnum` [R] Returns a value specifying the statement status. Field name: Status.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BankStatementRow (Object)

A data structure related to the BankStatementService holding the properties of a bank statement line. Access this object via BankStatement.BankStatementRows. Source table: OBNK

## Properties (52)
- `Public Property AccountName() As String` [R/W] Returns the G/L account name of the business partner as defined in Chart of Accounts. Field name: AcctName. Length: 100 characters.
- `Public Property AccountNumber() As String` [R] Sets or returns the G/L account code of the business partner as defined in Chart of Accounts. Field name: AcctCode. Mandatory property. Length: 15 characters.
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
- `Public Property Balance() As Double` [R/W] Returns or sets account balance. Field name: balance.
- `Public Property BankStmtDueDate() As Date` [R/W] Sets or returns the statement due date. Field name: BSValuDate.
- `Public Property BankStmtLineDate() As Date` [R/W] Sets or returns the line date. Field name: BSLineDate.
- `Public Property BPBankAccount() As String` [R/W] Sets or returns the business partner bank account. Field name:OposAct.
- `Public Property BPBankCode() As String` [R/W] Sets or returns the business partner bank code. Field name: BpBankCode
- `Public Property BPBICSwiftCode() As String` [R/W] The BIC/SWIFT code of the business partner bank account as defined in the Business Partner Bank Accounts – Setup window. Field name: BPswift. Length: 50 characters.
- `Public Property BPCode() As String` [R/W] Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Length: 15 characters.
  - remarks: SAP Business One validates the CardCode, and if not valid, returns an error code. To create a receipt that matches to the invoice, set the following properties: CardCode, AccountCode, InvoiceNumber, CreditAmount or DebitAmount that must be equal to the invoice amount, and PaymentCreated.
- `Public Property BPName() As String` [R/W] Sets or returns the name of the existing business partner. Field name: CardName. Length: 100 characters.
  - remarks: SAP Business One validates this code, and if not valid, returns an error code.
- `Public Property CreateMethod() As CreateMethodEnum` [R] Returns a value specifying whether the statement was created automatically or manualy. Field name: autoCreate.
- `Public Property CreditAmountFC() As Double` [R/W] Sets or returns the amount in foreign currency to credit the account. Field name: CredAmnt. Mandatory field in SAP Business One, if the amount is to credit the account.
- `Public Property CreditAmountLC() As Double` [R/W] Sets or returns the amount in local currency to credit the account. Field name: CredAmntLC.
- `Public Property CreditCurrency() As String` [R/W] Sets or returns the credit currency. Field name: CredAmntCu.
- `Public Property DebitAmountFC() As Double` [R/W] Sets or returns the amount in foreign currency to debit the account. Field name: DebAmount. Mandatory field in SAP Business One, if the amount is to debit the account.
- `Public Property DebitAmountLC() As Double` [R/W] Sets or returns the amount in local currency to debit the account. Field name: DebAmountLC.
- `Public Property Details() As String` [R/W] Sets or returns the details of a line in the bank statement. Field name: Memo. Length: 255 characters.
- `Public Property Details2() As String` [R/W] Sets or returns the details of a line in the bank statement. Field name: Memo2. Length: 255 characters.
- `Public Property DocNumType() As BoBpsDocTypes` [R/W] Sets or returns a boolean value that specifies the document type for identifying an invoice document. Field name: DocNumType.
  - remarks: Default value is: bpdt_DocNum, which identifies the invoice by its number.
- `Public Property DocumentType() As BankStatementDocTypeEnum` [R] Returns a value specifying the document type of the bank statement draft. Field name: ObjCrtType.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date in a bank statement row. Field name: DueDate.
- `Public Property ExchangeRate() As Double` [R/W] Sets or returns the exchange rate for foreign currency. Field name: ExchngRate.
- `Public Property ExternalBankStatementNo() As Long` [R] Sets or returns the number of the bank statement. Field name: IdNumber.
  - remarks: The StatementNumber property (together with CardCode, CardName, ExternalCode, InvoiceNumber, and PaymentCreated) enable to create a receipt that matches to the invoice. If the value of PaymentCreated property is set to Yes and the payment creation succeeds, the property type is changed to Read Only.
- `Public Property ExternalCode() As String` [R/W] Sets or returns the external code. Field name: ExternCode. Length: 30 characters.
  - remarks: The ExternalCode property (together with CardName, CardCode, StatementNumber, InvoiceNumber, PaymentCreated, and VisualOrder) enable to create a receipt that matches to the invoice. If the value of PaymentCreated property is set to Yes and the payment creation succeeds, the property type is changed to Read Only.
- `Public Property FeeDistributionRule() As String` [R/W] The distribution rule of the bank statement fee. Field name: FeeProfitC.
- `Public Property FeeDistributionRule2() As String` [R/W] The multiple distribution rule of the bank statement fee. Field name: FeeProfit2.
- `Public Property FeeDistributionRule3() As String` [R/W] The multiple distribution rule of the bank statement fee. Field name: FeeProfit3.
- `Public Property FeeDistributionRule4() As String` [R/W] The multiple distribution rule of the bank statement fee. Field name: FeeProfit4.
- `Public Property FeeDistributionRule5() As String` [R/W] The multiple distribution rule of the bank statement fee. Field name: FeeProfit5.
- `Public Property FeeOnTheLine() As Double` [R/W] Sets or returns the fee amount on the statement. Field name: Fee.
- `Public Property FeeProfitCenter() As String` [R] Returns the profit center of the bank statement fee. Field name: FeeProfitC.
- `Public Property FeeProject() As String` [R] Returns the project to which the fee is associated. Field name: FeeProj.
- `Public Property FolioNumber() As Long` [R/W] property FolioNumber
- `Public Property FolioPrefixString() As String` [R/W] property FolioPrefixString
- `Public Property GLAccountforFee() As String` [R] Returns the account for the fee. Field name: FeeAct.
- `Public Property IBANofBPBankAccount() As String` [R/W] Sets or returns the IBAN number of the business partner bank account. Field name: BPIBAN.
- `Public Property InternalBankOpCode() As Long` [R] Returns the bank code in SAP Business One associated with the external bank code specified in BankStatementRow.ExternalCode. Field name: InOpCode.
  - remarks: External bank codes are associated with internal codes during company setup in Setup > Banking > Bank Statement Processing.
- `Public Property JournalEntryID() As Long` [R] Returns the ID number of the bank statement journal entry. Field name: JDTID.
- `Public Property MultiplePayments() As MultiplePayments` [R] Returns reference to multiple payments properties set to the bank statement line.
- `Public Property PaymentID() As Long` [R] Returns the ID number of the bank statement payment.
- `Public Property PaymentReferenceNo() As String` [R/W] Sets or returns the payment reference that authorizes the payment process (according to the legal requirements). Field name: PaymentRef. Length: 27 characters.
- `Public Property PostingMethod() As PostingMethodEnum` [R] Returns a value that specifies the posting method that the system uses to create transactions after they are identified by their internal code. Field name: PstMethod.
- `Public Property ReconciliationNo() As Long` [R] Returns the statement reconciliation number. Field name: BankMatch.
- `Public Property Reference() As String` [R/W] Sets or returns the reference number in the bank statement row. Length: 8 characters. Field name: PaymentRef.
- `Public Property RowStatus() As String` [R] Returns the bank statement row status.
- `Public Property SequenceNo() As Long` [R] Returns the sequential number used, together with AccountCode, for identifying the bank account. Field name: Sequence.
- `Public Property Source() As BankStatementRowSourceEnum` [R] property Source
- `Public Property StatementNumber() As Long` [R] Sets or returns the number of the bank statement. Field name: StatemNo.
- `Public Property UserFields() As Fields` [R] property UserFields
- `Public Property VATAmountFC() As Double` [R/W] Sets or returns the amount of VAT in foreign currency. Field name: VatAmntFC.
- `Public Property VATAmountLC() As Double` [R/W] Sets or returns the amount of VAT in local currency. Field name: VatAmntLC
- `Public Property VisualOrder() As Long` [R/W] Sets or returns the appearance order of the bank statement line. Field name: VisOrder.
  - remarks: By default, the visual order number equals to the Sequence number. To add a row between exiting rows, set the VisualOrder value to the required row number and call the Add method.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BankStatementRows (Collection)

A data collection of BankStatementRow objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As BankStatementRow` Adds a new BankStatementRow object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As BankStatementRow` Returns reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub Remove(ByVal vtIndex As Variant)` Deletes the specified record from the data collection.
  - param `vtIndex`: Specifies the index of the record. Specifies the index of the record.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# BankStatements (Collection)

A data collection of BankStatement objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BankStatement` Adds a new BankStatement object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As BankStatement` Returns reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# BankStatementsFilter (Object)

This object fefines filtering properties for GetBankStatementList

## Properties (3)
- `Public Property Account() As String` [R/W] Sets or returns the account name for which you want to get bank statements.
- `Public Property Bank() As String` [R/W] Sets or returns the bank from which you want to get bank statements.
- `Public Property Country() As String` [R/W] Sets or returns the country for which you want to get bank statements.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BankStatementsImportFile (Object)

This object defines the properties of the external file you want to import in BankStatementFromFile.

## Properties (4)
- `Public Property Account() As String` [R/W] Sets or returns the account namde for the imported file.
- `Public Property Bank() As String` [R/W] Sets or returns the bank name for the imported file.
- `Public Property Country() As String` [R/W] Sets or returns the country for the imported file.
- `Public Property FileName() As String` [R/W] Sets or returns the imported file name.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BankStatementsParams (Collection)

A data collection of BankStatementParams.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of bank statements in the collection.

## Methods (5)
- `Public Function Add() As BankStatementParams` Adds a BankStatementParams object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As BankStatementParams` Returns a reference to a specified BankStatementParams object in the collection.
  - param `vtIndex`: Specifies the index of the object you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BankStatementsService (Object)

This service manages bank statements drafts that can be posted in SAP Business One. The service lets you add, update, delete, get, and get list of bank statements. Source tables: OBNH, OBNK, BNK1.

**Remarks:** Country-specific: Austria, Belgium, Czech Republic, Germany, Denmark, Finland, France, Netherlands, Norway, and Sweden. In new 2006 A installations, the BankStatements service is activated by default. When upgrading to 2006 A, the service is disabled. To activate it: in Administration > System Initialization > Company Details, choose the Basic Initialization tab and select Install Bank Statement Process. You will not be able to use thise service if it is not activated. When the BankStatement service is activated, you can use both this service and the BankPages object (without account that are in the accounts list of House Bank).

## Methods (8)
- `Public Function AddBankStatement(ByVal pIBankStatement As BankStatement) As BankStatementParams` Adds a bank statement row.
  - param `pIBankStatement`: Specifies the properties of the bank statement you want to add.
  - remarks: The bank statement is added as a draft document.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Sub AddBankStatement()

            Dim oBnkStSrv As SAPbobsCOM.BankStatementsService

            Dim oCmpSrv As SAPbobsCOM.CompanyService

            Dim oBankStatement As SAPbobsCOM.BankStatement

            Dim oBnkStRow As SAPbobsCOM.BankStatementRow

            Dim MultiPayment As SAPbobsCOM.MultiplePayment

            oCmpSrv = oCompany.GetCompanyService ' Assume oCompany is the DI company Object

            'Get Bank Statement Service

            oBnkStSrv = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.BankStatementsService)

            oBankStatement = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatement)

            oBankStatement.BankAccountKey = 1

            'Add Row to Bank Statement

            oBnkStRow = oBankStatement.BankStatementRows.Add()

            oBnkStRow.ExternalCode = "E1"

            'Add Payment to Bank Statement row

            MultiPayment = oBnkStRow.MultiplePayments.Add()

            MultiPayment.AmountFC = 20

            MultiPayment.IsDebit = SAPbobsCOM.BoYesNoEnum.tYES

            'Add Bank Statement

            oBnkStSrv.AddBankStatement(oBankStatement)

    End Sub
    ```
- `Public Sub DeleteBankStatement(ByVal pIBankStatementParams As BankStatementParams)` Deletes the specified bank statement row.
  - param `pIBankStatementParams`: Specifies the number of the statement you want to delet.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub DeleteBankStatement()

            Dim oBnkStSrv As SAPbobsCOM.BankStatementsService

            Dim oCmpSrv As SAPbobsCOM.CompanyService

            Dim oBankStmParm As SAPbobsCOM.BankStatementParams

            oCmpSrv = oCompany.GetCompanyService ' Assume oCompany is the DI company Object

            'Get Bank Statement Service

            oBnkStSrv = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.BankStatementsService)

            oBankStmParm = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatementParams)

            oBankStmParm.InternalNumber = 2

            'Delete Bank Statement

            oBnkStSrv.DeleteBankStatement(oBankStmParm)

    End Sub
    ```
- `Public Function GetBankStatement(ByVal pIBankStatementParams As BankStatementParams) As BankStatement` Returns an instance of BankStatement object according to the specified number.
  - param `pIBankStatementParams`: Specifies the number of the statement you want to get.
- `Public Function GetBankStatementList(ByVal pIBankStatementsFilter As BankStatementsFilter) As BankStatementsParams` Returns a collection of bank statement rows by a specified filter. The filter is defined in BankStatementsFilter object.
  - param `pIBankStatementsFilter`: Specifies a filter to the bank statements you want to get.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub GetBankStatementList()

            Dim oBnkStSrv As SAPbobsCOM.BankStatementsService

            Dim oCmpSrv As SAPbobsCOM.CompanyService

            Dim Filter As SAPbobsCOM.IBankStatementsFilter

            Dim Params As SAPbobsCOM.IBankStatementsParams

            oCmpSrv = oCompany.GetCompanyService ' Assume oCompany is the DI company Object

            'Get Bank Statement Service

            oBnkStSrv = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.BankStatementsService)

            'Set Bank Statement Filter

            Filter = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatementsFilter)

            Filter.Bank = "10000000"

            Filter.Account = "111"

            Filter.Country = "DE"

            Params = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatementsParams)

            'Get Bank Statement List

            Params = oBnkStSrv.GetBankStatementList(Filter)

    End Sub
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As BankStatementsServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BankStatementsServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - example note: Shows how to get an Openning Balance Account from an XML file.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As CompanyService

    Dim oAccountsService As AccountsService

    Dim oOpenBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oOpenBalanceAccountFrmFile As SAPbobsCOM.OpenningBalanceAccount

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oAccountsService = oCmpSrv.GetBusinessService(ServiceTypes.AccountsService)

    'get OpenBalanceAccount Data Interface

    oOpenBalanceAccount = oAccountsService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account number for the opening balance account

    oOpenBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'save data to xml file

    oOpenBalanceAccount.ToXMLFile("c:\MyAccount.xml")

    'create OpenBalanceAccount from xml file

    oOpenBalanceAccountFrmFile = oAccountsService.GetDataInterfaceFromXMLFile("c:\MyAccount.xml")
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: Specifies an XML string.
  - example note: Show to get an Openning Balance Account from an XML string.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As CompanyService

    Dim oAccountsService As AccountsService

    Dim oOpenBalanceAccount As SAPbobsCOM.OpenningBalanceAccount

    Dim oOpenBalanceAccountXmlStr As SAPbobsCOM.OpenningBalanceAccount

    Dim sOpenBalanceAccountXmlStr As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get account service

    oAccountsService = oCmpSrv.GetBusinessService(ServiceTypes.AccountsService)

    'get OpenBalanceAccount Data Interface

    oOpenBalanceAccount = oAccountsService.GetDataInterface(AccountsServiceDataInterfaces.asdiOpenningBalanceAccount)

    'set the account number for the opening balance account

    oOpenBalanceAccount.OpenBalanceAccount = "_SYS00000000078"

    'save data to xml string

    sOpenBalanceAccountXmlStr = oOpenBalanceAccount.ToXMLString

    'create OpenBalanceAccount from xml string

    oOpenBalanceAccountXmlStr = oAccountsService.GetDataInterfaceFromXMLString(sOpenBalanceAccountXmlStr)
    ```
- `Public Sub UpdateBankStatement(ByVal pIBankStatement As BankStatement)` Updates an existing bank statement.
  - param `pIBankStatement`: Specifies the properties you want to update.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Sub UpdateBankStatement()

          Dim oBnkStSrv As SAPbobsCOM.BankStatementsService

          Dim oCmpSrv As SAPbobsCOM.CompanyService

          Dim oBankStatement As SAPbobsCOM.IBankStatement

          Dim oBankStmParm As SAPbobsCOM.BankStatementParams

          oCmpSrv = oCompany.GetCompanyService ' Assume oCompany is the DI company Object

          'Get Bank Statement Service

          oBnkStSrv = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.BankStatementsService)

          oBankStmParm = oBnkStSrv.GetDataInterface(SAPbobsCOM.BankStatementsServiceDataInterfaces.bssBankStatementParams)

          oBankStmParm.InternalNumber = 1

          'Get Bank Statement

          oBankStatement = oBnkStSrv.GetBankStatement(oBankStmParm)

          'Change the Bank Statement Currency to USD

          oBankStatement.Currency = "USD"

          'Update Bank Statement

          oBnkStSrv.UpdateBankStatement(oBankStatement)

    End Sub
    ```

# BarCode (Object)

The bar codes for your items. Multiple bar codes are allowed for each single UoM of an item. Source table: OBCD.

**Remarks:** To access the Bar Codes window, from the SAP Business One Main Menu, choose Inventory --> Bar Codes.

## Properties (5)
- `Public Property AbsEntry() As Long` [R] The key of a bar code. Field name: BcdEntry.
- `Public Property BarCode() As String` [R/W] The bar code for the UoM. Field name: BcdCode. Length: 16 characters.
- `Public Property FreeText() As String` [R/W] The descriptions. Field name: BcdName. Length: 100 characters.
- `Public Property ItemNo() As String` [R/W] The item number. Field name: ItemCode. Length: 20 characters.
- `Public Property UoMEntry() As Long` [R/W] The key of a UoM. Field name: UomEntry.

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

# BarCodeParams (Object)

Holds the key to an existing bar code. This object is used to pass keys to and retrieve keys from BarCodesService methods.

## Properties (4)
- `Public Property AbsEntry() As Long` [R/W] The key of a bar code. Field name: BcdEntry.
- `Public Property BarCode() As String` [R] The bar code for the UoM. Field name: BcdCode. Length: 16 characters.
- `Public Property ItemNo() As String` [R] The item number. Field name: ItemCode. Length: 20 characters.
- `Public Property UoMEntry() As Long` [R] The key of a UoM. Field name: UomEntry.

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

# BarCodeParamsCollection (Collection)

A collection of BarCodeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BarCodeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BarCodeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BarCodesService (Object)

The BarCodesService service enables you to add, look up, update, and remove bar codes. Source table: OBCD.

**Remarks:** To access the Bar Codes window, from the SAP Business One Main Menu, choose Inventory --> Bar Codes.

## Methods (8)
- `Public Function Add(ByVal pIBarcode As BarCode) As BarCodeParams` Adds a bar code.
  - param `pIBarcode`: The data for the new bar code.
- `Public Sub Delete(ByVal pIBarcodeParams As BarCodeParams)` Deletes an existing bar code.
  - param `pIBarcodeParams`: The key of the bar code to be deleted.
- `Public Function Get(ByVal pIBarcodeParams As BarCodeParams) As BarCode` Retrieves a bar code. The bar code is specified by its key, which is contained in the BarCodeParams object passed to the method.
  - param `pIBarcodeParams`: The key of the bar code to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BarCodesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BarCodesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BarCodesServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetList() As BarCodeParamsCollection` Returns the BarCodeParamsCollection data collection that identifies all bar codes.
- `Public Sub Update(ByVal pIBarcode As BarCode)` Updates an existing bar code.
  - param `pIBarcode`: The data for the bar code to be updated. The BarCode object must contain the key of the object to be updated.

# BatchNumberDetail (Object)

The batch details for the item. Source table: OBTN, OITL, ITL1.

## Properties (13)
- `Public Property AdmissionDate() As Date` [R/W] The creation date of the batch number. Field name: InDate.
- `Public Property Batch() As String` [R] The batch number.
- `Public Property BatchAttribute1() As String` [R/W] Specify an additional value to define the batch.
- `Public Property BatchAttribute2() As String` [R/W] Specify an additional value to define the batch.
- `Public Property Details() As String` [R/W] Specify any additional free text regarding the batch. Field name: Notes. Length: 16 characters.
- `Public Property DocEntry() As Long` [R] The document entry key that identifies the batch number detail. Field name: DocEntry.
- `Public Property ExpirationDate() As Date` [R/W] The date on which the batch expires. Field name: ExpDate.
- `Public Property ItemCode() As String` [R] The number of the item. Field name: ItemCode. Length: 20 characters.
- `Public Property ItemDescription() As String` [R] The description of the item.
- `Public Property ManufacturingDate() As Date` [R/W] The date on which the item was manufactured. Field name: MnfDate.
- `Public Property Status() As BoDefaultBatchStatus` [R/W] The current batch status. Field name: Status.
- `Public Property SystemNumber() As Long` [R] The system number of the item. Field name: SysNumber.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

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

# BatchNumberDetailParams (Object)

Holds the key to the batch number details for the item. This object is used to pass keys to and retrieve keys from BatchNumberDetailsService methods.

## Properties (1)
- `Public Property DocEntry() As Long` [R/W] The document entry key that identifies the batch number detail. Field name: DocEntry.

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

# BatchNumberDetailsService (Object)

The BatchNumberDetailsService service enables you to look up and update batch details for the item. Source table: OBTN, OITL, ITL1.

**Remarks:** To open the Batch Details window, from the SAP Business One Main Menu, choose Inventory --> Item Management --> Batches --> Batch Details.

## Methods (5)
- `Public Function Get(ByVal pIBatchNumberDetailParams As BatchNumberDetailParams) As BatchNumberDetail` Retrieves the batch details for the item. The batch details is specified by its key, which is contained in the BatchNumberDetailParams object passed to the method.
  - param `pIBatchNumberDetailParams`: The key of the batch details to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BatchNumberDetailsServiceDataInterfaces) As Object` Creates an empty data structure for use with the BatchNumberDetailsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BatchNumberDetailsServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Sub Update(ByVal pIBatchNumberDetail As BatchNumberDetail)` Updates the batch details for the item.
  - param `pIBatchNumberDetail`: The data for the batch details to be updated. The BatchNumberDetail object must contain the key of the object to be updated.

# BatchNumbers (Object)

BatchNumbers is a business object that represents the batch numbers of an item in the Inventory and Production module. This object enables you to add batch numbers for a selected item row (one record per item). Source table: OBTN, OBTW, OBTQ, OITL, ITL1.

**Remarks:** Mandatory field in SAP Business One: BatchNumber. To display the form in the application: - Select Inventory --> Item Management --> Batches --> Define and Update Batch Numbers. - In the Batch No. for Receipt - Selection Criteria window, set your selection criteria and then click OK. Deallocate Batches To deallocate batches without actually remove them from the stock (based on a delivery document) is to update the Sales Order so that it has no batches defined. Note that batches allocated by Reserve Invoice cannot be deallocated. Batches allocated by Reserve Invoice can only be drawn to a Delivery or Invoice document.

## Properties (16)
- `Public Property AddmisionDate() As Date` [R/W] Sets or returns the admission date for the batch. Field name: InDate.
- `Public Property BaseLineNumber() As Long` [R/W] Sets or returns the row number in the current document. Field name: BaseNum.
- `Public Property BatchNumber() As String` [R/W] Sets or returns the batch number. The combination of the batchNumber, ItemCode, and WarehouseCode values must be unique. Field name: BatchNum. Mandatory property. Length: 32 characters.
- `Public Property Count() As Long` [R] Returns the number of records in the BatchNumbers object.
- `Public Property ExpiryDate() As Date` [R/W] Sets or returns the expiration date for the batch. Field name: ExpDate.
- `Public Property InternalSerialNumber() As String` [R/W] Sets or returns the internal serial number for the item. Length: 32 characters. Field name: IntrSerial.
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property Location() As String` [R/W] Sets or returns the location of the batch, for example, in the warehouse. Length: 100 characters. Field name: Located.
- `Public Property ManufacturerSerialNumber() As String` [R/W] Sets or returns the manufacturer's serial number for the selected item. Field name: SuppSerial. Length: 32 characters.
- `Public Property ManufacturingDate() As Date` [R/W] Sets or returns the manufacturing date for the batch. Field name: PrdDate.
- `Public Property Notes() As String` [R/W] Sets or returns a memo type string that specifies comments for the batch number. Length: 64,000 characters. Field name: Notes.
- `Public Property Quantity() As Double` [R/W] Sets or returns the quantity of items that are used to define or update batch numbers. Field name: Quantity.
- `Public Property SystemSerialNumber() As Long` [R/W] property SystemSerialNumber
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BillOfExchange (Object)

BillOfExchange is a business object that represents the Bill Of Exchange table in the Banking module. Bill Of Exchange is a commercial document used as a payment method in Spain, Portugal, Italy, France, Belgium, and Chile. Source table: OBOE.

**Remarks:** Mandatory fields in SAP Business One: BillOfExchangeDueDate and PaymentMethodCode. To display the form in the application: - Select Banking --> Bill of Exchange. - Select one of the Bill of Exchange sub-menus. The OBOE table relates to Management, Transactions lines, Receivables, Payables, and Fund. For Management or Fund, set your criteria and then click OK. Definition: A Bill of Exchange is a signed, written order prepared by one party (drawer) who instructs another party (drawee) to pay a certain sum to a third party (payee) at a due date. The Bill of Exchange is used as a method of incoming or outgoing payment with a due date, as credit for the customer or as a flexible financing tool. Process of incoming payments: - The company prepares a payment requirement to send to the vendor (status: Sent). If the vendor approves, proceed to step 2, else the payment requirement is canceled (status: Canceled). - SAP Business One generates a Bill Of Exchange (status: Generated). - The company deposits the Bill Of Exchange in the bank (status: Deposit). (Reconciliation between the Bill Of Exchange and the bank can be done.) - The bank pays the vendor (status: Paid). (Reconciliation between the Bill Of Exchange and the bank can be done.) If the payment succeeds the bank sends a payment confirmation to the company (in France only, the Bill Of Exchange status is changed to Closed). If the payment fails, the Bill Of Exchange status is changed to Failed. Note: Perform steps 1 and 2 using the BillOfExchange object. Perform steps 3 and 4 using the BillOfExchangeTransaction object. Process of outgoing payments: - The company approves the payment requirement issued by the vendor and generates a Bill Of Exchange (status: Generated). - The bank pays the vendor (status: Paid). (Reconciliation between the Bill Of Exchange and the bank can be done.) If the payment succeeds the bank sends a payment confirmation to the company (in France only, the Bill Of Exchange status is changed to Closed). If the payment fails, the Bill Of Exchange status is changed to Canceled. Note: Perform step 1 using the BillOfExchange object. Perform step 2 using the BillOfExchangeTransaction object.

## Properties (29)
- `Public Property BillOfExchangeDueDate() As Date` [R/W] Sets or returns the due date of the Bill Of Exchange. Field name: DueDate. Mandatory property.
  - remarks: In incoming payments, at the due date, the company claims the payment from the customer or asks the bank to claim it. In outgoing payments, at the due date, the company or the bank pays the payment to the vendor.
- `Public Property BillOfExchangeNo() As String` [R/W] Sets or returns the Bill Of Exchange number. Field name: BoeNum. Length: 11 characters.
  - remarks: The value of this property is received from DocNum property of the Payments object (incoming payments). If this number is already used by another Bill Of Exchange, in SAP Business One application the following error message appears: "Bill of exchange number already exists". If no value exists , in SAP Business One application the following error message appears: "Bill of exchange number does not exist ".
- `Public Property BPBankAct() As String` [R/W] Sets or returns the bank account number of the business partner. Field name: DpstAcct. Length: 50 characters.
  - remarks: For incoming payments, the value is received from DefaultAccount property of the BusinessPartners object. For outgoing payments, the value is received from the Payment Method table (OPYM) as defined in SAP Business One (the bank details should be set in SAP Business One).
- `Public Property BPBankCode() As String` [R/W] Sets or returns the bank code of the business partner. Field name: DpsBankCod. Length: 30 characters.
  - remarks: For incoming payments, the value is received from DefaultBankCode property of the BusinessPartners object. For outgoing payments, the value is received from the Payment Method table (OPYM) as defined in SAP Business One (the bank details should be set in SAP Business One).
- `Public Property BPBankCountry() As String` [R/W] Sets or returns the country code of the business partner bank account. Field name: BPBankCtr. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: For incoming payments, the value is received from BankCountry property of the BusinessPartners object. For outgoing payments, the value is received from the Payment Method table (OPYM) as defined in SAP Business One (the bank details should be set in SAP Business One). You can set any country code that is defined in the Countries table (OCRY - not exposed through the DI API).
- `Public Property ControlKey() As String` [R] Returns the bank control key of the business partner. Field name: ControlKey. Length: 2 characters.
  - remarks: The control key specifies the type of account, for example: 01 indicates Checking Account, 02 indicates Saving Account, and so on.
- `Public Property Details() As String` [R/W] Not used.
- `Public Property DiscountAmount() As Double` [R/W] property DiscountAmount
- `Public Property DiscountDate() As Date` [R/W] property DiscountDate
- `Public Property FineAmount() As Double` [R/W] property FineAmount
- `Public Property FineDate() As Date` [R/W] property FineDate
- `Public Property FolioNumber() As Long` [R/W] Sets or returns the additional number for a bill-of-exchange document. Country-specific field for Chile. Field name: FolioNum).
  - remarks: For Incoming Payments: the Folio number assigned to the bill of exchange after it was printed, the user can not change this data. For bill of exchange that is not yet printed this field is empty and not editable. For Outgoing Payments: the user specifies the Folio number for the outgoing bill of exchange. After the Outgoing Payment is added, the user can not change this field. If the user hasn't assigned the Folio number before adding the Outgoing Payment, the user can assign it by using the Folio Number Assignment function, after printing the document.
- `Public Property FolioPrefixString() As String` [R/W] Sets or returns the prefix string for the FolioNumber. Field name: FolioPref. Length: 2 characters.
- `Public Property InterestAmount() As Double` [R/W] property InterestAmount
- `Public Property InterestDate() As Date` [R/W] property InterestDate
- `Public Property IOFAmount() As Double` [R/W] property IOFAmount
- `Public Property LastPageFolioNumber() As Long` [R] Folio number of the last page of the marketing document in the Chile localization. Field name: LPgFolioN.
- `Public Property OtherExpensesAmount() As Double` [R/W] property OtherExpensesAmount
- `Public Property OtherIncomesAmount() As Double` [R/W] property OtherIncomesAmount
- `Public Property PaymentEngineStatus1() As String` [R/W] Sets or returns the status no. 1 of the Bill Of Exchange used in the Payment Engine add-on. Field name: PayEngSt1. Length: 1 character.
- `Public Property PaymentEngineStatus2() As String` [R/W] Sets or returns the status no. 2 of the Bill Of Exchange used in the Payment Engine add-on. Field name: PayEngSt2. Length: 1 character.
- `Public Property PaymentEngineStatus3() As String` [R/W] Sets or returns the status no. 3 of the Bill Of Exchange used in the Payment Engine add-on. Field name: PayEngSt3. Length: 3 characters.
- `Public Property PaymentMethodCode() As String` [R/W] Sets or returns the Payment Method Code as defined in SAP Business One. Field name: PayMethCod. Mandatory property. Length: 15 characters.
  - remarks: The payment method is set in OPYM table and includes, for each Payment Method Code, details such as payment type (incoming or outgoing), means of payment (check, bank transfer, or bill of exchange), and various options and restrictions.
- `Public Property ReferenceNo() As String` [R/W] Sets or returns the reference number for the Bill Of Exchange. Field name: RefNum. Length: 254 characters.
- `Public Property Remarks() As String` [R/W] Sets or returns the for the Bill Of Exchange. Field name: Comments. Length: 254 characters.
- `Public Property ServiceFeeAmount() As Double` [R/W] property ServiceFeeAmount
- `Public Property StampTaxAmount() As Double` [R/W] Sets or returns the amount of stamp tax required for the Bill Off Exchange approval. Field name: tmpTxAmnt. Field name: PayEngSt2.
- `Public Property StampTaxCode() As String` [R/W] Sets or returns the Stamp Tax code. Field name: StampTax. Length: 8 Characters. Field name: StampTax. This is a foreign key to the VatGroups Object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

# BillOfExchangeTrans_BankPages (Object)

For internal use.

## Properties (3)
- `Public Property AccountCode() As String` [R/W] For internal use.
- `Public Property Sequence() As Long` [R/W] For internal use.
- `Public Property UserFields() As UserFields` [R] For internal use.

# BillOfExchangeTrans_Deposits (Object)

BillOfExchangeTrans_Deposits is a child object of the BillOfExchangeTransaction object and represents the deposits information for incoming payments. Source table: ODPS.

**Remarks:** Mandatory fields is SAP Business One: BankAccount (bank code), BankCountry, and BankDepositAccount. To display the form in the application: - Select Banking --> Bill of Exchange. - Select one of the Bill of Exchange sub-menus Management or Fund. Set your criteria and then click OK. The ODPS table also relates to Banking --> Deposits --> Deposit --> Bill of Exchange tab.

## Properties (7)
- `Public Property BankAccount() As String` [R/W] Sets or returns the bank code of the house bank for deposits. Field name: BanckAcct. Mandatory field is SAP Business One. Length: 30 characters.
- `Public Property BankBranch() As String` [R/W] Sets or returns the branch number of the house bank for deposits. Field name: DeposBrnch. Length: 50 characters.
- `Public Property BankCountry() As String` [R/W] Sets or returns the country of the of the house bank for deposits. Field name: BankCountr. Mandatory field is SAP Business One. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property BankDepositAccount() As String` [R/W] Sets or returns the account number of the house bank for deposits. Field name: BanckAcct. Mandatory field is SAP Business One. Length: 50 characters.
- `Public Property DepositNorm() As String` [R/W] Sets or returns the file format for presentation as defined for the banks for each country. Field name: DepostNorm. Length: 8 characters.
  - remarks: The file format for presentation in each country is as follows: - Italy: ABI-specification for CBI formats. - Spain: CSB 58, CSB 19, and CSB 32. - Portugal: PS2. - France: AFB .
- `Public Property PostingType() As BoDepositPostingTypes` [R/W] Sets or returns a valid value of BoDepositPostingTypes type that specifies the posting type for the deposit transaction (at the due date or before the due date). Field name: FinncPriod.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

# BillOfExchangeTransaction (Object)

BillOfExchangeTransaction is a business object that represents the Bill Of Exchange Transaction table in the Banking module. Bill Of Exchange is a commercial document used as a payment method in Spain, Portugal, Italy, and France. Use this object for Bill Of Exchange documents that their status was changed to Generated. Each status change of a Bill-of-exchange creates a transaction. This object enables you to: - Add a Bill Of Exchange Transaction. - Retrieve a Bill Of Exchange Transaction. - Save the Bill Of Exchange Transaction in XML format. Source table: OBOT.

**Remarks:** Mandatory fields is SAP Business One: StatusFrom and StatusTo. To display the form in the application: - Select Banking --> Bill of Exchange --> Bill of Exchange Transactions.

## Properties (14)
- `Public Property BankPages() As BillOfExchangeTrans_BankPages` [R] Returns the BillOfExchangeTrans_BankPages object.
- `Public Property BOETransactionkey() As Long` [R] Returns the unique ID of the bill-of-exchange transaction (primary key). SAP Business One assigns a sequential number when adding a bill-of-exchange transaction. Field name: AbsEntry.
- `Public Property Browser() As DataBrowser` [R] returns the DataBrowser object.
- `Public Property Deposits() As BillOfExchangeTrans_Deposits` [R] Returns the BillOfExchangeTrans_Deposits object.
- `Public Property IsBoeReconciled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the Bill Of Exchange is reconciled. Field name: Reconciled.
  - remarks: Applies to a Bill Of Exchange with a status Deposit or Paid only.
- `Public Property Lines() As BillOfExchangeTransaction_Lines` [R] Returns the BillOfExchangeTransaction_Lines object.
- `Public Property PostingDate() As Date` [R/W] Sets or returns the posting date of the Bill Of Exchange transaction. Field name: PostDate.
- `Public Property StatusFrom() As BoBOTFromStatus` [R/W] Sets or returns a valid value of BoBOTFromStatus type that specifies the current status of the Bill Of Exchange. Mandatory field is SAP Business One. Field name: StatusFrom.
  - remarks: For example, you can use this property to change the status of the Bill Of Exchange from (StatusFrom) Generated to (StatusTo) Deposit.
- `Public Property StatusTo() As BoBOTToStatus` [R/W] Sets or returns a valid value of BoBOTToStatus type that specifies the required status of the Bill Of Exchange. Mandatory field is SAP Business One. Field name: StatusTo.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TransactionDate() As Date` [R] Sets or returns the transaction date. Field name: TranDate.
- `Public Property TransactionNumber() As Long` [R] Returns the transaction code that SAP Business One creates for the Bill Of Exchange. Field name: TransId. This is a foreign key to the JournalEntries object.
- `Public Property TransactionTime() As Date` [R] Returns the transaction time. Field name: TranTime.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (5)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal InternalKey As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `InternalKey`: Specifies an internal key identifier (read only) of a bill of exchange transaction that is provided by the system and used as a reference for other documents in the system.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
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

# BillOfExchangeTransaction_Lines (Object)

BillOfExchangeTransaction_Lines is a child object of the BillOfExchangeTransaction object, and represents the line entries of the Bill Of Exchange Transaction. This object enables you to add a line entry to the Bill Of Exchange Transaction table. Source table: BOT1.

**Remarks:** Mandatory fields in SAP Business One: BillOfExchangeNo and BillOfExchangeType.

## Properties (5)
- `Public Property BillOfExchangeDueDate() As Date` [R] Returns the due date of Bill Of Exchange on which the payment transaction will occur. Field name: DueDate.
- `Public Property BillOfExchangeNo() As Long` [R/W] Sets or returns the Bill Of Exchange number as defined in SAP Business One. Field name: BOENumber. Mandatory field is SAP Business One.
- `Public Property BillOfExchangeType() As BoBOETypes` [R/W] Sets or returns a valid value of BoBOETypes type that specifies the Bill Of Exchange type: incoming or outgoing. Mandatory field is SAP Business One.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# BinLocation (Object)

A bin location is the smallest addressable unit of space in a warehouse where your goods are stored. To facilitate bin location management, SAP Business One lets you maintain a master data record for each bin location. Source table: OBIN.

## Properties (41)
- `Public Property AbsEntry() As Long` [R] The key of the bin location. Field name: AbsEntry.
- `Public Property AlternativeSortCode() As String` [R/W] The alternative sort code for the bin location. Field name: AltSortCod. Length: 50 characters.
- `Public Property Attribute1() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr1Val. Length: 20 characters.
- `Public Property Attribute10() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr10Val. Length: 20 characters.
- `Public Property Attribute2() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr2Val. Length: 20 characters.
- `Public Property Attribute3() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr3Val. Length: 20 characters.
- `Public Property Attribute4() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr4Val. Length: 20 characters.
- `Public Property Attribute5() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr5Val. Length: 20 characters.
- `Public Property Attribute6() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr6Val. Length: 20 characters.
- `Public Property Attribute7() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr7Val. Length: 20 characters.
- `Public Property Attribute8() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr8Val. Length: 20 characters.
- `Public Property Attribute9() As String` [R/W] The attribute that are relevant to the bin location. Field name: Attr9Val. Length: 20 characters.
- `Public Property BarCode() As String` [R/W] The bar code for the bin location. Field name: BarCode. Length: 100 characters.
- `Public Property BatchRestrictions() As BinRestrictionBatchEnum` [R/W] The batch restriction status of the bin location. Field name: SngBatch.
- `Public Property BinCode() As String` [R] The code of the bin location. Field name: BinCode. Length: 228 characters.
- `Public Property DateRestrictionChanged() As Date` [R] The last date on which you updated the transaction restrictions of the bin location. Field name: RtrictDate.
- `Public Property Description() As String` [R/W] The description of the bin location. Field name: Descr. Length: 50 characters.
- `Public Property ExcludeAutoAllocOnIssue() As BoYesNoEnum` [R/W] property ExcludeAutoAllocOnIssue
- `Public Property Inactive() As BoYesNoEnum` [R/W] Indicates whether to deactivate the bin location. Field name: Disabled.
- `Public Property IsSystemBin() As BoYesNoEnum` [R] Indicates whether the bin location is the system bin location. Field name: SysBin.
- `Public Property MaximumQty() As Double` [R/W] The maximum quantity of items for the bin location. Field name: MaxLevel.
- `Public Property MaximumWeight() As Double` [R/W] property MaximumWeight
- `Public Property MaximumWeight1() As Double` [R/W] property MaximumWeight1
- `Public Property MaximumWeightUnit() As Long` [R/W] property MaximumWeightUnit
- `Public Property MaximumWeightUnit1() As Long` [R/W] property MaximumWeightUnit1
- `Public Property MinimumQty() As Double` [R/W] The minimum quantity of items for the bin location. Field name: MinLevel.
- `Public Property ReceivingBinLocation() As BoYesNoEnum` [R/W] Indicates whether the bin location is a receiving bin location. Field name: ReceiveBin.
- `Public Property RestrictedItemType() As BinRestrictItemEnum` [R/W] The item restriction status of the bin location. Field name: ItmRtrictT.
- `Public Property RestrictedTransType() As BinRestrictTransactionEnum` [R/W] The transaction restriction status of the bin location. Field name: RtrictType.
- `Public Property RestrictedUoMType() As BinRestrictUoMEnum` [R/W] property RestrictedUoMType
- `Public Property RestrictionReason() As String` [R/W] The reason for the transaction restrictions of the bin location. Field name: RtrictResn. Length: 254 characters.
- `Public Property SpecificItem() As String` [R/W] The specific item code. Field name: SpcItmCode. Length: 20 characters.
- `Public Property SpecificItemGroup() As Long` [R/W] The specific item group. Field name: SpcItmGrpC.
- `Public Property SpecificUoM() As Long` [R/W] property SpecificUoM
- `Public Property SpecificUoMGroup() As Long` [R/W] property SpecificUoMGroup
- `Public Property Sublevel1() As String` [R/W] The sublevel codes that represent the physical location of the bin. Field name: SL1Code. Length: 50 characters.
- `Public Property Sublevel2() As String` [R/W] The sublevel codes that represent the physical location of the bin. Field name: SL2Code. Length: 50 characters.
- `Public Property Sublevel3() As String` [R/W] The sublevel codes that represent the physical location of the bin. Field name: SL3Code. Length: 50 characters.
- `Public Property Sublevel4() As String` [R/W] The sublevel codes that represent the physical location of the bin. Field name: SL4Code. Length: 50 characters.
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property Warehouse() As String` [R/W] The warehouse where the bin is located. Field name: WhsCode. Length: 8 characters.

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

# BinLocationAttribute (Object)

You can set up different codes for each bin location attribute. Source table: OBAT.

## Properties (3)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Attribute() As Long` [R/W] The bin location attribute for which you want to define codes. Field name: FldAbs.
- `Public Property Code() As String` [R/W] The code for the bin location attribute. Field name: AttrValue. Length: 20 characters.

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

# BinLocationAttributeCollectionParams (Collection)

A collection of BinLocationAttributeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BinLocationAttributeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BinLocationAttributeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BinLocationAttributeParams (Object)

Holds the key to an existing bin location attribute code. This object is used to pass keys to and retrieve keys from BinLocationAttributesService methods.

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property Attribute() As Long` [R/W] The bin location attribute for which you want to define codes. Field name: FldAbs.
- `Public Property Code() As String` [R/W] The code for the bin location attribute. Field name: AttrValue. Length: 20 characters.

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

# BinLocationAttributesService (Object)

The BinLocationAttributesService service enables you to add, look up, update, and remove bin location attributes codes. Source table: OBAT.

**Remarks:** To access the Bin Location Attribute Codes - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Bin Locations --> Bin Location Attribute Codes.

## Methods (8)
- `Public Function Add(ByVal pIBinLocationAttribute As BinLocationAttribute) As BinLocationAttributeParams` Adds a bin location attribute code.
  - param `pIBinLocationAttribute`: The data for the new bin location attribute code.
- `Public Sub Delete(ByVal pIBinLocationAttributeParams As BinLocationAttributeParams)` Deletes an existing bin location attribute code.
  - param `pIBinLocationAttributeParams`: The key of the bin location attribute code to be deleted.
- `Public Function Get(ByVal pIBinLocationAttributeParams As BinLocationAttributeParams) As BinLocationAttribute` Retrieves a bin location attribute code. The bin location attribute code is specified by its key, which is contained in the BinLocationAttributeParams object passed to the method.
  - param `pIBinLocationAttributeParams`: The key of the bin location attribute code to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BinLocationAttributesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BinLocationAttributesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BinLocationAttributesServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetList() As BinLocationAttributeCollectionParams` Returns the BinLocationAttributeCollectionParams data collection that identifies all bin location attribute codes.
- `Public Sub Update(ByVal pIBinLocationAttribute As BinLocationAttribute)` Updates an existing bin location attribute code.
  - param `pIBinLocationAttribute`: The data for the bin location attribute code to be updated. The BinLocationAttribute object must contain the key of the object to be updated.

# BinLocationCollectionParams (Collection)

A collection of BinLocationParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BinLocationParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BinLocationParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BinLocationField (Object)

The bin location field you can specify and activate. Warehouse sublevels – The smaller units of space in a warehouse. SAP Business One lets you define up to 4 warehouse sssssssssublevels Bin location attributes – The attributes you maintain for your bin locations. SAP Business One lets you define up to 10 bin location attribute. Source table: OBFC.

## Properties (6)
- `Public Property AbsEntry() As Long` [R] The key of the bin location field. Field name: AbsEntry.
  - remarks: Values in range [1, 4] mean warehouse sublevel; [5, 14] mean bin attributes.
- `Public Property Activated() As BoYesNoEnum` [R/W] Indicates whether the bin location field is activated. Field name: Activated.
- `Public Property DefaultFieldName() As String` [R] The default name of the bin location field. Field name: DftName. Length: 20 characters.
  - remarks: When you input empty string for Name, the Name will be filled with DefaultFieldName automatically.
- `Public Property FieldNumber() As Long` [R] The number of the bin location field. Field name: FldNum.
- `Public Property FieldType() As BinLocationFieldTypeEnum` [R] The type of the bin location field. Field name: FldType.
- `Public Property Name() As String` [R/W] The name of the bin location field. Field name: DispName. Length: 20 characters.

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

# BinLocationFieldCollectionParams (Collection)

A collection of BinLocationFieldParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BinLocationFieldParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BinLocationFieldParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BinLocationFieldParams (Object)

Holds the key to an existing bin location field. This object is used to pass keys to and retrieve keys from BinLocationFieldsService methods.

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] The key of the bin location field. Field name: AbsEntry.

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

# BinLocationFieldsService (Object)

The BinLocationFieldsService service enables you to look up and update bin location fields. Source table: OBFC.

**Remarks:** To open the Bin Location Field Activation window, from the SAP Business One Main Menu, choose Administration -> Setup -> Inventory -> Bin Locations -> Bin Location Field Activation.

## Methods (6)
- `Public Function Get(ByVal pIBinLocationFieldParams As BinLocationFieldParams) As BinLocationField` Retrieves a bin location field. The bin location field is specified by its key, which is contained in the BinLocationFieldParams object passed to the method.
  - param `pIBinLocationFieldParams`: The key of the bin location field to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BinLocationFieldsServiceDataInterfaces) As Object` Creates an empty data structure for use with the BinLocationFieldsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BinLocationFieldsServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetList() As BinLocationFieldCollectionParams` Returns the BinLocationFieldCollectionParams data collection that identifies all bin location fields.
- `Public Sub Update(ByVal pIBinLocationField As BinLocationField)` Updates an existing bin location field.
  - param `pIBinLocationField`: The data for the bin location field to be updated. The BinLocationField object must contain the key of the object to be updated.

# BinLocationParams (Object)

Holds the key to an existing bin location. This object is used to pass keys to and retrieve keys from BinLocationsService methods.

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] The key of the bin location. Field name: AbsEntry.
- `Public Property BinCode() As String` [R/W] The code of the bin location. Field name: BinCode. Length: 228 characters.

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

# BinLocationsService (Object)

The BinLocationsService service enables you to add, look up, update, and remove bin locations. Source table: OBIN.

**Remarks:** To access the Bin Location Master Data window, from the SAP Business One Main Menu, choose Inventory --> Bin Locations --> Bin Location Master Data.

## Methods (8)
- `Public Function Add(ByVal pIBinLocation As BinLocation) As BinLocationParams` Adds a bin location.
  - param `pIBinLocation`: The data for the new bin location.
- `Public Sub Delete(ByVal pIBinLocationParams As BinLocationParams)` Deletes an existing bin location.
  - param `pIBinLocationParams`: The key of the bin location to be deleted.
- `Public Function Get(ByVal pIBinLocationParams As BinLocationParams) As BinLocation` Retrieves a bin location. The bin location is specified by its key, which is contained in the BinLocationParams object passed to the method.
  - param `pIBinLocationParams`: The key of the bin location to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BinLocationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the BinLocationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BinLocationsServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetList() As BinLocationCollectionParams` Returns the BinLocationCollectionParams data collection that identifies all bin locations.
- `Public Sub Update(ByVal pIBinLocation As BinLocation)` Updates an existing bin location.
  - param `pIBinLocation`: The data for the bin location to be updated. The BinLocation object must contain the key of the object to be updated.

# BlanketAgreement (Object)

A blanket agreement is a longer-term arrangement between a purchasing organization and a vendor, or a sales organization and a customer, for the supply of items or provision of services over a period of time based on predefined terms and conditions. If an approved and valid blanket agreement exists with a customer or vendor, SAP Business One automatically links sales and purchasing documents with the blanket agreement. As such, the prices agreed on with the business partners are automatically copied into the sales and purchasing document. You can also choose to remove the link and create a sales or purchasing document that is not governed by a blanket agreement. Source table: OOAT.

## Properties (37)
- `Public Property AgreementMethod() As BlanketAgreementMethodEnum` [R/W] property AgreementMethod
- `Public Property AgreementNo() As Long` [R] Sequential number of the agreement that is assigned automatically by SAP Business One. Field name: AbsID.
- `Public Property AgreementType() As BlanketAgreementTypeEnum` [R/W] The type (category) of the agreement you have made with your business partner. Field name: Type.
- `Public Property AmendmentTo() As Long` [R/W] property AmendmentTo
- `Public Property AttachmentEntry() As Long` [R/W] The file path of the agreement document that you want to attach to the blanket agreement. Field name: AtchEntry. Length: 11 characters.
- `Public Property BlanketAgreements_ItemsLines() As BlanketAgreements_ItemsLines` [R] The items that can be purchased or sold within the scope of the blanket agreement.
- `Public Property BPCode() As String` [R/W] Code of the business partner with whom you have made the agreement. Field name: BpCode. Length: 15 characters.
- `Public Property BPCurrency() As String` [R/W] property BPCurrency
- `Public Property BPName() As String` [R] Name of the business partner with whom you have made the agreement. Field name: BpName.
- `Public Property ContactPersonCode() As Long` [R/W] Code of the contact person. Field name: CntctCode. Length: 11 characters.
- `Public Property Description() As String` [R/W] Descriptive text for the agreement. Field name: Descript. Length: 254 characters.
- `Public Property DocNum() As Long` [R/W] property DocNum
- `Public Property EndDate() As Date` [R/W] Date until which the agreement is effective. Field name: EndDate.
- `Public Property ExchangeRate() As Double` [R/W] property ExchangeRate
- `Public Property HandWritten() As BoYesNoEnum` [R/W] property HandWritten
- `Public Property IgnorePricesInAgreement() As BoYesNoEnum` [R] If you set this flag, any special prices that may have been defined for the business partner in price lists take precedence over the price you specify in the blanket agreement. Field name: UseDiscnt.
- `Public Property NumAtCard() As String` [R/W] property NumAtCard
- `Public Property Owner() As Long` [R/W] Name of the user who is responsible for the blanket agreement. Field name: Owner. Length: 6 characters.
- `Public Property PaymentMethod() As String` [R/W] property PaymentMethod
- `Public Property PaymentTerms() As Long` [R/W] property PaymentTerms
- `Public Property PeriodIndicator() As String` [R] property PeriodIndicator
- `Public Property PriceList() As Long` [R/W] property PriceList
- `Public Property PriceMode() As PriceModeEnum` [R/W] property PriceMode
- `Public Property Project() As String` [R/W] property Project
- `Public Property Remarks() As String` [R/W] Comments about the agreement. Field name: Remarks. Length: 16 characters.
- `Public Property RemindTime() As Long` [R/W] The number of days, weeks, or months for an alert to appear prior to the termination of the blanket agreement. Field name: RemindVal. Length: 6 characters.
- `Public Property RemindUnit() As BoRemindUnits` [R/W] The reminder time units. Field name: RemindUnit.
- `Public Property Renewal() As BoYesNoEnum` [R/W] Enables you to set a reminder for renewing a service contract before it expires. Field name: Renewal.
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property Series() As Long` [R/W] property Series
- `Public Property SettlementProbability() As Double` [R/W] The percentage value to indicate how probable it is that the business partner will pay for the goods. Field name: SettleProb.
- `Public Property ShippingType() As Long` [R/W] property ShippingType
- `Public Property SigningDate() As Date` [R/W] property SigningDate
- `Public Property StartDate() As Date` [R/W] Date on which the agreement becomes effective. Field name: StartDate.
- `Public Property Status() As BlanketAgreementStatusEnum` [R/W] The status of the blanket agreement. Field name: Status.
- `Public Property TerminateDate() As Date` [R/W] Date on which the blanket agreement ceases to be effective, if the agreement is terminated before the actual end date. The agreement status changes to Terminated. Field name: TermDate.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

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

# BlanketAgreementParams (Object)

Holds the key to an existing blanket agreement. This object is used to pass keys to and retrieve keys from BlanketAgreementsService methods.

## Properties (1)
- `Public Property AgreementNo() As Long` [R/W] Number of the agreement.

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

# BlanketAgreements_DetailsLine (Object)

BlanketAgreements_DetailsLine is a child object of the BlanketAgreements_ItemsLine object and represents the details of a delivery plan for an item. Source table: OAT2.

## Properties (14)
- `Public Property AgreementEffectiveRowNumber() As Long` [R] The effective item row number in the agreement. Field name: AgrEfctNum.
- `Public Property AgreementNo() As Long` [R] Number of the agreement. Field name: AgrNo.
- `Public Property AgreementRowNumber() As Long` [R] Item row number in the agreement. Field name: AgrLnNum.
- `Public Property ConsumeSalesForecast() As BoYesNoEnum` [R/W] Specify whether the blanket agreement will be included in the MRP run. Field name: ConsumeFCT.
- `Public Property FreeText() As String` [R/W] Reference or remarks for the item. Field name: FreeTxt. Length: 100 characters.
- `Public Property Frequency() As BlanketAgreementDatePeriodsEnum` [R/W] Cycle interval options for item shipmen. Field name: DatePeriod.
- `Public Property From() As Date` [R/W] Start date of the shipment plan, that is, the date as of which shipment starts. This date cannot be earlier than the start date of the blanket agreement. Field name: FromDate.
- `Public Property PlannedAmountFC() As Double` [R/W] property PlannedAmountFC
- `Public Property PlannedAmountLC() As Double` [R/W] property PlannedAmountLC
- `Public Property Quantity() As Double` [R/W] Number of items to be shipped during the shipping period. Field name: Quantity.
- `Public Property ReleaseInformation() As String` [R/W] Number of items delivered or invoiced in association with the blanket agreement. Field name: CallUp. Length: 100 characters.
- `Public Property To() As Date` [R/W] End date of the shipment plan, that is, the date until which shipment takes place. This date cannot be later than the end date of the blanket agreement. Field name: ToDate.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property Warehouse() As String` [R/W] Warehouse from which the item should be shipped. Field name: WhsCode. Length: 8 characters.

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

# BlanketAgreements_DetailsLines (Collection)

A collection of BlanketAgreements_DetailsLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As BlanketAgreements_DetailsLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BlanketAgreements_DetailsLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BlanketAgreements_ItemsLine (Object)

BlanketAgreements_ItemsLine is a child object of the BlanketAgreement object and represents the items that can be purchased or sold within the scope of the blanket agreement. Source table: OAT1.

## Properties (34)
- `Public Property AgreementNo() As Long` [R] Number of the agreement. Field name: AgrNo.
- `Public Property AgreementRowNumber() As Long` [R] Item row number in the agreement. Field name: AgrLineNum.
- `Public Property BlanketAgreements_DetailsLines() As BlanketAgreements_DetailsLines` [R] The details of a delivery plan for an item.
- `Public Property CumulativeAmountFC() As Double` [R] The monetary value (in foreign currency) of those items that are included in sales or purchasing transactions associated with the blanket agreement. Field name: CumAmntFC.
- `Public Property CumulativeAmountLC() As Double` [R] The monetary value (in local currency) of those items that are included in sales or purchasing transactions associated with the blanket agreement. Field name: CumAmntLC.
- `Public Property CumulativeQuantity() As Double` [R] The total number of those items that are included in sales or purchasing transactions associated with the blanket agreement. Field name: CumQty.
- `Public Property CumulativeVATAmountFC() As Double` [R] property CumulativeVATAmountFC
- `Public Property CumulativeVATAmountLC() As Double` [R] property CumulativeVATAmountLC
- `Public Property EndOfWarranty() As Date` [R/W] Date on which the warranty of the goods expires. Field name: WrrtyEnd.
- `Public Property FreeText() As String` [R/W] Reference or remarks for the item. Field name: FreeTxt. Length: 100 characters.
- `Public Property InventoryUOM() As String` [R] Type of unit by which the inventory is managed as defined in the item master data. Field name: InvntryUom.
- `Public Property ItemDescription() As String` [R/W] Item description as maintained in the item master data. Field name: ItemName. Length: 100 characters.
- `Public Property ItemGroup() As Long` [R] Item group as maintained in the item master data. Field name: ItemGroup.
- `Public Property ItemNo() As String` [R/W] Number of the item that is covered by the blanket agreement. Field name: ItemCode. Length: 20 characters.
- `Public Property LineDiscount() As Double` [R/W] property LineDiscount
- `Public Property PlannedAmountFC() As Double` [R/W] property PlannedAmountFC
- `Public Property PlannedAmountLC() As Double` [R/W] property PlannedAmountLC
- `Public Property PlannedQuantity() As Double` [R/W] Total quantity of items that are supposed to be sold or bought within the scope of the blanket agreement. Field name: PlanQty.
- `Public Property PlannedVATAmountFC() As Double` [R/W] property PlannedVATAmountFC
- `Public Property PlannedVATAmountLC() As Double` [R/W] property PlannedVATAmountLC
- `Public Property PortionOfReturns() As Double` [R/W] The percentage value for the probability that damaged goods will be returned by the business partner. Field name: RetPortion.
- `Public Property PriceCurrency() As String` [R/W] The currency of the item's price. Field name: Currency. Length: 3 characters.
- `Public Property Project() As String` [R/W] property Project
- `Public Property ShippingType() As Long` [R/W] property ShippingType
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property TaxRate() As Double` [R] property TAXRate
- `Public Property UndeliveredCumulativeAmountFC() As Double` [R] property UndeliveredCumulativeAmountFC
- `Public Property UndeliveredCumulativeAmountLC() As Double` [R] property UndeliveredCumulativeAmountLC
- `Public Property UndeliveredCumulativeQuantity() As Double` [R] property UndeliveredCumulativeQuantity
- `Public Property UnitPrice() As Double` [R/W] The item price agreed upon with the business partner. Field name: UnitPrice.
- `Public Property UnitsOfMeasurement() As Double` [R] property UnitsOfMeasurement
- `Public Property UoMCode() As String` [R] property UoMCode
- `Public Property UoMEntry() As Long` [R/W] property UoMEntry
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

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

# BlanketAgreements_ItemsLines (Collection)

A collection of BlanketAgreements_ItemsLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As BlanketAgreements_ItemsLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BlanketAgreements_ItemsLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BlanketAgreementsDocument (Object)

BlanketAgreementsDocument is a child object of the BlanketAgreement object and you can view the documents associated with the blanket agreement. Source table: OAT4V.

## Properties (15)
- `Public Property AgreementRowNumber() As Long` [R] Row number in the agreement. Field name: AgrLineNum.
- `Public Property Discount() As Double` [R] property Discount
- `Public Property DocStatus() As BADocumentStatus` [R] property DocStatus
- `Public Property DocumentDate() As Date` [R] The related document posting date. Field name: DocDate.
- `Public Property DocumentNo() As Long` [R] Number of the document that was created and associated with the blanket agreement. Field name: DocNo.
- `Public Property DocumentRowNumber() As Long` [R] Number of the row in the document that is associated with the blanket agreement. Field name: DocLineNum.
- `Public Property DocumentType() As BlanketAgreementDocTypeEnum` [R] Type of document that was created and associated with the blanket agreement, for example, a sales order or A/P invoice. Field name: DocType.
- `Public Property ItemDescription() As String` [R] Item description on the related document row. Field name: ItemName.
- `Public Property ItemNo() As String` [R] Item number on the related document row. Field name: ItemCode.
- `Public Property Quantity() As Double` [R] Quantity on the related document row. Field name: Quantity.
- `Public Property RowStatus() As BoStatus` [R] Row status on the related document row. Field name: RowStatus.
- `Public Property UnitPrice() As Double` [R] Price of the item in the sales or purchasing document. Field name: UnitPrice.
- `Public Property UnitsOfMeasurement() As Double` [R] property UnitsOfMeasurement
- `Public Property UoM() As String` [R] Unit of measurement on the related document row. Field name: Uom.
- `Public Property UoMCode() As String` [R] property UoMCode

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

# BlanketAgreementsDocuments (Collection)

A collection of BlanketAgreementsDocument objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BlanketAgreementsDocument` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BlanketAgreementsDocument` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BlanketAgreementsParams (Collection)

A collection of BlanketAgreementParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BlanketAgreementParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BlanketAgreementParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BlanketAgreementsService (Object)

The BlanketAgreementsService service enables you to add, look up, cancel, and update blanket agreements. Source table: OOAT.

**Remarks:** To open the blanket agreement window, choose Business Partners -> Blanket Agreement. To display the available blanket agreements, choose Business Partners -> Business Partner Reports -> Blanket Agreements List.

## Methods (9)
- `Public Function AddBlanketAgreement(ByVal pIBlanketAgreement As BlanketAgreement) As BlanketAgreementParams` Adds a blanket agreement.
  - param `pIBlanketAgreement`: The data for the new blanket agreement.
- `Public Sub CancelBlanketAgreement(ByVal pIBlanketAgreementParams As BlanketAgreementParams)` Cancels an existing blanket agreement.
  - param `pIBlanketAgreementParams`: The key of the blanket agreement to be cancelled.
- `Public Function GetBlanketAgreement(ByVal pIBlanketAgreementParams As BlanketAgreementParams) As BlanketAgreement` Retrieves a blanket agreement. The blanket agreement is specified by its key, which is contained in the BlanketAgreementParams object passed to the method.
  - param `pIBlanketAgreementParams`: The key of the blanket agreement to retrieve.
- `Public Function GetBlanketAgreementList() As BlanketAgreementsParams` Returns the BlanketAgreementsParams data collection that identifies all blanket agreements.
- `Public Function GetDataInterface(ByVal enumMSDI As BlanketAgreementsServiceDataInterfaces) As Object` Creates an empty data structure for use with the BlanketAgreementsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BlanketAgreementsServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetRelatedDocuments(ByVal pIBlanketAgreementParams As BlanketAgreementParams) As BlanketAgreementsDocuments` Retrieves the related documents of a blanket agreement.
  - param `pIBlanketAgreementParams`: The key of the blanket agreement to retrieve.
- `Public Sub UpdateBlanketAgreement(ByVal pIBlanketAgreement As BlanketAgreement)` Updates an existing blanket agreement. The data for the blanket agreement, including the key of the blanket agreement to be updated, is contained in the BlanketAgreement object passed to the method. To update a blanket agreement, you must first retrieve it using the GetBlanketAgreement method.
  - param `pIBlanketAgreement`: The key of the blanket agreement to be updated.

# Blob (Object)

Holds blob content to be added to or retrieved from a blob field in the SAP Business One database.

## Properties (1)
- `Public Property Content() As String` [R/W] Holds the blob content to be added to the SAP Business One database.

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

# BlobParams (Object)

Specifies a set of blob fields, as follows: - The Table property specifies the database table. - The Field property specifies the blob field in the database table. - The BlobTableKeySegments property specifies the records whose blob fields are to be updated or whose contents are to be retrieved. For the LoadBlobFromFile and SaveBlobToFile methods, the FileName property specifies a file to which to save the blob content or from which to retrieve the blob content. For the SetBlob and GetBlob methods, the blob content is contained in the Blob object.

## Properties (4)
- `Public Property BlobTableKeySegments() As BlobTableKeySegments` [R] The records whose blob fields are to be set or retrieved.
- `Public Property Field() As String` [R/W] The name of the blob field to be set or retrieved.
- `Public Property FileName() As String` [R/W] The name of the file to which to save the blob field or from which to retrieve the blob content.
- `Public Property Table() As String` [R/W] The name of the database table in which blob fields are to be set or retrieved, for example, RDOC.

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

# BlobTableKeySegment (Object)

Specifies the record whose blob field is to be set.

## Properties (2)
- `Public Property Name() As String` [R/W] The name of the key field of the database table specified in the parent BlobParams object.
- `Public Property Value() As String` [R/W] The key of the record whose blob field is to be set. The database table and blob field are specified in the parent BlobParams object.

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

# BlobTableKeySegments (Collection)

A collection of BlobTableKeySegment objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BlobTableKeySegment` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BlobTableKeySegment` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BOEDocumentType (Object)

A data structure object holding properties for the BOEDocumentTypesService. Source table: ODTY.

## Properties (3)
- `Public Property DocDescription() As String` [R/W] Sets or returns a string specifying the document description. Field name: DocDespt.
- `Public Property DocEntry() As Long` [R] Returns a string specifying the document entry. Field name: AbsEntry.
- `Public Property DocType() As String` [R/W] Sets or returns a string specifying the document type. Field name: DocType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEDocumentTypeParams (Object)

This object holds identification properties for the BOEDocumentTypesService object. Source table: ODTY.

## Properties (2)
- `Public Property DocEntry() As Long` [R/W] Sets or returns a string specifying the document entry. Field name: AbsEntry.
- `Public Property DocType() As String` [R] Returns a string specifying the document type. Field name: DocType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEDocumentTypes (Collection)

This is a data collection of BOEDocumentType data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total objects in the collection.

## Methods (5)
- `Public Function Add() As BOEDocumentType` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retreives the XML schema of the data structrue.
- `Public Function Item(ByVal vtIndex As Variant) As BOEDocumentType` Returns a reference to a specified object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# BOEDocumentTypesParams (Collection)

This is a data collection of BOEDocumentTypeParams data structure.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total objects in the collection.

## Methods (5)
- `Public Function Add() As BOEDocumentTypeParams` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retreives the XML schema of the data structrue.
- `Public Function Item(ByVal vtIndex As Variant) As BOEDocumentTypeParams` Returns a reference to a specified object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
