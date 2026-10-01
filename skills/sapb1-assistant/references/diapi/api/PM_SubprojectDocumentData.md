<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PM_SubprojectDocumentData (Object)

Source table: OPHA.

## Properties (25)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property ActualCost() As Double` [R/W] property ActualCost
- `Public Property DueDate() As Date` [R/W] property DueDate
- `Public Property FinishedPercent() As Double` [R/W] property FinishedPercent
- `Public Property Order() As Long` [R/W] property Order
- `Public Property Owner() As Long` [R/W] property Owner
- `Public Property ParentID() As Long` [R/W] property ParentID
- `Public Property PlannedCost() As Double` [R/W] property PlannedCost
- `Public Property PMS_ActivitiesCollection() As PMS_ActivitiesCollection` [R] property PMS_ActivitiesCollection
- `Public Property PMS_DocAttachements() As PMS_DocAttachements` [R] property PMS_DocAttachements
- `Public Property PMS_DocumentsCollection() As PMS_DocumentsCollection` [R] property PMS_DocumentsCollection
- `Public Property PMS_OpenIssuesCollection() As PMS_OpenIssuesCollection` [R] property PMS_OpenIssuesCollection
- `Public Property PMS_StageAttachements() As PMS_StageAttachements` [R] property PMS_StageAttachements
- `Public Property PMS_StagesCollection() As PMS_StagesCollection` [R] property PMS_StagesCollection
- `Public Property PMS_SummaryData() As PMS_SummaryData` [R] property PMS_SummaryData
- `Public Property PMS_WorkOrdersCollection() As PMS_WorkOrdersCollection` [R] property PMS_WorkOrdersCollection
- `Public Property ProjectID() As Long` [R/W] property ProjectID
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property SubprojectContribution() As Double` [R/W] property SubprojectContribution
- `Public Property SubprojectDepth() As Long` [R] property SubprojectDepth
- `Public Property SubprojectEndDate() As Date` [R/W] property SubprojectEndDate
- `Public Property SubprojectName() As String` [R/W] property SubprojectName
- `Public Property SubprojectStatus() As SubprojectStatusTypeEnum` [R/W] property SubprojectStatus
- `Public Property SubprojectType() As Long` [R/W] property SubprojectType
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
