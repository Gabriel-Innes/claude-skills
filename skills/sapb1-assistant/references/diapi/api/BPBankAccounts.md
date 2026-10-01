<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPBankAccounts (Object)

BPBankAccounts is a business object that represents the bank accounts of the business partner. Source table: OCRB.

**Remarks:** To display the form in the application: - Select Business Partners --> Business Partner Master Data. - Select Payment Terms tab. - Near the Bank Country field, click the Choose icon.

## Properties (36)
- `Public Property ABARoutingNumber() As String` [R/W] The ABA routing number to identify the financial institution upon which payment was drawn. Field name: ABARoutNum. Length: 25 characters.
- `Public Property AccountName() As String` [R/W] Returns the Business partner's Account Name. Field name: AcctName. Length: 100 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property AccountNo() As String` [R/W] Sets or returns the bank account number. Field name: Account. Length: 50 characters.
- `Public Property BankCode() As String` [R/W] Sets or returns the bank code as defined in the Banks object. Field name: BankCode. Length: 30 characters.
- `Public Property BICSwiftCode() As String` [R/W] The BIC/SWIFT code to be used in transactions and messages between banks. Field name: SwiftNum. Length: 50 characters.
  - remarks: The default BIC/SWIFT code is taken from the Banks - Setup window of the selected bank code.
- `Public Property BIK() As String` [R/W] Returns the Business partner's Bank Identification Key. Field name: BIK. Length: 15 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property Block() As String` [R/W] Sets or returns the block address of the bank. Field name: Block. Length: 100 characters.
- `Public Property BPCode() As String` [R/W] Sets or returns the business partner identification code. Field name: CardCode. Length: 15 characters.
- `Public Property Branch() As String` [R/W] Sets or returns the branch number. Field name: Branch. Length: 50 characters.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the additional bank address details, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters.
- `Public Property City() As String` [R/W] Sets or returns the city of the bank address. Field name: City. Length: 100 characters.
- `Public Property ControlKey() As String` [R/W] Sets or returns the bank control key of the business partner. Field name: ControlKey. Length: 2 characters.
  - remarks: The control key specifies the type of account, for example: 01 indicates Checking Account, 02 indicates Saving Account, and so on.
- `Public Property CorrespondentAccount() As String` [R/W] Returns a G/L account number for the the Business partner's Correspondent Account. Field name: CorresAcct. Field name: CorresAcct. Length: 30 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property Count() As Long` [R] Returns the total number of bank accounts of the business partners.
- `Public Property Country() As String` [R/W] Sets or returns the country code of the bank. Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county of the bank. Field name: County. Length: 100 characters.
- `Public Property CustomerIdNumber() As String` [R/W] Sets or returns the customer Id. number. Field name: CustIdNum. Field name: CustIdNum. Length: 254 characters.
- `Public Property Fax() As String` [R/W] Returns the Business partner's Bank FAX number. Field name: FAX. Length: 25 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property IBAN() As String` [R/W] Sets or returns the International Bank Account Number (IBAN) for the business partner. Field name: IBAN. Length: 50 characters.
  - remarks: Europe only.
- `Public Property InternalKey() As Long` [R/W] Sets or returns the internal key identifier of the bank. Field name: AbsEntry.
- `Public Property ISRBillerID() As String` [R/W] Sets or returns the business partner ISR biller Id. Field name: ISRBillerI. Length: 9 characters.
- `Public Property ISRType() As Long` [R/W] Sets or returns the ISR type. Field name: ISRType.
- `Public Property LogInstance() As Long` [R/W] Sets or returns the key identifier of the log instance. Each activity with the BPBankAccount is logged to the ACRB log table with the LogInstance identifier. Field name: LogInstanc. Length: 3 characters.
- `Public Property MandateExpDate() As Date` [R/W] property MandateExpDate
- `Public Property MandateID() As String` [R/W] The code to identify the direct debit mandate between the business partner and the company. Field name: MandateID. Length: 35 characters.
- `Public Property Phone() As String` [R/W] Returns the Business partner's Bank Phone number. Field name: Phone. Length: 50 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia)
- `Public Property SEPASeqType() As SEPASequenceTypeEnum` [R/W] property SEPASeqType
- `Public Property SignatureDate() As Date` [R/W] The date on which the mandate is signed. Field name: SignDate.
- `Public Property State() As String` [R/W] Sets or returns the state code of the business partner bank account. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Street() As String` [R/W] Sets or returns the street of the bank address. Field name: State. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserNo1() As String` [R/W] Sets or returns the payee bank user number 1 or password. User numbers 1 - 4 are used to identify the payment file. Field name: UsrNumber1. Length: 25 characters.
- `Public Property UserNo2() As String` [R/W] Sets or returns the payee bank user number 2 or password. User numbers 1 - 4 are used to identify the payment file. Field name: UsrNumber2. Length: 25 characters.
- `Public Property UserNo3() As String` [R/W] Sets or returns the payee bank user number 3 or password. User numbers 1 - 4 are used to identify the payment file. Field name: UsrNumber3. Length: 25 characters.
- `Public Property UserNo4() As String` [R/W] Sets or returns the payee bank user number 4 or password. User numbers 1 - 4 are used to identify the payment file. Field name: UsrNumber4. Length: 25 characters.
- `Public Property ZipCode() As String` [R/W] Sets or returns the zip code of the bank address. Field name: ZipCode. Length: 20 characters.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: If you delete the default bank account for a business partner, the first bank account in the remaining list becomes the default.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.BusinessPartners oBP;

    // Delete BP bank account
    if (oBP.GetByKey("11") == true)
    {
        oBP.BPBankAccounts.SetCurrentLine(1);
        oBP.BPBankAccounts.Delete();
        oBP.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
