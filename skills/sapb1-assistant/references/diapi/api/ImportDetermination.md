<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ImportDetermination (Object)

ImportDetermination Class

## Properties (9)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property DefaultDigitalSeries() As Long` [R/W] property DefaultDigitalSeries
- `Public Property FieldType() As ImportFieldTypeEnum` [R/W] property FieldType
- `Public Property FieldTypeXPath() As String` [R/W] property FieldTypeXPath
- `Public Property ImportFormat() As Long` [R/W] property ImportFormat
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property ObjectType() As String` [R/W] property ObjectType
- `Public Property ObjectTypeXPath() As String` [R/W] property ObjectTypeXPath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
