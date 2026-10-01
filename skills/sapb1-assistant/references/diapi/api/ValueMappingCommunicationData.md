<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ValueMappingCommunicationData (Object)

ValueMappingCommunicationData Class

## Properties (10)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property CommunicationType() As VMCommunicationTypeEnum` [R/W] property CommunicationType
- `Public Property EndDate() As Date` [R/W] property EndDate
- `Public Property EndTime() As Long` [R/W] property EndTime
- `Public Property Message() As String` [R/W] property Message
- `Public Property ObjectID() As Long` [R/W] property ObjectId
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property StartTime() As Long` [R/W] property StartTime
- `Public Property Status() As VMCommunicationStatusEnum` [R/W] property Status
- `Public Property ThirdPartySystemId() As Long` [R/W] property ThirdPartySystemId

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
