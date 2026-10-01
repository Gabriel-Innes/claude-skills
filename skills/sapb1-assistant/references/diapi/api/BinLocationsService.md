<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BinLocationsService (Object)

The BinLocationsService service enables you to add, look up, update, and remove bin locations. Source table: OBIN.

**Remarks:** To access the Bin Location Master Data window, from the SAP Business One Main Menu, choose Inventory --> Bin Locations --> Bin Location Master Data.

## Methods (8)
- `Public Function Add(ByVal pIBinLocation As BinLocation) As BinLocationParams` Adds a bin location.
  - param `pIBinLocation`: The data for the new bin location.
- `Public Sub Delete(ByVal pIBinLocationParams As BinLocationParams)` Deletes an existing bin location.
  - param `pIBinLocationParams`: The key of the bin location to be deleted.
- `Public Function Get(ByVal pIBinLocationParams As BinLocationParams) As BinLocation` Retrieves a bin location. The bin location is specified by its key, which is contained in the BinLocationParams object passed to the method.
  - param `pIBinLocationParams`: The key of the bin location to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BinLocationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the BinLocationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BinLocationsServiceDataInterfaces.md`
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
- `Public Function GetList() As BinLocationCollectionParams` Returns the BinLocationCollectionParams data collection that identifies all bin locations.
- `Public Sub Update(ByVal pIBinLocation As BinLocation)` Updates an existing bin location.
  - param `pIBinLocation`: The data for the bin location to be updated. The BinLocation object must contain the key of the object to be updated.
