<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TrackingNoteItem (Object)

TrackingNoteItem Class

## Properties (10)
- `Public Property AccumulatedAPQuantity() As Double` [R] property AccumulatedAPQuantity
- `Public Property AccumulatedARQuantity() As Double` [R] property AccumulatedARQuantity
- `Public Property AccumulatedRelocatedQuantity() As Double` [R] property AccumulatedRelocatedQuantity
- `Public Property CountryOfOrigin() As String` [R/W] property CountryOfOrigin
- `Public Property CustomsGroupCode() As Long` [R/W] property CustomsGroupCode
- `Public Property ItemCCDNumber() As String` [R/W] property ItemCCDNumber
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property TrackingNoteLineNumber() As Long` [R] property TrackingNoteLineNumber
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
