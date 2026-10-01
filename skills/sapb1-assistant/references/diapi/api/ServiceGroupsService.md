<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceGroupsService (Object)

The ServiceGroupsService service enables you to add, look up, update, and remove service groups. Source table: OSGP.

**Remarks:** Country-specific for Brazil only. To see the service groups, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Tax --> Item Classification --> Service Group.

## Methods (8)
- `Public Function AddServiceGroup(ByVal pIServiceGroup As ServiceGroup) As ServiceGroupParams` Adds a service group.
  - param `pIServiceGroup`: The data for the new service group.
- `Public Sub DeleteServiceGroup(ByVal pIServiceGroupParams As ServiceGroupParams)` Deletes an existing service group.
  - param `pIServiceGroupParams`: The key of the service group to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As ServiceGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ServiceGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ServiceGroupsServiceDataInterfaces.md`
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
- `Public Function GetServiceGroup(ByVal pIServiceGroupParams As ServiceGroupParams) As ServiceGroup` Retrieves a service group. The service group is specified by its key, which is contained in the ServiceGroupParams object passed to the method.
  - param `pIServiceGroupParams`: The key of the service group to retrieve.
- `Public Function GetServiceGroupList() As ServiceGroupsParams` Returns the ServiceGroupsParams data collection that identify all service groups.
- `Public Sub UpdateServiceGroup(ByVal pIServiceGroup As ServiceGroup)` Updates an existing service group. The data for the service group, including the key of the service group to be updated, is contained in the ServiceGroup object passed to the method. To update a service group, you must first retrieve it using the GetServiceGroup method.
  - param `pIServiceGroup`: The data for the service group to be updated. The ServiceGroup object must contain the key of the object to be updated.
