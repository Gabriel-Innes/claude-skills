<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WarehouseSublevelCodesService (Object)

The WarehouseSublevelCodesService service enables you to add, look up, update, and remove warehouse sublevel codes. Source table: OBSL.

**Remarks:** To access the Warehouse Sublevel Codes - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Bin Locations --> Warehouse Sublevel Codes.

## Methods (8)
- `Public Function Add(ByVal pIWarehouseSublevelCode As WarehouseSublevelCode) As WarehouseSublevelCodeParams` Adds a warehouse sublevel code.
  - param `pIWarehouseSublevelCode`: The data for the new warehouse sublevel code.
- `Public Sub Delete(ByVal pIWarehouseSublevelCodeParams As WarehouseSublevelCodeParams)` Deletes an existing warehouse sublevel code.
  - param `pIWarehouseSublevelCodeParams`: The key of the warehouse sublevel code to be deleted.
- `Public Function Get(ByVal pIWarehouseSublevelCodeParams As WarehouseSublevelCodeParams) As WarehouseSublevelCode` The warehouse sublevel code is specified by its key, which is contained in the WarehouseSublevelCodeParams object passed to the method.
  - param `pIWarehouseSublevelCodeParams`: The key of the warehouse sublevel code to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As WarehouseSublevelCodesServiceDataInterfaces) As Object` Creates an empty data structure for use with the WarehouseSublevelCodesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/WarehouseSublevelCodesServiceDataInterfaces.md`
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
- `Public Function GetList() As WarehouseSublevelCodeCollectionParams` Returns the WarehouseSublevelCodeCollectionParams data collection that identifies all warehouse sublevel codes.
- `Public Sub Update(ByVal pIWarehouseSublevelCode As WarehouseSublevelCode)` Updates an existing warehouse sublevel code.
  - param `pIWarehouseSublevelCode`: The data for the warehouse sublevel code to be updated. The WarehouseSublevelCode object must contain the key of the object to be updated.
