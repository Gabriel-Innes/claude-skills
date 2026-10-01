<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TrackingNoteBroker (Object)

TrackingNoteBroker Class

## Properties (4)
- `Public Property AgreementNumber() As Long` [R/W] property AgreementNumber
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property TrackingNoteLineNumber() As Long` [R] property TrackingNoteLineNumber
- `Public Property TrackingNoteNumber() As Long` [R] property TrackingNoteNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
