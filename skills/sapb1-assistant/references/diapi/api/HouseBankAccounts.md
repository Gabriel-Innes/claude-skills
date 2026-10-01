<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# HouseBankAccounts (Object)

The HouseBankAccounts object enables to define the company bank accounts. Source table: DSC1.

**Remarks:** Mandatory fields in SAP Business One: BankKey. To display the form in the application: - Select Administration -->Setup -->Banking -->House Bank Accounts.

## Properties (64)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the house bank account as assigned by the system when adding a new entry. Field name: AbsEntry.
- `Public Property AccNo() As String` [R/W] Sets or returns the account number of the house bank. Field name: Account. Length: 50 characters.
- `Public Property AccountCheckDigit() As String` [R/W] Sets or returns the account check digit. Field name: AccountChk. Length: 1 character.
- `Public Property AccountName() As String` [R/W] The name of the bank account. Field: AcctName. Length: 250 characters.
- `Public Property AddressType() As String` [R/W] Sets or returns the address type, such as, City or Street. This property is applicable for cluster B only (country-specific for Brazil).
- `Public Property AgreementNumber() As String` [R/W] Sets or returns the agreement number. Field name: AgreeNum. Length: 4 characters.
- `Public Property BankCode() As String` [R] Returns the bank code as defined in the Banks object. Field name: BankCode. Length: 30 characters.
- `Public Property BankKey() As Long` [R/W] Sets or returns the foreign key of the bank as defined in the Banks object. Field name: BankKey. Mandatory property.
- `Public Property BankonCollection() As String` [R/W] Sets or returns the G/L account for bank on collection of bill-of-exchange transactions. Field name: BankCollec. Length: 15 characters.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property BankonDiscounted() As String` [R/W] Sets or returns the G/L account for bank on discounted bill-of-exchange transactions. Field name: BankDiscou. Length: 15 characters.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property BICSwiftCode() As String` [R/W] The BIC/SWIFT code to be used in transactions and messages between banks. Field: SwiftNum. Length: 50 characters.
  - remarks: The default BIC/SWIFT code is taken from the Banks - Setup window of the selected bank code.
- `Public Property BISR() As BoYesNoEnum` [R/W] Determines whether or not to enable printing the bank name and address on BISR invoices. Field name: BISR.
  - remarks: Country-specific for Switzerland.
- `Public Property Block() As String` [R/W] Sets or returns the block of the house bank address. Field name: Block. Length: 100 characters.
- `Public Property Branch() As String` [R/W] Sets or returns the branch of the house bank. Field name: Branch. Length: 50 characters.
- `Public Property BranchCheckDigit() As String` [R/W] property BranchCheckDigit
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Building() As String` [R/W] Sets or returns the Building/Floor/Room details of the house bank address. Field name: Building. Length: 64,000 characters.
- `Public Property City() As String` [R/W] Sets or returns the city of the house bank address. Field name: City. Length: 100 characters.
- `Public Property CollectionCode() As String` [R/W] property CollectionCode
- `Public Property ControlKey() As String` [R/W] Returns control key of the house bank. Field name: ControlKey. Length: 2 characters.
  - remarks: The control key specifies the type of account, for example: 01 indicates Checking Account, 02 indicates Saving Account, and so on. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property Country() As String` [R] Sets or returns the country code of the house bank (for example: DE). Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: You can set only country codes that are defined in the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county of the house bank address. Field name: County. Length: 100 characters. This is a foreign key to the States table (OCST - not exposed through the DI API).
- `Public Property CustomerIdNumber() As String` [R/W] Sets or returns the customer's Id number. Field name: CustIdNum.
  - remarks: This property is applicable if ISRType is set to BISR.
- `Public Property DaysInAdvance() As Long` [R/W] Sets or returns the number of days in advance. Field name: DaysInAdva.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property DebtofDiscountedBillofExc() As String` [R/W] Sets or returns the G/L account for debt of discounted bill-of-exchange transactions. Field name: DscountBOE. Length: 15 characters.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property DiscountAccount() As String` [R/W] property DiscountAccount
- `Public Property DiscountLimit() As Double` [R/W] Sets or returns the maximum discount allowed in a bill-of-exchage payment. Field name: DscntLimit.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property ECheck() As BoYesNoEnum` [R/W] Specifies whether the account is relevant for e-check functionality or not. Field name: ECheck.
- `Public Property FileSeqNextNumber() As Long` [R/W] property FileSeqNextNumber
- `Public Property FineAccount() As String` [R/W] property FineAccount
- `Public Property GLAccount() As String` [R/W] Sets or returns the G/L account number related to the house bank. This is a foreign key to ChartOfAccounts object. Field name: GLAccount. Lentgh: 15 characters.
- `Public Property GLInterimAccount() As String` [R/W] Sets or returns the G/L account number for intermidiate transactions related to the house bank. G/L accounts are defined through the ChartOfAccounts object. Field name: GLIntriAct. Lentgh: 15 characters.
- `Public Property IBAN() As String` [R/W] Sets or returns the International Bank Account Number (IBAN). Field name: IBAN. Length: 50 characters.
- `Public Property ImportFileName() As String` [R/W] Sets or returns the XML file format from which the system downloads the bank statement data of the bank account. Field name: FilePlug. Length: 50 characters.
  - remarks: To enable automatic download from the XML file format, in the application, the ImpStmt field (Imported Bank Statement) must be selected. This property is applicable only if the BankStatementInstalled property of AdminInfo object (OADM) is set to tYes.
- `Public Property IncomingPaymentSeries() As Long` [R/W] Sets or returns the numbering series to be used for incoming payment documents that are created through bank statement processing. This is a foreign key to the Series object. Field name: InSeri.
  - remarks: This property is applicable only if: - The BankStatementInstalled property of AdminInfo object (OADM) is set to tYes. - The field Permit More than One Document Type per Series (DocNmMtd of CINF) must be set to No. This field is not exposed by the DI API.
- `Public Property InterestAccount() As String` [R/W] property InterestAccount
- `Public Property IOFTaxAccount() As String` [R/W] property IOFTaxAccount
- `Public Property ISRBillerID() As String` [R/W] Sets or returns the ISRBillerId. (country-specific for Switzerland only). Field name: ISRBillerI.
- `Public Property ISRType() As Long` [R/W] Sets or returns a valid value that determines this house bank account ISR type. Country-specific for Switzerland only. Field name: ISRType.
- `Public Property JournalEntrySeries() As Long` [R/W] Sets or returns the numbering series to be used for journal entries that are posted through bank statement processing. This is a foreign key to the Series object. Field name: JDTSeri.
  - remarks: This property is applicable only if: - The BankStatementInstalled property of AdminInfo object (OADM) is set to tYes. - The field Permit More than One Document Type per Series (DocNmMtd of CINF) must be set to No. This field is not exposed by the DI API.
- `Public Property LockChecksPrinting() As BoYesNoEnum` [R/W] Determines whether or not to prevent printing checks of the same house bank account by different users simultaneously. Field name: LockChk.
- `Public Property MaxAmountofBillofExchan() As Double` [R/W] Sets or returns the maximum amount allowed in a bill-of-exchange payment. Field name: MaxAmntBOE.
  - remarks: Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property MaximumLines() As Long` [R/W] Sets or returns the maximum lines to print in the check stub. Field name: MaxChkLine.
- `Public Property MinAmountofBillofExchang() As Double` [R/W] Sets or returns the minimum amount allowed in a bill-of-exchange payment. Field name: MinAmntBOE.
  - remarks: Applicable for localizations that use Bill-of-Exchange as a payment method.
- `Public Property NextCheckNo() As Long` [R/W] Sets or returns the number for the next check. Field name: NextCheck.
- `Public Property NoValidationForStartingEndingBal() As BoYesNoEnum` [R/W] Define whether you can finalize a bank statement even if the difference does not equal zero; and whether the starting balance of your current bank statement can be different to the ending balance of the previous one. Field name: NoValidBal.
  - remarks: No - You can finalize a bank statement only when the difference equals zero; and the starting balance of your current bank statement must be the same to the ending balance of the previous one. Yes - You can finalize a bank statement even if the difference does not equal zero; and the starting balance of your current bank statement can be different to the ending balance of the previous one.
- `Public Property OtherExpensesAccount() As String` [R/W] property OtherExpensesAccount
- `Public Property OtherIncomesAccount() As String` [R/W] property OtherIncomesAccount
- `Public Property OurNumber() As Long` [R/W] Sets or returns the house bank number for Boleto method of payment. This property is applicable for cluser B (country-specific for Brazil). Field name: OurNum.
  - remarks: Boleto is a method of payment, which uses the structure and functions for bills of exchange (BOE).
- `Public Property OutgoingPaymentSeries() As Long` [R/W] Sets or returns the numbering series to be used for outgoing payment documents that are created through bank statement processing. This is a foreign key to the Series object. Field name: OutSeri.
  - remarks: This property is applicable only if: - The BankStatementInstalled property of AdminInfo object (OADM) is set to tYes. - The field Permit More than One Document Type per Series (DocNmMtd of CINF) must be set to No. This field is not exposed by the DI API.
- `Public Property PrintOn() As PrintOnEnum` [R/W] Determines the paper type and printing method of payment checks. Field name: LockChk.
  - remarks: To display the form in thwe application: - Select Administration --> System Initialization --> Print Preferences --> Per Document tab. - From the Document drop-down list, select Checks for Payment.
- `Public Property RetornoFileName() As String` [R/W] property RetornoFileName
- `Public Property ServiceFeeAccount() As String` [R/W] property ServiceFeeAccount
- `Public Property State() As String` [R/W] Sets or returns the state code of the house bank. This is a foreign key to the States table (OCST), which is not exposed through the DI API. Field name: State. Length: 3 characters.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Street() As String` [R/W] Sets or returns the street of the house bank address. Field name: Street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] Sets or returns the street number of the house bank address. This property is applicable for cluster B only (country-specific for Brazil).
- `Public Property TemplateName() As String` [R/W] Sets or returns the layout code of the checks template. The layout code is the key of the ReportLayoutParams object. Field name: TmpltName. Lentgh: 8 characters.
  - remarks: The House Bank Accounts form displays the template name such as, stub-check-stub, check-stub-stub, checks not based on invoice (US), but the TemplateName property actually contains the layout code (for example, CHO10001). The list of templates is a result of a system query that retrieves from the RDOC table all the templates that start with CHO, and then displays their names.
- `Public Property ToleranceDays() As Long` [R/W] Sets or returns the number of days earlier than the calculated due date to start expecting the bill-of-exchange payment. Field name: TolrnceDay.
  - remarks: For example: If the payment due date is October 1, and the value of ToleranceDays is 5, the payment is expected to be received starting from September 26. Applicable for localizations that use a Bill-of-Exchange as a payment method.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserNo1() As String` [R/W] Sets or returns the first number or password, defined by the user, for identifying a payment file for the specific account. Field name: UsrNumber1. Length: 25 characters.
- `Public Property UserNo2() As String` [R/W] Sets or returns the second number or password, defined by the user, for identifying a payment file for the specific account. Field name: UsrNumber2. Length: 25 characters.
- `Public Property UserNo3() As String` [R/W] Sets or returns the third number or password, defined by the user, for identifying a payment file for the specific account. Field name: UsrNumber3. Length: 25 characters.
- `Public Property UserNo4() As String` [R/W] Sets or returns the forth number or password, defined by the user, for identifying a payment file for the specific account. Field name: UsrNumber4. Length: 25 characters.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code of the house bank address. Field name: ZipCode. Length: 20 characters.

## Methods (7)
- `Public Function Add() As Long` Adds a new record of house bank accounts table.
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
