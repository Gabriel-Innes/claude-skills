<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ECMActionStatusData (Object)

ECMActionStatusData Class

## Properties (5)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property ActMessage() As String` [R/W] property ActMessage
- `Public Property ActStatus() As EcmActionStatusEnum` [R/W] property ActStatus
- `Public Property ReceivDate() As Date` [R/W] property ReceivDate
- `Public Property ReportID() As String` [R/W] property ReportID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
