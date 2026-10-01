<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TechnicianSchedulings (Object)

TechnicianSchedulings Class

## Properties (5)
- `Public Property EndDate() As Date` [R] property EndDate
- `Public Property IsClosed() As BoYesNoEnum` [R] property IsClosed
- `Public Property SchedulingLineNum() As Long` [R] property SchedulingLineNum
- `Public Property ServiceCallID() As Long` [R] property ServiceCallID
- `Public Property StartDate() As Date` [R] property StartDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
