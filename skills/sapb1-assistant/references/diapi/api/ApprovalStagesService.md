<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
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
  - enum: `../enums/ApprovalStagesServiceDataInterfaces.md`
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
