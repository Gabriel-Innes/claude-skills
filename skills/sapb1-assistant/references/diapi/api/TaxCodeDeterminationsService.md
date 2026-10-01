<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxCodeDeterminationsService (Object)

The TaxCodeDeterminationsService service enables you to add, look up, update, and remove tax code determination rules. For all localizations except Brazil, India, Israel and Puerto Rico, you can set up tax code determination rules that take precedence over the tax information in the business partner or item master data, and in G/L account determination. Source table: OTCX.

**Remarks:** To see the list of tax code determination rules, choose Administration --> Setup --> Financials --> Tax --> Tax Code Determination.

## Methods (8)
- `Public Function AddTaxCodeDetermination(ByVal pITaxCodeDetermination As TaxCodeDetermination) As TaxCodeDeterminationParams` Adds a tax code determination rule.
  - param `pITaxCodeDetermination`: The data for the new tax code determination rule.
- `Public Sub DeleteTaxCodeDetermination(ByVal pITaxCodeDeterminationParams As TaxCodeDeterminationParams)` Deletes an existing tax code determination rule.
  - param `pITaxCodeDeterminationParams`: The key of the tax code determination rule to be deleted.
- `Public Function GetDataInterface(ByVal enumMSDI As TaxCodeDeterminationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the TaxCodeDeterminationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/TaxCodeDeterminationsServiceDataInterfaces.md`
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
- `Public Function GetTaxCodeDetermination(ByVal pITaxCodeDeterminationParams As TaxCodeDeterminationParams) As TaxCodeDetermination` Retrieves a tax code determination rule. The tax code determination rule is specified by its key, which is contained in the TaxCodeDeterminationParams object passed to the method.
  - param `pITaxCodeDeterminationParams`: The key of the tax code determination rule to retrieve.
- `Public Function GetTaxCodeDeterminationList() As TaxCodeDeterminationsParams` Returns the TaxCodeDeterminationsParams data collection that identifies all tax code determination rules.
- `Public Sub UpdateTaxCodeDetermination(ByVal pITaxCodeDetermination As TaxCodeDetermination)` Updates an existing tax code determination rule. The data for the tax code determination rule, including the key of the tax code determination rule to be updated, is contained in the TaxCodeDetermination object passed to the method. To update a tax code determination rule, you must first retrieve it using the GetTaxCodeDetermination method.
  - param `pITaxCodeDetermination`: The data for the tax code determination rule to be updated. The TaxCodeDetermination object must contain the key of the object to be updated.
