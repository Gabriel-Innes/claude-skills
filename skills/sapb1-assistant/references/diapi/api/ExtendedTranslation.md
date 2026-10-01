<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExtendedTranslation (Object)

ExtendedTranslation Class

## Properties (8)
- `Public Property Category() As TranslationCategoryEnum` [R/W] property Category
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExtendedTranslation_ItemLines() As ExtendedTranslation_ItemLines` [R] property ExtendedTranslation_ItemLines
- `Public Property ID() As String` [R/W] property ID
- `Public Property SecondaryID() As String` [R/W] property SecondaryID
- `Public Property SourceLanguage() As Long` [R/W] property SourceLanguage
- `Public Property UpdateDate() As Date` [R] property UpdateDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
