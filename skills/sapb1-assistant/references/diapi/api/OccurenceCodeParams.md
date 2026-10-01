<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# OccurenceCodeParams (Object)

OccurenceCodeParams Class

## Properties (6)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property IsMovement() As BoYesNoEnum` [R/W] property IsMovement
- `Public Property Note() As String` [R] property Note
- `Public Property RequestedBoeStatus() As BoBoeStatus` [R] property RequestedBoeStatus

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
