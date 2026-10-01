<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxCodeDeterminationTCDValue (Object)

TaxCodeDeterminationTCDValue Class

## Properties (8)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property DefaultWTs() As TaxCodeDeterminationTCDDefaultWTs` [R] property DefaultWTs
- `Public Property DispOrder() As Long` [R/W] property DispOrder
- `Public Property Periods() As TaxCodeDeterminationTCDPeriods` [R] property Periods
- `Public Property Value1() As String` [R/W] property Value1
- `Public Property Value2() As String` [R/W] property Value2
- `Public Property Value3() As String` [R/W] property Value3
- `Public Property Value4() As String` [R/W] property Value4

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
