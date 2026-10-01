<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# IntrastatConfigurationParams (Object)

IntrastatConfigurationParams Class

## Properties (6)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property ConfType() As IntrastatConfigurationEnum` [R/W] property Configuration Type
- `Public Property Country() As String` [R/W] property Country
- `Public Property StatisticalCode() As String` [R/W] property Statistical Code
- `Public Property ValidFrom() As Date` [R/W] property Valid From

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
