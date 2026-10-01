<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BrazilMultiIndexerParams (Object)

BrazilMultiIndexerParams Class

## Properties (6)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description
- `Public Property FirstRefIndexerCode() As String` [R] property FirstRefIndexerCode
- `Public Property IndexerType() As BrazilMultiIndexerTypes` [R/W] property IndexerType
- `Public Property SecondRefIndexerCode() As String` [R] property SecondRefIndexerCode
- `Public Property ThirdRefIndexerCode() As String` [R] property ThirdRefIndexerCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
