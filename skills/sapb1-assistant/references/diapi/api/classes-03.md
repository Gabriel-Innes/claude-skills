<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# ApprovalStageParams (Object)

The ApprovalStageParams specifies the identification key combination (Code and Name) for which the ApprovalStagesService is related. Source table: OWST.

## Properties (2)
- `Public Property Code() As Long` [R/W] Sets or returns this approval stage Code. Field name: WstCode. This is a key to the ApprovalStage object.
- `Public Property Name() As String` [R] Returns the the stage approver's name. Field name: Name. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the an XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalStages (Collection)

The ApprovalStages is a Data Collection of ApprovalStage data structure. Source table: OWST.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalStage data structures in the ApprovalStages data collection.

## Methods (5)
- `Public Function Add() As ApprovalStage` Adds a new ApprovalStage data structure to the ApprovalStages Object.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalStage` Returns a reference to the ApprovalStage you want to get by its index.
  - param `vtIndex`: Specifies the index of the new item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalStagesParams (Collection)

ApprovalStagesParams is a Data Collection of ApprovalStageParams identification keys. Source table: OWST.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalStageParams identification keys in the ApprovalStagesParams data collection.

## Methods (5)
- `Public Function Add() As ApprovalStageParams` Adds a new ApprovalStageParams to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalStageParams` Returns reference to existing ApprovalStageParams in the collection by its index.
  - param `vtIndex`: Specifies the index of the new item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalStagesService (Object)

ApprovalStagesService is a business object that manages the Approval stages Process in SAP Business One environment. This object enables user to: - Add new Approval Stage to approval Process. - Get Approval Stage from approval Process. - Get a list of Approval Stages from approval Process. - Remove Approval Stage from approval Process. - Update Approval Stage within approval Process. - Get Data interfaces. Source table: OWST.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: Select Administration --> Approval Procedure --> Approval Stages.

## Methods (8)
- `Public Function AddApprovalStage(ByVal pApprovalStage As ApprovalStage) As ApprovalStageParams` Adds a new ApprovalStage to the ApprovalStages data collection Object.
  - param `pApprovalStage`: The ApprovalStage Object you want to add.
  - example note: This sample demonstrates the addition of Approval Stage and Approval Template.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalStage As ApprovalStage

    Dim oApprovalStageApprovers As ApprovalStageApprovers

    Dim oFirstApprover As ApprovalStageApprover

    Dim oSecondApprover As ApprovalStageApprover

    Dim oApprovalStageParams As ApprovalStageParams

    'Get new Approval Stage

    oApprovalStage = oApprovalStagesService.GetDataInterface(ApprovalStagesServiceDataInterfaces.assdiApprovalStage)

    'Set the name

    oApprovalStage.Name = My Approval

    oApprovalStage.Remarks = My Remarks

    'Get ApprovalStageApprovers collection

    oApprovalStageApprovers = oApprovalStage.ApprovalStageApprovers

    'Add new Approver

    oFirstApprover = oApprovalStageApprovers.Add

    'Set the approver id(manager)

    oFirstApprover.UserID = 1

    'Add new Approver

    oSecondApprover = oApprovalStageApprovers.Add

    'Set the approver id

    oSecondApprover.UserID = 2

    'Set the number of required approvers

    oApprovalStage.NoOfApproversRequired = 1

    'Add Approval Stage

    oApprovalStageParams=oApprovalStagesService.AddApprovalStage(oApprovalStage)
    ```
- `Public Function GetApprovalStage(ByVal pIApprovalStageParams As ApprovalStageParams) As ApprovalStage` Gets an ApprovalStage from the ApprovalStages data collection by it ApprovalStageParams.
  - param `pIApprovalStageParams`: The ApprovalStageParams of the ApprovalStage you want to get.
  - example note: Get an existing Approval Stage
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalStageParams As ApprovalStageParams

    Dim oApprovalStage As ApprovalStage

    'Get new Approval Stage Params

    oApprovalStageParams = oApprovalStagesService.GetDataInterface(ApprovalStagesServiceDataInterfaces.assdiApprovalStageParams)

    'Set the code

    oApprovalStageParams.Code = 1

    'Get an existing Approval Stage

    oApprovalStage = oApprovalStagesService.GetApprovalStage(oApprovalStageParams)
    ```
- `Public Function GetApprovalStageList() As ApprovalStagesParams` Returns the ApprovalStagesParams Data Collection.
  - example note: Get a list of Approval Stages
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalStageParams As ApprovalStagesParams

    Dim i As Integer

    'Get a list of Approval Stages

    oApprovalStageParams = oApprovalStagesService.GetApprovalStageList

    For i = 0 To oApprovalStageParams.Count - 1

        'Print the stage name

        Debug.WriteLine(oApprovalStageParams.Item(i).Name)

    Next
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ApprovalStagesServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ApprovalStagesServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: Specifies the XML String.
- `Public Sub RemoveApprovalStage(ByVal pIApprovalStageParams As ApprovalStageParams)` Remove an ApprovalStage from the ApprovalStages data collection by it ApprovalStageParams.
  - param `pIApprovalStageParams`: Specifies the ApprovalStageParams identification key combination (Code and Name) of the Approval stage you want to remove.
  - example note: Remove an existing Approval Stage
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalStageParams As ApprovalStageParams

    'Get new Approval Stage Params

    oApprovalStageParams = oApprovalStagesService.GetDataInterface(ApprovalStagesServiceDataInterfaces.assdiApprovalStageParams)

    'Set the code

    oApprovalStageParams.Code = 15

    'Remove an existing Approval Stage

    Call oApprovalStagesService.RemoveApprovalStage(oApprovalStageParams)
    ```
- `Public Sub UpdateApprovalStage(ByVal pIApprovalStage As ApprovalStage)` Replace this ApprovalStage with updated Approval Stage.
  - param `pIApprovalStage`: The target ApprovalStage Object.
  - example note: Update an Approval Stage
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalStageParams As ApprovalStageParams

    Dim oApprovalStage As ApprovalStage

    'Get new Approval Stage Params

    oApprovalStageParams = oApprovalStagesService.GetDataInterface(ApprovalStagesServiceDataInterfaces.assdiApprovalStageParams)

    'Set the code

    oApprovalStageParams.Code = 1

    'Get an existing Approval Stage

    oApprovalStage = oApprovalStagesService.GetApprovalStage(oApprovalStageParams)

    'set the remarks

    oApprovalStage.Remarks = "My Remarks"

    'update Approval Stage

    Call oApprovalStagesService.UpdateApprovalStage(oApprovalStage)
    ```

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

# ApprovalTemplateDocument (Object)

ApprovalTemplateDocument is a data structure related to the ApprovalTemplatesService. Source table: WTM3.

## Properties (1)
- `Public Property DocumentType() As ApprovalTemplatesDocumentTypeEnum` [R/W] Sets or returns a valid value that defines this document type. Field name: TransType. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalTemplateDocuments (Collection)

ApprovalTemplateDocuments is a Data Collection of ApprovalTemplateDocument data structures. Source table: WTM3.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateDocument data structures in the ApprovalTemplateDocuments data collection. Field name: NumOfDocs).

## Methods (5)
- `Public Function Add() As ApprovalTemplateDocument` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateDocument` Returns reference to existing ApprovalTemplateDocument in the collection by its index.
  - param `vtIndex`: Specifies the index of the ApprovalTemplateDocument you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalTemplateParams (Object)

The ApprovalTemplateParams specifies the identification key combination (Code and Name) for which the ApprovalTemplatesService is related. Source table: OWTM.

## Properties (2)
- `Public Property Code() As Long` [R/W] Sets or returns this approval template Code. Field name: WtmCode. This is a key to the ApprovalTemplate object.
- `Public Property Name() As String` [R] Returns this approval template Name. Field name: Name. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalTemplateQueries (Collection)

ApprovalTemplateQueries is a Data Collection of ApprovalTemplateQuery data structures. Source table: WTM5.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateQuery data structures. in the ApprovalTemplateQueries data collection. Field name: NumOfDocs.

## Methods (5)
- `Public Function Add() As ApprovalTemplateQuery` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateQuery` Returns reference to existing ApprovalTemplateQuery in the collection (by its index).
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalTemplateQuery (Object)

ApprovalTemplateQuery is a data structure related to the ApprovalTemplatesService.

## Properties (1)
- `Public Property QueryID() As Long` [R/W] Sets or returns this Approval Template Query Id. Field name: QueryId.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalTemplates (Collection)

ApprovalTemplates is a Data Collection of ApprovalTemplate data structures. Source table: OWTM.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplate data structures in the ApprovalTemplates data collection. Field name: NumOfDocs.

## Methods (5)
- `Public Function Add() As ApprovalTemplate` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplate` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the new item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalTemplatesParams (Collection)

ApprovalTemplatesParams is a Data Collection of ApprovalTemplateParams identification keys. Source table: OWTM.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateParams identification keys in the ApprovalTemplatesParams data collection.

## Methods (5)
- `Public Function Add() As ApprovalTemplateParams` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateParams` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# ApprovalTemplatesService (Object)

ApprovalTemplatesService is a business object that manages the Approval of deviations from organization limitations. This object enables to: - Add a new Approval Stage to approval process. - Get Approval Stage from approval process. - Get a list of Approval Stages from approval process. - Remove an Approval Stage from approval process. - Update an Approval Stage within approval process. Source table: OWTM.

**Remarks:** The ApprovalTemplatesService does not trigger the approval process for objects added via the DI API. To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: Select Administration --> Approval Procedure --> Approval Templates.

## Methods (8)
- `Public Function AddApprovalTemplate(ByVal pApprovalTemplate As ApprovalTemplate) As ApprovalTemplateParams` Adds a new instance of ApprovalTemplate Object to the ApprovalTemplates collection.
  - param `pApprovalTemplate`: The ApprovalTemplate Object you want to add.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalTemplateStage As ApprovalTemplateStage

    Dim oApprovalTemplate As ApprovalTemplate

    Dim oApprovalTemplateParams As ApprovalTemplateParams

    Dim oApprovalTemplateTerm As ApprovalTemplateTerm

    'get new Approval Stage

    oApprovalTemplate = oApprovalTemplateService.GetDataInterface(ApprovalTemplatesServiceDataInterfaces.atsdiApprovalTemplate)

    'set the name of the Approval Template

    oApprovalTemplate.Name = "My Template"

    'add the user that need the approval(userId=3 is "Fred")

    oApprovalTemplate.ApprovalTemplateUsers.Add.UserID= 3

    'Add Quotation documnet

    oApprovalTemplate.ApprovalTemplateDocuments.Add.DocumentType = ApprovalTemplatesDocumentTypeEnum.atdtQuotation

    'get Approval Stages

    oApprovalTemplateStage = oApprovalTemplate.ApprovalTemplateStages.Add

    'set the code of an existing stage(e.g code=1 the stage name is Accounting)

    oApprovalTemplateStage.ApprovalStageCode = 1

    'include terms in the template

    oApprovalTemplate.UseTerms = BoYesNoEnum.tYES

    'add new term

    oApprovalTemplateTerm = oApprovalTemplate.ApprovalTemplateTerms.Add

    'set the condition to Discount Percent

    oApprovalTemplateTerm.ConditionType = ApprovalTemplateConditionTypeEnum.atctDiscountPercent

    'set the Operation Type to Greater Than

    oApprovalTemplateTerm.OperationType = ApprovalTemplateOperationTypeEnum.opcodeGreaterThan

    'set the value

    oApprovalTemplateTerm.Value = 30

    'add Approval Template

    oApprovalTemplateParams = oApprovalTemplateService.AddApprovalTemplate(oApprovalTemplate)
    ```
- `Public Function GetApprovalTemplate(ByVal pIApprovalTemplateParams As ApprovalTemplateParams) As ApprovalTemplate` Gets an instance of the ApprovalTemplate Object from the ApprovalTemplates collection by its params.
  - param `pIApprovalTemplateParams`: The identification key of the ApprovalTemplate Object you want to get.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalTemplate As ApprovalTemplate

    Dim oApprovalTemplateParams As ApprovalTemplateParams

    'get new Approval Template Params

    oApprovalTemplateParams = oApprovalTemplateService.GetDataInterface(ApprovalTemplatesServiceDataInterfaces.atsdiApprovalTemplateParams)

    'set the code

    oApprovalTemplateParams.Code = 1

    'get an existing Approval Template

    oApprovalTemplate = oApprovalTemplateService.GetApprovalTemplate(oApprovalTemplateParams)
    ```
- `Public Function GetApprovalTemplateList() As ApprovalTemplatesParams` Returns the ApprovalTemplatesParams data collection that identify all instances of ApprovalTemplate exists in ApprovalTemplates collection.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalTemplatesParams As ApprovalTemplatesParams

    'get Approval Templates list

    oApprovalTemplatesParams = oApprovalTemplateService.GetApprovalTemplateList

    'print the first name on the list

    Debug.WriteLine(oApprovalTemplatesParams.Item(0).Name)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ApprovalTemplatesServiceDataInterfaces) As Object` Creates an empty data interface. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ApprovalTemplatesServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface schema from XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Retrieves the Data Interface schema from XML string.
  - param `bstrXMLString`: Specifies the XML string.
- `Public Sub RemoveApprovalTemplate(ByVal pIApprovalTemplateParams As ApprovalTemplateParams)` Remove ApprovalTemplate identified by its ApprovalTemplateParams from ApprovalTemplates collection.
  - param `pIApprovalTemplateParams`: ApprovalTemplate identification key combination (Code and Name).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalTemplateParams As ApprovalTemplateParams

    'get a new Approval Template Params

    oApprovalTemplateParams = oApprovalTemplateService.GetDataInterface(ApprovalTemplatesServiceDataInterfaces.atsdiApprovalTemplateParams)

    'set the code

    oApprovalTemplateParams.Code = 41

    'remove an existing Approval Template

    oApprovalTemplateService.RemoveApprovalTemplate(oApprovalTemplateParams)
    ```
- `Public Sub UpdateApprovalTemplate(ByVal pIApprovalTemplate As ApprovalTemplate)` Update this ApprovalTemplate by another ApprovalTemplate.
  - param `pIApprovalTemplate`: The new ApprovalTemplate Object.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oApprovalTemplate As ApprovalTemplate

    Dim oApprovalTemplateParams As ApprovalTemplateParams

    'get a new Approval Template Params

    oApprovalTemplateParams = oApprovalTemplateService.GetDataInterface(ApprovalTemplatesServiceDataInterfaces.atsdiApprovalTemplateParams)

    'set the code

    oApprovalTemplateParams.Code = 1

    'get an existing Approval Template

    oApprovalTemplate = oApprovalTemplateService.GetApprovalTemplate(oApprovalTemplateParams)

    'set a new Template name

    oApprovalTemplate.Name = "My Budget"

    'update Approval Template

    oApprovalTemplateService.UpdateApprovalTemplate(oApprovalTemplate)
    ```

# ApprovalTemplateStage (Object)

ApprovalTemplateStage is a data structure related to the ApprovalTemplatesService. Source table: WTM2.

## Properties (3)
- `Public Property ApprovalStageCode() As Long` [R/W] Sets or returns the confirmation level of this approval. Field name: WstCode. This is a foreign key to the ApprovalStagesService object.
- `Public Property Remarks() As String` [R/W] Sets or returns the description of this Approval Template . Field name: Remarks. Length: 100 characters.
- `Public Property SortID() As Long` [R/W] Sets or returns the Sort code. Field name: SortId.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalTemplateStages (Collection)

ApprovalTemplateStages is a Data Collection of ApprovalTemplateStage data structures. Source table: WTM2.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateStage data structures in the ApprovalTemplateStages data collection.

## Methods (5)
- `Public Function Add() As ApprovalTemplateStage` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateStage` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# ApprovalTemplateTerm (Object)

ApprovalTemplateTerm is a data structure related to the ApprovalTemplatesService. Source table: WTM4.

## Properties (3)
- `Public Property ConditionType() As ApprovalTemplateConditionTypeEnum` [R/W] Sets or returns a valid value that defines the Deviation type that needs approval. Field name: CondId.
- `Public Property OperationType() As ApprovalTemplateOperationTypeEnum` [R/W] Sets or returns the logical operation required to define the deviation that initiate this Approval Template. Field name: opCode.
- `Public Property Value() As String` [R/W] Sets or returns the value associated with this Approval Template. Field name: opValue.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the an XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalTemplateTerms (Collection)

ApprovalTemplateTerms is a Data Collection of ApprovalTemplateTerm data structures. Source table: WTM4.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateTerm data structures in the ApprovalTemplateTerms data collection. Field name: NumOfDocs).

## Methods (5)
- `Public Function Add() As ApprovalTemplateTerm` Adds a new ApprovalTemplateterm data structure to the ApprovalTemplateTerms Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the ApprovalTemplateTerm data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateTerm` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# ApprovalTemplateUser (Object)

ApprovalTemplateUser is a Data structure related to the ApprovalTemplatesService. Source table: WTM1.

## Properties (1)
- `Public Property UserID() As Long` [R/W] Sets or returns the user Id. of the user authorized to handle this approval template. Field name: UserID. This is a foreign key to the Users object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# ApprovalTemplateUsers (Collection)

ApprovalTemplateUsers is a Data Collection of ApprovalTemplateUser data structures. Source table: WTM1.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateUser data structures in the ApprovalTemplateUsers data collection. Field name: NumOfDocs.

## Methods (5)
- `Public Function Add() As ApprovalTemplateUser` Adds a new ApprovalTemplateUser to the ApprovalTemplateUsers Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the ApprovalTemplateUser data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateUser` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AssetClass (Object)

With SAP Business One, you can use asset classes to classify fixed assets according to business and legal requirements. For each asset class, you can assign various depreciation areas and depreciation types. After you assign an asset class to an asset, the depreciation areas and depreciation types are taken to the asset master data as defaults. Source table: OACS.

## Properties (8)
- `Public Property AssetClassCollection() As AssetClassCollection` [R] Represents the line entries of an asset class.
- `Public Property AssetType() As AssetTypeEnum` [R/W] The type of the asset. Field name: AssetType.
- `Public Property AttributeGroup() As Long` [R/W] The attribute group that you want to assign to the asset class. Field name: AttrGrp.
- `Public Property BPLID() As Long` [R/W] Represents the branch ID (in Brazilian localization); represents the business place ID (in Korean localization). Field name: BPLId.
- `Public Property Code() As String` [R/W] The unique code for the asset class. Field name: Code. Length: 20 characters.
- `Public Property Description() As String` [R/W] The description of the asset class. Field name: Name. Length: 100 characters.
- `Public Property ValueLimitFrom() As Double` [R/W] The lower limit for low value assets. Field name: LimitFrom.
- `Public Property ValueLimitTo() As Double` [R/W] The upper limit for low value assets. Field name: LimitTo.

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

# AssetClassCollection (Collection)

A collection of AssetClassLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetClassLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetClassLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetClassesService (Object)

The AssetClassesService service enables you to create, update and view asset classes. Source table: OACS.

**Remarks:** To open this window, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Fixed Assets --> Asset Classes.

## Methods (8)
- `Public Function Add(ByVal pIAssetClass As AssetClass) As AssetClassParams` Adds an asset class.
  - param `pIAssetClass`: The data for the new asset class.
- `Public Sub Delete(ByVal pIAssetClassParams As AssetClassParams)` Deletes an existing asset class.
  - param `pIAssetClassParams`: The key of the asset class to be deleted.
- `Public Function Get(ByVal pIAssetClassParams As AssetClassParams) As AssetClass` Retrieves an asset class. The asset class is specified by its key, which is contained in the AssetClassParams object passed to the method.
  - param `pIAssetClassParams`: The key of the asset class to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As AssetClassesServiceDataInterfaces) As Object` Creates an empty data structure for use with the AssetClassesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AssetClassesServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetList() As AssetClassParamsCollection` Returns the AssetClassParamsCollection data collection that identifies all asset classes.
- `Public Sub Update(ByVal pIAssetClass As AssetClass)` Updates an existing asset class. The data for the asset class, including the key of the asset class to be updated, is contained in the AssetClass object passed to the method. To update an asset class, you must first retrieve it using the Get method.
  - param `pIAssetClass`: The data for the asset class to be updated. The AssetClass object must contain the key of the object to be updated.

# AssetClassLine (Object)

AssetClassLine is a child object of AssetClass object and represents the depreciation area fields of an asset class. Source table: ACS1.

## Properties (7)
- `Public Property AccountDetermination() As String` [R/W] The account determination for the Posting to G/L type of depreciation areas. Field name: AcctDtn. Length: 15 characters.
- `Public Property ActiveStatus() As BoYesNoEnum` [R/W] Indicate whether the depreciation area is active for the asset class. The system calculates the asset depreciation in all active depreciation areas. Field name: Active.
- `Public Property Code() As String` [R] The unique code for the asset class. Field name: Code. Length: 20 characters.
- `Public Property DepreciationAreaID() As String` [R/W] The depreciation areas for the asset class. Field name: DprAreaID. Length: 15 characters.
- `Public Property DepreciationTypeID() As String` [R/W] The depreciation type in the depreciation area. Field name: DprTypID. Length: 15 characters.
- `Public Property LineNumber() As Long` [R] The current row number in the list. Field name: LineNum.
- `Public Property UseLife() As Long` [R/W] The useful life in months for the assets in this asset class. Field name: UseLife.

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

# AssetClassParams (Object)

Holds the key to an existing asset class. This object is used to pass keys to and retrieve keys from AssetClassesService methods.

## Properties (2)
- `Public Property Code() As String` [R/W] The unique code for the asset class. Field name: Code. Length: 20 characters.
- `Public Property Description() As String` [R] The description of the asset class. Field name: Name. Length: 100 characters.

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

# AssetClassParamsCollection (Collection)

A collection of AssetClassParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetClassParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetClassParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetDepreciationGroup (Object)

AssetDepreciationGroup Class

## Properties (3)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property Group() As String` [R/W] property Group

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

# AssetDepreciationGroupParams (Object)

AssetDepreciationGroupParams Class

## Properties (2)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description

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

# AssetDepreciationGroupParamsCollection (Collection)

AssetDepreciationGroupParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetDepreciationGroupParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetDepreciationGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetDepreciationGroupsService (Object)

AssetDepreciationGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIAssetDepreciationGroup As AssetDepreciationGroup) As AssetDepreciationGroupParams` Add
  - param `pIAssetDepreciationGroup`: 
- `Public Sub Delete(ByVal pIAssetDepreciationGroupParams As AssetDepreciationGroupParams)` Delete
  - param `pIAssetDepreciationGroupParams`: 
- `Public Function Get(ByVal pIAssetDepreciationGroupParams As AssetDepreciationGroupParams) As AssetDepreciationGroup` Get
  - param `pIAssetDepreciationGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As AssetDepreciationGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AssetDepreciationGroupsServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As AssetDepreciationGroupParamsCollection` GetList
- `Public Sub Update(ByVal pIAssetDepreciationGroup As AssetDepreciationGroup)` Update
  - param `pIAssetDepreciationGroup`: 

# AssetDocument (Object)

AssetDocument is a business object that represents the header data of asset documents in the Fixed Asset function of SAP Business One application. With SAP Business One, you can carry out a series of transactions for your fixed assets as follows: - Capitalization - Capitalization Credit Memo - Retirement - Transfer - Manual Depreciation Source table: OACQ.

## Properties (31)
- `Public Property AssetDocumentAreaJournalCollection() As AssetDocumentAreaJournalCollection` [R] Represents the Accounting tab fields of an asset document.
- `Public Property AssetDocumentLineCollection() As AssetDocumentLineCollection` [R] Represents the line entries of an asset document.
- `Public Property AssetValueDate() As Date` [R/W] The date on which the asset is valued. By default, the date is the same as the posting date. Field name: AssetDate.
- `Public Property BaseReference() As String` [R] Displays the document number according to the definition in the Document Numbering - Setup window. Field name: BaseRef.
- `Public Property BPLID() As Long` [R/W] Represents the branch ID (in Brazilian localization); represents the business place ID (in Korean localization). Field name: BPLId.
- `Public Property BPLName() As String` [R/W] Represents the branch name (in Brazilian localization); represents the business place name (in Korean localization). Field name: BPLName. Length: 100 characters.
- `Public Property CancellationDate() As Date` [R/W] The cancellation date. Field name: CancelDate.
- `Public Property CancellationOption() As ClosingOptionEnum` [R/W] The cancellation option - specify a posting date to be used in the cancelled asset document. Field name: CancelOpt.
- `Public Property Currency() As String` [R/W] The currency for the asset document. Field name: Currency. Length: 3 characters.
- `Public Property DepreciationArea() As String` [R/W] The depreciation area in which the asset's depreciation takes effect. Field name: DprArea. Length: 100 characters.
- `Public Property DocEntry() As Long` [R] The internal ID of the asset document. Field name: DocEntry.
- `Public Property DocNum() As Long` [R/W] The number of the asset document. Field name: DocNum.
- `Public Property DocumentDate() As Date` [R/W] The document date. By default, the document date is the same as the posting date. Field name: DocDate.
- `Public Property DocumentRate() As Double` [R/W] The exchange rate of the document currency. Field name: DocRate.
- `Public Property DocumentTotal() As Double` [R] The total amount of the document. Field name: DocTotal.
- `Public Property DocumentTotalFC() As Double` [R] The total amount of the document in foreign currency. Field name: DocTotalFC.
- `Public Property DocumentTotalSC() As Double` [R] The total amount of the document in system currency. Field name: DocTotalSC.
- `Public Property DocumentType() As AssetDocumentTypeEnum` [R/W] The transaction type of the asset document. Field name: DocType.
- `Public Property HandWritten() As BoYesNoEnum` [R/W] Indicates whether it is manual numbering. Field name: Handwrtten.
- `Public Property LowValueAssetRetirement() As BoYesNoEnum` [R/W] Indicates whether this is low value asset retirement. Field name: LVARetire.
- `Public Property ManualDepreciationType() As String` [R/W] The type of the manual depreciation. Field name: ManDprType. Length: 15 characters.
- `Public Property Origin() As Long` [R] The origin of the asset document. Field name: CreatedBy.
- `Public Property OriginalType() As AssetOriginalTypeEnum` [R] The original type of the asset document. Field name: TransType.
- `Public Property PostingDate() As Date` [R/W] The date on which the journal entry is posted. Field name: PostDate.
- `Public Property Reference() As String` [R/W] The additional information about the asset document. Field name: Reference. Length: 32 characters.
- `Public Property Remarks() As String` [R/W] The remarks about the asset. Field name: Comments. Length: 254 characters.
- `Public Property Series() As Long` [R/W] Specify a numbering series. Field name: Series.
- `Public Property Status() As AssetDocumentStatusEnum` [R] The status of the asset document. Field name: DocStatus.
- `Public Property SummerizeByDistributionRules() As BoYesNoEnum` [R/W] Consolidates journal entry rows according to the distribution rules assigned to the assets. Field name: DstRlSmarz.
- `Public Property SummerizeByProjects() As BoYesNoEnum` [R/W] Consolidates journal entry rows according to the projects assigned to the assets. Field name: PrjSmarz.
- `Public Property VATRegNum() As String` [R/W] Represents CNPJ (in Brazilian localization); represents the VAT registration number (in Korean localization). Field name: VatRegNum. Length: 32 characters.

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

# AssetDocumentAreaJournal (Object)

AssetDocumentAreaJournal is a child object of AssetDocument object and represents the Accounting tab fields of an asset document. Source table: ACQ2.

## Properties (7)
- `Public Property CancellationJournalRemarks() As String` [R/W] The remark about the journal entry generated upon the cancellation of the asset document. Field name: JrnlMemo1. Length: 50 characters.
- `Public Property CancellationTransactionNumber() As Long` [R] The transaction number that SAP Business One creates for the cancellation of the asset document. Field name: TransNum1.
- `Public Property DepreciationArea() As String` [R/W] The Posting to G/L depreciation areas that are associated with the selected assets in this document. Field name: DprArea. Length: 15 characters.
- `Public Property DocEntry() As Long` [R] The internal ID of the asset document. Field name: DocEntry.
- `Public Property JournalRemarks() As String` [R/W] The remark about the journal entry generated in each depreciation area. Field name: JrnlMemo. Length: 50 characters.
- `Public Property LineNumber() As Long` [R/W] The current row number in the list. Field name: LineNum.
- `Public Property TransactionNumber() As Long` [R] The transaction number that SAP Business One creates for the asset document. Field name: TransNum.

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

# AssetDocumentAreaJournalCollection (Collection)

A collection of AssetDocumentAreaJournal objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetDocumentAreaJournal` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetDocumentAreaJournal` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetDocumentLine (Object)

AssetDocumentLine is a child object of AssetDocument object and represents the line entries of an asset document. Source table: ACQ1.

## Properties (20)
- `Public Property APC() As Double` [R/W] If you want to retire an asset partially and the asset is not planned for quantity maintenance, specify how much of the asset's acquisition and production costs are retired. Field name: APC.
- `Public Property AssetNumber() As String` [R/W] The asset you want to acquire. Field name: ItemCode. Length: 20 characters.
- `Public Property DepreciationArea() As String` [R] The Posting to G/L depreciation areas that are associated with the selected assets in this document. Field name: DprArea. Length: 15 characters.
- `Public Property DistributionRule() As String` [R/W] property DistributionRule
- `Public Property DistributionRule2() As String` [R/W] property DistributionRule2
- `Public Property DistributionRule3() As String` [R/W] property DistributionRule3
- `Public Property DistributionRule4() As String` [R/W] property DistributionRule4
- `Public Property DistributionRule5() As String` [R/W] property DistributionRule5
- `Public Property DocEntry() As Long` [R] The internal ID of the asset document. Field name: DocEntry.
- `Public Property GLAccount() As String` [R/W] The clearing account for the acquisition and production costs of the fixed assets. By default, is the Acquisition Clearing Account you have specified for the asset. Field name: AcctCode. Length: 15 characters.
- `Public Property LineNumber() As Long` [R/W] The current row number in the list. Field name: LineNum.
- `Public Property NewAssetClass() As String` [R/W] The new asset class for the asset to which you want to transfer the asset. Field name: NewAstCls. Length: 20 characters.
- `Public Property NewAssetNumber() As String` [R/W] The target asset to which you want to transfer the asset. Field name: NewItemCod. Length: 20 characters.
- `Public Property Partial() As BoYesNoEnum` [R/W] Indicates whether the asset retirement is partial. Only part of the asset quantity or value is removed from the portfolio. Field name: Partial.
- `Public Property Project() As String` [R/W] property Project
- `Public Property Quantity() As Double` [R/W] If the asset is planned for quantity maintenance, specify the acquired quantity. Field name: Quantity.
- `Public Property Remarks() As String` [R/W] The remarks about the asset. Field name: Remarks. Length: 100 characters.
- `Public Property TotalFC() As Double` [R/W] The acquisition cost of the asset in foreign currency. Field name: TotalFrgn.
- `Public Property TotalLC() As Double` [R/W] The acquisition cost of the asset in local currency. Field name: LineTotal.
- `Public Property TotalSC() As Double` [R] The acquisition cost of the asset in system currency. Field name: TotalSys.

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

# AssetDocumentLineCollection (Collection)

A collection of AssetDocumentLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetDocumentLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetDocumentLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetDocumentParams (Object)

Holds the key and cancellation information to an existing asset document. This object is used to pass keys to and retrieve keys from AssetDocumentService methods.

## Properties (3)
- `Public Property CancellationDate() As Date` [R/W] The cancellation date. Field name: CancelDate.
- `Public Property CancellationOption() As ClosingOptionEnum` [R/W] The cancellation option - specify a posting date to be used in the cancelled asset document. Field name: CancelOpt.
- `Public Property Code() As Long` [R/W] The unique code for the asset document.

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

# AssetDocumentParamsCollection (Collection)

A collection of AssetDocumentParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetDocumentParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetDocumentParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetDocumentService (Object)

The AssetDocumentService service enables you to add, look up, update, cancel, and remove asset documents. Source table: OACQ.

**Remarks:** From the SAP Business One Main Menu, choose Financials --> Fixed Assets.

**Example:**
- C# example (from SAP's help):
  ```csharp
  AssetDocumentService AssetService = (AssetDocumentService)m_oCompanyService.GetBusinessService(ServiceTypes.AssetCapitalizationService);
  AssetDocument AssetDocument = AssetService.GetDataInterface(AssetDocumentServiceDataInterfaces.adsAssetDocument);
  AssetDocumentLine line = AssetDocument.AssetDocumentLineCollection.Add();
  AssetDocumentAreaJournal journalEn = AssetDocument.AssetDocumentAreaJournalCollection.Add();

  AssetDocument.AssetValueDate = New DateTime(2013, 8, 1);
  line.AssetNumber = "FA01";
  line.TotalLC = 15000;
  journalEn.DepreciationArea = "DA_test";
  journalEn.JournalRemarks = "Remark_test";

  AssetService.Add(AssetDocument);
  ```
- C# example (from SAP's help):
  ```csharp
  AssetDocumentService AssetService = (AssetDocumentService)m_oCompanyService.GetBusinessService(ServiceTypes.AssetCapitalizationService);
  AssetDocumentParams faDocumentParams = (AssetDocumentParams)AssetService.GetDataInterface(AssetDocumentServiceDataInterfaces.adsAssetDocumentParams);
  faDocumentParams.Code = 1;
  AssetDocument AssetDocument = AssetService.Get(faDocumentParams);

  AssetDocument.AssetDocumentLineCollection.Item(0).Remarks = "Test1";
  AssetDocument.Remarks = "Test2";

  AssetService.Update(AssetDocument);
  ```
- C# example (from SAP's help):
  ```csharp
  AssetDocumentService AssetService = (AssetDocumentService)m_oCompanyService.GetBusinessService(ServiceTypes.AssetCapitalizationService);
  AssetDocumentParams faDocumentParams = AssetService.GetDataInterface(AssetDocumentServiceDataInterfaces.adsAssetDocumentParams);

  faDocumentParams.Code = 1;
  faDocumentParams.CancellationOption = ClosingOptionEnum.coBySpecifiedDate;
  faDocumentParams.CancellationDate = new DateTime(2013, 10, 1);
  AssetService.Cancel(faDocumentParams);
  ```

## Methods (9)
- `Public Function Add(ByVal pIAssetDocument As AssetDocument) As AssetDocumentParams` Adds an asset document.
  - param `pIAssetDocument`: The data for the new asset document.
- `Public Sub Cancel(ByVal pIAssetDocumentParams As AssetDocumentParams)` Cancels an existing asset document.
  - param `pIAssetDocumentParams`: The key of the asset document to be cancelled.
- `Public Sub Delete(ByVal pIAssetDocumentParams As AssetDocumentParams)` Deletes an existing asset document.
  - param `pIAssetDocumentParams`: The key of the asset document to be deleted.
- `Public Function Get(ByVal pIAssetDocumentParams As AssetDocumentParams) As AssetDocument` Retrieves an asset document. The asset document is specified by its key, which is contained in the AssetDocumentParams object passed to the method.
  - param `pIAssetDocumentParams`: The key of the asset document to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As AssetDocumentServiceDataInterfaces) As Object` Creates an empty data structure for use with the AssetDocumentService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AssetDocumentServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetList() As AssetDocumentParamsCollection` Returns the AssetDocumentParamsCollection data collection that identifies all asset documents.
- `Public Sub Update(ByVal pIAssetDocument As AssetDocument)` Updates an existing asset document. The data for the asset document, including the key of the asset document to be updated, is contained in the AssetDocument object passed to the method. To update an asset document, you must first retrieve it using the Get method.
  - param `pIAssetDocument`: The data for the asset document to be updated. The AssetDocument object must contain the key of the object to be updated.

# AssetGroup (Object)

The asset group to which the asset belongs. Source table: OAGS.

## Properties (2)
- `Public Property Code() As String` [R/W] The unique code for the asset group. Field name: Code. Length: 15 characters.
- `Public Property Description() As String` [R/W] The description of the asset group. Field name: Descr. Length: 100 characters.

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

# AssetGroupParams (Object)

Holds the key to an existing asset group. This object is used to pass keys to and retrieve keys from AssetGroupsService methods.

## Properties (2)
- `Public Property Code() As String` [R/W] The unique code for the asset group. Field name: Code. Length: 15 characters.
- `Public Property Description() As String` [R] The description of the asset group. Field name: Descr. Length: 100 characters.

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

# AssetGroupParamsCollection (Collection)

A collection of AssetGroupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetGroupParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetGroupsService (Object)

The AssetGroupsService service enables you to add, look up, update, and remove asset groups. Source table: OAGS.

**Remarks:** To open the Asset Groups - Setup window, in the Asset Master Data window - Fixed Assets tab - Overview Subtab - Asset Group field, select Define New from the dropdown list.

## Methods (8)
- `Public Function Add(ByVal pIAssetGroup As AssetGroup) As AssetGroupParams` Adds an asset group.
  - param `pIAssetGroup`: The data for the new asset group.
- `Public Sub Delete(ByVal pIAssetGroupParams As AssetGroupParams)` Deletes an existing asset group.
  - param `pIAssetGroupParams`: The key of the asset group to be deleted.
- `Public Function Get(ByVal pIAssetGroupParams As AssetGroupParams) As AssetGroup` Retrieves an asset group. The asset group is specified by its key, which is contained in the AssetGroupParams object passed to the method.
  - param `pIAssetGroupParams`: The key of the asset group to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As AssetGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the AssetGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AssetGroupsServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetList() As AssetGroupParamsCollection` Returns the AssetGroupParamsCollection data collection that identifies all asset groups.
- `Public Sub Update(ByVal pIAssetGroup As AssetGroup)` Updates an existing asset group. The data for the asset group, including the key of the asset group to be updated, is contained in the AssetGroup object passed to the method. To update an asset group, you must first retrieve it using the Get method.
  - param `pIAssetGroup`: The data for the asset group to be updated. The AssetGroup object must contain the key of the object to be updated.

# AssetRevaluation (Object)

Use the object to revaluate assets. Source table: OFAR.

**Remarks:** Financials --> Fixed Assets --> Asset Revaluation

## Properties (19)
- `Public Property AssetRevaluationLineCollection() As AssetRevaluationLineCollection` [R] Asset revaluation line collection
- `Public Property AssetValueDate() As Date` [R/W] The date on which the revaluation takes place. Field name: AssetDate.
- `Public Property BPLID() As Long` [R/W] Branch. Field name: BPLId.
- `Public Property BPLName() As String` [R] Branch name. Field name: BPLName. Length: 100 characters.
- `Public Property DepreciationArea() As String` [R/W] The depreciation area in which the asset revaluation takes effect. Field name: DprArea. Length: 15 characters.
- `Public Property DocEntry() As Long` [R] Internal number. Field name: DocEntry.
- `Public Property DocNum() As Long` [R] Document number. Field name: DocNum.
- `Public Property DocumentDate() As Date` [R/W] Document date. Field name: DocDate.
- `Public Property HandWritten() As BoYesNoEnum` [R/W] Manual numbering. Field name: Handwrtten.
- `Public Property IfrsPosting() As BoYesNoEnum` [R/W] Whether to post asset revaluations according to International Financial Reporting Standards (IFRS) for depreciation areas whose Posting of Depreciation is Indirect Posting. Field name: IfrsPsting.
- `Public Property JournalRemarks() As String` [R/W] Journal remarks. Field name: JrnlMemo. Length: 254 characters.
- `Public Property PeriodIndicator() As String` [R] Period indicator. Field name: PIndicator. Length: 10 characters.
- `Public Property PostingDate() As Date` [R/W] The date on which the journal entry is posted. Field name: PostDate.
- `Public Property Reference() As String` [R/W] The additional information about the revaluation. Field name: Ref. Length: 32 characters.
- `Public Property Remarks() As String` [R/W] Journal remarks. Field name: Comments. Length: 254 characters.
- `Public Property RevaluationPercent() As Double` [R/W] The revaluation percentage. Field name: RevalPerc.
- `Public Property Series() As Long` [R/W] Series. Field name: Series.
- `Public Property TransId() As Long` [R] Transaction number. Field name: TransId.
- `Public Property VATRegNum() As String` [R/W] VAT reg. number. Field name: VatRegNum. Length: 32 characters.

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

# AssetRevaluationLine (Object)

Source table: FAR1.

## Properties (7)
- `Public Property AssetNumber() As String` [R/W] Asset No. Field name: ItemCode. Length: 50 characters.
- `Public Property CurrentNBV() As Double` [R] The asset's net book value on the asset value date you specified. Field name: NBV.
- `Public Property DocEntry() As Long` [R] Internal number. Field name: DocEntry.
- `Public Property LineNumber() As Long` [R] Line number. Field name: LineNum.
- `Public Property NewNBV() As Double` [R/W] The new net book value of the asset after the revaluation. Field name: New_NBV.
- `Public Property Remarks() As String` [R/W] The remarks about the asset. Field name: Remarks. Length: 100 characters.
- `Public Property RevaluationPercent() As Double` [R/W] Revaluation percentage. Field name: RevalPerc.

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

# AssetRevaluationLineCollection (Collection)

AssetRevaluationLineCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetRevaluationLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetRevaluationLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetRevaluationParams (Object)

AssetRevaluationParams Class

## Properties (1)
- `Public Property DocEntry() As Long` [R/W] Internal number. Field name: DocEntry.

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

# AssetRevaluationParamsCollection (Collection)

AssetRevaluationParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AssetRevaluationParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AssetRevaluationParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AssetRevaluationService (Object)

Use the AssetRevaluationService service to revaluate assets. Source table: OFAR.

**Remarks:** Financials --> Fixed Assets --> Asset Revaluation

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.AssetRevaluationService revaluationSer = (SAPbobsCOM.AssetRevaluationService)cs.GetBusinessService(SAPbobsCOM.ServiceTypes.AssetRevaluationService);
  SAPbobsCOM.AssetRevaluation revaluationObj = revaluationSer.GetDataInterface(AssetRevaluationServiceDataInterfaces.arsAssetRevaluation);
  SAPbobsCOM.AssetRevaluationParams revaluationParams = revaluationSer.GetDataInterface(AssetRevaluationServiceDataInterfaces.arsAssetRevaluationParams);

  revaluationObj.PostingDate = new System.DateTime(2025, 12, 31, 0, 0, 0);
  revaluationObj.AssetValueDate = revaluationObj.PostingDate;
  revaluationObj.DocumentDate = revaluationObj.PostingDate;
  revaluationObj.DepreciationArea = ""MainArea"";

  AssetRevaluationLineCollection lines = revaluationObj.AssetRevaluationLineCollection;
  AssetRevaluationLine line = lines.Add();
  line.AssetNumber = ""FA001"";
  //line.NewNBV = 76800;
  line.RevaluationPercent = 110;

  revaluationParams = revaluationSer.Add(revaluationObj);
  ```

## Methods (8)
- `Public Function Add(ByVal pIAssetRevaluation As AssetRevaluation) As AssetRevaluationParams` Add
  - param `pIAssetRevaluation`: 
- `Public Sub Delete(ByVal pIAssetRevaluationParams As AssetRevaluationParams)` Delete
  - param `pIAssetRevaluationParams`: 
- `Public Function Get(ByVal pIAssetRevaluationParams As AssetRevaluationParams) As AssetRevaluation` Get
  - param `pIAssetRevaluationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As AssetRevaluationServiceDataInterfaces) As Object` Creates an empty data structure for use with the AssetRevaluationService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AssetRevaluationServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Function GetList() As AssetRevaluationParamsCollection` GetList
- `Public Sub Update(ByVal pIAssetRevaluation As AssetRevaluation)` Update
  - param `pIAssetRevaluation`: 

# Attachment (Object)

The Attachment object represents an external file that is attached to business objects, such as, Contacts, Messages, and ServiceContracts. From DI API version 2005, use the Attachments2 object.

## Properties (1)
- `Public Property FileName() As String` [R/W] Sets or returns the attachment file name.
  - remarks: In SAP Business One, attachments are stored in a file. Use this property to set the file name of the attachment. If you updates an existing record, you can leave this field empty and the specified Attachment item will be deleted in the update process.

# Attachments (Collection)

Attachments is a collection of one or more Attachment objects. From DI API version 2005, use the Attachments2 object.

**Remarks:** To remove an Attachment item, set its FileName property to NULL ("") and call the Update method of the calling object.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of Attachment items in the collection.

## Methods (3)
- `Public Sub Add()` Adds a new Attachment item to the Attachments collection.
- `Public Function Item(ByVal Index As Variant) As Attachment` Retrieves an existing attachment item from the Attachments object.
  - param `Index`: specifies the index value of the item (starts from 0).
  - returns: The Item method returns an Attachment object, or nothing if failed.
  - remarks: You can use the Add method to add a new Attachment object to the Attachments collection, and then use the Item method to reference the attachment object by its index value.
- `Public Sub Refresh()` Refreshen the attachments collection.
  - remarks: Call this method after using the GetBusinessObjectFromXML method.

# Attachments2 (Object)

The Attachments2 object enables to copy files from a source folder to the Attachments folder that is defined through the application. Files stored in the Attachments folder can be associated by the AttachmentEntry property of the following objects: Contacts, ContractTemplates, CustomerEquipmentCards, EmployeeInfo, KnowledgeBaseSolutions, Messages, Message, SalesOpportunities, and ServiceContracts. This object replaces the Attachment and Attachments objects. Source table: OATC.

**Remarks:** The Attachments Path must be defined in the application before using this object. This path is stored in the AttachePath field of the OADP table, which is not exposed through the DI API. Mandatory property: Lines. You must set the Attachments2_Lines child object whith the following properties: SourcePath, FileName, and FileExtension. To define the Attachments Path in the application: - Select Administration -->System Initialization -->General Settings -->Path tab.

## Properties (4)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the attachment file as assigned by SAP Business One when adding an attachment file. Field name: AbsEntry.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Lines() As Attachments2_Lines` [R] Returns the Attachments2_Lines child object (mandatory).
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds attachment files that are specified by the Attachments2_Lines child object.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lAbsoluteEntry As Long) As Boolean` Determines wether or not the object identified by its AbsoluteEntry exists. If the object exists, the method gets it.
  - param `lAbsoluteEntry`: Specifies the AbsoluteEntry of the object you want to get.
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

# Attachments2_Lines (Object)

The Attachments2_Lines is a child object of the Attachments2 object. Each line stores details about one attachment file. Source table: ATC1.

**Remarks:** Mandatory properties: Attachments2_Lines, FileName, and FileExtension. To display the form in the application: - Select the Attachments tab of one of the following forms: Employee Master Data, Contracts, Contract Template, Service Contract, and Customer Equipment Card.

## Properties (13)
- `Public Property AbsoluteEntry() As Long` [R] Returns the identification key of the attachment file as assigned by SAP Business One when adding an attachment file. Field name: AbsEntry.
- `Public Property AttachmentDate() As Date` [R] Returns the date when the file was copied to the system attachments folder. Field name: Date.
- `Public Property CopyToProductionOrder() As BoYesNoEnum` [R/W] Copy attachments automatically from BOM to production order. Field name: CopyToProd.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Attachments2 att = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oAttachments2); success = att.GetByKey(productionOrder.AttachmentEntry);
    att.Lines.SetCurrentLine(0);
    att.Lines.CopyToProductionOrder = BoYesNoEnum.tYES;
    ```
- `Public Property CopyToTargetDoc() As BoYesNoEnum` [R/W] Copy to target document. Field name: CopyToTrgt.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property FileExtension() As String` [R/W] Sets or returns the file extension. Field name: FileExt. Length: 8 characters.
  - remarks: Mandatory fields in SAP Business One: FileExtension.
- `Public Property FileName() As String` [R/W] Sets or returns the file name. Field name: FileName. Length: 254 characters.
  - remarks: Mandatory fields in SAP Business One: FileName.
- `Public Property FreeText() As String` [R/W] Free text. Field name: FreeText. Length: 100 characters.
- `Public Property LineNum() As Long` [R/W] Row number. Field name: Line.
- `Public Property Override() As BoYesNoEnum` [R/W] Determines whether or not to override a file, with the same name, that is already stored in the system attachments folder. Field name: Override.
- `Public Property SourcePath() As String` [R/W] Sets or returns the folder name and path where the source files are stored. Field name: srcPath. Length: 64,000 characters.
  - remarks: Mandatory fields in SAP Business One: SourcePath.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserID() As Long` [R] Returns the identification key of the user who operates the system. Field name: UsrID. Returns the identification key of the active user who operates the system.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# AttributeGroup (Object)

Source table: OFAA.

## Properties (4)
- `Public Property AttributeGroupCollection() As AttributeGroupCollection` [R] property AttributeGroupCollection
- `Public Property Code() As Long` [R] The code of an attribute group. Field name: Code.
- `Public Property Locked() As BoYesNoEnum` [R] Indicates whether the attribute group is locked. Field name: Locked.
- `Public Property Name() As String` [R/W] The name of the attribute group. Field name: Name. Length: 100 characters.

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

# AttributeGroupCollection (Collection)

AttributeGroupCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AttributeGroupLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AttributeGroupLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AttributeGroupLine (Object)

Source table: FAA1.

## Properties (6)
- `Public Property AttributeID() As Long` [R/W] The ID of the active attribute in the attribute group that you assigned to the asset class of the asset. Field name: AttrID.
- `Public Property AttributeName() As String` [R/W] The name of the active attribute in the attribute group that you assigned to the asset class of the asset. Field name: AttrName. Length: 100 characters.
- `Public Property Code() As Long` [R] The code of an attribute group. Field name: Code.
- `Public Property DefaultValue() As String` [R/W] The attribute value that is taken to the asset master data as the default attribute value. Field name: DefaultVal. Length: 100 characters.
- `Public Property FieldType() As AttributeGroupFieldTypeEnum` [R] The predefined type of the attribute field. Field name: FieldType.
- `Public Property SortNumber() As Long` [R/W] The current row number in the list. Field name: LineNum.

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

# AttributeGroupParams (Object)

AttributeGroupParams Class

## Properties (2)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property Name() As String` [R] property Name

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

# AttributeGroupParamsCollection (Collection)

AttributeGroupParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As AttributeGroupParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As AttributeGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# AttributeGroupsService (Object)

AttributeGroupsService Class

## Methods (8)
- `Public Function Add(ByVal pIAttributeGroup As AttributeGroup) As AttributeGroupParams` Add
  - param `pIAttributeGroup`: 
- `Public Sub Delete(ByVal pIAttributeGroupParams As AttributeGroupParams)` Delete
  - param `pIAttributeGroupParams`: 
- `Public Function Get(ByVal pIAttributeGroupParams As AttributeGroupParams) As AttributeGroup` Get
  - param `pIAttributeGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As AttributeGroupsServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AttributeGroupsServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As AttributeGroupParamsCollection` GetList
- `Public Sub Update(ByVal pIAttributeGroup As AttributeGroup)` Update
  - param `pIAttributeGroup`: 

# BankChargesAllocationCode (Object)

Represents codes for the allocation of bank charges. These codes can be used as sorting or filtering parameters in the OPEX table that is created by SAP Business One and processed by Payment Engine. Source table: OBCA.

## Properties (2)
- `Public Property Code() As String` [R/W] The allocation code for bank charges. Field name: Code. Length: 3 characters.
- `Public Property Description() As String` [R/W] The description of the allocation code for bank charges. Field name: Name. Length: 50 characters.

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

# BankChargesAllocationCodeParams (Object)

Holds the key and name to a bank charges allocation code. This object is used to pass keys to and retrieve keys from BankChargesAllocationCodesService methods.

## Properties (2)
- `Public Property Code() As String` [R/W] The key that identifies the allocation code for bank charges. Field name: Code. Length: 3 characters.
- `Public Property Description() As String` [R] The description of the allocation code for bank charges. Field name: Name. Length: 50 characters.

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

# BankChargesAllocationCodesParams (Collection)

A collection of BankChargesAllocationCodeParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As BankChargesAllocationCodeParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As BankChargesAllocationCodeParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# BankChargesAllocationCodesService (Object)

The BankChargesAllocationCodesService service enables you to add, look up, update, and remove allocation codes for bank charges. Source table: OBCA.

**Remarks:** To see the list of codes for the allocation of bank charges, from SAP Business One, choose Administration --> Setup --> Banking --> Bank Charges Allocation Codes.

## Methods (9)
- `Public Function AddBankChargesAllocationCode(ByVal pIBankChargesAllocationCode As BankChargesAllocationCode) As BankChargesAllocationCodeParams` Adds a bank charges allocation code.
  - param `pIBankChargesAllocationCode`: The data for the bank charges allocation code.
- `Public Sub DeleteBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams)` Deletes an existing bank charges allocation code.
  - param `pIBankChargesAllocationCodeParams`: The key of the bank charges allocation code to be deleted.
- `Public Function GetBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams) As BankChargesAllocationCode` Retrieves a bank charges allocation code. The bank charges allocation code is specified by its key, which is contained in the BankChargesAllocationCodeParams object passed to the method.
  - param `pIBankChargesAllocationCodeParams`: The key of the bank charges allocation code to retrieve.
- `Public Function GetBankChargesAllocationCodeList() As BankChargesAllocationCodesParams` Returns the BankChargesAllocationCodesParams data collection that identify all bank charges allocation codes.
- `Public Function GetDataInterface(ByVal enumMSDI As BankChargesAllocationCodesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BankChargesAllocationCodesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `BankChargesAllocationCodesServiceDataInterfaces` in `../enums/enums-01.md`
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
- `Public Sub SetDefaultBankChargesAllocationCode(ByVal pIBankChargesAllocationCodeParams As BankChargesAllocationCodeParams)` Sets the default bank charges allocation code.
  - param `pIBankChargesAllocationCodeParams`: The key of the bank charges allocation code.
  - C# example (from SAP's help):
    ```csharp
    void SetDefaultCode ()
            {
                Try
                {
                    CompanyService oCompSrv = MyCompany.GetCompanyService();
                    BankChargesAllocationCodesService oBCACodeSrv = (BankChargesAllocationCodesService)(oCompSrv.GetBusinessService(ServiceTypes.BankChargesAllocationCodesService));
                    BCACodeParams defaultCode;
                    defaultCode = (BCACodeParams)oBCACodeSrv.GetDataInterface(BankChargesAllocationCodesServiceDataInterfaces.bcacsBCACodeParams);
                    defaultCode.Code = "1";
                    oBCACodeSrv. SetDefaultBankChargesAllocationCode(defaultCode);
                }
                Catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString());
                }
    }
    ```
- `Public Sub UpdateBankChargesAllocationCode(ByVal pIBankChargesAllocationCode As BankChargesAllocationCode)` Updates an existing bank charges allocation code. The data for the bank charges allocation code, including the key of the bank charges allocation code to be updated, is contained in the BankChargesAllocationCode object passed to the method. To update a bank charges allocation code, you must first retrieve it using the GetBankChargesAllocationCode method.
  - param `pIBankChargesAllocationCode`: The data for the bank charges allocation code to be updated. The BankChargesAllocationCode object must contain the key of the object to be updated.

# BankPages (Object)

BankPages is a business object that represents external bank statements in the Banking module. This object enables you to: - Add bank statements. - Retrieve a bank statement by its key. - Update bank statements. - Save the object in XML format. Source table: OBNK.

**Remarks:** Mandatory fields in SAP Business One: AccountCode, and CreditAmount or DebitAmount. To display the form in the application: - Select Banking --> Bank Statements and Reconciliations --> Process External Bank Statement.

## Properties (24)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code of the business partner as defined in Chart of Accounts. Field name: AcctCode. Mandatory property. Length: 15 characters.
  - remarks: To set the AccountCode value when working with segmentation, use the FormatCode to find its key value (for example, _SYS00000000010) as follows: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim sStr As String

        Dim vRs As SAPbobsCOM.Recordset

        Dim vBOB As SAPbobsCOM.SBObob

        Dim vCH As SAPbobsCOM.ChartOfAccounts

        Set vCH = Vcmp.GetBusinessObject(oChartOfAccounts)

        Set vBOB = Vcmp.GetBusinessObject(BoBridge)

        Set vRs = Vcmp.GetBusinessObject(BoRecordset)

        Set vRs = vBOB.GetObjectKeyBySingleValue(oBusinessPartners, "CardName", "aaa", bqc_Equal)

        ' When working with segmentation use this function

        ' to find the account key in the ChartOfAccount object

        Set vRs = vBOB.GetObjectKeyBySingleValue(oChartOfAccounts, "FormatCode", "125100000100101", bqc_Equal)

        'The Recordset retrieves the value of the key (for example,  sStr = _SYS00000000010).

        sStr = vRs.Fields.Item(0).Value

        'Use the sStr value to set the AccountCode
    ```
- `Public Property AccountName() As String` [R] Returns the G/L account name of the business partner as defined in Chart of Accounts. Field name: AcctName. Length: 100 characters.
- `Public Property BankMatch() As Long` [R] Returns the status indicating whether or not the amount in the line of the bank statement is reconciled with amount in the line of the G/L account or business partner account. Field name: BankMatch.
- `Public Property BICSwiftCode() As String` [R/W] The BIC/SWIFT code of the business partner bank account as defined in the Business Partner Bank Accounts – Setup window. Field name: BPswift. Length: 50 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Length: 15 characters.
  - remarks: SAP Business One validates the CardCode, and if not valid, returns an error code. To create a receipt that matches to the invoice, set the following properties: CardCode, AccountCode, InvoiceNumber, CreditAmount or DebitAmount that must be equal to the invoice amount, and PaymentCreated.
- `Public Property CardName() As String` [R/W] Sets or returns the name of the existing business partner. Field name: CardName. Length: 100 characters.
  - remarks: SAP Business One validates this code, and if not valid, returns an error code.
- `Public Property CreditAmount() As Double` [R/W] Sets or returns the amount in foreign currency to credit the account. Field name: CredAmnt. Mandatory field in SAP Business One, if the amount is to credit the account.
- `Public Property DataSource() As String` [R] Not supported.
- `Public Property DebitAmount() As Double` [R/W] Sets or returns the amount in foreign currency to debit the account. Field name: DebAmount. Mandatory field in SAP Business One, if the amount is to debit the account.
- `Public Property DocNumberType() As BoBpsDocTypes` [R/W] Sets or returns a boolean value that specifies the document type for identifying an invoice document. Field name: DocNumType.
  - remarks: Default value is: bpdt_DocNum, which identifies the invoice by its number.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date in a bank statement row. Field name: DueDate.
- `Public Property ExternalCode() As String` [R/W] Sets or returns the external code. Field name: ExternCode. Length: 30 characters.
  - remarks: The ExternalCode property (together with CardName, CardCode, StatementNumber, InvoiceNumber, PaymentCreated, and VisualOrder) enable to create a receipt that matches to the invoice. If the value of PaymentCreated property is set to Yes and the payment creation succeeds, the property type is changed to Read Only.
- `Public Property InvoiceNumber() As Long` [R/W] Sets or returns the number of the invoice for payment. From release 2004, use the InvoiceNumberEx property, which is a string, instead of this property. Field name: DocNum. Length: 27 characters.
  - remarks: The InvoiceNumber property (together with CardCode, CardName, ExternalCode, PaymentCreated, and StatementNumber) enable to create a receipt that matches to the invoice. If the value of PaymentCreated property is set to Yes and the payment creation succeeds, the property type is changed to Read Only.
- `Public Property InvoiceNumberEx() As String` [R/W] Sets or returns a string that specifies the number of the invoice for payment. Field name: ExternCode. Length: 30 characters.
  - remarks: Use this property instead of InvoiceNumber (which remains the DI API to maintain backward compatibility).
- `Public Property Memo() As String` [R/W] Sets or returns the details of a line in the bank statement. Field name: Memo. Length: 255 characters.
- `Public Property PaymentCreated() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the payment was created. Field name: PaymCreat.
  - remarks: If the payment creation fails, the value of PaymentCreated property is changed to No.
- `Public Property PaymentReference() As String` [R/W] Sets or returns the payment reference that authorizes the payment process (according to the legal requirements). Field name: PaymentRef. Length: 27 characters.
- `Public Property Reference() As String` [R/W] Sets or returns the reference number in the bank statement row. Length: 8 characters. Field name: PaymentRef.
- `Public Property Sequence() As Long` [R] Returns the sequential number used, together with AccountCode, for identifying the bank account. Field name: Sequence.
- `Public Property StatementNumber() As Long` [R/W] Sets or returns the number of the bank statement. Field name: IdNumber.
  - remarks: The StatementNumber property (together with CardCode, CardName, ExternalCode, InvoiceNumber, and PaymentCreated) enable to create a receipt that matches to the invoice. If the value of PaymentCreated property is set to Yes and the payment creation succeeds, the property type is changed to Read Only.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the bank statement. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property VisualOrder() As Long` [R/W] Sets or returns the appearance order of the bank statement line. Field name: VisOrder.
  - remarks: By default, the visual order number equals to the Sequence number. To add a row between exiting rows, set the VisualOrder value to the required row number and call the Add method.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal AccountCode As String, ByVal Sequence As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `AccountCode`: Specifies the bank account code.
  - param `Sequence`: Specifies the sequential number used for identifying (together with the AccountCode) the bank account.
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
