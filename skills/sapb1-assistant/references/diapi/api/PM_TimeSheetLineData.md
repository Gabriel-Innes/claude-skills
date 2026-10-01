<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PM_TimeSheetLineData (Object)

PM_TimeSheetLineData Class

## Properties (22)
- `Public Property ActivityType() As Long` [R/W] property ActivityType
- `Public Property BillableTime() As Date` [R] property BillableTime
- `Public Property Branch() As Long` [R/W] property Branch
- `Public Property Break() As Date` [R/W] property Break
- `Public Property CostCenter() As String` [R/W] property CostCenter
- `Public Property Date() As Date` [R/W] property Date
- `Public Property EffectiveTime() As Date` [R] property EffectiveTime
- `Public Property EndTime() As Date` [R/W] property EndTime
- `Public Property FinancialProject() As String` [R/W] property FinancialProject
- `Public Property FullDay() As BoYesNoEnum` [R/W] property FullDay
- `Public Property GPSData() As String` [R/W] property GPSData
- `Public Property LaborItem() As String` [R/W] property LaborItem
- `Public Property LineId() As Long` [R] property LineID
- `Public Property Location() As Long` [R/W] property Location
- `Public Property NonBillableTime() As Date` [R/W] property NonBillableTime
- `Public Property ProjectID() As Long` [R/W] property ProjectID
- `Public Property ServiceCall() As Long` [R/W] property ServiceCall
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property StartTime() As Date` [R/W] property StartTime
- `Public Property SubprojectID() As Long` [R/W] property SubprojectID
- `Public Property UserFields() As Fields` [R] property User Fields
- `Public Property Workorder() As Long` [R/W] property Workorder

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
