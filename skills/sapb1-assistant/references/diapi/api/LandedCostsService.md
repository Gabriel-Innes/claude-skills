<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# LandedCostsService (Object)

The LandedCostsService service enables you to add, look up, update, cancel, and close landed costs documents. Source table: OIPF.

**Remarks:** To access the window, choose Purchasing A/P --> Landed Costs.

## Methods (9)
- `Public Function AddLandedCost(ByVal pILandedCost As LandedCost) As LandedCostParams` Adds a landed costs document.
  - param `pILandedCost`: The data for the new landed costs document.
- `Public Sub CancelLandedCost(ByVal pILandedCostParams As LandedCostParams)` Cancels an existing landed costs document.
  - param `pILandedCostParams`: The key of the landed costs document to be cancelled.
- `Public Sub CloseLandedCost(ByVal pILandedCostParams As LandedCostParams)` Closes an existing landed costs document.
  - param `pILandedCostParams`: The key of the landed costs document to be closed.
- `Public Function GetDataInterface(ByVal enumMSDI As LandedCostsServiceDataInterfaces) As Object` Creates an empty data structure for use with the LandedCostsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/LandedCostsServiceDataInterfaces.md`
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
- `Public Function GetLandedCost(ByVal pILandedCostParams As LandedCostParams) As LandedCost` Retrieves a landed costs document. The landed costs document is specified by its key, which is contained in the LandedCostParams object passed to the method.
  - param `pILandedCostParams`: The key of the landed costs document to retrieve.
- `Public Function GetLandedCostList() As LandedCostsParams` Returns the LandedCostsParams data collection that identifies all landed costs documents.
- `Public Sub UpdateLandedCost(ByVal pILandedCost As LandedCost)` Updates an existing landed costs document. The data for the landed costs document, including the key of the landed costs document to be updated, is contained in the LandedCost object passed to the method. To update a landed costs document, you must first retrieve it using the GetLandedCost method.
  - param `pILandedCost`: The data for the landed costs document to be updated. The LandedCost object must contain the key of the object to be updated.
