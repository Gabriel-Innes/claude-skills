<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MaterialGroupsService (Object)

The MaterialGroupsService service enables you to add, look up, update, and remove material groups. Source table: OMGP.

**Remarks:** Country-specific for Brazil only. To see the material groups, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Tax --> Item Classification --> Material Group.

## Methods (8)
- `Public Function AddMaterialGroup(ByVal pIMaterialGroup As MaterialGroup) As MaterialGroupParams` Adds a material group.
  - param `pIMaterialGroup`: The data for the new material group.
- `Public Sub DeleteMaterialGroup(ByVal pIMaterialGroupParams As MaterialGroupParams)` Deletes an existing material group.
  - param `pIMaterialGroupParams`: The key of the material group to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As MaterialGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the MaterialGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/MaterialGroupsServiceDataInterfaces.md`
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
- `Public Function GetMaterialGroup(ByVal pIMaterialGroupParams As MaterialGroupParams) As MaterialGroup` Retrieves a material group. The material group is specified by its key, which is contained in the MaterialGroupParams object passed to the method.
  - param `pIMaterialGroupParams`: The key of the material group to retrieve.
- `Public Function GetMaterialGroupList() As MaterialGroupsParams` Returns the MaterialGroupsParams data collection that identify all material groups.
- `Public Sub UpdateMaterialGroup(ByVal pIMaterialGroup As MaterialGroup)` Updates an existing material group. The data for the material group, including the key of the material group to be updated, is contained in the MaterialGroup object passed to the method. To update a material group, you must first retrieve it using the GetMaterialGroup method.
  - param `pIMaterialGroup`: The data for the material group to be updated. The MaterialGroup object must contain the key of the object to be updated.
