<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReplStateSubService (Object)

The TaxReplStateSubService service enables you to add, look up, update, and remove tax replacement state subscription. Source table: OTRSS.

**Remarks:** Administration -> System Initialization -> Company Details -> Localization Fields tab.

## Methods (7)
- `Public Function Add(ByVal pITaxReplStateSubData As TaxReplStateSubData) As TaxReplStateSubParams` Adds tax replacement state subscription data.
  - param `pITaxReplStateSubData`: The tax replacement state subscription data.
- `Public Sub Delete(ByVal pITaxReplStateSubParams As TaxReplStateSubParams)` Deletes existing tax replacement state subscription data.
  - param `pITaxReplStateSubParams`: The key of the tax replacement state subscription data to be deleted.
- `Public Function GetByParams(ByVal pITaxReplStateSubParams As TaxReplStateSubParams) As TaxReplStateSubData` Retrieves tax replacement state subscription data. The tax replacement state subscription data is specified by its key, which is contained in the TaxReplStateSubParams object passed to the method.
  - param `pITaxReplStateSubParams`: The key of the tax replacement state subscription data to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As TaxReplStateSubServiceDataInterfaces) As Object` Creates an empty data structure for use with the TaxReplStateSubService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TaxReplStateSubServiceDataInterfaces.md`
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
- `Public Sub Update(ByVal pITaxReplStateSubData As TaxReplStateSubData)` Updates existing tax replacement state subscription data.
  - param `pITaxReplStateSubData`: The tax replacement state subscription data to be updated. The TaxReplStateSubData object must contain the key of the object to be updated.
