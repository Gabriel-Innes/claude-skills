<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EcmActionLog (Object)

EcmActionLog Class

## Properties (9)
- `Public Property ActionID() As Long` [R/W] property ActionID
- `Public Property Data() As String` [R/W] property Data
- `Public Property ExportFile() As String` [R/W] property ExportFile
- `Public Property ExportFormat() As Long` [R/W] property ExportFormat
- `Public Property LogDate() As Date` [R/W] property LogDate
- `Public Property LogID() As Long` [R] property LogID
- `Public Property LogTime() As Long` [R/W] property LogTime
- `Public Property Message() As String` [R/W] property Message
- `Public Property Type() As EcmActionLogTypeEnum` [R/W] property Type

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
