<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExtendedTranslationParams (Object)

ExtendedTranslationParams Class

## Properties (4)
- `Public Property Category() As TranslationCategoryEnum` [R/W] property Category
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property ID() As String` [R/W] property ID
- `Public Property SecondaryID() As String` [R/W] property SecondaryID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
