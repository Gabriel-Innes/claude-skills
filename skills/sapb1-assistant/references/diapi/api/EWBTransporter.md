<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EWBTransporter (Object)

EWBTransporter Class

## Properties (5)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property EWBTransporter_Lines() As EWBTransporter_Lines` [R] property EWBTransporter_Lines
- `Public Property TransporterCode() As String` [R/W] property TransporterCode
- `Public Property TransporterID() As String` [R/W] property TransporterID
- `Public Property TransporterName() As String` [R/W] property TransporterName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
