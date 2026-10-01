<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DNFCodeSetupService (Object)

The DNFCodeSetupService service enables you to add, look up and remove DNF codes in the DNF codes master data table. NCM codes are assigned to items, and then DNF codes can be assigned to that NCM code for that item. To see the list of DNF codes, select Inventory --> Item Master Data. Select an NCM code, and then select Define New in the DNF Code field. Source table: ODNF

**Remarks:** Relevant for Brazil only.

## Methods (8)
- `Public Function AddDNFCodeSetup(ByVal pIDNFCodeSetup As DNFCodeSetup) As DNFCodeSetupParams` Adds a DNF code.
  - param `pIDNFCodeSetup`: The data for the new DNF code.
  - returns: Contains the key (AbsEntry) of the new DNF code.
  - C# example (from SAP's help):
    ```csharp
    DNFCodeSetup dnfCode = dnfCodesService.GetDataInterface(DNFCodeSetupServiceDataInterfaces.dnfcssDNFCodeSetup) As DNFCodeSetup;

    dnfCode.DNFCode = "Code";
    dnfCode.UoM = "dnf UoM";
    dnfCode.Factor = 1.1;
    dnfCode.NCMCode = 5;
    dnfCodesService.AddDNFCodeSetup(dnfCode);
    ```
- `Public Sub DeleteDNFCodeSetup(ByVal pIDNFCodeSetupParams As DNFCodeSetupParams)` Deletes an existing DNF code. The DNF code is specified by its key (AbsEntry), which is contained in the DNFCodeSetupParams object passed to the method.
  - param `pIDNFCodeSetupParams`: The key of the DNF code to be deleted.
  - remarks: You cannot delete a DNF code that is associated with an item.
  - C# example (from SAP's help):
    ```csharp
    DNFCodeSetupParams dnfCodeParams = dnfCodesService.GetDataInterface(DNFCodeSetupServiceDataInterfaces.dnfcssDNFCodeSetupParams) As DNFCodeSetupParams;
    dnfCodeParams.AbsEntry = 5;

    Console.WriteLine("Delete a DNFCodeSetup with key=" + dnfCodeParams.AbsEntry);

    dnfCodesService.DeleteDNFCodeSetup(dnfCodeParams);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As DNFCodeSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the DNFCodeSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/DNFCodeSetupServiceDataInterfaces.md`
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
- `Public Function GetDNFCodeSetup(ByVal pIDNFCodeSetupParams As DNFCodeSetupParams) As DNFCodeSetup` Retrieves a DNF code. The DNF code is specified by its key (AbsEntry), which is contained in the DNFCodeSetupParams object passed to the method.
  - param `pIDNFCodeSetupParams`: The key of the DNF code to retrieve.
  - returns: The DNF code with the specified key.
- `Public Function GetDNFCodeSetupList() As DNFCodeSetupParamsCollection` Retrieves the keys and names of all the DNF codes.
  - C# example (from SAP's help):
    ```csharp
    DNFCodeSetupParamsCollection paramsCollection = dnfCodesService.GetDNFCodeSetupList();
    int i = 1;
    int[] keys = new int[paramsCollection.Count];
    foreach (DNFCodeSetupParams codeParams in paramsCollection)
    {
        Console.WriteLine("item {0}: InternalKey:{1}, Code:{2}", i, codeParams.AbsEntry, codeParams.DNFCode);
        keys[i - 1] = codeParams.AbsEntry;
        i++;
    }
    ```
- `Public Sub UpdateDNFCodeSetup(ByVal pIDNFCodeSetup As DNFCodeSetup)` Updates an existing DNF code. The data for the DNF code, including the key of the DNF code to be updated, is contained in the DNFCodeSetup object passed to the method. To update a DNF code, you must first retrieve it using the GetDNFCodeSetup method.
  - param `pIDNFCodeSetup`: The data for the DNF code to be updated. The DNFCodeSetup object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    DNFCodeSetupParams dnfCodeParams = dnfCodesService.GetDataInterface(DNFCodeSetupServiceDataInterfaces.dnfcssDNFCodeSetupParams) As DNFCodeSetupParams;

    dnfCodeParams.AbsEntry = 5;
    DNFCodeSetup dnfCode = dnfCodesService.GetDNFCodeSetup(dnfCodeParams);

    dnfCode.DNFCode = "1";
    dnfCodesService.UpdateDNFCodeSetup(dnfCode);
    ```
