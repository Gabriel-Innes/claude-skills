<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PaymentInvoiceEntry (Object)

PaymentInvoiceEntry Class

## Properties (4)
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property DocNum() As Long` [R] property DocNum
- `Public Property DocType() As PaymentInvoiceTypeEnum` [R/W] property DocType
- `Public Property InstallmentId() As Long` [R/W] property InstallmentId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
