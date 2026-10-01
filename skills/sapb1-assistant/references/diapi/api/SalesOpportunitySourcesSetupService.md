<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesOpportunitySourcesSetupService (Object)

The SalesOpportunitySourcesSetupService service enables you to add, look up and remove sources in the sources master data table. Sources can be assigned to sales opportunities; the source explains how a sales opportunity was generated. To see the list of sources, select Sales Opportunities --> Sales Opportunity, and then select the General tab. In the Information Source field, select Define New. Source table: OOSR

## Methods (8)
- `Public Function AddSalesOpportunitySourceSetup(ByVal pISalesOpportunitySourceSetup As SalesOpportunitySourceSetup) As SalesOpportunitySourceSetupParams` Adds a source.
  - param `pISalesOpportunitySourceSetup`: The data for the new source.
  - returns: Contains the key (Num) of the new source.
  - C# example (from SAP's help):
    ```csharp
    SalesOpportunitySourceSetup source = sourceService.GetDataInterface(
        SalesOpportunitySourcesSetupServiceDataInterfaces.sosssSalesOpportunitySourceSetup) as SalesOpportunitySourceSetup;

    source.Description = "book";
    source.Sort = 1000;
    Console.WriteLine("Add a new information source: Description: " + source.Description + "  Sort:" + source.Sort.ToString());

    try
    {
        sourceService.AddSalesOpportunitySourceSetup(source);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteSalesOpportunitySourceSetup(ByVal pISalesOpportunitySourceSetupParams As SalesOpportunitySourceSetupParams)` Deletes an existing source. The source is specified by its key (Num), which is contained in the SalesOpportunitySourceSetupParams object passed to the method.
  - param `pISalesOpportunitySourceSetupParams`: The key of the source to be deleted.
  - remarks: You cannot delete a sales opportunity source that is associated with a sales opportunity.
  - C# example (from SAP's help):
    ```csharp
    SalesOpportunitySourceSetupParams sourceParams = sourceService.GetDataInterface(
        SalesOpportunitySourcesSetupServiceDataInterfaces.sosssSalesOpportunitySourceSetupParams) as SalesOpportunitySourceSetupParams;

    // Make sure that a record with SequenceNo = 1 exists
    sourceParams.SequenceNo = 1;

    Console.WriteLine("Delete a SalesOpportunitySourceSetup object with key=" + sourceParams.SequenceNo.ToString());
    try
    {
        sourceService.DeleteSalesOpportunitySourceSetup(sourceService.GetSalesOpportunitySourceSetup(sourceParams));
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SalesOpportunitySourcesSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the SalesOpportunitySourcesSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/SalesOpportunitySourcesSetupServiceDataInterfaces.md`
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
- `Public Function GetSalesOpportunitySourceSetup(ByVal pISalesOpportunitySourceSetupParams As SalesOpportunitySourceSetupParams) As SalesOpportunitySourceSetup` Retrieves a source. The source is specified by its key (Num), which is contained in the SalesOpportunitySourceSetupParams object passed to the method.
  - param `pISalesOpportunitySourceSetupParams`: The key of the source to retrieve.
  - returns: The source with the specified key.
- `Public Function GetSalesOpportunitySourceSetupList() As SalesOpportunitySourceSetupParamsCollection` Retrieves the keys and names of all the sources.
  - C# example (from SAP's help):
    ```csharp
    SalesOpportunitySourceSetupParamsCollection sourcesParams = sourceService.GetSalesOpportunitySourceSetupList();
    int i = 1;
    foreach (SalesOpportunitySourceSetupParams sourceParams in sourcesParams)
    {
        Console.WriteLine("item {0}: SequenceNum:{1}, Description:{2}", i++, sourceParams.SequenceNo, sourceParams.Description);
    }
    ```
- `Public Sub UpdateSalesOpportunitySourceSetup(ByVal pISalesOpportunitySourceSetup As SalesOpportunitySourceSetup)` Updates an existing source. The data for the source, including the key of the source to be updated, is contained in the SalesOpportunitySourceSetup object passed to the method. To update a source, you must first retrieve it using the GetSalesOpportunitySourceSetup method.
  - param `pISalesOpportunitySourceSetup`: The data for the source to be updated. The SalesOpportunitySourceSetup object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SalesOpportunitySourceSetupParams sourceParams = sourceService.GetDataInterface(
        SalesOpportunitySourcesSetupServiceDataInterfaces.sosssSalesOpportunitySourceSetupParams) as SalesOpportunitySourceSetupParams;

    // Make sure that a record with SequenceNo = 1 exists
    sourceParams.SequenceNo = 1;

    SalesOpportunitySourceSetup source = sourceService.GetSalesOpportunitySourceSetup(sourceParams);
    source.Description = "new value";
    source.Sort = source.Sort + 1;

    try
    {
        sourceService.UpdateSalesOpportunitySourceSetup(source);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
