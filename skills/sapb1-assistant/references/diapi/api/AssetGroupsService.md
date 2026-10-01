<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AssetGroupsService (Object)

The AssetGroupsService service enables you to add, look up, update, and remove asset groups. Source table: OAGS.

**Remarks:** To open the Asset Groups - Setup window, in the Asset Master Data window - Fixed Assets tab - Overview Subtab - Asset Group field, select Define New from the dropdown list.

## Methods (8)
- `Public Function Add(ByVal pIAssetGroup As AssetGroup) As AssetGroupParams` Adds an asset group.
  - param `pIAssetGroup`: The data for the new asset group.
- `Public Sub Delete(ByVal pIAssetGroupParams As AssetGroupParams)` Deletes an existing asset group.
  - param `pIAssetGroupParams`: The key of the asset group to be deleted.
- `Public Function Get(ByVal pIAssetGroupParams As AssetGroupParams) As AssetGroup` Retrieves an asset group. The asset group is specified by its key, which is contained in the AssetGroupParams object passed to the method.
  - param `pIAssetGroupParams`: The key of the asset group to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As AssetGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the AssetGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AssetGroupsServiceDataInterfaces.md`
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
- `Public Function GetList() As AssetGroupParamsCollection` Returns the AssetGroupParamsCollection data collection that identifies all asset groups.
- `Public Sub Update(ByVal pIAssetGroup As AssetGroup)` Updates an existing asset group. The data for the asset group, including the key of the asset group to be updated, is contained in the AssetGroup object passed to the method. To update an asset group, you must first retrieve it using the Get method.
  - param `pIAssetGroup`: The data for the asset group to be updated. The AssetGroup object must contain the key of the object to be updated.
