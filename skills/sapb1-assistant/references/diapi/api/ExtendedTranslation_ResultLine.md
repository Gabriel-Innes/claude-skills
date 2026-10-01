<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExtendedTranslation_ResultLine (Object)

ExtendedTranslation_ResultLine Class

## Properties (5)
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property LanguageCode() As Long` [R/W] property LanguageCode
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property SubLineNumber() As Long` [R] property SubLineNumber
- `Public Property TranslatedText() As String` [R/W] property TranslatedText

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
