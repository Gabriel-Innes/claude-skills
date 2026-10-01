<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxInvoiceReport (Object)

TaxInvoiceReport Class

## Properties (16)
- `Public Property BaseAmount() As Double` [R] property BaseAmount
- `Public Property BPCode() As String` [R] property BPCode
- `Public Property BPName() As String` [R] property BPName
- `Public Property BusinessPlace() As Long` [R] property BusinessPlace
- `Public Property Canceled() As String` [R] property Canceled
- `Public Property Date() As Date` [R] property Date
- `Public Property ETaxNo() As String` [R/W] property ETaxNo
- `Public Property ETaxWebSite() As Long` [R/W] property ETaxWebSite
- `Public Property NTSApproval() As TaxInvoiceReportNTSApprovedEnum` [R/W] property NTSApproval
- `Public Property NTSApprovalNo() As String` [R/W] property NTSApprovalNo
- `Public Property OriginalNTSApprovalNo() As String` [R/W] property OriginalNTSApprovalNo
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property ReportType() As Long` [R] property ReportType
- `Public Property TaxAmount() As Double` [R] property TaxAmount
- `Public Property TaxInvoiceReportLineCollection() As TaxInvoiceReportLineCollection` [R] property TaxInvoiceReportLineCollection
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
