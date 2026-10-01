<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
