<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EWBTransporter_Line (Object)

EWBTransporter_Line Class

## Properties (5)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property Mode() As Long` [R/W] property Mode
- `Public Property VehicleNo() As String` [R/W] property VehicleNo
- `Public Property VehicleType() As String` [R/W] property VehicleType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
