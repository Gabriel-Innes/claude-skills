<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxInvoiceReportLine (Object)

TaxInvoiceReportLine Class

## Properties (18)
- `Public Property BaseAmount() As Double` [R] property BaseAmount
- `Public Property BPCode() As String` [R] property BPCode
- `Public Property BPName() As String` [R] property BPName
- `Public Property BusinessPlace() As Long` [R] property BusinessPlace
- `Public Property Currency() As String` [R] property Currency
- `Public Property DocumentDate() As Date` [R] property DocumentDate
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property DocumentType() As Long` [R] property DocumentType
- `Public Property ItemDescription() As String` [R] property ItemDescription
- `Public Property ItemNo() As String` [R] property ItemNo
- `Public Property ItemPrice() As Double` [R] property ItemPrice
- `Public Property ItemQuantity() As Double` [R] property ItemQuantity
- `Public Property Legacy() As String` [R] property Legacy
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property LineType() As TaxInvoiceReportLineTypeEnum` [R] property LineType
- `Public Property TaxAmount() As Double` [R] property TaxAmount
- `Public Property TaxCode() As String` [R] property TaxCode
- `Public Property TaxInvoiceReportNumber() As String` [R] property TaxInvoiceReportNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
