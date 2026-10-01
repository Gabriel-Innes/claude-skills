<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PM_WorkOrderData (Object)

Source table: PMG7.

## Properties (5)
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property DocNumber() As Long` [R/W] property DocNumber
- `Public Property LineId() As Long` [R] property LineID
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property UserFields() As Fields` [R] property User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
