<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WIPMapping (Object)

WIPMapping Class

## Properties (4)
- `Public Property AbsoluteEntry() As Long` [R] property AbsoluteEntry
- `Public Property AccountFrom() As String` [R/W] property AccountFrom
- `Public Property AccountTo() As String` [R/W] property AccountTo
- `Public Property LineNumber() As Long` [R] property LineNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
