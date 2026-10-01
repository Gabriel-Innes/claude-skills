<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FAAccountDeterminationsService (Object)

The FAAccountDeterminationsService service enables you to define and view different sets of G/L accounts for your fixed assets. Source table: OADT.

**Remarks:** To open the Account Determination - Setup window, from the SAP Business One Main Menu, choose Administration --> Setup --> Financials --> Fixed Assets --> Account Determination.

## Methods (8)
- `Public Function Add(ByVal pIFAAccountDetermination As FAAccountDetermination) As FAAccountDeterminationParams` Adds a fixed asset account determination rule.
  - param `pIFAAccountDetermination`: The data for the new fixed asset account determination rule.
- `Public Sub Delete(ByVal pIFAAccountDeterminationParams As FAAccountDeterminationParams)` Deletes an existing fixed asset account determination rule.
  - param `pIFAAccountDeterminationParams`: The key of the fixed asset account determination rule to be deleted.
- `Public Function Get(ByVal pIFAAccountDeterminationParams As FAAccountDeterminationParams) As FAAccountDetermination` Retrieves a fixed asset account determination rule. The fixed asset account determination rule is specified by its key, which is contained in the FAAccountDeterminationParams object passed to the method.
  - param `pIFAAccountDeterminationParams`: The key of the fixed asset account determination rule to retrieve
- `Public Function GetDataInterface(ByVal enumMSDI As FAAccountDeterminationsServiceDataInterfaces) As Object` Creates an empty data structure for use with the FAAccountDeterminationsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/FAAccountDeterminationsServiceDataInterfaces.md`
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
- `Public Function GetList() As FAAccountDeterminationParamsCollection` Returns the FAAccountDeterminationParamsCollection data collection that identifies all fixed asset account determination rules.
- `Public Sub Update(ByVal pIFAAccountDetermination As FAAccountDetermination)` Updates an existing fixed asset account determination rule. The data for the fixed asset account determination rule, including the key of the fixed asset account determination rule to be updated, is contained in the FAAccountDetermination object passed to the method. To update a fixed asset account determination rule, you must first retrieve it using the Get method.
  - param `pIFAAccountDetermination`: The data for the fixed asset account determination rule to be updated. The FAAccountDetermination object must contain the key of the object to be updated.
