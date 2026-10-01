<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BinLocationAttributesService (Object)

The BinLocationAttributesService service enables you to add, look up, update, and remove bin location attributes codes. Source table: OBAT.

**Remarks:** To access the Bin Location Attribute Codes - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Bin Locations --> Bin Location Attribute Codes.

## Methods (8)
- `Public Function Add(ByVal pIBinLocationAttribute As BinLocationAttribute) As BinLocationAttributeParams` Adds a bin location attribute code.
  - param `pIBinLocationAttribute`: The data for the new bin location attribute code.
- `Public Sub Delete(ByVal pIBinLocationAttributeParams As BinLocationAttributeParams)` Deletes an existing bin location attribute code.
  - param `pIBinLocationAttributeParams`: The key of the bin location attribute code to be deleted.
- `Public Function Get(ByVal pIBinLocationAttributeParams As BinLocationAttributeParams) As BinLocationAttribute` Retrieves a bin location attribute code. The bin location attribute code is specified by its key, which is contained in the BinLocationAttributeParams object passed to the method.
  - param `pIBinLocationAttributeParams`: The key of the bin location attribute code to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BinLocationAttributesServiceDataInterfaces) As Object` Creates an empty data structure for use with the BinLocationAttributesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BinLocationAttributesServiceDataInterfaces.md`
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
- `Public Function GetList() As BinLocationAttributeCollectionParams` Returns the BinLocationAttributeCollectionParams data collection that identifies all bin location attribute codes.
- `Public Sub Update(ByVal pIBinLocationAttribute As BinLocationAttribute)` Updates an existing bin location attribute code.
  - param `pIBinLocationAttribute`: The data for the bin location attribute code to be updated. The BinLocationAttribute object must contain the key of the object to be updated.
