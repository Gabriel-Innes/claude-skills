<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesOpportunityInterestsSetupService (Object)

The SalesOpportunityInterestsSetupService service enables you to add, look up and remove interests in the interests master data table. Interests can be assigned to sales opportunities; the interest describes an area of interest to the sales opportunity. To see the list of interests, select Sales Opportunities --> Sales Opportunity, and then select the Potential tab. In the Description column of the Interest Range list, select Define New. The Reasons list is disabled if the Opportunity Status is Open. Source table: OOIN

## Methods (8)
- `Public Function AddSalesOpportunityInterestSetup(ByVal pISalesOpportunityInterestSetup As SalesOpportunityInterestSetup) As SalesOpportunityInterestSetupParams` Adds an interest.
  - param `pISalesOpportunityInterestSetup`: The data for the new interest.
  - returns: Contains the key (Num) of the new interest.
  - C# example (from SAP's help):
    ```csharp
    SalesOpportunityInterestSetup interest = interestService.GetDataInterface(
        SalesOpportunityInterestsSetupServiceDataInterfaces.soissSalesOpportunityInterestSetup) as SalesOpportunityInterestSetup;

    interest.Description = "book";
    interest.Sort = 1000;
    Console.WriteLine("Add a new interest: Description: " + interest.Description + "  Sort:" + interest.Sort.ToString());
    try
    {
        interestService.AddSalesOpportunityInterestSetup(interest);
    }
    catch (Exception e)
    {
        PrintExceptionMessage(e);
    }
    ```
- `Public Sub DeleteSalesOpportunityInterestSetup(ByVal pISalesOpportunityInterestSetupParams As SalesOpportunityInterestSetupParams)` Deletes an existing interest. The interest is specified by its key (Num), which is contained in the SalesOpportunityInterestSetupParams object passed to the method.
  - param `pISalesOpportunityInterestSetupParams`: The key of the interest to be deleted.
  - remarks: You cannot delete a sales opportunity interest that is associated with a sales opportunity.
  - C# example (from SAP's help):
    ```csharp
    SalesOpportunityInterestSetupParams interestParams = interestService.GetDataInterface(
        SalesOpportunityInterestsSetupServiceDataInterfaces.soissSalesOpportunityInterestSetupParams) as SalesOpportunityInterestSetupParams;

    // Make sure that a record with SequenceNumber = 1 exists
    interestParams.SequenceNo = 1;

    Console.WriteLine("Get a SalesOpportunityInterestSetup object with key=" + interestParams.SequenceNo.ToString());
    SalesOpportunityInterestSetup interest = interestService.GetSalesOpportunityInterestSetup(interestParams);

    try
    {
        interestService.DeleteSalesOpportunityInterestSetup(interestParams);
    }
    catch (Exception e)
    {
        PrintExceptionMessage(e);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SalesOpportunityInterestsSetupServiceDataInterfaces) As Object` Creates an empty data structure for use with the SalesOpportunityInterestsSetupService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/SalesOpportunityInterestsSetupServiceDataInterfaces.md`
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
- `Public Function GetSalesOpportunityInterestSetup(ByVal pISalesOpportunityInterestSetupParams As SalesOpportunityInterestSetupParams) As SalesOpportunityInterestSetup` Retrieves an interest. The interest is specified by its key (Num), which is contained in the SalesOpportunityInterestSetupParams object passed to the method.
  - param `pISalesOpportunityInterestSetupParams`: The key of the interest to retrieve.
  - returns: The interest with the specified key.
- `Public Function GetSalesOpportunityInterestSetupList() As SalesOpportunityInterestSetupParamsCollection` Retrieves the keys and names of all the interests.
  - C# example (from SAP's help):
    ```csharp
    SalesOpportunityInterestSetupParamsCollection interestsParams
        = interestService.GetSalesOpportunityInterestSetupList();
    int i = 1;
    foreach (SalesOpportunityInterestSetupParams interestParams in interestsParams)
    {
        Console.WriteLine("item {0}: SequenceNum:{1}, Description:{2}", i++, interestParams.SequenceNo, interestParams.Description);
    }
    ```
- `Public Sub UpdateSalesOpportunityInterestSetup(ByVal pISalesOpportunityInterestSetup As SalesOpportunityInterestSetup)` Updates an existing interest. The data for the interest, including the key of the interest to be updated, is contained in the SalesOpportunityInterestSetup object passed to the method. To update an interest, you must first retrieve it using the GetSalesOpportunityInterestSetup method.
  - param `pISalesOpportunityInterestSetup`: The data for the interest to be updated. The SalesOpportunityInterestSetup object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SalesOpportunityInterestSetupParams interestParams = interestService.GetDataInterface(SalesOpportunityInterestsSetupServiceDataInterfaces.soissSalesOpportunityInterestSetupParams)
             as SalesOpportunityInterestSetupParams;

    // Make sure that a record with SequenceNumber = 1 exists
    interestParams.SequenceNo = 1;

    SalesOpportunityInterestSetup interest = interestService.GetSalesOpportunityInterestSetup(interestParams);

    interest.Description = "new value";
    interest.Sort = interest.Sort + 1;
    try
    {
        interestService.UpdateSalesOpportunityInterestSetup(interest);
    }
    catch (Exception e)
    {
        PrintExceptionMessage(e);
    }
    ```
