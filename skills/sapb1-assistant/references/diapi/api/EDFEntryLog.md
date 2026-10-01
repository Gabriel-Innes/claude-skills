<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EDFEntryLog (Object)

EDFEntryLog Class

## Properties (9)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property ExportFile() As String` [R/W] property ExportFile
- `Public Property ExportFormat() As Long` [R/W] property ExportFormat
- `Public Property LogData() As String` [R/W] property LogData
- `Public Property LogMessage() As String` [R/W] property LogMessage
- `Public Property LogNumber() As Long` [R] property LogNumber
- `Public Property LogOperationDate() As Date` [R/W] property LogOperationDate
- `Public Property LogOperationTime() As Long` [R/W] property LogOperationTime
- `Public Property LogType() As ElectronicDocumentEntryLogTypeEnum` [R/W] property LogType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
