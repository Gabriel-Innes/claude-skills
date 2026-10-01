<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EcmAction (Object)

EcmAction Class

## Properties (25)
- `Public Property ActionID() As Long` [R] property ActionID
- `Public Property AssignedID() As String` [R/W] property AssignedID
- `Public Property BusinessPlace() As Long` [R/W] property BusinessPlace
- `Public Property Description() As String` [R/W] property Description
- `Public Property DocumentBatch() As String` [R/W] property DocumentBatch
- `Public Property DocumentBatchLine() As Long` [R/W] property DocumentBatchLine
- `Public Property Environment() As Long` [R/W] property Environment
- `Public Property GenerationType() As EcmActionGenerationTypeEnum` [R/W] property GenerationType
- `Public Property IsCanceled() As BoYesNoEnum` [R] property IsCanceled
- `Public Property IsRemoved() As BoYesNoEnum` [R] property IsRemoved
- `Public Property Message() As String` [R/W] property Message
- `Public Property ObjectID() As String` [R/W] property ObjectID
- `Public Property PeriodDateFrom() As Date` [R/W] property PeriodDateFrom
- `Public Property PeriodDateTo() As Date` [R/W] property PeriodDateTo
- `Public Property PeriodNumber() As Long` [R/W] property PeriodNumber
- `Public Property PeriodType() As EcmActionPeriodTypeEnum` [R/W] property PeriodType
- `Public Property PeriodYear() As Long` [R/W] property PeriodYear
- `Public Property Protocol() As String` [R/W] property Protocol
- `Public Property ReportID() As String` [R/W] property ReportID
- `Public Property SourceObject() As Long` [R/W] property SourceObject
- `Public Property SourceType() As String` [R/W] property SourceType
- `Public Property Status() As EcmActionStatusEnum` [R/W] property Status
- `Public Property Submits() As Long` [R/W] property Submits
- `Public Property Type() As EcmActionTypeEnum` [R/W] property Type
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
