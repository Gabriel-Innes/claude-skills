<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AssetClassesService (Object)

The AssetClassesService service enables you to create, update and view asset classes. Source table: OACS.

**Remarks:** To open this window, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Fixed Assets --> Asset Classes.

## Methods (8)
- `Public Function Add(ByVal pIAssetClass As AssetClass) As AssetClassParams` Adds an asset class.
  - param `pIAssetClass`: The data for the new asset class.
- `Public Sub Delete(ByVal pIAssetClassParams As AssetClassParams)` Deletes an existing asset class.
  - param `pIAssetClassParams`: The key of the asset class to be deleted.
- `Public Function Get(ByVal pIAssetClassParams As AssetClassParams) As AssetClass` Retrieves an asset class. The asset class is specified by its key, which is contained in the AssetClassParams object passed to the method.
  - param `pIAssetClassParams`: The key of the asset class to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As AssetClassesServiceDataInterfaces) As Object` Creates an empty data structure for use with the AssetClassesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AssetClassesServiceDataInterfaces.md`
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
- `Public Function GetList() As AssetClassParamsCollection` Returns the AssetClassParamsCollection data collection that identifies all asset classes.
- `Public Sub Update(ByVal pIAssetClass As AssetClass)` Updates an existing asset class. The data for the asset class, including the key of the asset class to be updated, is contained in the AssetClass object passed to the method. To update an asset class, you must first retrieve it using the Get method.
  - param `pIAssetClass`: The data for the asset class to be updated. The AssetClass object must contain the key of the object to be updated.
