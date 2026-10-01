<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# GovPayCodeAuthority (Object)

GovPayCodeAuthority Class

## Properties (4)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property BPLID() As Long` [R/W] property BPLId
- `Public Property CardCode() As String` [R/W] property CardCode
- `Public Property State() As String` [R/W] property State

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
