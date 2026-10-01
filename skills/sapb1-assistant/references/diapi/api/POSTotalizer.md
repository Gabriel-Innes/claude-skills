<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# POSTotalizer (Object)

POSTotalizer Class

## Properties (5)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property LineNum() As Long` [R] property LineNum
- `Public Property Number() As Long` [R/W] property Number
- `Public Property Total() As Double` [R/W] property Total

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
