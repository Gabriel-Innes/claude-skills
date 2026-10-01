<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EDFProtocolWithParameters (Object)

EDFProtocolWithParameters Class

## Properties (4)
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property EDFProtocolParametersCollection() As EDFProtocolParametersCollection` [R] property EDFProtocolParametersCollection
- `Public Property IsActive() As BoYesNoEnum` [R/W] property IsActive

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
