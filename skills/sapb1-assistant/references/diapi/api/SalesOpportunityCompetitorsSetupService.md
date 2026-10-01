<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesOpportunityCompetitorsSetupService (Object)

The SalesOpportunityCompetitorsSetupService service enables you to add, look up and remove competitors in the competitors master data table. Competitors can be assigned to sales opportunities. To see the list of competitors, select Sales Opportunities --> Sales Opportunity, select a sales opportunity and select the Competitors tab. In the Name column, select Define New. Source table: OCMT

## Methods (8)
- `Public Function AddSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetup As SalesOpportunityCompetitorSetup) As SalesOpportunityCompetitorSetupParams` Adds a competitor.
  - param `pISalesOpportunityCompetitorSetup`: The data for the new competitor.
  - returns: Contains the key (CompetId) of the new competitor.
  - C# example (from SAP's help):
    ```csharp
    try
    {
         SalesOpportunityCompetitorsSetupService oCompetSrv;
         oCompetSrv = (SalesOpportunityCompetitorsSetupService)
             (MainModule.oCmpSrv.GetBusinessService(ServiceTypes.SalesOpportunityCompetitorsSetupService));

         SalesOpportunityCompetitorSetup addLine;
         addLine = (SalesOpportunityCompetitorSetup)oCompetSrv.GetDataInterface(
              SalesOpportunityCompetitorsSetupServiceDataInterfaces.socssSalesOpportunityCompetitorSetup);

         addLine.Name = "competitor1";
         addLine.ThreatLevel = ThreatLevelEnum.Medium;
         addLine.Details = "Discount";
         oCompetSrv.AddSalesOpportunityCompetitorSetup(addLine);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub DeleteSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetupParams As SalesOpportunityCompetitorSetupParams)` Deletes an existing competitor. The competitor is specified by its key (CompetId), which is contained in the SalesOpportunityCompetitorSetupParams object passed to the method.
  - param `pISalesOpportunityCompetitorSetupParams`: The key of the competitor to be deleted.
  - remarks: You cannot delete a sales opportunity competitor that is associated with a sales opportunity.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityCompetitorSetupParams delLine;
        delLine = (SalesOpportunityCompetitorSetupParams)oCompetSrv.GetDataInterface(SalesOpportunityCompetitorsSetupServiceDataInterfaces.socssSalesOpportunityCompetitorSetupParams);

        // Delete a record
        // The SequenceNo should be the competitor ID of a record in the DB
        delLine.SequenceNo = 31;
        oCompetSrv.DeleteSalesOpportunityCompetitorSetup(delLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SalesOpportunityCompetitorsSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the SalesOpportunityCompetitorsSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/SalesOpportunityCompetitorsSetupServiceDataInterfaces.md`
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
- `Public Function GetSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetupParams As SalesOpportunityCompetitorSetupParams) As SalesOpportunityCompetitorSetup` Retrieves a competitor. The competitor is specified by its key (CompetId), which is contained in the SalesOpportunityCompetitorSetupParams object passed to the method.
  - param `pISalesOpportunityCompetitorSetupParams`: The key of the competitor to retrieve.
  - returns: The competitor with the specified key.
- `Public Function GetSalesOpportunityCompetitorSetupList() As SalesOpportunityCompetitorSetupParamsCollection` Retrieves the keys and names of all the competitors.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityCompetitorSetupParamsCollection getlistParams;
        getlistParams = oCompetSrv.GetSalesOpportunityCompetitorSetupList();

        String resultSet = "";

        foreach(SalesOpportunityCompetitorSetupParams record in getlistParams)
        {
            resultSet = resultSet + record.SequenceNo + "\t" + record.Name + "\t" + record.ThreatLevel + "\n";
            Interaction.MsgBox(resultSet, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
        }
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Sub UpdateSalesOpportunityCompetitorSetup(ByVal pISalesOpportunityCompetitorSetup As SalesOpportunityCompetitorSetup)` Updates an existing competitor. The data for the competitor, including the key of the competitor to be updated, is contained in the SalesOpportunityCompetitorSetup object passed to the method. To update a competitor, you must first retrieve it using the GetSalesOpportunityCompetitorSetup method.
  - param `pISalesOpportunityCompetitorSetup`: The data for the competitor to be updated. The SalesOpportunityCompetitorSetup object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SalesOpportunityCompetitorSetupParams getLine;
        SalesOpportunityCompetitorSetup updateLine;
        getLine = (SalesOpportunityCompetitorSetupParams)oCompetSrv.GetDataInterface(SalesOpportunityCompetitorsSetupServiceDataInterfaces.socssSalesOpportunityCompetitorSetupParams);

        //update a record
        //please note that the SequenceNo should be the Competitor ID of a record in DB
        getLine.SequenceNo = 30;

        updateLine = oCompetSrv.GetSalesOpportunityCompetitorSetup(getLine);
        updateLine.Details = "updated memo";
        updateLine.Name = "updated name";
        updateLine.ThreatLevel = ThreatLevelEnum.High;
        oCompetSrv.UpdateSalesOpportunityCompetitorSetup(updateLine);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
