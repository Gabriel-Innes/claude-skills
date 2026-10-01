<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
