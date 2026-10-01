<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# LegalDataDetail (Object)

LegalDataDetail Class

## Properties (6)
- `Public Property amount() As Double` [R/W] property Amount
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property LineSequence() As Long` [R] property LineSequence
- `Public Property LineType() As LegalDataLineTypeEnum` [R/W] property LineType
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property TaxRate() As Double` [R/W] property TaxRate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
