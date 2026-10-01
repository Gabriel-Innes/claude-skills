<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PaymentAmountParams (Object)

PaymentAmountParams Class

## Properties (10)
- `Public Property CashDiscountAmount() As Double` [R] property CashDiscountAmount
- `Public Property CashDiscountAmountFC() As Double` [R] property CashDiscountAmountFC
- `Public Property CashDiscountAmountSC() As Double` [R] property CashDiscountAmountSC
- `Public Property CashDiscountPercentage() As Double` [R] property CashDiscountPercentage
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property DocType() As PaymentInvoiceTypeEnum` [R] property DocType
- `Public Property InstallmentId() As Long` [R] property InstallmentId
- `Public Property TotalPaymentAmount() As Double` [R] property TotalPaymentAmount
- `Public Property TotalPaymentAmountFC() As Double` [R] property TotalPaymentAmountFC
- `Public Property TotalPaymentAmountSC() As Double` [R] property TotalPaymentAmountSC

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
