<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExtendedTranslation_ItemLine (Object)

ExtendedTranslation_ItemLine Class

## Properties (9)
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExtendedTranslation_ResultLines() As ExtendedTranslation_ResultLines` [R] property ExtendedTranslation_ResultLines
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property ItemType() As String` [R/W] property ItemType
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property MaxLength() As Long` [R/W] property MaxLength
- `Public Property Memo() As String` [R/W] property Memo
- `Public Property SlimType() As String` [R/W] property SlimType
- `Public Property SourceText() As String` [R/W] property SourceText

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
