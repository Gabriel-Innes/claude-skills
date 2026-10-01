<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCallProblemTypesService (Object)

The ServiceCallProblemTypesService service enables you to add, look up and remove service call problem types in the service call problem type master data table. Service call problem types are used to classify service calls. To see the list of service call problem types, select Service --> Service Call, and then select the General tab. The service call problem types are listed in the Problem Type field. Source table: OSCP

## Methods (8)
- `Public Function AddServiceCallProblemType(ByVal pIServiceCallProblemType As ServiceCallProblemType) As ServiceCallProblemTypeParams` Adds a service call problem type.
  - param `pIServiceCallProblemType`: The data for the new service call problem type.
  - returns: Contains the key (prblmTypID) of the new service call problem type.
  - C# example (from SAP's help):
    ```csharp
    public void Add()
    {
        ServiceCallProblemType callProblemType;

        callProblemType = callProblemTypesService.GetDataInterface(ServiceCallProblemTypesServiceDataInterfaces.scptsServiceCallProblemType) As ServiceCallProblemType;

        callProblemType.Name = "problem type";
        callProblemType.Description = "problem description";

        try
        {
            callProblemTypesService.AddServiceCallProblemType(callProblemType);
        }
        catch (Exception ex)
        {
            Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    ```
- `Public Sub DeleteServiceCallProblemType(ByVal pIServiceCallProblemTypeParams As ServiceCallProblemTypeParams)` Deletes an existing service call problem type. The service call problem type is specified by its key (prblmTypID), which is contained in the ServiceCallProblemTypeParams object passed to the method.
  - param `pIServiceCallProblemTypeParams`: The key of the service call problem type to be deleted.
  - remarks: If the problem type is linked to a specific service call, it cannot be deleted.
  - C# example (from SAP's help):
    ```csharp
    public void Delete()
    {
        ServiceCallProblemTypeParams callProblemTypeParams = callProblemTypesService.GetDataInterface(ServiceCallProblemTypesServiceDataInterfaces.scptsServiceCallProblemTypeParams) as ServiceCallProblemTypeParams;
        callProblemTypeParams.ProblemTypeID = 3;

        try
        {
            callProblemTypesService.DeleteServiceCallProblemType(callProblemTypeParams);
        }
        catch (Exception e)
        {
            PrintExceptionMessage(e);
        }
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceCallProblemTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceCallProblemTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ServiceCallProblemTypesServiceDataInterfaces.md`
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
- `Public Function GetServiceCallProblemType(ByVal pIServiceCallProblemTypeParams As ServiceCallProblemTypeParams) As ServiceCallProblemType` Retrieves a service call problem type. The service call problem type is specified by its key (prblmTypID), which is contained in the ServiceCallProblemTypeParams object passed to the method.
  - param `pIServiceCallProblemTypeParams`: The key of the service call problem type to retrieve.
  - returns: The service call problem type with the specified key.
- `Public Function GetServiceCallProblemTypeList() As ServiceCallProblemTypeParamsCollection` Retrieves the keys and names of all the service call problem types.
  - C# example (from SAP's help):
    ```csharp
    public void GetList()
    {
        ServiceCallProblemTypeParamsCollection callProblemTypeParamsCollection = callProblemTypesService.GetServiceCallProblemTypeList();

        int i = 1;
        foreach (ServiceCallProblemTypeParams callProblemTypeParams in callProblemTypeParamsCollection)
        {
            Console.WriteLine("item {0}: SequenceNo:{1}, Name:{2}", i++, callProblemTypeParams.ProblemTypeID, callProblemTypeParams.Name);
        }
    }
    ```
- `Public Sub UpdateServiceCallProblemType(ByVal pIServiceCallProblemType As ServiceCallProblemType)` Updates an existing service call problem type. The data for the service call problem type, including the key of the problem type to be updated, is contained in the ServiceCallProblemType passed to the method. To update a service call problem type, you must first retrieve it using the GetServiceCallProblemType method.
  - param `pIServiceCallProblemType`: The data for the service call problem type to be updated. The ServiceCallProblemType object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    public void Update()
    {
        ServiceCallProblemTypeParams callProblemTypeParams;
        callProblemTypeParams = callProblemTypesService.GetDataInterface(ServiceCallProblemTypesServiceDataInterfaces.scptsServiceCallProblemTypeParams) as ServiceCallProblemTypeParams;
        callProblemTypeParams.ProblemTypeID = 3;
        ServiceCallProblemType callProblemType = callProblemTypesService.GetServiceCallProblemType(callProblemTypeParams);
        callProblemType.Name = "new Name";
        callProblemType.Description = "new description";

        try
        {
            callProblemTypesService.UpdateServiceCallProblemType(callProblemType);
        }
        catch (Exception e)
        {
            PrintExceptionMessage(e);
        }
    }
    ```
