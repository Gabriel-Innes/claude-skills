<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplate (Object)

ApprovalTemplate is a data structure related to the ApprovalTemplatesService. Source table: OWTM.

**Example:**
- example note: When the item is “Wood” or Variance is greater than 15%, approval process will be triggered.
- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
  ```vb
  Dim oApprovalTemplateStage As ApprovalTemplateStage
  Dim oApprovalTemplate As ApprovalTemplate
  Dim oApprovalTemplateParams As ApprovalTemplateParams
  Dim oApprovalTemplateTerm As ApprovalTemplateTerm

  'get new Approval Stage
  oApprovalTemplate = oApprovalTemplateService.GetDataInterface(ApprovalTemplatesServiceDataInterfaces.atsdiApprovalTemplate)

  'set the name of the Approval Template
  oApprovalTemplate.Name = "My Template"

  'add the user that need the approval(userId=3 is "Green")
  oApprovalTemplate.ApprovalTemplateUsers.Add.UserID= 3

  'Add Inventory Counting & Posting documnet
  oApprovalTemplate.ApprovalTemplateDocuments.Add.DocumentType = ApprovalTemplatesDocumentTypeEnum.atdtInventoryCounting
  oApprovalTemplate.ApprovalTemplateDocuments.Add.DocumentType = ApprovalTemplatesDocumentTypeEnum.atdtInventoryPosting

  'get Approval Stages
  oApprovalTemplateStage = oApprovalTemplate.ApprovalTemplateStages.Add

  'set the code of an existing stage(e.g code=1 the stage name is Accounting)
  oApprovalTemplateStage.ApprovalStageCode = 1

  'include terms in the template
  oApprovalTemplate.UseTerms = BoYesNoEnum.tYES

  'add new term
  oApprovalTemplateTerm = oApprovalTemplate.ApprovalTemplateTerms.Add

  'set the condition to Item Code
  oApprovalTemplateTerm.ConditionType = ApprovalTemplateConditionTypeEnum.atctItemCode

  'set the Operation Type to Equal
  oApprovalTemplateTerm.OperationType = ApprovalTemplateOperationTypeEnum.opcodeEqual

  'set the value
  oApprovalTemplateTerm.Value = "Wood"

  'set the condition to Variance Percent
  oApprovalTemplateTerm.ConditionType = ApprovalTemplateConditionTypeEnum.atctVariancePercent

  'set the Operation Type to Greater Than
  oApprovalTemplateTerm.OperationType = ApprovalTemplateOperationTypeEnum.opcodeGreaterThan

  'set the value
  oApprovalTemplateTerm.Value = 15

  'add Approval Template
  oApprovalTemplateParams = oApprovalTemplateService.AddApprovalTemplate(oApprovalTemplate)
  ```

## Properties (11)
- `Public Property ApprovalTemplateDocuments() As ApprovalTemplateDocuments` [R] Returns the ApprovalTemplateDocuments Object, a Data Collection of all the documents attached to this approval template.
- `Public Property ApprovalTemplateQueries() As ApprovalTemplateQueries` [R] Returns the ApprovalTemplateQueries Object, a Data Collection of all the Queries attached to this approval template.
- `Public Property ApprovalTemplateStages() As ApprovalTemplateStages` [R] Returns the ApprovalTemplateStages Object, a Data Collection of all the stages attached to this approval template.
- `Public Property ApprovalTemplateTerms() As ApprovalTemplateTerms` [R] Returns the ApprovalTemplateTerms Object, a Data Collection of all the terms attached to this approval template.
- `Public Property ApprovalTemplateUsers() As ApprovalTemplateUsers` [R] Returns the ApprovalTemplateUsers Object, a Data Collection of all the users attached to this approval template.
- `Public Property Code() As Long` [R] Returns this Approval Template Code. Field name: WtmCode. This is a key to the ApprovalTemplate object.
- `Public Property IsActive() As BoYesNoEnum` [R/W] Determines whether or not this ApprovalTemplate is active. Field name: Active.
- `Public Property IsActiveWhenUpdatingDocuments() As BoYesNoEnum` [R/W] property IsActiveWhenUpdatingDocuments
- `Public Property Name() As String` [R/W] Sets or returns this Approval Template name. Field name: Name. Length: 20 characters.
- `Public Property Remarks() As String` [R/W] Sets or returns this Approval Template description. Field name: Remarks. Length: 100 characters.
- `Public Property UseTerms() As BoYesNoEnum` [R/W] Determines whether or not manual approval is required for this Approval Template. Field name: Conds.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
