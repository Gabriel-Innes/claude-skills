<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BinLocationFieldsService (Object)

The BinLocationFieldsService service enables you to look up and update bin location fields. Source table: OBFC.

**Remarks:** To open the Bin Location Field Activation window, from the SAP Business One Main Menu, choose Administration -> Setup -> Inventory -> Bin Locations -> Bin Location Field Activation.

## Methods (6)
- `Public Function Get(ByVal pIBinLocationFieldParams As BinLocationFieldParams) As BinLocationField` Retrieves a bin location field. The bin location field is specified by its key, which is contained in the BinLocationFieldParams object passed to the method.
  - param `pIBinLocationFieldParams`: The key of the bin location field to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As BinLocationFieldsServiceDataInterfaces) As Object` Creates an empty data structure for use with the BinLocationFieldsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/BinLocationFieldsServiceDataInterfaces.md`
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
- `Public Function GetList() As BinLocationFieldCollectionParams` Returns the BinLocationFieldCollectionParams data collection that identifies all bin location fields.
- `Public Sub Update(ByVal pIBinLocationField As BinLocationField)` Updates an existing bin location field.
  - param `pIBinLocationField`: The data for the bin location field to be updated. The BinLocationField object must contain the key of the object to be updated.
