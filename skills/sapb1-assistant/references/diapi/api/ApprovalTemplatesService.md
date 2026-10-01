<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
  - enum: `../enums/ApprovalTemplatesServiceDataInterfaces.md`
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
