<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallStatusService (Object)

The ServiceCallStatusService service enables you to add, look up and remove service call statuses in the service call status master data table. Service call statuses are used to specify the status of a service call. To see the list of service call statuses, select Service --> Service Call. The service call statuses are listed in the Call Status field. Source table: OSCS

## Methods (8)
- `Public Function AddServiceCallStatus(ByVal pIServiceCallStatus As ServiceCallStatus) As ServiceCallStatusParams` Adds a service call status.
  - param `pIServiceCallStatus`: The data for the new service call status.
  - returns: Contains the key (statusID) of the new service call status.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallStatus callStatus = callStatusService
        .GetDataInterface(ServiceCallStatusServiceDataInterfaces.scssServiceCallStatus) as ServiceCallStatus;

    callStatus.Name = "Thank you";
    callStatus.Description = "Thank you for using our products.";

    Console.WriteLine("Add a new callStatus: Name: " + callStatus.Name + "  Description: " + callStatus.Description);

    callStatusService.AddServiceCallStatus(callStatus);
    ```
- `Public Sub DeleteServiceCallStatus(ByVal pIServiceCallStatusParams As ServiceCallStatusParams)` Deletes an existing service call status. The service call status is specified by its key (statusID), which is contained in the ServiceCallStatusParams object passed to the method.
  - param `pIServiceCallStatusParams`: The key of the service call status to be deleted.
  - remarks: If the status is system defined or is linked to a specific service call, the status cannot be deleted. A status is system defined if the Locked field in the OSCS table is set to Y.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallStatusParams statusParams = callStatusService
        .GetDataInterface(ServiceCallStatusServiceDataInterfaces.scssServiceCallStatusParams) as ServiceCallStatusParams;
    statusParams.StatusId = 11;
    callStatusService.DeleteServiceCallStatus(statusParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallStatusServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallStatusService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ServiceCallStatusServiceDataInterfaces.md`
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
- `Public Function GetServiceCallStatus(ByVal pIServiceCallStatusParams As ServiceCallStatusParams) As ServiceCallStatus` Retrieves a service call status. The service call status is specified by its key (statusID), which is contained in the ServiceCallStatusParams object passed to the method.
  - param `pIServiceCallStatusParams`: The key of the service call status to retrieve.
  - returns: The service call status with the specified key.
- `Public Function GetServiceCallStatusList() As ServiceCallStatusParamsCollection` Retrieves the keys and names of all the service call statuses.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallStatusParamsCollection callStatusParamsCollection = callStatusService.GetServiceCallStatusList();
    int i = 1;
    foreach (ServiceCallStatusParams statusParams in callStatusParamsCollection)
    {
        Console.WriteLine("item {0}: StatusId:{1}, Name:{2}", i++, statusParams.StatusId, statusParams.Name);
    }
    ```
- `Public Sub UpdateServiceCallStatus(ByVal pIServiceCallStatus As ServiceCallStatus)` Updates an existing service call status. The data for the service call status, including the key of the status to be updated, is contained in the ServiceCallStatus passed to the method. To update a service call status, you must first retrieve it using the GetServiceCallStatus method.
  - param `pIServiceCallStatus`: The data for the service call status to be updated. The ServiceCallStatus object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallStatusParams statusParams = callStatusService
        .GetDataInterface(ServiceCallStatusServiceDataInterfaces.scssServiceCallStatusParams) as ServiceCallStatusParams;

    statusParams.StatusId = 9;
    ServiceCallStatus callStatus = callStatusService.GetServiceCallStatus(statusParams);

    callStatus.Name = "new Name";
    callStatusService.UpdateServiceCallStatus(callStatus);
    ```
