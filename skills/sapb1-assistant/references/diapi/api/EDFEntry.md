<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EDFEntry (Object)

EDFEntry Class

## Properties (40)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property AssignedID() As String` [R/W] property AssignedID
- `Public Property Authority() As String` [R/W] property Authority
- `Public Property BranchID() As Long` [R/W] property BranchID
- `Public Property CancellationStatus() As ElectronicDocumentEntryCancellationStatusEnum` [R/W] property CancellationStatus
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property CreateDate() As Date` [R] property CreateDate
- `Public Property CreateTime() As Long` [R] property CreateTime
- `Public Property Description() As String` [R/W] property Description
- `Public Property DocBatchID() As String` [R/W] property DocBatchID
- `Public Property DocBatchIndex() As Long` [R/W] property DocBatchIndex
- `Public Property EDocNum() As String` [R/W] property EDocNum
- `Public Property EDocType() As Long` [R/W] property EDocType
- `Public Property Environment() As Long` [R/W] property Environment
- `Public Property GenerationType() As ElectronicDocGenTypeEnum` [R/W] property GenerationType
- `Public Property Guid() As String` [R/W] property GUID
- `Public Property IsCancelation() As BoYesNoEnum` [R] property IsCancelation
- `Public Property IsRemoved() As BoYesNoEnum` [R] property IsRemoved
- `Public Property Message() As String` [R/W] property Message
- `Public Property ObjectID() As String` [R/W] property ObjectID
- `Public Property ParentAbsEntry() As Long` [R/W] property ParentAbsEntry
- `Public Property PeriodDateFrom() As Date` [R/W] property PeriodDateFrom
- `Public Property PeriodDateTo() As Date` [R/W] property PeriodDateTo
- `Public Property PeriodNumber() As Long` [R/W] property PeriodNumber
- `Public Property PeriodType() As ElectronicDocumentEntryPeriodTypeEnum` [R/W] property PeriodType
- `Public Property PeriodYear() As Long` [R/W] property PeriodYear
- `Public Property ProcessingTarget() As String` [R/W] property ProcessingTarget
- `Public Property ReportID() As String` [R/W] property ReportID
- `Public Property ScheduledJobID() As Long` [R/W] property ScheduledJobID
- `Public Property SrcAbsEntry() As Long` [R/W] property SrcAbsEntry
- `Public Property SrcObjType() As String` [R/W] property SrcObjType
- `Public Property Status() As ElectronicDocumentEntryStatusEnum` [R/W] property Status
- `Public Property Submits() As Long` [R/W] property Submits
- `Public Property TestMode() As BoYesNoEnum` [R/W] property TestMode
- `Public Property Type() As ElectronicDocumentEntryTypeEnum` [R/W] property Type
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Long` [R] property UpdateTime
- `Public Property User() As Long` [R] property User
- `Public Property User2() As Long` [R] property User2
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
