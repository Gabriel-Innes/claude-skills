<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TrackingNote (Object)

TrackingNote Class

## Properties (8)
- `Public Property CCDNumber() As String` [R/W] property CCDNumber
- `Public Property CountryOfOrigin() As String` [R/W] property CountryOfOrigin
- `Public Property CustomsTerminal() As String` [R/W] property CustomsTerminal
- `Public Property Date() As Date` [R/W] property Date
- `Public Property IsDirectImport() As BoYesNoEnum` [R/W] property IsDirectImport
- `Public Property TrackingNoteBrokerCollection() As TrackingNoteBrokerCollection` [R] property TrackingNoteBrokerCollection
- `Public Property TrackingNoteItemCollection() As TrackingNoteItemCollection` [R] property TrackingNoteItemCollection
- `Public Property TrackingNoteNumber() As Long` [R] property TrackingNoteNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
