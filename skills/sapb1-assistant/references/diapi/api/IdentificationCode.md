<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# IdentificationCode (Object)

IdentificationCode Class

## Properties (6)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property Codelist() As IdentificationCodeTypeEnum` [R/W] property Codelist
- `Public Property Description() As String` [R/W] property Description
- `Public Property SchemaCode() As String` [R/W] property SchemaCode
- `Public Property SchemaDesc() As String` [R/W] property SchemaDesc

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
