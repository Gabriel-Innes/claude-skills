<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PM_OpenIssueData (Object)

Source table: PMG2.

## Properties (12)
- `Public Property Area() As Long` [R/W] property Area
- `Public Property Closed() As BoYesNoEnum` [R/W] property Closed
- `Public Property Effort() As Double` [R/W] property Effort
- `Public Property EnteredBy() As Long` [R/W] property EnteredBy
- `Public Property EnteredDate() As Date` [R/W] property EnteredDate
- `Public Property LineId() As Long` [R] property LineID
- `Public Property Priority() As Long` [R/W] property Priority
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property Responsible() As Long` [R/W] property Responsible
- `Public Property SolutionID() As Long` [R/W] property SolutionID
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
