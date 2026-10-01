<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PartnersSetupsService (Object)

The PartnersSetupsService service enables you to add, look up, update, and remove partners. Source table: OPRT.

**Remarks:** To open the Partners - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Sales Opportunities --> Partners.

## Methods (8)
- `Public Function Add(ByVal pIPartnersSetup As PartnersSetup) As PartnersSetupParams` Adds a partner.
  - param `pIPartnersSetup`: The data for the new partner.
- `Public Sub Delete(ByVal pIPartnersSetupParams As PartnersSetupParams)` Deletes an existing partner.
  - param `pIPartnersSetupParams`: The key of the partner to be deleted.
- `Public Function Get(ByVal pIPartnersSetupParams As PartnersSetupParams) As PartnersSetup` Retrieves a partner. The partner is specified by its key, which is contained in the PartnersSetupParams object passed to the method.
  - param `pIPartnersSetupParams`: The key of the partner to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As PartnersSetupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the PartnersSetupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/PartnersSetupsServiceDataInterfaces.md`
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
- `Public Function GetList() As PartnersSetupsParams` Returns the PartnersSetupsParams data collection that identifies all partners.
- `Public Sub Update(ByVal pIPartnersSetup As PartnersSetup)` Updates an existing partner.
  - param `pIPartnersSetup`: The data for the partner to be updated. The PartnersSetup object must contain the key of the object to be updated.
