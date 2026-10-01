<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalRequestsService (Object)

ApprovalRequestsService is a business object that manages the approval requests process in the SAP Business One environment. This object enables users to do the following: - Get an approval request from the approval process. - Get a list of approval requests from the approval process. - Get a list of open approval requests from the approval process. - Update an approval request within the approval process. - Get data interfaces. Source table: OWDD.

**Remarks:** From the SAP Business One application, you can do the following: Approve draft documents in the Request for Approval window when you are reviewing messages in the Messages/Alert Overview window. Approve draft documents in the Approval Decision Report window when you generate a report of the status of draft documents requiring approval. Approving draft documents from the Request for Approval window: - Choose Window --> Messages/Alert Overview. The Messages/Alert Overview window appears. - To display the details of the message in the Request for Document Approval area, select the required message. To open the Request for Approval window, click the link arrow. In the Decision list, select your decision for the approval request. Choose the Update button. An internal message is sent to the document originator regarding the approval. Approving draft documents from the Approval Decision Report window: Choose Administration --> Approval Procedures --> Approval Decision Report. The Approval Decision Report - Selection Criteria window appears. To generate the report, choose the required criteria. Choose the OK button. The Approval Decision Report window appears. In the Answer column, select your decision for the approval request. Choose the Update button. An internal message is sent to the document originator regarding the approval.

**Example:**
- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
  ```vb
  Dim oApprovalRequestsService As ApprovalRequestsService = oCompany.GetCompanyService().GetBusinessService(ServiceTypes.ApprovalRequestsService)
  Dim oApprovalRequest As ApprovalRequest = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequest)
  Dim oApprovalRequestParams As ApprovalRequestParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestParams)

  oApprovalRequestParams.Code = indexNum ' The approval index

  ' Get approval request details
  oApprovalRequest = oApprovalRequestsService.GetApprovalRequest(oApprovalRequestParams)

  txtDocType.Text = oApprovalRequest.ObjectType
  txtDocNo.Text = oApprovalRequest.ObjectEntry
  txtUser.Text = oApprovalRequest.OriginatorID.ToString
  txtCurrStage.Text = oApprovalRequest.CurrentStage
  txtRemarks.Text = oApprovalRequest.ApprovalRequestLines.Item(0).Remarks

  ' Get draft document
  Dim oDraft As Documents = oCompany.GetBusinessObject(BoObjectTypes.oDrafts)

  If oApprovalRequest.ObjectType = 112 Then
      oDraft.GetByKey(oApprovalRequest.ObjectEntry)

      'Get actual document type.
      txtRealDocType.Text = oDraft.DocObjectCode
          End If
  ```
- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
  ```vb
  Dim oApprovalRequestsService As ApprovalRequestsService = oCompany.GetCompanyService().GetBusinessService(ServiceTypes.ApprovalRequestsService)
  Dim oApprovalRequestsParams As ApprovalRequestsParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestsParams)
  Dim oApprovalRequest As ApprovalRequest = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequest)
  Dim oApprovalRequestParams As ApprovalRequestParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestParams)

  'Get request list
  oApprovalRequestsParams = oApprovalRequestsService.GetAllApprovalRequestsList()
  oApprovalRequestParams = oApprovalRequestsParams.Item(oApprovalRequestsParams.Count - 1)

  'Approve request
  oApprovalRequest = oApprovalRequestsService.GetApprovalRequest(oApprovalRequestParams)
  oApprovalRequest.ApprovalRequestDecisions.Add()
  oApprovalRequest.ApprovalRequestDecisions.Item(0).Remarks = "Approved"
  oApprovalRequest.ApprovalRequestDecisions.Item(0).Status = BoApprovalRequestStatusEnum.arsApproved

  ' Incase we want to approve with another user, uncomment the following 2 lines
  'oApprovalRequest.ApprovalRequestDecisions.Item(0).ApproverUserName = B1User
  'oApprovalRequest.ApprovalRequestDecisions.Item(0).ApproverPassword = B1Password

  Try
      oApprovalRequestsService.UpdateRequest(oApprovalRequest)
  Catch ex As Exception
      MessageBox.Show(ex.Message)
  End Try
  ```

## Methods (10)
- `Public Sub CancelApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams)` CancelApprovalRequest
  - param `pIApprovalRequestParams`: 
- `Public Function GetAllApprovalRequestsList() As ApprovalRequestsParams` Returns all approval requests in your company.
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    'Get full list of approval request
    Dim oApprovalRequestsService As ApprovalRequestsService = oCompany.GetCompanyService().GetBusinessService(ServiceTypes.ApprovalRequestsService)
    Dim oApprovalRequest As ApprovalRequest = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequest)
    Dim oApprovalRequestsParams As ApprovalRequestsParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestsParams)
    Dim oApprovalRequestParams As ApprovalRequestParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestParams)

    'Get full list
    oApprovalRequestsParams = oApprovalRequestsService.GetAllApprovalRequestsList()

    Dim i As Integer
    Dim approvalcode As Integer
    Dim sRemarks, sXML, sStatus As String
    Dim sReqStatus As SAPbobsCOM.BoApprovalRequestStatusEnum

    For i = 0 To oApprovalRequestsParams.Count - 1

        ' Get request information in order to find the request you want to approve
        approvalcode = oApprovalRequestsParams.Item(i).Code
        sRemarks = oApprovalRequestsParams.Item(i).Remarks
        sReqStatus = oApprovalRequestsParams.Item(i).Status

        sStatus = ""
        Select Case sReqStatus
            Case BoApprovalRequestStatusEnum.arsApproved
                sStatus = "Approved"
            Case BoApprovalRequestStatusEnum.arsCancelled
                sStatus = "Cancelled"
            Case BoApprovalRequestStatusEnum.arsGenerated
                sStatus = "Approved"
            Case BoApprovalRequestStatusEnum.arsGeneratedByAuthorizer
                sStatus = "GeneratedByAuthorizer"
            Case BoApprovalRequestStatusEnum.arsNotApproved
                sStatus = "NotApproved"
            Case BoApprovalRequestStatusEnum.arsPending
                sStatus = "Pending"
        End Select
        sXML = oApprovalRequestsParams.Item(i).ToXMLString

    Next
    ```
- `Public Function GetApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams) As ApprovalRequest` Retrieves an ApprovalRequest. The approval request is specified by its key (WddCode), which is contained in the ApprovalRequestParams object passed to the method.
  - param `pIApprovalRequestParams`: The ApprovalRequestParams of the ApprovalRequest you want to get.
- `Public Function GetApprovalRequestList() As ApprovalRequestsParams` Returns approval requests of the logged-on user as authorizer.
  - C# example (from SAP's help):
    ```csharp
    ApprovalRequestsService approvalSrv = MainModule.oCmpSrv.GetBusinessService(ServiceTypes.ApprovalRequestsService) As ApprovalRequestsService;
    ApprovalRequestsParams oList = approvalSrv.GetApprovalRequestList();
    String result = "";
    foreach (ApprovalRequestParams oParams In oList)
    {
      result += oParams.Code + " " + oParams.Remarks + " " + oParams.Status + "\n";
    }
    Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ApprovalRequestsServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default settings/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ApprovalRequestsServiceDataInterfaces.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: Specifies the XML String.
- `Public Function GetOpenApprovalRequestList() As ApprovalRequestsParams` Returns the open approval requests of the logged-on user as authorizer.
  - returns: Returns the ApprovalRequestsParams object, a DataCollection of ApprovalRequestParams data structures.
  - C# example (from SAP's help):
    ```csharp
    ApprovalRequestsService approvalSrv = MainModule.oCmpSrv.GetBusinessService(ServiceTypes.ApprovalRequestsService) As ApprovalRequestsService;
    ApprovalRequestsParams oList = approvalSrv.GetOpenApprovalRequestList();
    String result = "";

    foreach (ApprovalRequestParams oParams In oList)
    {
      result += oParams.Code + " " + oParams.Remarks + "\n";
    }
    Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    ```
- `Public Sub RestoreApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams)` RestoreApprovalRequest
  - param `pIApprovalRequestParams`: 
- `Public Sub UpdateRequest(ByVal pIApprovalRequest As ApprovalRequest)` Reply this ApprovalRequest with the approval decision.
  - param `pIApprovalRequest`: The target ApprovalRequest Object.
  - C# example (from SAP's help):
    ```csharp
    ApprovalRequestsService approvalSrv = MainModule.oCmpSrv.GetBusinessService(ServiceTypes.ApprovalRequestsService) As ApprovalRequestsService;
    ApprovalRequestParams oParams = approvalSrv.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestParams) As ApprovalRequestParams;
    oParams.Code = 1;
    ApprovalRequest oData = approvalSrv.GetApprovalRequest(oParams);

    //Add an approval decision
      oData.ApprovalRequestDecisions.Add();
      oData.ApprovalRequestDecisions.Item(0).ApproverUserName = "manager";
      oData.ApprovalRequestDecisions.Item(0).ApproverPassword = "manager";
      oData.ApprovalRequestDecisions.Item(0).Status = BoApprovalRequestDecisionEnum.ardApproved;
      oData.ApprovalRequestDecisions.Item(0).Remarks = "ok";

    //Update the approval request
      approvalSrv.UpdateRequest(oData);
    ```
