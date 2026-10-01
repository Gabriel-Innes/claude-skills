<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxCodeDeterminationTCDKeyField (Object)

TaxCodeDeterminationTCDKeyField Class

## Properties (17)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property Description() As String` [R/W] property Description
- `Public Property KeyField1() As Long` [R/W] property KeyField1
- `Public Property KeyField2() As Long` [R/W] property KeyField2
- `Public Property KeyField3() As Long` [R/W] property KeyField3
- `Public Property KeyField4() As Long` [R/W] property KeyField4
- `Public Property LegalText() As String` [R/W] Legal text defined on the Tax Code Determination - Setup window. Field name: LegalText. Length: 250 characters.
- `Public Property Priority() As Long` [R/W] property Priority
- `Public Property UDFAlias1() As String` [R/W] property UDFAlias1
- `Public Property UDFAlias2() As String` [R/W] property UDFAlias2
- `Public Property UDFAlias3() As String` [R/W] property UDFAlias3
- `Public Property UDFAlias4() As String` [R/W] property UDFAlias4
- `Public Property UDFTable1() As String` [R/W] property UDFTable1
- `Public Property UDFTable2() As String` [R/W] property UDFTable2
- `Public Property UDFTable3() As String` [R/W] property UDFTable3
- `Public Property UDFTable4() As String` [R/W] property UDFTable4
- `Public Property Values() As TaxCodeDeterminationTCDValues` [R] property Values

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
