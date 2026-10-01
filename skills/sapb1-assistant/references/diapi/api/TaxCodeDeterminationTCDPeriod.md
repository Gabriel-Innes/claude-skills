<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxCodeDeterminationTCDPeriod (Object)

TaxCodeDeterminationTCDPeriod Class

## Properties (5)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property ByUsages() As TaxCodeDeterminationTCDByUsages` [R] property ByUsages
- `Public Property EffectFrom() As Date` [R/W] property EffectFrom
- `Public Property EffectTo() As Date` [R/W] property EffectTo
- `Public Property TaxCode() As String` [R/W] property TaxCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
