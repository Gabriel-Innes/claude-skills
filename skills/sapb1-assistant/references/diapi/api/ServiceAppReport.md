<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceAppReport (Object)

ServiceAppReport Class

## Properties (4)
- `Public Property Code() As Long` [R] property Code
- `Public Property CustomizedReportName() As String` [R/W] property CustomizedReportName
- `Public Property ReportChoice() As MobileAppReportChoiceEnum` [R/W] property ReportChoice
- `Public Property SystemReportName() As String` [R/W] property SystemReportName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
