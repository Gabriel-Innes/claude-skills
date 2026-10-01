<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ReportLayout_TranslationLine (Object)

ReportLayout_TranslationLine Class

## Properties (8)
- `Public Property CreateDate() As Date` [R/W] property CreateDate
- `Public Property CreateTime() As Long` [R/W] property CreateTime
- `Public Property DocEntry() As String` [R] property DocEntry
- `Public Property DocName() As String` [R/W] property DocName
- `Public Property LanguageCode() As Long` [R/W] property LanguageCode
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property UpdateDate() As Date` [R/W] property UpdateDate
- `Public Property UpdateTime() As Long` [R/W] property UpdateTime

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
