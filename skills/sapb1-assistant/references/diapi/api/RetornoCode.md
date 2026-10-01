<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RetornoCode (Object)

RetornoCode Class

## Properties (8)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property BankCode() As String` [R/W] property BankCode
- `Public Property BOEStatus() As BoBoeStatus` [R/W] property BoeStatus
- `Public Property Color() As Long` [R/W] property Color
- `Public Property Description() As String` [R/W] property Description
- `Public Property FileFormat() As String` [R/W] property FileFormat
- `Public Property MovementCode() As Long` [R/W] property MovementCode
- `Public Property OccurenceCode() As Long` [R/W] property OccurenceCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
