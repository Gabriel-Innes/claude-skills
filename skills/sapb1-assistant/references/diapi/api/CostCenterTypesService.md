<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CostCenterTypesService (Object)

A cost center type is for selection by future reports and analyses. The CostCenterTypesService service enables you to add, look up, update, and remove cost center types. Source table: OCCT.

**Remarks:** To define cost center types, from the SAP Business One Main Menu, choose Financials --> Cost Accounting --> Cost Centers, in the Cost Center Type field, select Define New to open the Cost Center Type – Setup window.

## Methods (8)
- `Public Function AddCostCenterType(ByVal pICostCenterType As CostCenterType) As CostCenterTypeParams` Adds a cost center type.
  - param `pICostCenterType`: The data for the new cost center type.
- `Public Sub DeleteCostCenterType(ByVal pICostCenterTypeParams As CostCenterTypeParams)` Deletes an existing cost center type.
  - param `pICostCenterTypeParams`: The key of the cost center type to be deleted.
- `Public Function GetCostCenterType(ByVal pICostCenterTypeParams As CostCenterTypeParams) As CostCenterType` Retrieves a cost center type. The cost center type is specified by its key, which is contained in the CostCenterTypeParams object passed to the method.
  - param `pICostCenterTypeParams`: The key of the cost center type to retrieve.
- `Public Function GetCostCenterTypeList() As CostCenterTypesParams` Returns the CostCenterTypesParams data collection that identify all cost center types.
- `Public Function GetDataInterface(ByVal enumMSDI As CostCenterTypesServiceDataInterfaces) As Object` Creates an empty data structure for use with the CostCenterTypesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/CostCenterTypesServiceDataInterfaces.md`
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
- `Public Sub UpdateCostCenterType(ByVal pICostCenterType As CostCenterType)` Updates an existing cost center type. The data for the cost center type, including the key of the cost center type to be updated, is contained in the CostCenterType object passed to the method. To update a cost center type, you must first retrieve it using the GetCostCenterType method.
  - param `pICostCenterType`: The data for the cost center type to be updated. The CostCenterType object must contain the key of the object to be updated.
