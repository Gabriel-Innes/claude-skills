<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# NFTaxCategory (Object)

NFTaxCategory Class

## Properties (5)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property CESTRelevant() As BoYesNoEnum` [R/W] Tax category is relevant for CEST.
- `Public Property Code() As String` [R/W] property Code
- `Public Property GPCId() As Long` [R/W] property GPCId
- `Public Property Locked() As BoYesNoEnum` [R/W] property Locked

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
