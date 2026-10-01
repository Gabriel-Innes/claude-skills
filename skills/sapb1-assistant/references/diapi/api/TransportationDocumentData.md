<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TransportationDocumentData (Object)

TransportationDocumentData Class

## Properties (19)
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property Canceled() As BoYesNoEnum` [R/W] property Canceled
- `Public Property CarrierCode() As String` [R/W] property CarrierCode
- `Public Property ElDocExportFormat() As Long` [R/W] property ElDocExportFormat
- `Public Property ElDocGenType() As ElectronicDocGenTypeEnum` [R/W] property ElDocGenType
- `Public Property ExpirationDate() As Date` [R/W] property ExpirationDate
- `Public Property IssueGate() As Long` [R/W] property IssueGate
- `Public Property NextNumber() As Long` [R/W] property NextNumber
- `Public Property PostDate() As Date` [R/W] property PostDate
- `Public Property TrailerID() As String` [R/W] property TrailerID
- `Public Property TranspDocNumber() As Long` [R] property TranspDocNumber
- `Public Property TransportationDocumentLineDataCollection() As TransportationDocumentLineDataCollection` [R] property TransportationDocumentLineDataCollection
- `Public Property TransportationDocumentParamsCollection() As TransportationDocumentParamsCollection` [R] property TransportationDocumentParamsCollection
- `Public Property TransportationNumber() As String` [R/W] property TransportationNumber
- `Public Property TransportedTotalLC() As Double` [R] property TransportedTotalLC
- `Public Property VehicleID() As String` [R/W] property VehicleID
- `Public Property WarehouseCode() As String` [R/W] property WarehouseCode
- `Public Property Weight() As Double` [R] property Weight
- `Public Property WeightUnit() As Long` [R] property WeightUnit

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
