<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EDFEntryAddLogInputParams (Object)

EDFEntryAddLogInputParams Class

## Properties (9)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property ExportFile() As String` [R/W] property ExportFile
- `Public Property ExportFormat() As Long` [R/W] property ExportFormat
- `Public Property Guid() As String` [R/W] property GUID
- `Public Property LogData() As String` [R/W] property LogData
- `Public Property LogDataContentType() As ElectronicDocumentBlobContentTypeEnum` [R/W] property LogDataContentType
- `Public Property LogMessage() As String` [R/W] property LogMessage
- `Public Property LogType() As ElectronicDocumentEntryLogTypeEnum` [R/W] property LogType
- `Public Property ZipLogData() As BoYesNoEnum` [R/W] property ZipLogData

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
