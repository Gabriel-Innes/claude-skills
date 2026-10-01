<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ElectronicSeries (Object)

ElectronicSeries Class

## Properties (10)
- `Public Property ApprovalNumber() As Long` [R/W] property ApprovalNumber
- `Public Property ApprovalYear() As Long` [R/W] property ApprovalYear
- `Public Property ElectronicSeries() As Long` [R] property ElectronicSeries
- `Public Property InitialNumber() As String` [R/W] property InitialNumber
- `Public Property LastNumber() As String` [R/W] property LastNumber
- `Public Property Name() As String` [R/W] property Name
- `Public Property NextNumber() As String` [R] property NextNumber
- `Public Property Prefix() As String` [R/W] property Prefix
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property Series() As Long` [R/W] property Series

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
