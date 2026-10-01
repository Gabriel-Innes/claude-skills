<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ElectronicFileFormatsService (Object)

The ElectronicFileFormatsService service enables you to import, look up, and delete the generic electronic file formats in SAP Business One. Source table: OLLF.

**Remarks:** To display the Electronic File Manager - Setup window, from SAP Business One, choose Administration --> Setup --> General --> Electronic File Manager - Setup.

## Methods (7)
- `Public Function AddElectronicFileFormat(ByVal pIImportFileParam As ImportFileParam) As ElectronicFileFormatParams` Adds a new electronic file format.
  - param `pIImportFileParam`: The data for the new electronic file format.
- `Public Sub DeleteElectronicFileFormat(ByVal pIElectronicFileFormatParams As ElectronicFileFormatParams)` Deletes an existing electronic file format.
  - param `pIElectronicFileFormatParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As ElectronicFileFormatsServiceDataInterfaces) As Object` Creates an empty data structure for use with the ElectronicFileFormatsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ElectronicFileFormatsServiceDataInterfaces.md`
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
- `Public Function GetElectronicFileFormat(ByVal pIElectronicFileFormatParams As ElectronicFileFormatParams) As ElectronicFileFormat` Retrieves an electronic file format. The electronic file format is specified by its key, which is contained in the ElectronicFileFormatParams object passed to the method.
  - param `pIElectronicFileFormatParams`: The key of the electronic file format to retrieve.
- `Public Function GetElectronicFileFormatList() As ElectronicFileFormatsParams` Returns the ElectronicFileFormatsParams data collection that identify all electronic file formats.
