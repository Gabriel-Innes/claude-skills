<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InventoryOpeningBalanceCCDNumber (Object)

InventoryOpeningBalanceCCDNumber Class

## Properties (9)
- `Public Property BaseLineNumber() As Long` [R/W] property BaseLineNumber
- `Public Property CCDNumber() As String` [R/W] property CCDNumber
- `Public Property ChildNumber() As Long` [R/W] property ChildNumber
- `Public Property CountryOfOrigin() As String` [R/W] property CountryOfOrigin
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property SubLineNumber() As Long` [R/W] property SubLineNumber
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
