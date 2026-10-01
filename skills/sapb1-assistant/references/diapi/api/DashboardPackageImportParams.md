<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DashboardPackageImportParams (Object)

DashboardPackageImportParams Class

## Properties (4)
- `Public Property ForceOverwritePackage() As BoYesNoEnum` [R/W] property ForceOverwritePackage
- `Public Property ForceOverwriteQuery() As BoYesNoEnum` [R/W] property ForceOverwriteQuery
- `Public Property ImportQueries() As BoYesNoEnum` [R/W] property ImportQueries
- `Public Property PackageFilePath() As String` [R/W] property PackageFilePath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
