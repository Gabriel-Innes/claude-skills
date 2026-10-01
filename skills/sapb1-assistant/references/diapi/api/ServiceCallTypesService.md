<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallTypesService (Object)

The ServiceCallTypesService service enables you to add, look up and remove service call types in the service call type master data table. Service call types are used to classify service calls. To see the list of service call types, select Service --> Service Call, and then select the General tab. The service call types are listed in the Call Type field. Source table: OSCT

## Methods (8)
- `Public Function AddServiceCallType(ByVal pIServiceCallType As ServiceCallType) As ServiceCallTypeParams` Adds a service call type.
  - param `pIServiceCallType`: The data for the new service call type.
  - returns: Contains the key (callTypeID) of the new service call type.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallType callType = callTypesService.GetDataInterface(ServiceCallTypesServiceDataInterfaces.sctsServiceCallType) as ServiceCallType;

    callType.Name = "a new call type";
    callType.Description = "description for this type";

    try
    {
         callTypesService.AddServiceCallType(callType);
    }
    catch(Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteServiceCallType(ByVal pIServiceCallTypeParams As ServiceCallTypeParams)` Deletes an existing service call type. The service call type is specified by its key (callTypeID), which is contained in the ServiceCallTypeParams object passed to the method.
  - param `pIServiceCallTypeParams`: The key of the service call type to be deleted.
  - remarks: If the type is linked to a specific service call, it cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallTypeParams callTypeParams = callTypesService.GetDataInterface(ServiceCallTypesServiceDataInterfaces.sctsServiceCallTypeParams) as ServiceCallTypeParams;
    callTypeParams.CallTypeID = 2;

    try
    {
         callTypesService.DeleteServiceCallType(callTypeParams);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ServiceCallTypesServiceDataInterfaces.md`
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
- `Public Function GetServiceCallType(ByVal pIServiceCallTypeParams As ServiceCallTypeParams) As ServiceCallType` Retrieves a service call type. The service call type is specified by its key (callTypeID), which is contained in the ServiceCallTypeParams object passed to the method.
  - param `pIServiceCallTypeParams`: The key of the service call type to retrieve.
  - returns: The service call type with the specified key.
- `Public Function GetServiceCallTypeList() As ServiceCallTypeParamsCollection` Retrieves the keys and names of all the service call types.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallTypeParamsCollection callTypeParamsCollection = callTypesService.GetServiceCallTypeList();
    int i = 1;
    foreach (ServiceCallTypeParams typeParams in callTypeParamsCollection)
    {
         Console.WriteLine("item {0}: CallTypeId:{1}, Name:{2}", i++, typeParams.CallTypeID, typeParams.Name);
    }
    ```
- `Public Sub UpdateServiceCallType(ByVal pIServiceCallType As ServiceCallType)` Updates an existing service call type. The data for the service call type, including the key of the type to be updated, is contained in the ServiceCallType passed to the method. To update a service call type, you must first retrieve it using the GetServiceCallType method.
  - param `pIServiceCallType`: The data for the service call type to be updated. The ServiceCallType object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    ServiceCallTypeParams callTypeParams = callTypesService.GetDataInterface(ServiceCallTypesServiceDataInterfaces.sctsServiceCallTypeParams) as ServiceCallTypeParams;
    callTypeParams.CallTypeID = 2;
    ServiceCallType callType = callTypesService.GetServiceCallType(callTypeParams);
    callType.Name = "new Name";

    try
    {
         callTypesService.UpdateServiceCallType(callType);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
