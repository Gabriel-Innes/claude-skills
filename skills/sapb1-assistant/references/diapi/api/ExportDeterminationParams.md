<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExportDeterminationParams (Object)

ExportDeterminationParams Class

## Properties (7)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property BusinessPartner() As String` [R/W] property BusinessPartner
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property Country() As String` [R/W] property Country
- `Public Property DocumentSubType() As String` [R/W] property DocumentSubType
- `Public Property DocumentType() As String` [R/W] property DocumentType
- `Public Property Series() As Long` [R/W] property Series

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
