<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BrazilMultiIndexer (Object)

BrazilMultiIndexer Class

## Properties (7)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property FirstRefIndexerCode() As String` [R/W] property FirstRefIndexerCode
- `Public Property ID() As Long` [R] property ID
- `Public Property IndexerType() As BrazilMultiIndexerTypes` [R/W] property IndexerType
- `Public Property SecondRefIndexerCode() As String` [R/W] property SecondRefIndexerCode
- `Public Property ThirdRefIndexerCode() As String` [R/W] property ThirdRefIndexerCode

## Methods (6)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetReferencedIndexerType(ByVal referenceIndex As Long, ByRef penumRsltType As BrazilIndexerTypes, ByRef plRsltValue As Long) As Boolean` method GetReferencedIndexerType
  - param `referenceIndex`: 
  - param `penumRsltType`: one of the enumeration's values (see the enum file)
  - param `plRsltValue`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
