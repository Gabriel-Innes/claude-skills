<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PaymentRunExport_Lines (Object)

PaymentRunExport_Lines is a child object of the PaymentRunExport object and represents the line entries of each payment. Source table: PEX1.

## Properties (32)
- `Public Property BPDebitPayableAccount() As String` [R] Returns the account of the business partner debtor/payable Field name: . Length: 15 characters.
- `Public Property Count() As Long` [R] Returns the total rows in the payment run.
- `Public Property CustomerNumber() As String` [R] Returns the customer number. Field name: CustNum. Length: 15 characters. This is a foreign key to the
- `Public Property DateOfPaymentRun() As Date` [R] Returns the date of the payment run. Field name: PayRunDate.
- `Public Property DocumentCurrency() As String` [R] Returns the document currency. Field name: DocCurr. Length: 3 characters.
- `Public Property DocumentLocalCurrency() As String` [R] Returns the document local currency. Field name: DocLocCurr. Length: 3 characters.
- `Public Property DocumentNumber() As Long` [R] Returns the Document Number of the payment in this line. Field name: DocNum.
- `Public Property DocumentObjectType() As Long` [R] Returns the document object type. Field name: ObjType. Length: 20 characters.
- `Public Property DocumentObjectTypeEx() As String` [R] Returns the document object type.
- `Public Property DocumentPaymentTerms() As Long` [R] Returns the document payment terms. Field name: DocPrmTerm. This is a foreign key to the PaymentTermsTypes Object.
- `Public Property DocumentPostingDate() As Date` [R] Returns the document posting date. Field name: DocDate.
- `Public Property DocumentRate() As Double` [R] Returns the document rate. Field name: DocRate.
- `Public Property DocumentRemarks() As String` [R] Returns the document remarks. Field name: DocRemarks. Length: 254 characters.
- `Public Property DocumentTaxAmount() As Double` [R] Returns the document tax amount in local currency. Field name: DocTaxAmnt.
- `Public Property DocumentTaxAmountFC() As Double` [R] Returns the document tax amount in foreign currency. Field name: DoxTxAmtFC.
- `Public Property DocumentTaxDate() As Date` [R] Returns the document tax date. Field name: TaxDate.
- `Public Property DocumentTotal() As Double` [R] Returns the document total in local currency. Field name: DocTotal.
- `Public Property DocumentTotalFC() As Double` [R] Returns the document total in foreign currency. Field name: DocTotalFC.
- `Public Property FiscalYear() As Date` [R] Returns the fiscal year (date type). Field name: FiscalYear.
- `Public Property FreeText1() As String` [R] property FreeText1
- `Public Property FreeText2() As String` [R] property FreeText2
- `Public Property FreeText3() As String` [R] property FreeText3
- `Public Property PaymentDocNum() As Long` [R] Returns the payment document number. Field name: DocNum.
- `Public Property PaymentDocReference() As String` [R] Returns the payment document reference. Field name: DocPymRef. Length: 27 characters.
- `Public Property PaymentMeans() As String` [R] Returns the payment method (check, bank transfer, etc.). Field name: PaymMethod. Length: 15 characters. This is a foreign key to the WizardPaymentMethods object.
- `Public Property PaymentNumber() As Long` [R] Returns the payment number. Field name: PymNum. Length: 11 characters.
- `Public Property PaymentOrderNum() As Long` [R] property PaymentOrderNum
- `Public Property PaymentTermsPeriod() As Long` [R] Returns the payment terms period. Field name: PymTermPer. Length: 15 characters.
- `Public Property PaymentWizardCode() As String` [R] Returns the payment run ID (wizard code). Field name: PaymWizCod. Length: 15 characters.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (starts from 1). Field name: LineId.
- `Public Property VendorNumber() As String` [R] Returns the vendor code. Field name: VendorNum. Length: 15 characters.
- `Public Property VendorRefNum() As String` [R] Returns the vendor reference number. Field name: VendRefNum. Length: 16 characters.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
