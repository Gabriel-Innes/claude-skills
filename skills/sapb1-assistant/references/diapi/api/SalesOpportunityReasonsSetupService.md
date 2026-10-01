<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesOpportunityReasonsSetupService (Object)

The SalesOpportunityReasonsSetupService service enables you to add, look up and remove reasons in the reasons master data table. Reasons can be assigned to sales opportunities; the reason explain why a sales opportunity was won or lost. To see the list of reasons, select Sales Opportunities --> Sales Opportunity, and then select the Summary tab. In the Description column of the Reasons list, select Define New. The Reasons list is disabled if the Opportunity Status is Open. Source table: OOFR

## Methods (8)
- `Public Function AddSalesOpportunityReasonSetup(ByVal pISalesOpportunityReasonSetup As SalesOpportunityReasonSetup) As SalesOpportunityReasonSetupParams` Adds a reason.
  - param `pISalesOpportunityReasonSetup`: The data for the new reason.
  - returns: Contains the key (Num) of the new reason.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityReasonsSetupService oReasonSrv;
        oReasonSrv = (SalesOpportunityReasonsSetupService)(MainModule.oCmpSrv.GetBusinessService(ServiceTypes.SalesOpportunityReasonsSetupService));

        SalesOpportunityReasonSetup addLine;
        addLine = (SalesOpportunityReasonSetup)oReasonSrv.GetDataInterface(SalesOpportunityReasonsSetupServiceDataInterfaces.sorssSalesOpportunityReasonSetup);

        addLine.Description = "Reason1";
        addLine.Sort = 215;
        oReasonSrv.AddSalesOpportunityReasonSetup(addLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteSalesOpportunityReasonSetup(ByVal pISalesOpportunityReasonSetupParams As SalesOpportunityReasonSetupParams)` Deletes an existing reason. The reason is specified by its key (Num), which is contained in the SalesOpportunityReasonSetupParams object passed to the method.
  - param `pISalesOpportunityReasonSetupParams`: The key of the reason to be deleted.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityReasonSetupParams delLine;
        delLine = (SalesOpportunityReasonSetupParams)oReasonSrv.GetDataInterface(SalesOpportunityReasonsSetupServiceDataInterfaces.sorssSalesOpportunityReasonSetupParams);

        // Delete
        // The SequenceNo should be the ID of an existing record
        delLine.SequenceNo = 26;
        oReasonSrv.DeleteSalesOpportunityReasonSetup(delLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SalesOpportunityReasonsSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the SalesOpportunityReasonsSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/SalesOpportunityReasonsSetupServiceDataInterfaces.md`
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
- `Public Function GetSalesOpportunityReasonSetup(ByVal pISalesOpportunityReasonSetupParams As SalesOpportunityReasonSetupParams) As SalesOpportunityReasonSetup` Retrieves a reason. The reason is specified by its key (Num), which is contained in the SalesOpportunityReasonSetupParams object passed to the method.
  - param `pISalesOpportunityReasonSetupParams`: The key of the reason to retrieve.
  - returns: The reason with the specified key.
- `Public Function GetSalesOpportunityReasonSetupList() As SalesOpportunityReasonSetupParamsCollection` Retrieves the keys and names of all the reasons.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityReasonSetupParamsCollection getParams;
        getParams = oReasonSrv.GetSalesOpportunityReasonSetupList();

        String resultSet = "";
        foreach (SalesOpportunityReasonSetupParams record in getParams)
        {
            resultSet = resultSet + record.Description + "\t" + "\n";
        }

        Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub UpdateSalesOpportunityReasonSetup(ByVal pISalesOpportunityReasonSetup As SalesOpportunityReasonSetup)` Updates an existing reason. The data for the reason, including the key of the reason to be updated, is contained in the SalesOpportunityReasonSetup object passed to the method. To update a reason, you must first retrieve it using the GetSalesOpportunityReasonSetup method.
  - param `pISalesOpportunityReasonSetup`: The data for the reason to be updated. The SalesOpportunityReasonSetup object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityReasonSetupParams getLine;
        SalesOpportunityReasonSetup updateLine;
        getLine = (SalesOpportunityReasonSetupParams)oReasonSrv.GetDataInterface(SalesOpportunityReasonsSetupServiceDataInterfaces.sorssSalesOpportunityReasonSetupParams);

        //please note that the SequenceNo should be the ID of an existing record.
        getLine.SequenceNo = 28;

        updateLine = oReasonSrv.GetSalesOpportunityReasonSetup(getLine);
        updateLine.Description = "Updated reason";
        updateLine.Sort = 150;
        oReasonSrv.UpdateSalesOpportunityReasonSetup(updateLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
