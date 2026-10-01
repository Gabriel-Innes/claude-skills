<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WTDFreight (Object)

WTDFreight Class

## Properties (5)
- `Public Property EffectiveDateFrom() As Date` [R/W] property EffectiveDateFrom
- `Public Property EffectiveDateTo() As Date` [R/W] property EffectiveDateTo
- `Public Property FreightCode() As Long` [R/W] property FreightCode
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property WTaxCode() As String` [R/W] property WTaxCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
