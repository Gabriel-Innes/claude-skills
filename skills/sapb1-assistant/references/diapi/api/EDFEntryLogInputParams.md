<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EDFEntryLogInputParams (Object)

EDFEntryLogInputParams Class

## Properties (7)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property FileName() As String` [R/W] property FileName
- `Public Property Guid() As String` [R/W] property GUID
- `Public Property KeepLogDataPrefix() As BoYesNoEnum` [R/W] property KeepLogDataPrefix
- `Public Property LogDataContentType() As ElectronicDocumentBlobContentTypeEnum` [R/W] property LogDataContentType
- `Public Property LogType() As ElectronicDocumentEntryLogTypeEnum` [R/W] property LogType
- `Public Property UnzipLogData() As BoYesNoEnum` [R/W] property UnzipLogData

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
