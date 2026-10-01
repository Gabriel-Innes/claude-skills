<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# IntrastatConfiguration (Object)

IntrastatConfiguration Class

## Properties (14)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Code() As String` [R/W] property Code
- `Public Property ConfID() As String` [R] property Configuration ID
- `Public Property ConfType() As IntrastatConfigurationEnum` [R/W] property Configuration Type
- `Public Property Country() As String` [R/W] property Country
- `Public Property Description() As String` [R/W] property Description
- `Public Property PercentageValue() As Double` [R/W] property Percentage Value
- `Public Property StatisticalCode() As String` [R/W] property Statistical Code
- `Public Property SupplementaryUnit() As Long` [R/W] property Supplementary Unit
- `Public Property TriangDeal() As IntrastatConfigurationTriangDealEnum` [R/W] property Triangulate Deal
- `Public Property ValidExport() As BoYesNoEnum` [R/W] property Valid for Export
- `Public Property ValidFrom() As Date` [R/W] property Valid From
- `Public Property ValidImport() As BoYesNoEnum` [R/W] property Valid for Import
- `Public Property ValidTo() As Date` [R/W] property Valid To

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
