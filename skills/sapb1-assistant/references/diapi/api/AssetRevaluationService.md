<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AssetRevaluationService (Object)

Use the AssetRevaluationService service to revaluate assets. Source table: OFAR.

**Remarks:** Financials --> Fixed Assets --> Asset Revaluation

**Example:**
- C# example (from SAP's help):
  ```csharp
  SAPbobsCOM.AssetRevaluationService revaluationSer = (SAPbobsCOM.AssetRevaluationService)cs.GetBusinessService(SAPbobsCOM.ServiceTypes.AssetRevaluationService);
  SAPbobsCOM.AssetRevaluation revaluationObj = revaluationSer.GetDataInterface(AssetRevaluationServiceDataInterfaces.arsAssetRevaluation);
  SAPbobsCOM.AssetRevaluationParams revaluationParams = revaluationSer.GetDataInterface(AssetRevaluationServiceDataInterfaces.arsAssetRevaluationParams);

  revaluationObj.PostingDate = new System.DateTime(2025, 12, 31, 0, 0, 0);
  revaluationObj.AssetValueDate = revaluationObj.PostingDate;
  revaluationObj.DocumentDate = revaluationObj.PostingDate;
  revaluationObj.DepreciationArea = ""MainArea"";

  AssetRevaluationLineCollection lines = revaluationObj.AssetRevaluationLineCollection;
  AssetRevaluationLine line = lines.Add();
  line.AssetNumber = ""FA001"";
  //line.NewNBV = 76800;
  line.RevaluationPercent = 110;

  revaluationParams = revaluationSer.Add(revaluationObj);
  ```

## Methods (8)
- `Public Function Add(ByVal pIAssetRevaluation As AssetRevaluation) As AssetRevaluationParams` Add
  - param `pIAssetRevaluation`: 
- `Public Sub Delete(ByVal pIAssetRevaluationParams As AssetRevaluationParams)` Delete
  - param `pIAssetRevaluationParams`: 
- `Public Function Get(ByVal pIAssetRevaluationParams As AssetRevaluationParams) As AssetRevaluation` Get
  - param `pIAssetRevaluationParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As AssetRevaluationServiceDataInterfaces) As Object` Creates an empty data structure for use with the AssetRevaluationService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/AssetRevaluationServiceDataInterfaces.md`
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
- `Public Function GetList() As AssetRevaluationParamsCollection` GetList
- `Public Sub Update(ByVal pIAssetRevaluation As AssetRevaluation)` Update
  - param `pIAssetRevaluation`:
