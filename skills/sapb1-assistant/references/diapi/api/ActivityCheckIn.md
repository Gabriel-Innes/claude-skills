<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ActivityCheckIn (Object)

ActivityCheckIn Class

## Properties (8)
- `Public Property Date() As Date` [R] property Date
- `Public Property HandledBy() As Long` [R] property HandledBy
- `Public Property HandledByEmployee() As Long` [R] property HandledByEmployee
- `Public Property Latitude() As String` [R/W] property Latitude
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property Location() As String` [R/W] property Location
- `Public Property Longitude() As String` [R/W] property Longitude
- `Public Property Time() As Date` [R] property Time

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
