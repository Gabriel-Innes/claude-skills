<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallOriginsService (Object)

The ServiceCallOriginsService service enables you to add, look up and remove service call origins in the service call origin master data table. Service call origins are used to specify the channel through which a call was made, such as by telephone or via the Web. To see the list of service call origins, select Service --> Service Call, and then select the General tab. The service call origins are listed in the Origin field. Source table: OSCO

## Methods (8)
- `Public Function AddServiceCallOrigin(ByVal pIServiceCallOrigin As ServiceCallOrigin) As ServiceCallOriginParams` Adds a service call origin.
  - param `pIServiceCallOrigin`: The data for the new service call origin.
  - returns: Contains the key (originID) of the new service call origin.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallOrigin callOrigin = callOriginsService.GetDataInterface(ServiceCallOriginsServiceDataInterfaces.scosServiceCallOrigin) as ServiceCallOrigin;

    callOrigin.Name = "a new call origin";
    callOrigin.Description = "description for this origin";

    Console.WriteLine("Add a new service call origin: Name: " + callOrigin.Name + "  Description: " + callOrigin.Description);

    try
    {
        callOriginsService.AddServiceCallOrigin(callOrigin);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteServiceCallOrigin(ByVal pIServiceCallOriginParams As ServiceCallOriginParams)` Deletes an existing service call origin. The service call origin is specified by its key (originID), which is contained in the ServiceCallOriginParams object passed to the method.
  - param `pIServiceCallOriginParams`: The key of the service call origin to be deleted.
  - remarks: If the origin is system defined or is linked to a specific service call, the origin cannot be deleted. An origin is system defined if the Locked field in the OSCO table is set to Y.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallOriginParams originParams = callOriginsService.GetDataInterface(ServiceCallOriginsServiceDataInterfaces.scosServiceCallOriginParams) as ServiceCallOriginParams;
    originParams.OriginID = 3;
    Console.WriteLine("Delete a ServiceCall Origin with id=" + originParams.OriginID);
    try
    {
        callOriginsService.DeleteServiceCallOrigin(originParams);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallOriginsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallOriginsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ServiceCallOriginsServiceDataInterfaces.md`
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
- `Public Function GetServiceCallOrigin(ByVal pIServiceCallOriginParams As ServiceCallOriginParams) As ServiceCallOrigin` Retrieves a service call origin. The service call origin is specified by its key (originID), which is contained in the ServiceCallOriginParams object passed to the method.
  - param `pIServiceCallOriginParams`: The key of the service call origin to retrieve.
  - returns: The service call origin with the specified key.
- `Public Function GetServiceCallOriginList() As ServiceCallOriginParamsCollection` Retrieves the keys and names of all the service call origins.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallOriginParamsCollection originParamsCollection = callOriginsService.GetServiceCallOriginList();
    int i = 1;
    foreach (ServiceCallOriginParams originParams in originParamsCollection)
    {
        Console.WriteLine("item {0}: originID:{1}, Name:{2}", i++, originParams.OriginID, originParams.Name);
    }
    ```
- `Public Sub UpdateServiceCallOrigin(ByVal pIServiceCallOrigin As ServiceCallOrigin)` Updates an existing service call origin. The data for the service call origin, including the key of the origin to be updated, is contained in the ServiceCallOrigin passed to the method. To update a service call origin, you must first retrieve it using the GetServiceCallOrigin method.
  - param `pIServiceCallOrigin`: The data for the service call origin to be updated. The ServiceCallOrigin object must contain the key of the object to be updated.
  - remarks: You cannot update a system-defined origin. An origin is system defined if the Locked field in the OSCO table is set to Y.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallOriginParams originParams = callOriginsService
        .GetDataInterface(ServiceCallOriginsServiceDataInterfaces.scosServiceCallOriginParams) as ServiceCallOriginParams;

    originParams.OriginID = 3;
    ServiceCallOrigin callOrigin = callOriginsService.GetServiceCallOrigin(originParams);
    callOrigin.Name = "new Name";

    Console.WriteLine("Update a ServiceCall Origin with id=" + originParams.OriginID);

    try
    {
        callOriginsService.UpdateServiceCallOrigin(callOrigin);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
