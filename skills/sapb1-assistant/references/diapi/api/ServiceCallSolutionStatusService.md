<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallSolutionStatusService (Object)

The ServiceCallSolutionStatusService service enables you to add, look up and remove service call solution statuses in the service call solution status master data table. Service call solution statuses are used to specify the status of a solution for a service call. To see the list of service call solution statuses, select Service --> Service Call, and then select the Solutions tab. Create a new solution or edit an existing solution. The service call solution statuses are listed in the Status field. Source table: OSST

## Methods (8)
- `Public Function AddServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatus As ServiceCallSolutionStatus) As ServiceCallSolutionStatusParams` Adds a service call solution status.
  - param `pIServiceCallSolutionStatus`: The data for the new service call solution status.
  - returns: Contains the key (Number) of the new service call solution status.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallSolutionStatus solutionStatus = solutionStatusService.GetDataInterface(ServiceCallSolutionStatusServiceDataInterfaces.scsssServiceCallSolutionStatus) as ServiceCallSolutionStatus;

    solutionStatus.Name = "a solution status";
    solutionStatus.Description = "description";

    Console.WriteLine("Add a new service call solution status: Name: " + solutionStatus.Name + "  Description: " + solutionStatus.Description);

    solutionStatusService.AddServiceCallSolutionStatus(solutionStatus);
    ```
- `Public Sub DeleteServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatusParams As ServiceCallSolutionStatusParams)` Deletes an existing service call solution status. The service call solution status is specified by its key (Number), which is contained in the ServiceCallSolutionStatusParams object passed to the method.
  - param `pIServiceCallSolutionStatusParams`: The key of the service call solution status to be deleted.
  - remarks: If the solution status is linked to a specific service call, it cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallSolutionStatusParams solutionStatusParams = solutionStatusService.GetDataInterface(ServiceCallSolutionStatusServiceDataInterfaces.scsssServiceCallSolutionStatusParams) as ServiceCallSolutionStatusParams;
    solutionStatusParams.StatusId = 8;

    Console.WriteLine("Delete a ServiceCall Solution Status with id=" + solutionStatusParams.StatusId);

    solutionStatusService.DeleteServiceCallSolutionStatus(solutionStatusParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallSolutionStatusServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallSolutionStatusService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ServiceCallSolutionStatusServiceDataInterfaces.md`
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
- `Public Function GetServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatusParams As ServiceCallSolutionStatusParams) As ServiceCallSolutionStatus` Retrieves a service call solution status. The service call solution status is specified by its key (Number), which is contained in the ServiceCallSolutionStatusParams object passed to the method.
  - param `pIServiceCallSolutionStatusParams`: The key of the service call solution status to retrieve.
  - returns: The service call solution status with the specified key.
- `Public Function GetServiceCallSolutionStatusList() As ServiceCallSolutionStatusParamsCollection` Retrieves the keys and names of all the service call solution statuses.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallSolutionStatusParamsCollection solutionParamsCollection
        = solutionStatusService.GetServiceCallSolutionStatusList();
    int i = 1;
    foreach (ServiceCallSolutionStatusParams solutionStatusParams in solutionParamsCollection)
    {
        Console.WriteLine("item {0}: statusId:{1}, Name:{2}", i++, solutionStatusParams.StatusId, solutionStatusParams.Name);
    }
    ```
- `Public Sub UpdateServiceCallSolutionStatus(ByVal pIServiceCallSolutionStatus As ServiceCallSolutionStatus)` Updates an existing service call solution status. The data for the service call solution status, including the key of the solution status to be updated, is contained in the ServiceCallSolutionStatus passed to the method. To update a service call solution status, you must first retrieve it using the GetServiceCallSolutionStatus method.
  - param `pIServiceCallSolutionStatus`: The data for the service call solution status to be updated. The ServiceCallSolutionStatus object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallSolutionStatusParams solutionStatusParams = solutionStatusService.GetDataInterface(ServiceCallSolutionStatusServiceDataInterfaces
        .scsssServiceCallSolutionStatusParams) as ServiceCallSolutionStatusParams;

    solutionStatusParams.StatusId = 8;
    ServiceCallSolutionStatus solutionStatus = solutionStatusService.GetServiceCallSolutionStatus(solutionStatusParams);
    solutionStatus.Name = "new Name";

    Console.WriteLine("Update a ServiceCall Solution Status with id=" + solutionStatusParams.StatusId);

    solutionStatusService.UpdateServiceCallSolutionStatus(solutionStatus);
    ```
