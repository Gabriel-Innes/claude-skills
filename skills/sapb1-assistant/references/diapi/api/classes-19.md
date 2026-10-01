<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# PM_DocumentData (Object)

Source table: PMG4.

## Properties (12)
- `Public Property AmountCategory() As AmountCatTypeEnum` [R] property AmountCategory
- `Public Property Categorize() As PMCategorizeTypeEnum` [R/W] property Categorize
- `Public Property DocDate() As Date` [R] property DocDate
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property DocType() As PMDocumentTypeEnum` [R/W] property DocType
- `Public Property LineId() As Long` [R] property LineID
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property Operation() As PMOperationTypeEnum` [R/W] property Operation
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property Status() As LineStatusTypeEnum` [R] property Status
- `Public Property Total() As Double` [R] property Total
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

# PM_DocumentsCollection (Collection)

PM_DocumentsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PM_DocumentData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_DocumentData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

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

# PM_OpenIssuesCollection (Collection)

PM_OpenIssuesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PM_OpenIssueData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_OpenIssueData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

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

# PM_ProjectDocumentParams (Object)

Source table: OPMG.AbsEntry.

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_StageAttachement (Object)

Source table: PMG1.AtcEntry.

## Properties (6)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property AttachementDate() As Date` [R/W] property AttachementDate
- `Public Property FileExtension() As String` [R/W] property FileExtension
- `Public Property FileName() As String` [R/W] property FileName
- `Public Property LineId() As Long` [R] property LineID
- `Public Property SourcePath() As String` [R/W] property SourcePath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_StageAttachements (Collection)

PM_StageAttachements Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PM_StageAttachement` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_StageAttachement` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_StageData (Object)

Source table: PMG1.

## Properties (31)
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property CloseDate() As Date` [R/W] property CloseDate
- `Public Property DependsOnStage1() As Long` [R/W] property DependsOnStage1
- `Public Property DependsOnStage2() As Long` [R/W] property DependsOnStage2
- `Public Property DependsOnStage3() As Long` [R/W] property DependsOnStage3
- `Public Property DependsOnStage4() As Long` [R/W] property DependsOnStage4
- `Public Property DependsOnStageID1() As Long` [R/W] property DependsOnStageID1
- `Public Property DependsOnStageID2() As Long` [R/W] property DependsOnStageID2
- `Public Property DependsOnStageID3() As Long` [R/W] property DependsOnStageID3
- `Public Property DependsOnStageID4() As Long` [R/W] property DependsOnStageID4
- `Public Property Description() As String` [R/W] property Description
- `Public Property ExpectedCosts() As Double` [R/W] property ExpectedCosts
- `Public Property FinishedDate() As Date` [R/W] property FinishedDate
- `Public Property InvoicedAmountPurchase() As Double` [R/W] property InvoicedAmountPurchase
- `Public Property InvoicedAmountSales() As Double` [R/W] property InvoicedAmountSales
- `Public Property IsFinished() As BoYesNoEnum` [R/W] property IsFinished
- `Public Property LineId() As Long` [R] property LineID
- `Public Property OpenAmountPurchase() As Double` [R/W] property OpenAmountPurchase
- `Public Property OpenAmountSales() As Double` [R/W] property OpenAmountSales
- `Public Property PercentualCompletness() As Double` [R/W] property PercentualCompletness
- `Public Property StageDependency1Type() As StageDepTypeEnum` [R/W] property StageDependency1Type
- `Public Property StageDependency2Type() As StageDepTypeEnum` [R/W] property StageDependency2Type
- `Public Property StageDependency3Type() As StageDepTypeEnum` [R/W] property StageDependency3Type
- `Public Property StageDependency4Type() As StageDepTypeEnum` [R/W] property StageDependency4Type
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property StageOwner() As Long` [R/W] property StageOwner
- `Public Property StageType() As Long` [R/W] property StageType
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property Task() As Long` [R/W] property Task
- `Public Property UniqueID() As String` [R/W] property UniqueID
- `Public Property UserFields() As Fields` [R] User defined fields for Project Management stage.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_StagesCollection (Collection)

PM_StagesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PM_StageData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_StageData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

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

# PM_SubprojectDocumentParams (Object)

Source table: OPHA.AbsEntry.

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_SubprojectDocumentsCollection (Collection)

PM_SubprojectDocumentsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PM_SubprojectDocumentParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_SubprojectDocumentParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_SubprojectParams (Object)

Source table: OPMG/OPHA.AbsEntry + IsSubproject.

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property IsSubproject() As BoYesNoEnum` [R/W] property IsSubproject

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_SummaryData (Object)

PM_SummaryData Class

## Properties (34)
- `Public Property AccumInvoicedAmountPurchase() As Double` [R] property AccumInvoicedAmountPurchase
- `Public Property AccumInvoicedAmountSales() As Double` [R] property AccumInvoicedAmountSales
- `Public Property AccumOpenAmountPurchase() As Double` [R] property AccumOpenAmountPurchase
- `Public Property AccumOpenAmountSales() As Double` [R] property AccumOpenAmountSales
- `Public Property AccumPotentialSubprojectAmount() As Double` [R] property AccumPotentialSubprojectAmount
- `Public Property AccumSubprojectBudget() As Double` [R] property AccumSubprojectBudget
- `Public Property AccumTotalPurchase() As Double` [R] property AccumTotalPurchase
- `Public Property AccumTotalSales() As Double` [R] property AccumTotalSales
- `Public Property AccumTotalVariancePurchase() As Double` [R] property AccumTotalVariancePurchase
- `Public Property AccumTotalVarianceSales() As Double` [R] property AccumTotalVarianceSales
- `Public Property AccumVariancePerceptionPurchase() As Double` [R] property AccumVariancePerceptionPurchase
- `Public Property AccumVariancePerceptionSales() As Double` [R] property AccumVariancePerceptionSales
- `Public Property ActualAdditionalCost() As Double` [R] property ActualAdditionalCost
- `Public Property ActualByProductCost() As Double` [R] property ActualByProductCost
- `Public Property ActualClosingDate() As Date` [R] property ActualClosingDate
- `Public Property ActualItemComponentCost() As Double` [R] property ActualItemComponentCost
- `Public Property ActualProductCost() As Double` [R] property ActualProductCost
- `Public Property ActualResourceComponentCost() As Double` [R] property ActualResourceComponentCost
- `Public Property DueDate() As Date` [R] property DueDate
- `Public Property LineId() As Long` [R] property LineID
- `Public Property Overdue() As Long` [R] property Overdue
- `Public Property PotentialSubprojectAmount() As Double` [R/W] property PotentialSubprojectAmount
- `Public Property SubprojectBudget() As Double` [R] property SubprojectBudget
- `Public Property SumInvoicedAmountPurchase() As Double` [R] property SumInvoicedAmountPurchase
- `Public Property SumInvoicedAmountSales() As Double` [R] property SumInvoicedAmountSales
- `Public Property SumOpenAmountPurchase() As Double` [R] property SumOpenAmountPurchase
- `Public Property SumOpenAmountSales() As Double` [R] property SumOpenAmountSales
- `Public Property TotalAmountPurchase() As Double` [R] property TotalAmountPurchase
- `Public Property TotalAmountSales() As Double` [R] property TotalAmountSales
- `Public Property TotalVariance() As Double` [R] property TotalVariance
- `Public Property TotalVariancePurchase() As Double` [R] property TotalVariancePurchase
- `Public Property TotalVarianceSales() As Double` [R] property TotalVarianceSales
- `Public Property VariancePerceptionPurchase() As Double` [R] property VariancePerceptionPurchase
- `Public Property VariancePerceptionSales() As Double` [R] property VariancePerceptionSales

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_TimeSheetData (Object)

PM_TimeSheetData Class

## Properties (14)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property DateFrom() As Date` [R/W] property DateFrom
- `Public Property Dateto() As Date` [R/W] property DateTo
- `Public Property Department() As Long` [R/W] property Department
- `Public Property DocNumber() As Long` [R] property DocNumber
- `Public Property FirstName() As String` [R/W] property FirstName
- `Public Property LastName() As String` [R/W] property LastName
- `Public Property PM_TimeSheetLineDataCollection() As PM_TimeSheetLineDataCollection` [R] property PM_TimeSheetLineDataCollection
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property TimeSheetType() As TimeSheetTypeEnum` [R/W] property TimeSheetType
- `Public Property UserCode() As String` [R/W] property UserCode
- `Public Property UserFields() As Fields` [R] property User Fields
- `Public Property UserID() As Long` [R/W] property UserID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

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

# PM_TimeSheetLineDataCollection (Collection)

PM_TimeSheetLineDataCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As PM_TimeSheetLineData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_TimeSheetLineData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PM_TimeSheetParams (Object)

PM_TimeSheetParams Class

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

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

# PM_WorkOrdersCollection (Collection)

PM_WorkOrdersCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PM_WorkOrderData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PM_WorkOrderData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_ActivityCollection (Collection)

PMC_ActivityCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMC_ActivityData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMC_ActivityData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_ActivityData (Object)

PMC_ActivityData Class

## Properties (5)
- `Public Property ActivityID() As Long` [R/W] property ActivityID
- `Public Property ActivityType() As String` [R/W] property ActivityType
- `Public Property IsAbsence() As BoYesNoEnum` [R/W] property IsAbsence
- `Public Property IsChargeable() As BoYesNoEnum` [R/W] property IsChargeable
- `Public Property LaborItem() As String` [R/W] property LaborItem

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_AreaCollection (Collection)

PMC_AreaCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMC_AreaData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMC_AreaData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_AreaData (Object)

PMC_AreaData Class

## Properties (2)
- `Public Property AreaID() As Long` [R/W] property AreaID
- `Public Property AreaName() As String` [R/W] property AreaName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_PriorityCollection (Collection)

PMC_PriorityCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMC_PriorityData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMC_PriorityData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_PriorityData (Object)

PMC_PriorityData Class

## Properties (2)
- `Public Property PriorityID() As Long` [R/W] property PriorityID
- `Public Property PriorityName() As String` [R/W] property PriorityName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_StageTypeCollection (Collection)

PMC_StageTypeCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMC_StageTypeData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMC_StageTypeData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_StageTypeData (Object)

PMC_StageTypeData Class

## Properties (3)
- `Public Property StageDescription() As String` [R/W] property StageDescription
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property StageName() As String` [R/W] property StageName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_SubprojectTypeData (Object)

PMC_SubprojectTypeData Class

## Properties (2)
- `Public Property SubprojectTypeID() As Long` [R/W] property SubprojectTypeID
- `Public Property SubprojectTypeName() As String` [R/W] property SubprojectTypeName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_SubprojectTypesCollection (Collection)

PMC_SubprojectTypesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMC_SubprojectTypeData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMC_SubprojectTypeData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_TaskCollection (Collection)

PMC_TaskCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMC_TaskData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMC_TaskData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMC_TaskData (Object)

PMC_TaskData Class

## Properties (2)
- `Public Property TaskID() As Long` [R/W] property TaskID
- `Public Property TaskName() As String` [R/W] property TaskName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_ActivitiesCollection (Collection)

PMS_ActivitiesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMS_ActivityData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMS_ActivityData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_ActivityData (Object)

Source table: PHA6.

## Properties (4)
- `Public Property ActivityID() As Long` [R/W] property ActivityID
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

# PMS_DocAttachement (Object)

Source table: OPHA.AtcEntry.

## Properties (6)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property AttachementDate() As Date` [R/W] property AttachementDate
- `Public Property FileExtension() As String` [R/W] property FileExtension
- `Public Property FileName() As String` [R/W] property FileName
- `Public Property LineId() As Long` [R] property LineID
- `Public Property SourcePath() As String` [R/W] property SourcePath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_DocAttachements (Collection)

PMS_DocAttachements Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMS_DocAttachement` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMS_DocAttachement` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_DocumentData (Object)

Source table: PHA4.

## Properties (12)
- `Public Property AmountCategory() As AmountCatTypeEnum` [R] property AmountCategory
- `Public Property Categorize() As PMCategorizeTypeEnum` [R/W] property Categorize
- `Public Property DocDate() As Date` [R] property DocDate
- `Public Property DocEntry() As Long` [R/W] property DocEntry
- `Public Property DocType() As PMDocumentTypeEnum` [R/W] property DocType
- `Public Property LineId() As Long` [R] property LineID
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property Operation() As PMOperationTypeEnum` [R/W] property Operation
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property Status() As LineStatusTypeEnum` [R] property Status
- `Public Property Total() As Double` [R] property Total
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

# PMS_DocumentsCollection (Collection)

PMS_DocumentsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMS_DocumentData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMS_DocumentData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_OpenIssueData (Object)

Source table: PHA2.

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

# PMS_OpenIssuesCollection (Collection)

PMS_OpenIssuesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMS_OpenIssueData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMS_OpenIssueData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_StageAttachement (Object)

Source table: PHA1.AtcEntry.

## Properties (6)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property AttachementDate() As Date` [R/W] property AttachementDate
- `Public Property FileExtension() As String` [R/W] property FileExtension
- `Public Property FileName() As String` [R/W] property FileName
- `Public Property LineId() As Long` [R] property LineID
- `Public Property SourcePath() As String` [R/W] property SourcePath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_StageAttachements (Collection)

PMS_StageAttachements Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMS_StageAttachement` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMS_StageAttachement` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_StageData (Object)

Source table: PHA1.

## Properties (31)
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property CloseDate() As Date` [R/W] property CloseDate
- `Public Property DependsOnStage1() As Long` [R/W] property DependsOnStage1
- `Public Property DependsOnStage2() As Long` [R/W] property DependsOnStage2
- `Public Property DependsOnStage3() As Long` [R/W] property DependsOnStage3
- `Public Property DependsOnStage4() As Long` [R/W] property DependsOnStage4
- `Public Property DependsOnStageID1() As Long` [R/W] property DependsOnStageID1
- `Public Property DependsOnStageID2() As Long` [R/W] property DependsOnStageID2
- `Public Property DependsOnStageID3() As Long` [R/W] property DependsOnStageID3
- `Public Property DependsOnStageID4() As Long` [R/W] property DependsOnStageID4
- `Public Property Description() As String` [R/W] property Description
- `Public Property ExpectedCosts() As Double` [R/W] property ExpectedCosts
- `Public Property FinishedDate() As Date` [R/W] property FinishedDate
- `Public Property InvoicedAmountPurchase() As Double` [R/W] property InvoicedAmountPurchase
- `Public Property InvoicedAmountSales() As Double` [R/W] property InvoicedAmountSales
- `Public Property IsFinished() As BoYesNoEnum` [R/W] property IsFinished
- `Public Property LineId() As Long` [R] property LineID
- `Public Property OpenAmountPurchase() As Double` [R/W] property OpenAmountPurchase
- `Public Property OpenAmountSales() As Double` [R/W] property OpenAmountSales
- `Public Property PercentualCompletness() As Double` [R/W] property PercentualCompletness
- `Public Property StageDependency1Type() As StageDepTypeEnum` [R/W] property StageDependency1Type
- `Public Property StageDependency2Type() As StageDepTypeEnum` [R/W] property StageDependency2Type
- `Public Property StageDependency3Type() As StageDepTypeEnum` [R/W] property StageDependency3Type
- `Public Property StageDependency4Type() As StageDepTypeEnum` [R/W] property StageDependency4Type
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property StageOwner() As Long` [R/W] property StageOwner
- `Public Property StageType() As Long` [R/W] property StageType
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property Task() As Long` [R/W] property Task
- `Public Property UniqueID() As String` [R/W] property UniqueID
- `Public Property UserFields() As Fields` [R] User defined fields for Project Management subproject stage.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_StagesCollection (Collection)

PMS_StagesCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMS_StageData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMS_StageData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_SummaryData (Object)

Source table: PHA8.

## Properties (34)
- `Public Property AccumInvoicedAmountPurchase() As Double` [R] property AccumInvoicedAmountPurchase
- `Public Property AccumInvoicedAmountSales() As Double` [R] property AccumInvoicedAmountSales
- `Public Property AccumOpenAmountPurchase() As Double` [R] property AccumOpenAmountPurchase
- `Public Property AccumOpenAmountSales() As Double` [R] property AccumOpenAmountSales
- `Public Property AccumPotentialSubprojectAmount() As Double` [R] property AccumPotentialSubprojectAmount
- `Public Property AccumSubprojectBudget() As Double` [R] property AccumSubprojectBudget
- `Public Property AccumTotalPurchase() As Double` [R] property AccumTotalPurchase
- `Public Property AccumTotalSales() As Double` [R] property AccumTotalSales
- `Public Property AccumTotalVariancePurchase() As Double` [R] property AccumTotalVariancePurchase
- `Public Property AccumTotalVarianceSales() As Double` [R] property AccumTotalVarianceSales
- `Public Property AccumVariancePerceptionPurchase() As Double` [R] property AccumVariancePerceptionPurchase
- `Public Property AccumVariancePerceptionSales() As Double` [R] property AccumVariancePerceptionSales
- `Public Property ActualAdditionalCost() As Double` [R] property ActualAdditionalCost
- `Public Property ActualByProductCost() As Double` [R] property ActualByProductCost
- `Public Property ActualClosingDate() As Date` [R] property ActualClosingDate
- `Public Property ActualItemComponentCost() As Double` [R] property ActualItemComponentCost
- `Public Property ActualProductCost() As Double` [R] property ActualProductCost
- `Public Property ActualResourceComponentCost() As Double` [R] property ActualResourceComponentCost
- `Public Property DueDate() As Date` [R] property DueDate
- `Public Property LineId() As Long` [R] property LineID
- `Public Property Overdue() As Long` [R] property Overdue
- `Public Property PotentialSubprojectAmount() As Double` [R/W] property PotentialSubprojectAmount
- `Public Property SubprojectBudget() As Double` [R] property SubprojectBudget
- `Public Property SumInvoicedAmountPurchase() As Double` [R] property SumInvoicedAmountPurchase
- `Public Property SumInvoicedAmountSales() As Double` [R] property SumInvoicedAmountSales
- `Public Property SumOpenAmountPurchase() As Double` [R] property SumOpenAmountPurchase
- `Public Property SumOpenAmountSales() As Double` [R] property SumOpenAmountSales
- `Public Property TotalAmountPurchase() As Double` [R] property TotalAmountPurchase
- `Public Property TotalAmountSales() As Double` [R] property TotalAmountSales
- `Public Property TotalVariance() As Double` [R] property TotalVariance
- `Public Property TotalVariancePurchase() As Double` [R] property TotalVariancePurchase
- `Public Property TotalVarianceSales() As Double` [R] property TotalVarianceSales
- `Public Property VariancePerceptionPurchase() As Double` [R] property VariancePerceptionPurchase
- `Public Property VariancePerceptionSales() As Double` [R] property VariancePerceptionSales

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PMS_WorkOrderData (Object)

Source table: PHA7.

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

# PMS_WorkOrdersCollection (Collection)

PMS_WorkOrdersCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PMS_WorkOrderData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PMS_WorkOrderData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# POSDailySummary (Object)

POSDailySummary Class

## Properties (11)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property COFINSTotal() As Double` [R/W] property COFINSTotal
- `Public Property CounterPosition() As Long` [R/W] property CounterPosition
- `Public Property Date() As Date` [R/W] property Date
- `Public Property EquipmentNo() As String` [R/W] property EquipmentNo
- `Public Property GrossSales() As Double` [R/W] property GrossSales
- `Public Property OperationCounter() As Long` [R/W] property OperationCounter
- `Public Property PISTotal() As Double` [R/W] property PISTotal
- `Public Property POSTotalizerCollection() As POSTotalizerCollection` [R] property POSTotalizerCollection
- `Public Property ResetCounterPosition() As Long` [R/W] property ResetCounterPosition
- `Public Property Total() As Double` [R/W] property Total

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# POSDailySummaryParams (Object)

POSDailySummaryParams Class

## Properties (1)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# POSDailySummaryService (Object)

POSDailySummaryService Class

## Methods (7)
- `Public Function Add(ByVal pIPOSDailySummary As POSDailySummary) As POSDailySummaryParams` Add
  - param `pIPOSDailySummary`: 
- `Public Sub Delete(ByVal pIPOSDailySummaryParams As POSDailySummaryParams)` Delete
  - param `pIPOSDailySummaryParams`: 
- `Public Function Get(ByVal pIPOSDailySummaryParams As POSDailySummaryParams) As POSDailySummary` Get
  - param `pIPOSDailySummaryParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As POSDailySummaryServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `POSDailySummaryServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Sub Update(ByVal pIPOSDailySummary As POSDailySummary)` Update
  - param `pIPOSDailySummary`: 

# PostingTemplates (Object)

PostingTemplates Class

## Properties (7)
- `Public Property AutomaticVAT() As BoYesNoEnum` [R/W] property AutomaticVAT
- `Public Property Code() As String` [R/W] property Code
- `Public Property DeferredTax() As BoYesNoEnum` [R/W] property DeferredTax
- `Public Property Description() As String` [R/W] property Description
- `Public Property ManageWTax() As BoYesNoEnum` [R/W] property ManageWTax
- `Public Property PostingTemplatesLineCollection() As PostingTemplatesLineCollection` [R] property PostingTemplatesLineCollection
- `Public Property StampTax() As BoYesNoEnum` [R/W] property StampTax

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PostingTemplatesLine (Object)

PostingTemplatesLine Class

## Properties (21)
- `Public Property AccountCode() As String` [R/W] property AccountCode
- `Public Property AccountName() As String` [R/W] property AccountName
- `Public Property ControlAccount() As String` [R/W] property ControlAccount
- `Public Property CostElementCode() As String` [R] property CostElementCode
- `Public Property CostingCode1() As String` [R/W] property CostingCode1
- `Public Property CostingCode2() As String` [R/W] property CostingCode2
- `Public Property CostingCode3() As String` [R/W] property CostingCode3
- `Public Property CostingCode4() As String` [R/W] property CostingCode4
- `Public Property CostingCode5() As String` [R/W] property CostingCode5
- `Public Property Credit() As Double` [R/W] property Credit
- `Public Property Debit() As Double` [R/W] property Debit
- `Public Property DistributionRule() As String` [R/W] property DistributionRule
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ProjectCode() As String` [R/W] property ProjectCode
- `Public Property TaxCode() As String` [R/W] property TaxCode
- `Public Property TaxGroup() As String` [R/W] property TaxGroup
- `Public Property TaxPostingAccount() As BoTaxPostingAccountTypeEnum` [R/W] property TaxPostingAccount
- `Public Property TrtCode() As String` [R] property TrtCode
- `Public Property VatLine() As BoYesNoEnum` [R/W] property VatLine
- `Public Property WTaxLiable() As BoYesNoEnum` [R/W] property WTaxLiable
- `Public Property WTaxLine() As BoYesNoEnum` [R/W] property WTaxLine

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PostingTemplatesLineCollection (Collection)

PostingTemplatesLineCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As PostingTemplatesLine` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PostingTemplatesLine` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PostingTemplatesParams (Object)

PostingTemplatesParams Class

## Properties (2)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PostingTemplatesParamsCollection (Collection)

PostingTemplatesParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As PostingTemplatesParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As PostingTemplatesParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PostingTemplatesService (Object)

PostingTemplatesService Class

## Methods (8)
- `Public Function Add(ByVal pIPostingTemplates As PostingTemplates) As PostingTemplatesParams` Add
  - param `pIPostingTemplates`: 
- `Public Sub Delete(ByVal pIPostingTemplatesParams As PostingTemplatesParams)` Delete
  - param `pIPostingTemplatesParams`: 
- `Public Function Get(ByVal pIPostingTemplatesParams As PostingTemplatesParams) As PostingTemplates` Get
  - param `pIPostingTemplatesParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As PostingTemplatesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `PostingTemplatesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As PostingTemplatesParamsCollection` GetList
- `Public Sub Update(ByVal pIPostingTemplates As PostingTemplates)` Update
  - param `pIPostingTemplates`: 

# POSTotalizer (Object)

POSTotalizer Class

## Properties (5)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property LineNum() As Long` [R] property LineNum
- `Public Property Number() As Long` [R/W] property Number
- `Public Property Total() As Double` [R/W] property Total

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# POSTotalizerCollection (Collection)

POSTotalizerCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As POSTotalizer` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As POSTotalizer` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# PredefinedText (Object)

Represents a predefined text. Source table: OPDT Mandatory properties: TextCode

## Properties (3)
- `Public Property Numerator() As Long` [R] The key of the predefined text. Field name: AbsEntry
- `Public Property Text() As String` [R/W] The text to be saved for display in marketing documents. The field must contain at least one non-space character and must be a valid key string (i.e., it cannot contain *,{,},%,!,^,=,<,>,?,|). Field name: Text
- `Public Property TextCode() As String` [R/W] The display name for the predefined text. The field must contain at least one non-space character and must be a valid key string (i.e., it cannot contain *,{,},%,!,^,=,<,>,?,|). Field name: TextCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# PredefinedTextParams (Object)

Holds the key and name to an existing predefined text. This object is used to pass keys to and retrieve keys from PredefinedTextsService methods.

## Properties (2)
- `Public Property Numerator() As Long` [R/W] The key for a specific text. Field name: AbsEntry
- `Public Property TextCode() As String` [R] The text to be saved for use in marketing documents. Field name: Text

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# PredefinedTextsParams (Collection)

A collection of PredefinedTextParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As PredefinedTextParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As PredefinedTextParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# PredefinedTextsService (Object)

The PredefinedTextsService service enables you to add, look up and remove predefined texts in the predefined texts master data table. Predefined texts are stored text strings that can be added as remarks in marketing documents. To see the list of predefined texts, select Administration --> Setup --> General --> Predefined Text. You can also view a table of all predefined texts by opening a marketing document, selecting Goto --> Opening and Closing Remarks, and clicking Insert Predefined Texts. Source table: OPDT

## Methods (8)
- `Public Function AddPredefinedText(ByVal pIPredefinedText As PredefinedText) As PredefinedTextParams` Adds a predefined text.
  - param `pIPredefinedText`: The data for the new predefined text.
  - returns: The key (AbsEntry) of the new predefined text.
  - C# example (from SAP's help):
    ```csharp
    // Get predefined text service
    PredefinedTextsService textService;
    companyService = company.GetCompanyService();
    textService = (PredefinedTextsService)companyService.GetBusinessService(ServiceTypes.PredefinedTextsService);

    // Add predefined text
    PredefinedText text = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedText) As PredefinedText;
    text.TextCode = "Thank you";
    text.Text = "Thank you for using our products.";
    textService.AddPredefinedText(text);
    ```
- `Public Sub DeletePredefinedText(ByVal pIPredefinedTextParams As PredefinedTextParams)` Deletes an existing predefined text. The predefined text is specified by its key (AbsEntry), which is contained in the PredefinedTextParams object passed to the method.
  - param `pIPredefinedTextParams`: The key of the predefined text to be deleted.
  - C# example (from SAP's help):
    ```csharp
    // Get predefined text service
    PredefinedTextsService textService;
    companyService = company.GetCompanyService();
    textService = (PredefinedTextsService)companyService.GetBusinessService(ServiceTypes.PredefinedTextsService);

    PredefinedText text = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedText) as PredefinedText;
    PredefinedTextParams textParams = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedTextParams) as PredefinedTextParams;

    // Specify the key of the predefined text to delete
    textParams.Numerator = 2;

    // Delete text
    textService.DeletePredefinedText(textParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As PredefinedTextsServiceDataInterfaces) As Object` Creates an empty data structure for use with the PredefinedTextsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `PredefinedTextsServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
- `Public Function GetPredefinedText(ByVal pIPredefinedTextParams As PredefinedTextParams) As PredefinedText` Retrieves a predefined text. The predefined text is specified by its key (AbsEntry), which is contained in the PredefinedTextParams object passed to the method.
  - param `pIPredefinedTextParams`: The key of the predefined text to retrieve.
  - returns: The predefined text with the specified key.
- `Public Function GetPredefinedTextList() As PredefinedTextsParams` Retrieves the keys and names of all the predefined texts.
  - C# example (from SAP's help):
    ```csharp
    // Get list of predefined text
    PredefinedTextsParams textsParams = textService.GetPredefinedTextList();

    int i = 1;

    // Print the list
    foreach (PredefinedTextParams textParams In textsParams)
    {
        Console.WriteLine("item {0}: Numerator:{1}, TextCode:{2}", i++, textParams.Numerator, textParams.TextCode);
    }
    ```
- `Public Sub UpdatePredefinedText(ByVal pIPredefinedText As PredefinedText)` Updates an existing predefined text. The data for the predefined text, including the key of the predefined text to be updated, is contained in the PredefinedText passed to the method. To update a predefined text, you must first retrieve it using the GetPredefinedText method.
  - param `pIPredefinedText`: The data for the predefined text to be updated. The PredefinedText object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    // Get predefined text service
    PredefinedTextsService textService;
    companyService = company.GetCompanyService();
    textService = (PredefinedTextsService)companyService.GetBusinessService(ServiceTypes.PredefinedTextsService);

    PredefinedText text = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedText) as PredefinedText;
    PredefinedTextParams textParams = textService.GetDataInterface(PredefinedTextsServiceDataInterfaces.ptsPredefinedTextParams) as PredefinedTextParams;

    // Get the predefined text to update
    textParams.Numerator = 2;
    PredefinedText text = textService.GetPredefinedText(textParams);

    // Update text
    text.Text = "new Text";
    textService.UpdatePredefinedText(text);
    ```

# PriceLists (Object)

PriceLists is a business object that represents the management of price lists in the Inventory module. A price list is used by Items_Prices object to set the item prices. An item can have several prices, with each based on a different price list, for example, purchase price list, sales price list, distributor price list, and so on. This object enables you to: - Add a price list. - Retrieve a price list by its key. - Update a price list. - Delete a price list. - Save the object in XML format. Source table: OPLN.

**Remarks:** To display the form in the application: - Select Inventory --> Price Lists --> Price Lists.

## Properties (19)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property BasePriceList() As Long` [R/W] Sets or returns the base price list on which the price list (PriceListName) is based. Field name: BASE_NUM.
  - remarks: The base price lists are defined in the ASHP table which is not exposed through the DI API.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DefaultAdditionalCurrency1() As String` [R/W] property DefaultAdditionalCurrency1
- `Public Property DefaultAdditionalCurrency2() As String` [R/W] property DefaultAdditionalCurrency2
- `Public Property DefaultPrimeCurrency() As String` [R/W] property DefaultPrimeCurrency
- `Public Property Factor() As Double` [R/W] Sets or returns the factor for calculating prices of items based on the specified price list. Field name: Factor.
  - remarks: An item price (that is based on PriceListName) equals to the item price (that is based on BasePriceList) multiplied by the Factor.
- `Public Property FixedAmount() As Double` [R/W] property FixedAmount
- `Public Property GroupNum() As BoPriceListGroupNum` [R/W] Sets or returns a valid value of BoPriceListGroupNum type that specifies the group number to which the price list is related. Field name: GroupCode.
  - remarks: In SAP Business One, in General Authorization, you can set the access rights of a user to a price list group for modifying price lists.
- `Public Property IsGrossPrice() As BoYesNoEnum` [R/W] property IsGrossPrice
- `Public Property PriceListName() As String` [R/W] property PriceListName
  - remarks: Sets or returns the price list name (or description). Length: 32 characters. Field name: ListName.
- `Public Property PriceListNo() As Long` [R] Returns the price list unique ID. SAP Business One assigns a sequential number for each price list. Field name: ListNum.
- `Public Property RoundingFormatDecimalPart() As String` [R/W] property RoundingFormatDecimalPart
- `Public Property RoundingFormatIntegerPart() As String` [R/W] property RoundingFormatIntegerPart
- `Public Property RoundingMethod() As BoRoundingMethod` [R/W] Sets or returns a valid value of BoRoundingMethod type that specifies the rounding method of the item price calculation. Field name: RoundSys.
- `Public Property RoundingRule() As BoRoundingRule` [R/W] property RoundingRule
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property ValidFrom() As Date` [R/W] property ValidFrom
- `Public Property ValidTo() As Date` [R/W] property ValidTo

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal QueueID As String) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database. Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `QueueID`: Price list unique ID (PriceListNo).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You cannot delete a price list if it is: - The base price list of another price list. - Associated with a business partner. - Associated with a product tree (ProductTrees) record. - Associated with a payment term type (PaymentTermsTypes) record. You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.

# ProductionOrders (Object)

The ProductionOrders object supports the creation and maintenance of production orders. This object replaces the WorkOrders object of release 2004. During upgrade to 2005, SAP Business One creates production orders based on the data of the existing work orders (OWKO, WKO1). Therefore, you must upgrade add-ons that use the WorkOrders object to use the ProductionOrders object. After the upgrade process work orders can be displayed only but cannot be maintained. Source table: OWOR.

**Remarks:** Mandatory properties for creating a new production order: ItemNo and DueDate. To display the form in the application: - Select Production --> Production Orders.

## Properties (45)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the production order as assigned by SAP Business One when adding one. Field name: DocEntry. Length: 11 characters.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ClosingDate() As Date` [R/W] Returns the date when the production order status is changed to Closed. Field name: CloseDate.
- `Public Property CompletedQuantity() As Double` [R] Returns the total quantity of the completed products that were received from production. Field name: CmpltQty.
  - remarks: The system calculates the total quantity by summing the Quantity of each transaction in IGN1 with the valid value botrntComplete (TransactionType).
- `Public Property CreationDate() As Date` [R] Returns the date of creation of the Production Order. Field name: CreateDate.
- `Public Property CustomerCode() As String` [R/W] Sets or returns the customer code, which is the card code in the business partner master data. Mandatory field in SAP Business One. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
  - remarks: During upgrade, this property retrieves the value from CustomerRefNo (WorkOrders).
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocumentNumber() As Long` [R] Returns the production order number, which is a sequential number, assigned by the system. Field name: DocNum. Length: 11 characters.
  - remarks: During upgrade, the system sets the next available number for the selected series. If the work order includes few rows, then each row is added as a separate production order. The system copies the work order number (OrderNum) to the production order remarks field.
- `Public Property DocumentReferences() As ProductionOrders_DocumentReferences` [R] property DocumentReferences
- `Public Property DueDate() As Date` [R/W] Sets or returns the planned completion date of the production order. The DueDate can be modified (read-write) while the ProductionOrderStatus is either Planned or Released (read-only when the status is Closed). Mandatory for creating a new production order. Field name: DueDate.
  - remarks: During upgrade, if ExpectedCompletionDate (WorkOrders) exists, the system copies it as is to DueDate, otherwise, the system sets the DueDate with the value of PostingDate.
- `Public Property InventoryUOM() As String` [R] Returns the inventory Unit of Measurement for the product (for example: box, case, piece). Field name: Uom. Length: 20 characters
- `Public Property ItemNo() As String` [R/W] Sets or returns the key of the product. Mandatory for creating a new production order. Field name: ItemCode. Length: 20 characters. This is a foreign key to the ProductTrees object.
- `Public Property JournalRemarks() As String` [R/W] Sets or returns the journal remarks for the G/L account that is related to the production order. Field name: JrnlMemo. Length: 50 characters.
- `Public Property Lines() As ProductionOrders_Lines` [R] Returns the ProductionOrders_Lines child object.
- `Public Property PlannedQuantity() As Double` [R/W] Sets or returns the planned quantity of the completed product. Field name: PlannedQty.
  - remarks: When upgrading SAP Business One from release 2004 to 2005, the value of the PlannedQuantity property will be as follows: If the 'Quantity' field in the work order is positive, the system will create a 'Standard' production order type, and the planned quantity will be similar to the work order quantity.If the 'Quantity' field in the work is negative, the system will create a 'Disassembly' production order type, and the planned quantity will be the same as the WO quantity without the minus sign (i.e. -9 will be 9 and order type= disassembly)
- `Public Property PostingDate() As Date` [R/W] Sets or returns the order date of the product. Field name: PostDate.
- `Public Property Printed() As BoYesNoEnum` [R] Returns a valid value that determines wether to use a printed copy or an original . Field name: Printed.
- `Public Property Priority() As Long` [R/W] The degree of importance of a production order, indicated by integer numbers. The default value is 100. You can manually change the number here. The smaller the number, the more important the production order. Field name: Priority.
- `Public Property ProductDescription() As String` [R/W] The descritpion of the product. Field name: ProdName. Length: 100 characters.
- `Public Property ProductionOrderOrigin() As BoProductionOrderOriginEnum` [R/W] Sets or returns the origin type of the production order (Manual, MRP, or Sales Order). Field name: OriginType.
- `Public Property ProductionOrderOriginEntry() As Long` [R/W] Sets or returns the key number of sales order that is linked to the production order. Field name: OriginAbs.
- `Public Property ProductionOrderOriginNumber() As Long` [R] The sales order number that is linked to the production order. Field name: OriginNum.
  - remarks: Only open sales order can be linked to a production order.
- `Public Property ProductionOrderStatus() As BoProductionOrderStatusEnum` [R/W] Sets or returns the status of the production order (Planned, Released, Closed, or Cancelled). Field name: Sets or returns the status of the production order (Planned, Released, Closed, or Cancelled)..
- `Public Property ProductionOrderType() As BoProductionOrderTypeEnum` [R/W] Set or returns the production order type (Standard, Special, or Disassembly). Field name: Type.
- `Public Property Project() As String` [R/W] The project that relates to the components of the product. Field: Project. Length: 20 characters.
- `Public Property RejectedQuantity() As Double` [R] Returns the total quantity of the rejected products that were received from production. Field name: RjctQty.
  - remarks: The system calculates the total quantity by summing the Quantity of each transaction in IGN1 with the valid value botrntReject (TransactionType).
- `Public Property ReleaseDate() As Date` [R] Returns the date when the production order status is changed to Released. Field name: RlsDate.
- `Public Property Remarks() As String` [R/W] Sets or returns remarks related to the production order. Field name: Comments. Length: 254 characters.
  - remarks: When upgrading SAP Business One from release 2004 to 2005, the value of the Remarks property will include the following information: - 'Series - ZZZ' (where: ZZZ is the series description) - 'WO No. XXX' (where: XXX is the old work order number) - 'Ref. No. YYY' (where: YYY is information from Customer Ref. No.) - WO Remarks. Example: 'Series - Primary, WO No. 213. Very important order' in the example, no data were in the ref. no. field'
- `Public Property RoutingDateCalculation() As ResourceAllocationEnum` [R/W] Determines how the resource allocation will occur. Field name: RouDatCalc.
- `Public Property SalesOrderLines() As ProductionOrders_SalesOrderLines` [R] Returns the ProductionOrders_SalesOrderLines object.
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property Series() As Long` [R/W] Sets or returns the key of the series that determines the production order number (DocumentNumber). Field name: Series.
  - remarks: During upgrade, this property retrieves the value from Series (WorkOrders).
- `Public Property Stages() As ProductionOrders_Stages` [R] Returns the ProductionOrders_Stages child object.
- `Public Property StartDate() As Date` [R/W] The start date of the production. You can change it manually, which may affect Due Date. Field name: StartDate.
- `Public Property TransactionNumber() As Long` [R] Returns the transaction code that SAP Business One creates for the production order. Field name: TransId. This is a foreign key to the JournalEntries object.
- `Public Property UoMEntry() As Long` [R] The internal key of the UoM. Field name: UomEntry.
- `Public Property UpdateAllocation() As BoUpdateAllocationEnum` [R/W] property UpdateAllocation
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who manages the production order. Field name: UserSign.
- `Public Property Warehouse() As String` [R/W] Sets or returns the identification key of the warehouse that will receive the completed product. Length: 8 characters. Field name: Warehouse. This is a foreign key to the Warehouses object.

## Methods (7)
- `Public Function Add() As Long` Adds a new record to the table.
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: For vesrions prior to 2007 A, use DocumentNumber property. From version 2007 A, use AbsoluteEntry property. Historically the GetByKey method for production order got the DocumentNumber property Field name: DocNum) as an input, different from any other document that got the DocEntry as an input. Starting from SAP Business One 2007 A release the GetByKey for production order gets as an input the AbsoluteEntry property Field name: DocEntry), like any other document.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# ProductionOrders_DocumentReferences (Object)

ProductionOrders_DocumentReferences Class

## Properties (9)
- `Public Property Count() As Long` [R] property Count
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExtDocNum
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ReferencedDocEntry() As Long` [R/W] property RefDocEntr
- `Public Property ReferencedDocNumber() As Long` [R] property RefDocNum
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property RefObjType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# ProductionOrders_Lines (Object)

The ProductionOrders_Lines is a child object of the ProductionOrders object. Each line represents a component (item) of the product. Source table: WOR1.

**Remarks:** To display the form in the application: - Select Production --> Production Orders.

## Properties (32)
- `Public Property AdditionalQuantity() As Double` [R/W] The value is copied from the Additional Qty field in the Bill of Materials window; however, you can change it manually in the production order. Field name: AdditQty.
  - remarks: Only components of the Manual issue method can have zero Base Qty and the Additional Quantity larger than zero. The additional quantity for by-products is always zero.
- `Public Property BaseQuantity() As Double` [R/W] Sets or returns the quantity of the items required for manufacturing a single product. The default value is retrieved from the Quantity property (ProductTrees object). Field name: BaseQty.
  - remarks: The Base Quantity value of a resource component cannot be less than zero.
- `Public Property BatchNumbers() As BatchNumbers` [R] property BatchNumbers
- `Public Property Count() As Long` [R] Returns the total number of records in the table. Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property DocumentAbsoluteEntry() As Long` [R] Returns the production order number (AbsoluteEntry).
- `Public Property EndDate() As Date` [R/W] The latest date by which a component needs to be used in the production process. Field: EndDate.
- `Public Property IssuedQuantity() As Double` [R] Sets or returns the total items quantity already issued for the production order. That is, BaseQuantity multiplied by PlannedQuantity (ProductionOrders object). Field name: IssuedQty.
- `Public Property ItemName() As String` [R/W] property ItemName
- `Public Property ItemNo() As String` [R/W] Sets or returns the item code in the inventory. Length: 20 characters. Field name: ItemCode. This is a foreign key to the Items object.
- `Public Property ItemType() As ProductionItemType` [R/W] The type of the production item. Field name: ItemType.
- `Public Property LineNumber() As Long` [R] Returns the current row number in the list. Field name: LineNum.
- `Public Property LineText() As String` [R/W] Add text in the line. Field name: LineText. Length: 16 characters.
  - remarks: The text is added automatically from the corresponding line in the Bill of Materials window associated with the parent item.
- `Public Property LocationCode() As Long` [R/W] The location for the items in this line of the production order. Field name: LocCode This is a foreign key to the WarehouseLocations object.
- `Public Property PlannedQuantity() As Double` [R/W] Sets or returns the total items quantity planned to be issued for the production order. For each component line, the value of this field is calculated according to the following formula: (Planned Quantity of the parent * Base Qty of the component) + Additional Qty of the component. Field name: PlannedQty.
- `Public Property ProductionOrderIssueType() As BoIssueMethod` [R/W] Determines the method for issuing the components of the product from the inventory, whether Manual or Backflash(automatic). Field name: IssueType.
  - remarks: Manual - The user issues individual components of a parent item manually. For example, serial or batch-controlled items must be issued manually. Backflash - The system issues the components of a parent item automatically to the production order according to the parent item completion status (ProductionOrderStatus).
- `Public Property Project() As String` [R/W] The project that relates to the components of the product. Field: Project. Length: 20 characters.
- `Public Property RequiredDays() As Double` [R] The number of days required for a specific Resource to complete the Planned Quantity of a particular route stage. This field will be automatically calculated for a production order that has at least one route stage, one resource line, and whose Routing Date Calculation field is either Start Date Forwards or End Date Backwards. Field: ReqDays.
- `Public Property ResourceAllocation() As ResourceAllocationEnum` [R/W] Determines how the resource allocation will occur, for a production order that has route stages. Field name: ResAlloc.
- `Public Property SerialNumbers() As SerialNumbers` [R] property SerialNumbers
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property StartDate() As Date` [R/W] The earliest date on which the component is needed in the production process. Field name: StartDate.
- `Public Property UoMCode() As String` [R] The unique code for the UoM. Field name: UomCode. Length: 20 characters.
- `Public Property UoMEntry() As Long` [R] The internal key of the UoM. Field name: UomEntry.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VisualOrder() As Long` [R] Returns the visual order number. The value for the first row is null, and from the second row the number starts from 1. Field name: VisOrder.
- `Public Property Warehouse() As String` [R/W] Sets or returns the warehouse identification key from which the items are issued. Field name: wareHouse. Length: 8 characters.
- `Public Property WipAccount() As String` [R/W] If the production order lines are populated with components from a BOM, the account defined in the WIP Account field of the BOM for the relevant component populates this field. If theWIP Account field for the relevant component is blank in the BOM, this account is blank, too. You can manually update the account in this field before the production order closure. The value of this field is then copied into the Account Code field of the issue for production. Field name: WipActCode.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: You cannot delete a line if it is the only line in the ProductionOrders object.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ProductionOrders oProdOrder;

    // Delete production order line
    if(oProdOrder.GetByKey(0) == true)
    {
        oProdOrder.Lines.SetCurrentLine(0);
        oProdOrder.Lines.Delete();
        oProdOrder.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ProductionOrders_SalesOrderLines (Object)

The ProductionOrders_SalesOrderLines is a child object of the ProductionOrders object. You can set the sales order to which to link the production order. Source table: WOR2.

**Remarks:** To display the form in the application, choose Production --> Production Orders. And click the link button of the Sales Order field.

## Properties (5)
- `Public Property BaseAbsEntry() As Long` [R] The production order base entry. Field name: BaseEntry.
- `Public Property BaseLine() As Long` [R] The production order base line. Field name: BaseLine.
- `Public Property BaseNumber() As Long` [R] The production order base number. Field name: BaseNum.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DocEntry() As Long` [R] The internal ID of the production order. Field name: DocEntry.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ProductionOrders_Stages (Object)

The ProductionOrders_Stages is a child object of the ProductionOrders object. You can set the route stages to which to link the production order. Source table: WOR4.

## Properties (11)
- `Public Property CalculationProportion() As Double` [R/W] The percentage of resource capacity that will be consumed in a particular route stage. Field name: RtCalcProp.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DocEntry() As Long` [R] The internal ID of the production order. Field name: DocEntry.
- `Public Property EndDate() As Date` [R/W] The latest date by which a component needs to be used in the production process. Field name: EndDate.
- `Public Property Name() As String` [R/W] The stage name. Field name: Name. Length: 100 characters.
- `Public Property RequiredDays() As Double` [R] The number of days required for a specific Resource to complete the Planned Qty. of a particular route stage. Field name: ReqDays.
- `Public Property SequenceNumber() As Long` [R/W] The sequence number that is assigned to each route stage. The sequence indicates the precise order in which the routing stages must be performed during the production process. Field name: SeqNum.
- `Public Property StageEntry() As Long` [R/W] property StageEntry
- `Public Property StageID() As Long` [R] The stage ID. Field name: StageId.
- `Public Property StartDate() As Date` [R/W] The earliest date on which the component is needed in the production process. For a production order that has route stages, the Start Date for the first Route Stage type line (included in the calculation) is set to the production order header Start Date. And by default, the Start Date for the next Route Stage type line is the same as the calculated End Date of the previous route stage. You can manually change the Route Stage type line Start Date to any date that falls between or is equal to the production order header Start Date and Due Date. Field name: StartDate.
- `Public Property WaitingDays() As Double` [R/W] The number of days to wait after the completion of the route stage. This field will not be visible by default. As soon as a Route Stage type line is created, you can manually enter the number of waiting days. Field name: WaitDays.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ProductTrees (Object)

ProductTrees is a business object that represents a completed product comprising parts and raw materials, which is described by means of a bill of materials. This object is part of the Inventory module. This object enables you to: - Add an item to the product tree. - Retrieve an item by its keys from the product tree. - Update an item in the product tree. - Remove an item from the product tree. - Save the object in XML format. Source table: OITT.

**Remarks:** Mandatory fields in SAP Business One: TreeCode and TreeType. To display the form in the application: - Select Production --> Define Bill of Materials.

## Properties (18)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property HideBOMComponentsInPrintout() As BoYesNoEnum` [R/W] property HideBOMComponentsInPrintout
- `Public Property Items() As ProductTrees_Lines` [R] Returns the ProductTrees_Lines object.
- `Public Property PlanAvgProdSize() As Double` [R/W] property PlanAvgProdSize
- `Public Property PriceList() As Long` [R/W] property PriceList
- `Public Property ProductDescription() As String` [R/W] property ProductDescription
- `Public Property Project() As String` [R/W] The project that relates to the bill of materials. Field: Project. Length: 20 characters.
- `Public Property Quantity() As Double` [R/W] Sets or returns the items quantity. Field name: BaseQty.
- `Public Property Stages() As ProductTrees_Stages` [R] property Stages
- `Public Property TreeCode() As String` [R/W] Sets or returns BaseQtythe product tree code. Mandatory property. Field name: Code. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property TreeType() As BoItemTreeTypes` [R/W] Sets or returns a valid value of BoItemTreeTypes type that specifies the product tree type of the item (also known as bill of material type). Field name: TreeType. Mandatory property.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Warehouse() As String` [R/W] property Warehouse

## Methods (10)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function Close() As Long` Closes a record of the object in SAP Business One database.
  - example note: The following sample shows how to close a document record. Use this sample as a basis to all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Sub CloseDocument()

        Dim RetVal    As Long

        Dim ErrCode   As Long

        Dim ErrMsg    As String

        Dim vOrder As SAPbobsCOM.Documents

        Set vOrder = vCmp.GetBusinessObject(oOrders)

        'Retrieve the document record to close from the database

        RetVal = vOrder.GetByKey("55")

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

                Exit Sub

        End If

        'Close the record

        RetVal = vOrder.Close

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox "Failed to Close the record " & ErrCode & " " & ErrMsg

        End If

    End Sub
    ```
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Key As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Key`: Specifies the product tree code (see TreeCode property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
- `Public Function UpdateFromXML(ByVal FileName As String) As Long` method UpdateFromXML
  - param `FileName`: 

# ProductTrees_Lines (Object)

ProductTrees_Lines is a child object of the ProductTrees object and it represents the line entries of each product tree. This object is part of the Inventory and Production module. Source table: ITT1.

**Remarks:** Mandatory fields in SAP Business One: ItemCode. To display the form in the application: - Select Production --> Define Bill of Materials.

## Properties (26)
- `Public Property AdditionalQuantity() As Double` [R/W] property AdditionalQuantity
- `Public Property ChildNum() As Long` [R] property ChildNum
- `Public Property Comment() As String` [R/W] Sets or returns comments for the item in the product tree line. Field name: Comment. Length: 254 characters.
- `Public Property Count() As Long` [R] Returns the total item rows.
  - remarks: When you add an item to the product tree, the Count value is incremented automatically.
- `Public Property Currency() As String` [R/W] Sets or returns the bill of materials currency. Field name: Currency. Length: 3 characters. Sets or returns the price currency used in the document row. Field name: Currency. Length: 3 characters.
  - remarks: You must define the currency strings before using this property. One business transaction may include more than one currency. In multiple currencies transaction, first call the GetCurrencyRate method to unify the total amount in different currencies into one currency. The value for multiple currencies is ##.
- `Public Property DistributionRule() As String` [R/W] The distribution rule for allocating costs and revenues (both direct and indirect) to one or more cost centers. This is a foreign key to the DistributionRule object. Field name: OcrCode
- `Public Property DistributionRule2() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode2
- `Public Property DistributionRule3() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode3
- `Public Property DistributionRule4() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode4
- `Public Property DistributionRule5() As String` [R/W] Multiple distribution rules for allocating costs and revenues (both direct and indirect) to one or more cost centers. Field name: OcrCode5
- `Public Property InventoryUOM() As String` [R] Returns the Unit of Measurement for the item in the product tree line (for example: box, case, piece). Field name: Uom. Length: 5 characters.
  - remarks: The origin of the value is the Items object.
- `Public Property IssueMethod() As BoIssueMethod` [R/W] Sets or returns a valid value of BoIssueMethod that determines Specifies the methods for issuing items from the inventory: - Backflash (automatic) - Manual. Field name: IssueMthd.
- `Public Property ItemCode() As String` [R/W] Sets or returns the component item code. Field name: Code. Length: 254 characters. This is a foreign key to the Items object. Sets or returns the item code in the inventory. The item code must be unique. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property ItemName() As String` [R/W] property ItemName
- `Public Property ItemType() As ProductionItemType` [R/W] property ItemType
- `Public Property LineText() As String` [R/W] property LineText
- `Public Property ParentItem() As String` [R/W] Sets or returns the code of the parent item (product tree). Field name: Father. Length: 20 characters. This is a foreign key to the ProductTrees object.
  - remarks: The origin is the ProductTrees object.
- `Public Property Price() As Double` [R/W] Sets or returns the item price before taxation. Field name: Price.
- `Public Property PriceList() As Long` [R/W] Sets or returns the price list key of the item. Field name: PriceList. This is a foreign key to the PriceLists object.
  - remarks: The origin of the value is the PriceLists Object (OPLN table).
- `Public Property Project() As String` [R/W] The project that relates to the bill of materials. Field: Project. Length: 20 characters.
- `Public Property Quantity() As Double` [R/W] Sets or returns the items quantity in the bill of material. Field name: Quantity.
- `Public Property StageID() As Long` [R/W] property StageID
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VisualOrder() As Long` [R] property VisualOrder
- `Public Property Warehouse() As String` [R/W] Sets or returns the Warehouse identification key. Field name: Warehouse. Length: 8 characters. This is a foreign key to the Warehouses object.
- `Public Property WipAccount() As String` [R/W] property WipAccount

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: You cannot delete a line if it is the only line in the ProductTrees object.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ProductTrees oProdTree;

    // Delete Product Tree
    if(oProdTree.GetByKey("ProdTree") == true)
    {
        oProdTree.Items.SetCurrentLine(1);
        oProdTree.Items.Delete();
        oProdTree.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ProductTrees_Stages (Object)

ProductTrees_Stages Class

## Properties (7)
- `Public Property Count() As Long` [R] property Count
- `Public Property Father() As String` [R] property Father
- `Public Property Name() As String` [R/W] property Name
- `Public Property SequenceNumber() As Long` [R/W] property SequenceNumber
- `Public Property StageEntry() As Long` [R/W] property StageEntry
- `Public Property StageID() As Long` [R] property StageID
- `Public Property WaitingDays() As Double` [R/W] property WaitingDays

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ProfitCenter (Object)

Represents a profit center. Source table: OPRC Mandatory properties: CenterCode, CenterName

**Remarks:** The terminology "Profit Center" and "Cost Center" are the same. A cost center is a company unit or division that performs a specific business function.

## Properties (10)
- `Public Property Active() As BoYesNoEnum` [R/W] Specify whether the cost center is active. Field name: Active.
  - remarks: In SAP Business One, you can use only active cost centers.
- `Public Property CenterCode() As String` [R/W] The key of the cost center. Field name: PrcCode. Length: 8 characters.
- `Public Property CenterName() As String` [R/W] The display name of the cost center. Field name: PrcName. Length: 30 characters.
- `Public Property CenterOwner() As Long` [R/W] property CenterOwner
- `Public Property CostCenterType() As String` [R/W] The cost center type, for selection by future reports and analyses. Field name: CCTypeCode. Length: 8 characters.
- `Public Property Effectivefrom() As Date` [R/W] The start date of the effective period of the cost center. Field name: ValidFrom.
  - remarks: After you add the cost center, you cannot change the Effective From date.
- `Public Property EffectiveTo() As Date` [R/W] The end date of the effective period of the cost center. Field name: ValidTo.
- `Public Property GroupCode() As String` [R/W] The code of the cost center's group. You can assign cost centers the same group code in order to group them within reports. Field name: GrpCode.
- `Public Property InWhichDimension() As Long` [R/W] The dimension in which this profit is located. Field name: DimCode.
  - remarks: The dimension must be active.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ProfitCenterParams (Object)

Holds the key and name to an existing profit center. This object is used to pass keys to and retrieve keys from ProfitCentersService methods.

## Properties (2)
- `Public Property CenterCode() As String` [R/W] The key for a specific cost center. Field name: PrcCode
- `Public Property CenterName() As String` [R] The display name for a specific cost center. Field name: PrcName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ProfitCentersParams (Collection)

A collection of ProfitCenterParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ProfitCenterParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ProfitCenterParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ProfitCentersService (Object)

The ProfitCentersService service enables you to add, look up and remove profit centers. To see the list of profit centers, select Financials --> Cost Accounting --> Cost Centers, and then choose Open Table. Source table: OPRC

**Remarks:** The terminology "Profit Center" and "Cost Center" are the same.

## Methods (8)
- `Public Function AddProfitCenter(ByVal pIProfitCenter As ProfitCenter) As ProfitCenterParams` Adds a profit center.
  - param `pIProfitCenter`: The data for the new profit center.
  - returns: Contains the key (PrcCode) of the new profit center.
  - remarks: When you add a profit center, a distribution rule is automatically created with the same name and one line. The rule distributes the cost or expense 100 percent to the profit center, and the rule cannot be changed.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oCmpSrv = oCompany.GetCompanyService()

    Dim oPCService As SAPbobsCOM.IProfitCentersService

    Dim oPC As SAPbobsCOM.IProfitCenter

    Dim oPCParams As SAPbobsCOM.IProfitCenterParams

    Dim oPCsParams As SAPbobsCOM.IProfitCentersParams

    oPCService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.ProfitCentersService)

    oPCParams = oPCService.GetDataInterface(SAPbobsCOM.DimensionsServiceDataInterfaces.dsDimensionParams)

    oPC = oPCService.GetDataInterface(SAPbobsCOM.ProfitCentersServiceDataInterfaces.pcsProfitCenter)

    oPC.CenterCode = "code"

    oPC.CenterName = "name"

    oPC.GroupCode = "GRP"

    oPC.InWhichDimension = 1

    oPCParams = oPCService.AddProfitCenter(oPC)

    oStr = oPCParams.CenterCode
    ```
- `Public Sub DeleteProfitCenter(ByVal pIProfitCenterParams As ProfitCenterParams)` Deletes an existing profit center. The profit center is specified by its key (PrcCode), which is contained in the ProfitCenterParams object passed to the method.
  - param `pIProfitCenterParams`: The key of the profit center to be deleted.
  - remarks: If the profit center is system defined or is linked to a distribution rule, the profit center cannot be deleted. A profit center is system defined if the Locked field in the OPRC table is set to Y.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oPCParams.CenterCode = "Code"

    oPCService.DeleteProfitCenter(oPCParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ProfitCentersServiceDataInterfaces) As Object` Creates an empty data structure for use with the ProfitCentersService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ProfitCentersServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates an object from an XML file.
  - param `bstrFileName`: The path and name of the XML file with which to create the object.
  - remarks: The XML file can be created using an object's ToXMLFile method. The XML file defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLFile(Hashtable Properties, String Path)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair In Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        oGeneralData.ToXMLFile(Path);

        //Retrieve XML and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLFile(Path);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates an object from XML.
  - param `bstrXMLString`: The XML with which to create the object.
  - remarks: The XML can be created using an object's ToXMLString method. The XML defines the object and its data.
  - C# example (from SAP's help):
    ```csharp
    public void AddFromXMLString(Hashtable Properties)
    {
        //Store GeneralData object as XML
        SAPbobsCOM.GeneralService oGeneralService;
        SAPbobsCOM.GeneralData oGeneralData;
        SAPbobsCOM.GeneralData oGeneralDataXML;
        string XMLString;

        oGeneralService = cConnection.Instance.DICompanyService.GetGeneralService(UDOID);
        oGeneralData = (GeneralData)oGeneralService.GetDataInterface(GeneralServiceDataInterfaces.gsGeneralData);

        foreach (DictionaryEntry Pair in Properties)
            oGeneralData.SetProperty(Pair.Key.ToString(), Pair.Value.ToString());

        XMLString = oGeneralData.ToXMLString();

        //Retrieve XML string and create GeneralData object from the XML
        oGeneralDataXML = (GeneralData)oGeneralService.GetDataInterfaceFromXMLString(XMLString);
        oGeneralService.Add(oGeneralDataXML);
    }
    ```
- `Public Function GetProfitCenter(ByVal pIProfitCenterParams As ProfitCenterParams) As ProfitCenter` Retrieves a profit center. The profit center is specified by its key (PrcCode), which is contained in the ProfitCenterParams object passed to the method.
  - param `pIProfitCenterParams`: The key of the profit center to retrieve.
  - returns: The profit center with the specified key.
- `Public Function GetProfitCenterList() As ProfitCentersParams` Retrieves the keys and names of all the profit centers.
- `Public Sub UpdateProfitCenter(ByVal pIProfitCenter As ProfitCenter)` Updates an existing profit center. The data for the profit center, including the key of the profit center to be updated, is contained in the ProfitCenter object passed to the method. To update a profit center, you must first retrieve it using the GetProfitCenter method.
  - param `pIProfitCenter`: The data for the profit center to be updated. The ProfitCenter object must contain the key of the object to be updated.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    oPCParams.CenterCode = "Code"

    oPC = oPCService.GetProfitCenter(oPCParams)

    oPC.InWhichDimension = 1

    oPCService.UpdateProfitCenter(oPC)
    ```

# Project (Object)

A data structure object holding properties for the ProjectsService (Code and Name). Source table: OPRJ.

## Properties (6)
- `Public Property Active() As BoYesNoEnum` [R/W] Specify whether the project status is active. Field: Active.
- `Public Property Code() As String` [R/W] Sets or returns a string specifying the project unique ID. Length: 20 characters.
- `Public Property Name() As String` [R/W] Sets or returns a string specifying the project name.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property ValidFrom() As Date` [R/W] The valid period of the project. Field: ValidFrom.
- `Public Property ValidTo() As Date` [R/W] The valid period of the project. Field: ValidTo.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ProjectManagementConfigurationService (Object)

ProjectManagementConfigurationService Class

## Methods (27)
- `Public Sub AddActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)` AddActivities
  - param `pIPMC_ActivityCollection`: 
- `Public Sub AddAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)` AddAreas
  - param `pIPMC_AreaCollection`: 
- `Public Sub AddPriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)` AddPriorities
  - param `pIPMC_PriorityCollection`: 
- `Public Sub AddStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)` AddStageTypes
  - param `pIPMC_StageTypeCollection`: 
- `Public Sub AddSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)` AddSubprojectTypes
  - param `pIPMC_SubprojectTypesCollection`: 
- `Public Sub AddTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)` AddTasks
  - param `pIPMC_TaskCollection`: 
- `Public Sub DeleteActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)` DeleteActivities
  - param `pIPMC_ActivityCollection`: 
- `Public Sub DeleteAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)` DeleteAreas
  - param `pIPMC_AreaCollection`: 
- `Public Sub DeletePriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)` DeletePriorities
  - param `pIPMC_PriorityCollection`: 
- `Public Sub DeleteStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)` DeleteStageTypes
  - param `pIPMC_StageTypeCollection`: 
- `Public Sub DeleteSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)` DeleteSubprojectTypes
  - param `pIPMC_SubprojectTypesCollection`: 
- `Public Sub DeleteTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)` DeleteTasks
  - param `pIPMC_TaskCollection`: 
- `Public Function GetActivities() As PMC_ActivityCollection` GetActivities
- `Public Function GetAreas() As PMC_AreaCollection` GetAreas
- `Public Function GetDataInterface(ByVal enumMSDI As ProjectManagementConfigurationServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ProjectManagementConfigurationServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetPriorities() As PMC_PriorityCollection` GetPriorities
- `Public Function GetStageTypes() As PMC_StageTypeCollection` GetStageTypes
- `Public Function GetSubprojectTypes() As PMC_SubprojectTypesCollection` GetSubprojectTypes
- `Public Function GetTasks() As PMC_TaskCollection` GetTasks
- `Public Sub UpdateActivities(ByVal pIPMC_ActivityCollection As PMC_ActivityCollection)` UpdateActivities
  - param `pIPMC_ActivityCollection`: 
- `Public Sub UpdateAreas(ByVal pIPMC_AreaCollection As PMC_AreaCollection)` UpdateAreas
  - param `pIPMC_AreaCollection`: 
- `Public Sub UpdatePriorities(ByVal pIPMC_PriorityCollection As PMC_PriorityCollection)` UpdatePriorities
  - param `pIPMC_PriorityCollection`: 
- `Public Sub UpdateStageTypes(ByVal pIPMC_StageTypeCollection As PMC_StageTypeCollection)` UpdateStageTypes
  - param `pIPMC_StageTypeCollection`: 
- `Public Sub UpdateSubprojectTypes(ByVal pIPMC_SubprojectTypesCollection As PMC_SubprojectTypesCollection)` UpdateSubprojectTypes
  - param `pIPMC_SubprojectTypesCollection`: 
- `Public Sub UpdateTasks(ByVal pIPMC_TaskCollection As PMC_TaskCollection)` UpdateTasks
  - param `pIPMC_TaskCollection`: 
