<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# NCMCodesSetupService (Object)

The NCMCodesSetupService service enables you to add, look up and remove NCM codes in the NCM codes master data table. NCM codes can be assigned to items via the NCMCode field of the Items object. To see the list of NCM codes, select Inventory --> Item Master Data, and select an item. In the NCM Code field, select Define New. Source table: ONCM

**Remarks:** Relevant for Brazil only.

## Methods (8)
- `Public Function AddNCMCodeSetup(ByVal pINCMCodeSetup As NCMCodeSetup) As NCMCodeSetupParams` Adds an NCM code.
  - param `pINCMCodeSetup`: The data for the new NCM code.
  - returns: Contains the key (AbsEntry) of the new NCM code.
  - C# example (from SAP's help):
    ```csharp
    NCMCodesSetupService oNCMSrv;
    oNCMSrv = (NCMCodesSetupService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.NCMCodesSetupService));

    SAPbobsCOM.NCMCodeSetup addLine;
    addLine = (SAPbobsCOM.NCMCodeSetup)oNCMSrv.GetDataInterface(NCMCodesSetupServiceDataInterfaces.ncmcssNCMCodeSetup);
    addLine.NCMCode = "C1";
    addLine.Description = "Desc C1";

    oNCMSrv.AddNCMCodeSetup(addLine);
    ```
- `Public Sub DeleteNCMCodeSetup(ByVal pINCMCodeSetupParams As NCMCodeSetupParams)` Deletes an existing NCM code. The NCM code is specified by its key (AbsEntry), which is contained in the NCMCodeSetupParams object passed to the method.
  - param `pINCMCodeSetupParams`: The key of the NCM code to be deleted.
  - remarks: You cannot delete an NCM code that is associated with a DNF code, an item, or an item group.
  - C# example (from SAP's help):
    ```csharp
    NCMCodeSetupParams delLine;

    delLine.AbsEntry = 1234;
    oNCMSrv.DeleteNCMCodeSetup(delLine);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As NCMCodesSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the NCMCodesSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/NCMCodesSetupServiceDataInterfaces.md`
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
- `Public Function GetNCMCodeSetup(ByVal pINCMCodeSetupParams As NCMCodeSetupParams) As NCMCodeSetup` Retrieves an NCM code. The NCM code is specified by its key (AbsEntry), which is contained in the NCMCodeSetupParams object passed to the method.
  - param `pINCMCodeSetupParams`: The key of the NCM code to retrieve.
  - returns: The NCM code with the specified key.
- `Public Function GetNCMCodeSetupList() As NCMCodeSetupParamsCollection` Retrieves the keys and names of all the NCM codes.
  - C# example (from SAP's help):
    ```csharp
    NCMCodeSetupParamsCollection getlistParams;
    getlistParams = oNCMSrv.GetNCMCodeSetupList();

    String resultSet = "";

    foreach (NCMCodeSetupParams record in getlistParams)
    {
        resultSet = resultSet + record.NCMCode + "\t" + record.Description + "\n";
        if (record.AbsEntry >= 10)
            break;
    }
    ```
- `Public Sub UpdateNCMCodeSetup(ByVal pINCMCodeSetup As NCMCodeSetup)` Updates an existing NCM code. The data for the NCM code, including the key of the NCM code to be updated, is contained in the NCMCodeSetup object passed to the method. To update a NCM code, you must first retrieve it using the GetNCMCodeSetup method.
  - param `pINCMCodeSetup`: The data for the competitor to be updated. The SalesOpportunityCompetitorSetup object must contain the key of the object to be updated.
  - remarks: You cannot update an NCM code that is associated with a DNF code, an item, or an item group.
  - C# example (from SAP's help):
    ```csharp
    NCMCodeSetupParams getLine;
    SAPbobsCOM.NCMCodeSetup updateLine;
    getLine = (NCMCodeSetupParams)oNCMSrv.GetDataInterface(NCMCodesSetupServiceDataInterfaces.ncmcssNCMCodeSetupParams);

    getLine.AbsEntry = 9789;

    updateLine = oNCMSrv.GetNCMCodeSetup(getLine);
    updateLine.NCMCode = "updated";
    updateLine.Description = "updated description";

    oNCMSrv.UpdateNCMCodeSetup(updateLine);
    ```
