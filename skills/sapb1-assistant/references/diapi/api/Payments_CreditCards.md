<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Payments_CreditCards (Object)

Payments_CreditCards is a child object of the Payments object and represents the payments by credit cards in the Banking module. Source tables: RCT3 (incoming payments) and VPM3 (outgoing payments).

**Remarks:** Mandatory fields in SAP Business One: CardValidUntil, CreditCard, CreditCardNumber, and CreditSum. To display the form in the application: - For RCT3 table, select Sales - A/R --> A/R Invoice. - or - For VPM3 table, select Purchasing - A/P --> A/P Invoice. - On the toolbar, click the Payment Means icon. - Select the Credit Card tab.

## Properties (20)
- `Public Property AdditionalPaymentSum() As Double` [R/W] Sets or returns the payment amount added to the first payment, due to rounding results. Field name: AddPmntSum.
  - remarks: SAP Business One uses the amount due, number of payments, and first partial payment amount to calculate the amount that is to be paid with the further payments. Rounding results are added to the first payment.
- `Public Property CardValidUntil() As Date` [R/W] Sets or returns the credit card expiration date. Mandatory property. Field name: CardValid.
- `Public Property ConfirmationNum() As String` [R/W] Sets or returns the confirmation number for the payment through a credit card. Field name: ConfNum. Length: 20 characters.
- `Public Property Count() As Long` [R] Returns the number of lines in this document.
  - remarks: The value of this property increases automatically, after you add lines to the document.
- `Public Property CreditAcct() As String` [R/W] Sets or returns the credit account number. Field name: CreditAcct. Length: 15 characters.
- `Public Property CreditCard() As Long` [R/W] Sets or returns the key of a credit card. Mandatory property. Field name: CreditCard. This is a foreign key to the CreditCards object.
- `Public Property CreditCardNumber() As String` [R/W] Sets or returns the credit card number. Field name: CrCardNum. Mandatory property. Length: 20 characters.
- `Public Property CreditSum() As Double` [R/W] Sets or returns the total payment amount. Mandatory property. Field name: CreditSum.
  - remarks: Credit card payment can be divided into several installments. The AdditionalPaymentSum property represents any additional installments. For the first payment, use the FirstPaymentSum property. The total number of payments is set in the NumOfPayments property, and the total payment amount is set in the CreditSum property.
- `Public Property CreditType() As BoRcptCredTypes` [R/W] Sets or returns a valid value of BoRcptCredTypes type that specifies the way for providing the credit card details (directly or by phone). Field name: CreditType.
- `Public Property FirstPaymentDue() As Date` [R/W] Sets or returns the due date of the first payment. Field name: FirstDue.
  - remarks: Applies only if the payment method allows partial payments.
- `Public Property FirstPaymentSum() As Double` [R/W] Sets or returns the amount of the first payment, when the transaction is divided to installments. Field name: FirstSum.
  - remarks: Credit card payment can be divided into several installments. The AdditionalPaymentSum property represents any additional installments. For the first payment, use the FirstPaymentSum property. The total number of payments is set in the NumOfPayments property, and the total payment amount is set in the CreditSum property. Applies only if the payment method allows partial payments.
- `Public Property LineNum() As Long` [R] Returns the number of the current line. Field name: LineID.
- `Public Property NumOfCreditPayments() As Long` [R/W] Sets or returns the number of payments through the credit card. Field name: NumOfPmnts.
- `Public Property NumOfPayments() As Long` [R/W] Sets or returns the number of installments. Field name: NumOfPmnts.
  - remarks: Credit card payment can be divided into several installments. The AdditionalPaymentSum property represents any additional installments. For the first payment, use the FirstPaymentSum property. The total number of payments is set in the NumOfPayments property, and the total payment amount is set in the CreditSum property. Applies only if the payment method allows partial payments.
- `Public Property OwnerIdNum() As String` [R/W] Sets or returns the ID number of the credit card owner. Field name: OwnerIdNum. Length: 15 characters.
- `Public Property OwnerPhone() As String` [R/W] Sets or returns the phone number of the credit card owner. Field name: OwnerPhone. Length: 50 characters.
- `Public Property PaymentMethodCode() As Long` [R/W] Sets or returns the key of the credit payment method. Field name: CrTypeCode. This is a foreign key to the CreditPaymentMethods object.
- `Public Property SplitPayments() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to split the payment for the transaction into separate rows. Field name: SpiltCred.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VoucherNum() As String` [R/W] Sets or returns the number of the credit document. Field name: VoucherNum. Length: 20 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
