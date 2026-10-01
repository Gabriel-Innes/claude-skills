<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PM_ProjectDocumentData (Object)

Source table: OPMG.

## Properties (31)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property AllowSubprojects() As BoYesNoEnum` [R/W] property AllowSubprojects
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BusinessPartner() As String` [R/W] property BusinessPartner
- `Public Property BusinessPartnerName() As String` [R/W] property BusinessPartnerName
- `Public Property ClosingDate() As Date` [R/W] property ClosingDate
- `Public Property ContactPerson() As Long` [R/W] property ContactPerson
- `Public Property DocNum() As Long` [R] property DocNum
- `Public Property DueDate() As Date` [R/W] property DueDate
- `Public Property FinancialProject() As String` [R/W] property FinancialProject
- `Public Property FinishedPercent() As Double` [R/W] property FinishedPercent
- `Public Property Industry() As Long` [R/W] property Industry
- `Public Property Owner() As Long` [R/W] property Owner
- `Public Property PM_ActivitiesCollection() As PM_ActivitiesCollection` [R] property PM_ActivitiesCollection
- `Public Property PM_DocAttachements() As PM_DocAttachements` [R] property PM_DocAttachements
- `Public Property PM_DocumentsCollection() As PM_DocumentsCollection` [R] property PM_DocumentsCollection
- `Public Property PM_OpenIssuesCollection() As PM_OpenIssuesCollection` [R] property PM_OpenIssuesCollection
- `Public Property PM_StageAttachements() As PM_StageAttachements` [R] property PM_StageAttachements
- `Public Property PM_StagesCollection() As PM_StagesCollection` [R] property PM_StagesCollection
- `Public Property PM_SummaryData() As PM_SummaryData` [R] property PM_SummaryData
- `Public Property PM_WorkOrdersCollection() As PM_WorkOrdersCollection` [R] property PM_WorkOrdersCollection
- `Public Property ProjectName() As String` [R/W] property ProjectName
- `Public Property ProjectStatus() As ProjectStatusTypeEnum` [R/W] property ProjectStatus
- `Public Property ProjectType() As ProjectTypeEnum` [R/W] property ProjectType
- `Public Property Reason() As String` [R/W] property Reason
- `Public Property RiskLevel() As RiskLevelTypeEnum` [R/W] property RiskLevel
- `Public Property SalesEmployee() As Long` [R/W] property SalesEmployee
- `Public Property Series() As Long` [R] property Series
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property Territory() As Long` [R/W] property Territory
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
