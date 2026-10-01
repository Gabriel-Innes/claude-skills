<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxCodeDeterminationTCDByUsage (Object)

TaxCodeDeterminationTCDByUsage Class

## Properties (6)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property FreightTaxCode() As String` [R/W] property FreightTaxCode
- `Public Property PurchaseTaxCode() As String` [R/W] property PurchaseTaxCode
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property Type() As TaxCodeDeterminationTCDByUsageTypeEnum` [R/W] property Type
- `Public Property UsageCode() As Long` [R/W] property UsageCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
