<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WorkflowTaskService (Object)

WorkflowTaskService is a business object that manages the tasks of the SAP Business One Workflow component. This object enables you to do the following: - Get workflow tasks owned by the current user and filter tasks by status. - Complete a workflow approval task of a given task ID and other parameters. Source table: OWLS.

**Remarks:** This service supports only the operations of approval tasks in this stage. To use the task service, proceed as follows: - Connect to a valid company. - Call CompanyService, which is the main DI service that you must call before using any other service. - Call the GetBusinessService method for the required service.

## Methods (5)
- `Public Sub Complete(ByVal pIWorkflowTaskCompleteParams As WorkflowTaskCompleteParams)` Completes a given approval task specified by WorkflowTaskCompleteParams (TaskID), adds notes, and triggers parameters for the task given in WorkflowTaskCompleteParams (Note, TriggerParams). This function, which is asynchronous, sends a signal to the workflow engine to complete the task specified by the "TaskID". You can check the task status to ensure that the task has been completed successfully. Note: This function is available only for the approval tasks that possess all the follwing features: - Type "U". - Operation "P". - Status "W" or "G".
  - param `pIWorkflowTaskCompleteParams`: The key of the approval task to be completed.
  - C# example (from SAP's help):
    ```csharp
    // using packages
    using SAPbobsCOM;
    using System.Runtime.InteropServices;

    // get Workflow Task Service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    SAPbobsCOM.WorkflowTaskService taskService = null;
    taskService = (SAPbobsCOM.WorkflowTaskService)oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.WorkflowTaskService);

    // get approval task
    SAPbobsCOM.WorkflowApprovalTaskListParams taskParam;
    taskParam = (SAPbobsCOM.WorkflowApprovalTaskListParams)taskService.GetDataInterface(WorkflowTaskServiceDataInterfaces.wtsWorkflowApprovalTaskListParams);
    taskParam.Status = "W|G";

    try
    {
                    SAPbobsCOM.WorkflowTaskCollection tasks = taskService.GetApprovalTaskList(taskParam);
    }
    catch (COMException ex)
    {
                    int code = ex.ErrorCode;
                    string msg = ex.Message;
                    //error handling
    }

    if(tasks.count>0)
    {
                    completeParam.TaskID = tasks.Item(0).TaskID;
                    completeParam.Note = "Default Comment";
                    completeParam.TriggerParams = "<Params><Param><Key>Result</Key><Value Type=\"string\">1</Value></Param></Params>";
                    try
                    {
                                    taskService.Complete(completeParam);
                    }
                    catch (COMException ex)
                    {
                                    int code = ex.ErrorCode;
                                    string msg = ex.Message;
                                    //error handling
                    }
    }
    ```
- `Public Function GetApprovalTaskList(ByVal pIWorkflowApprovalTaskListParams As WorkflowApprovalTaskListParams) As WorkflowTaskCollection` Returns the WorkflowTaskCollection object. Note: A task will be listed only for its owner or candidate.
  - param `pIWorkflowApprovalTaskListParams`: The key of the workflow task collection to retrieve.
  - C# example (from SAP's help):
    ```csharp
    // using packages
    using SAPbobsCOM;
    using System.Runtime.InteropServices;

    // get Workflow Task Service
    CompanyService oCompanyService = oCompany.GetCompanyService();
    SAPbobsCOM.WorkflowTaskService taskService = null;
    taskService = (SAPbobsCOM.WorkflowTaskService)oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.WorkflowTaskService);

    // get approval tasks
    SAPbobsCOM.WorkflowApprovalTaskListParams taskParam = null;
    taskParam = (SAPbobsCOM.WorkflowApprovalTaskListParams)taskService.GetDataInterface(WorkflowTaskServiceDataInterfaces.wtsWorkflowApprovalTaskListParams);
    taskParam.Status = "W|G";

    try
    {
        SAPbobsCOM.WorkflowTaskCollection tasks = taskService.GetApprovalTaskList(taskParam);
        foreach (SAPbobsCOM.WorkflowTask task in tasks)
        {
            int TaskID = task.TaskID;
            foreach (SAPbobsCOM.WorkflowTaskInputObject inputObj in task.WorkflowTaskInputObjectCollection)
            {
                int id = inputObj.TaskID;
                string objType = inputObj.Type;
                string objKey = inputObj.Key;
            }
        }
    }
    catch (COMException ex)
    {
        int code = ex.ErrorCode;
        string msg = ex.Message;
        //error handling
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As WorkflowTaskServiceDataInterfaces) As Object` Creates an empty data structure for use with the GeneralService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/WorkflowTaskServiceDataInterfaces.md`
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
