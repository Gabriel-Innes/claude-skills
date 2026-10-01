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
  - enum: `SalesOpportunityInterestsSetupServiceDataInterfaces` in `../enums/enums-03.md`
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

# SalesOpportunityReasonSetup (Object)

Represents a reason for a successful or unsuccessful sales opportunity. Source table: OOFR Mandatory properties: Description

**Remarks:** The SalesOpportunitiesReasons object represents the reasons for a specific sales opportunity.

## Properties (3)
- `Public Property Description() As String` [R/W] The description of the reason. Field name: Descript
  - remarks: Cannot be blank.
- `Public Property SequenceNo() As Long` [R] The key for a specific reason. Field name: Num
- `Public Property Sort() As Long` [R/W] A value for determining in what order to display the items in the user interface. Default is 100. Field name: SortOrder
  - remarks: Cannot be negative. If two or more items have the same sort value, these items are sorted in alphabetical order. When a user starts to add a new item, the application automatically sets the sort value to one more than the current highest sort value. If the user clears this suggested value and adds the record with no sort value, the application automatically sets the sort value to 100.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunityReasonSetupParams (Object)

Holds the key and name to an existing reason. This object is used to pass keys to and retrieve keys from SalesOpportunityReasonsSetupService methods.

## Properties (2)
- `Public Property Description() As String` [R] The description of the reason. Field name: Descript
- `Public Property SequenceNo() As Long` [R/W] The key for a specific reason. Field name: Num

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunityReasonSetupParamsCollection (Collection)

A collection of SalesOpportunityReasonSetupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As SalesOpportunityReasonSetupParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As SalesOpportunityReasonSetupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

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
  - enum: `SalesOpportunityReasonsSetupServiceDataInterfaces` in `../enums/enums-03.md`
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

# SalesOpportunitySourceSetup (Object)

Represents a source from which sales opportunities can be generated. Source table: OOSR Mandatory properties: Description

## Properties (3)
- `Public Property Description() As String` [R/W] The description of the source. Field name: Descript
  - remarks: Cannot be blank.
- `Public Property SequenceNo() As Long` [R] The key for a specific source. Field name: Num
- `Public Property Sort() As Long` [R/W] A value for determining in what order to display the items in the user interface. Default is 100. Field name: SortOrder
  - remarks: Cannot be negative. If two or more items have the same sort value, these items are sorted in alphabetical order. When a user starts to add a new item, the application automatically sets the sort value to one more than the current highest sort value. If the user clears this suggested value and adds the record with no sort value, the application automatically sets the sort value to 100.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunitySourceSetupParams (Object)

Holds the key and name to a source. This object is used to pass keys to and retrieve keys from SalesOpportunitySourcesSetupService methods.

## Properties (2)
- `Public Property Description() As String` [R] The description of the source. Field name: Descript
- `Public Property SequenceNo() As Long` [R/W] The key for a specific source. Field name: Num

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SalesOpportunitySourceSetupParamsCollection (Collection)

A collection of SalesOpportunitySourceSetupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As SalesOpportunitySourceSetupParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As SalesOpportunitySourceSetupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

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
  - enum: `SalesOpportunitySourcesSetupServiceDataInterfaces` in `../enums/enums-03.md`
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

# SalesPersons (Object)

The SalesPersons object enables to define sales employees and their commision percentage. Source table: OSLP.

**Remarks:** Mandatory fields in SAP Business One: SalesEmployeeName. To display the form in the application: - Select Administration -->Setup -->General -->Sales Employees.

## Properties (14)
- `Public Property Active() As BoYesNoEnum` [R/W] Determines whether the sales employee is active or not. Field name: Active.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CommissionForSalesEmployee() As Double` [R/W] Sets or returns the commission percentage for the sales employee. Field name: Commission.
  - remarks: Applicable when SetCommissionbySE (AdminInfo object) is set to tYes.
- `Public Property CommissionGroup() As Long` [R/W] Sets or returns commission group code, which is relevant to the sales employee. This is a foreign key to the CommissionGroups object. Sets or returns the commission percentage for the sales employee. Field name: GroupCode. This is a foreign key to the CommissionGroups object.
  - remarks: Applicable when SetCommissionbySE (AdminInfo object) is set to tYes.
- `Public Property eMail() As String` [R/W] Sets or returns the Email of the sales employee. Length: 100 characters. Field name: Email.
- `Public Property EmployeeID() As Long` [R] Returns the employee ID code. Field name: EmpID. This is a foreign key to the EmployeesInfo object.
- `Public Property Fax() As String` [R/W] Sets or returns the fax number of the sales employee. Length: 50 characters. Field name: Fax.
- `Public Property Locked() As BoYesNoEnum` [R] Returns whether or not the sales person definition is locked for update. Field name: Locked.
  - remarks: tYes - the record is locked. The record -1 -No Sales Employee- is locked by the system. tNo - the record is available for update. All the records starting from 1 are available for update.
- `Public Property Mobile() As String` [R/W] Sets or returns the mobile number of the sales employee. Length: 50 characters. Field name: Mobil.
- `Public Property Remarks() As String` [R/W] Sets or returns the remarks related to the sales employee. Length: 50 characters. Field name: Memo.
- `Public Property SalesEmployeeCode() As Long` [R] Returns the primary key of the sales employee as assigned by the system. Field name: SlpCode.
  - remarks: This property is a system numerator available from number 1. The default value is -1 that means No Sales Employee. You can set another default value for a specific user or users group by the SalesEmployee (UserDefaultGroups).
- `Public Property SalesEmployeeName() As String` [R/W] Sets or returns the name of the sales employee. Mandatory property. Field name: SlpName. Length: 155 characters.
- `Public Property Telephone() As String` [R/W] Sets or returns the telephone number of the sales employee. Length: 50 characters. Field name: Telephone.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a sales person employee.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lSlpCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lSlpCode`: SalesEmployeeCode.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# SalesStages (Object)

The SalesStages object enables defining sales stages and their probability percentage. For example: Lead, Meeting, Quotation, Negotiation, and Order. These definitions are used as default values for the SalesOpportunities object. Source table: OOST.

**Remarks:** Mandatory fields in SAP Business One: Name and Stageno. To display the form in the application: - Select Administration -->Setup -->Sales Opportunities -->Sales Stages.

## Properties (9)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Cancelled() As BoYesNoEnum` [R/W] Returns whether or not the sales stage is cancelled. Field name: Canceled.
  - remarks: In the Sales Opportunities form, stages that are cancelled cannot be selected.
- `Public Property ClosingPercentage() As Double` [R/W] Sets or returns the probability percentage to complete the sales stage successfuly. Field name: CloPrcnt.
  - remarks: The value must not be negative.
- `Public Property IsPurchasing() As BoYesNoEnum` [R/W] property IsPurchasing
- `Public Property IsSales() As BoYesNoEnum` [R/W] property IsSales
- `Public Property Name() As String` [R/W] Sets or returns the stage name. Mandatory property. Field name: Descript. Langth: 30 characters.
- `Public Property SequenceNo() As Long` [R] Returns the primary identification key of the sales stage as assigned by the system when adding a new sales stage (numerator). Property type Read-only property " --> Field name: Num.
- `Public Property Stageno() As Long` [R/W] Sets or returns the stage identification number. Mandatory property. Field name: StepId.
  - remarks: The stage number must be a unique and not a negative number.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a sales stage definition.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lNum As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lNum`: SequenceNo.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# SalesTaxAuthorities (Object)

SalesTaxAuthorities is a business object that represents the sales tax jurisdictions data for US and Canada localizations, or sales tax types for Latin America localization. In US and Canada localizations, the sales tax jurisdictions can be defined, for example, for each state, country, and city. In Latin America localization, the sales tax types are related to specific items, such as fuel and cigarettes, that are liable to tax (Rate) in addition to VAT. This object enables you to: - Add a sales tax authority. - Retrieve a sales tax authority by its key. - Update a sales tax authority data. - Save the object in XML format. Source table: OSTA.

**Remarks:** Mandatory field in SAP Business One: Code. To display the form in the application (US and Canada localizations): - Select Administration --> Setup --> Financials --> Tax --> Sales Tax Jurisdiction. A Selection Criteria dialog box opens. - From the Define Sales Tax Jurisdiction Types - Selection Criteria select a tax jurisdiction type and click OK. To display the form in the application (Latin America localization): - Select Administration --> Setup --> Financials --> Tax --> Tax Types. - From the Define Tax Types - Selection Criteria select a tax category and click OK.

## Properties (30)
- `Public Property AOrPTaxAccount() As String` [R/W] Sets or returns the G/L account for purchase (A/P) tax. Field name: PurchTax. Length: 15 characters.
- `Public Property AOrRTaxAccount() As String` [R/W] Sets or returns the G/L account for sales (A/R) tax. Field name: SalesTax. Length: 15 characters. This is a foreign key to the ChartOfAccounts object, not exposed through the DI API).
- `Public Property APExpAccount() As String` [R/W] property APExpAccount
- `Public Property ARExpAccount() As String` [R/W] property ARExpAccount
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R/W] Sets or returns the code of the tax authority. Mandatory in SAP Business One. Field name: Code. Length: 8 characters.
- `Public Property DeferredTaxAccount() As String` [R/W] Sets or returns the G/L account for deferred tax. Field name: deferrAcct. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property Exempt() As BoYesNoEnum` [R/W] property Exempt
- `Public Property FlatTaxAmount() As Double` [R/W] The maximum tax to be applied to a document for this jurisdiction, or the maximum tax to be applied for each item in a document for a jurisdiction if Single Item Tax (IsItemLevel property of the SalesTaxCodes object) is selected for the tax code. Field name: FlatAmount
  - remarks: For the United States only.
- `Public Property InclInFirstInstallment() As BoYesNoEnum` [R/W] property InclInFirstInstallment
- `Public Property InclInGrossRevenue() As BoYesNoEnum` [R/W] property InclInGrossRevenue
- `Public Property InclInPrice() As BoYesNoEnum` [R/W] property InclInPrice
- `Public Property MaxTaxableAmount() As Double` [R/W] Maximum amount for which to apply this tax. If the amount is above the value in this field, the tax is applied only to the value in this field. The maximum amount is by default compared to the document amount; if Single Item Tax is selected for the tax code (IsItemLevel property of the SalesTaxCodes object), the maximum amount is compared to each item's amount. Field name: MaxAmount
  - remarks: For the United States only.
- `Public Property MinTaxableAmount() As Double` [R/W] Minimum amount for which to apply this tax. If the amount is below the value in this field, the tax for this jurisdiction is 0. The minimum amount is by default compared to the document amount; if Single Item Tax is selected for the tax code (IsItemLevel property of the SalesTaxCodes object), the minimum amount is compared to each item's amount. Field name: MinAmount
  - remarks: For the United States only.
- `Public Property Name() As String` [R/W] Sets or returns the name of the sales tax authority. Field name: Name. Length: 100 characters.
- `Public Property NonDeductibleAccount() As String` [R/W] Sets or returns the G/L account for non deductible tax amounts. Field name: NonDdctAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property NonDeductiblePrecent() As Double` [R/W] Sets or returns the percentage of non deductible tax. Field name: NonDdctPrc.
- `Public Property Rate() As Double` [R/W] Sets or returns the tax percentage of the tax authority. Mandatory in SAP Business One. Field name: Rate.
  - remarks: In the United States and canada localizations, if you set a rate, the system creates a Tax Definition row with the rate and the current system date.
- `Public Property ReverseChargePercent() As Double` [R/W] property ReverseChargePercent
- `Public Property SalesTaxRCMAccount() As String` [R/W] property SalesTaxRCMAccount
- `Public Property SalesTaxRCMClrAccount() As String` [R/W] property SalesTaxRCMClrAccount
- `Public Property TaxDefinitions() As TaxDefinitions` [R] The tax definitions for this jurisdiction. A tax definition specifies a rate and the date from which it is in effect.
  - remarks: For the United States and Canada only.
- `Public Property TextCode() As Long` [R/W] property TextCode
- `Public Property Type() As Long` [R/W] Sets or returns the type of the sales tax authority as defined in SalesTaxAuthoritiesTypes object. Field name: Type. This is a foreign key to the SalesTaxAuthoritiesTypes object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the object's details. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property UseTaxAccount() As String` [R/W] Sets or returns the G/L account for Use Tax. Field name: UseTax. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property VATExemption() As BoYesNoEnum` [R/W] property VATExemption
- `Public Property VATExemptionBasePercent() As Double` [R/W] property VATExemptionBasePercent
- `Public Property VATExemptionPercent() As Double` [R/W] property VATExemptionPercent

## Methods (6)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Code As String, ByVal Type As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Code`: Sales tax authority code (Code).
  - param `Type`: Sales tax authority type (Type).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Field name: . Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# SalesTaxAuthoritiesTypes (Object)

SalesTaxAuthoritiesTypes is a business object that represents the type of sales tax authorities. It specifies whether or not the sales tax authority includes also VAT. This object enables you to: - Add a sales tax authority type. - Retrieve a sales tax authority type by its key. - Update a sales tax authority type data. - Save the object in XML format. Source table: OSTT.

**Remarks:** Mandatory field in SAP Business One: Name. To display the form in the application (US and Canada localizations): - Select Administration --> Setup --> Financials --> Tax --> Sales Tax Jurisdiction Types. To display the form in the application (Latin America localization): - Select Administration --> Setup --> Financials --> Tax --> Tax Categories.

## Properties (9)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Name() As String` [R/W] Sets or returns the name of the tax authority type. For example, State, Country, and City, which are default for US and Canada localizations. Mandatory in SAP Business One. Field name: Name. Length: 40 characters.
- `Public Property NfTaxId() As Long` [R/W] property NfTaxId
- `Public Property Numerator() As Long` [R] Returns the identification key of the Tax Authority Type as assigned by SAP Business One (starts from 1). Field name: AbsId.
- `Public Property TaxCreditControl() As BoYesNoEnum` [R/W] property TaxCreditControl
- `Public Property TaxParamSetId() As Long` [R/W] property TaxParamSetId
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the object's details. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property VAT() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the tax type includes also VAT. Field name: IsVat.
  - remarks: Country-specific for Latin America.

## Methods (6)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Key As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Key`: Identification key of the Tax Authority Type (Numerator).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# SalesTaxCodes (Object)

SalesTaxCodes is a business object that represents the inclusive sales tax codes. Each sales tax code consists of one or more sales taxes as defined in SalesTaxAuthorities object. This object enables you to: - Add a sales tax code. - Retrieve a sales tax code by its key. - Update a sales tax code data. - Save the object in XML format. Source table: OSTC.

**Remarks:** Mandatory fields in SAP Business One: ValidForAP and /or ValidForAR must be tYES. To display the form in the application (US and Canada localizations): - Select Administration --> Setup --> Financials --> Tax --> Sales Tax Codes. To display the form in the application (Latin America localization): - Select Administration --> Setup --> Financials --> Tax --> Tax Codes.

## Properties (17)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CFOPIn() As String` [R/W] property CFOPIn
- `Public Property CFOPOut() As String` [R/W] property CFOPOut
- `Public Property Code() As String` [R/W] Sets or returns the tax code. Mandatory in SAP Business One. Field name: Code. Length: 8 characters.
- `Public Property FADebit() As BoYesNoEnum` [R/W] property FADebit
- `Public Property Freight() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to calculate the tax also on expenses, such as shipping expenses. Default: tNO. Field name: Freight.
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property IsItemLevel() As BoYesNoEnum` [R/W] Indicates whether to apply a jurisdiction's minimum amount, maximum amount, and flat tax thresholds (MinTaxableAmount, MaxTaxableAmount, and FlatTaxAmount properties of the SalesTaxAuthorities object) to the document amount or to each item's amount.
- `Public Property Lines() As SalesTaxCodes_Lines` [R] Returns the SalesTaxCodes_Lines child object.
- `Public Property Name() As String` [R/W] Sets or returns the name of the tax code. Field name: Name. Length: 100 characters.
- `Public Property Rate() As Double` [R] Returns the inclusive tax percentage based on the selected tax authorities/types in SalesTaxCodes_Lines child object. Field name: Rate.
  - remarks: The inclusive rate equals to sum of EffectiveRate specified in each line.
- `Public Property TypeFormulaCombId() As Long` [R/W] property TypeFormulaCombId
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the object's details. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property ValidForAP() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the tax is valid for purchase - A/P. Field name: ValidForAP.
  - remarks: Default: tYES. If you set to tNO, you must set ValidForAR to tYES.
- `Public Property ValidForAR() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the tax is valid for Sales - A/R. Field name: ValidForAR.
  - remarks: Default: tYES. If you set to tNO, you must set ValidForAP to tYES.
- `Public Property VATExemption() As BoYesNoEnum` [R/W] property VATExemption

## Methods (6)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
  - example note: The following sample shows how to add an invoice (with lines) document to the database. Use this sample as a basis for all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub AddInvoice_Click()

        Dim RetVal As Long

        Dim ErrCode As Long

        Dim ErrMsg As String

        'Create the Documents object

        Dim vInvoice    As SAPbobsCOM.Documents

        Set vInvoice = vCmp.GetBusinessObject(oInvoices)

        'Set values to the fields

        vInvoice.Series = 0

        vInvoice.CardCode = "BP234"

        vInvoice.HandWritten = tNO

        vInvoice.PaymentGroupCode = "-1"

        vInvoice.DocDate = "21/8/2003"

        vInvoice.DocTotal = 264.6

        'Invoice Lines - Set values to the first line

        vInvoice.Lines.ItemCode = "A00023"

        vInvoice.Lines.ItemDescription = "Banana"

        vInvoice.Lines.PriceAfterVAT = 2.36

        vInvoice.Lines.Quantity = 50

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Invoice Lines - Set values to the second line

        vInvoice.Lines.Add

        vInvoice.Lines.ItemCode = " A00033"

        vInvoice.Lines.ItemDescription = "Orange"

        vInvoice.Lines.PriceAfterVAT = 118

        vInvoice.Lines.Quantity = 1

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Add the Invoice

        RetVal = vInvoice.Add

       'Check the result

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox ErrCode & " " & ErrMsg

        End If

     End Sub
    ```
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Key As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Key`: (Code).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.

# SalesTaxCodes_Lines (Object)

TaxCodes_Lines is a child object of the SalesTaxCodes object and represents the tax authorities/types from which the tax code is combined. Source table: STC1.

## Properties (12)
- `Public Property Count() As Long` [R] Returns the total rows in the table.
- `Public Property CSTCodeIn() As String` [R/W] property CSTCodeIn
- `Public Property CSTSuffix() As String` [R/W] property CSTSuffix
- `Public Property EffectiveRate() As Double` [R] Returns the effective rate based on the rate of the specified tax authority/type (Rate) and tax-on-tax calculation (STATaxonTaxCode and STATaxOnTaxType). Field name: EfctivRate.
  - remarks: For example, if a tax code is combined of two lines (two tax jurisdictions): - New York state - tax rate 4 - New York city - tax rate 10 The effective rate of the first line equals to 4STATaxonTaxCode and STATaxOnTaxType relates to New York state, then the effective rate of the second line equals to 10.4"> (10 + 10 x 4Rate) is 14.4"> (4). If the values of STATaxonTaxCode and STATaxOnTaxType relates to null, then the effective rate of the second line equals to 10Rate) is 14"> (4 + 10).
- `Public Property FormulaId() As Long` [R/W] property FormulaId
- `Public Property RowNumber() As Long` [R] Returns the current available row number (starts from 1). Field name: Line_ID.
- `Public Property STACode() As String` [R/W] Sets or returns the code of the tax authority. Field name: e. Length: 8 characters.
  - remarks: STACode is the primary key.
- `Public Property STATaxonTaxCode() As String` [R/W] Sets or returns the code of the tax authority on which the tax-on-tax is based. Field name: TaxOnTCod. Length: 8 characters.
- `Public Property STATaxOnTaxType() As Long` [R/W] Sets or returns the type of the sales tax authority on which the tax-on-tax is based. Field name: TaxOnTType.
- `Public Property STAType() As Long` [R/W] Sets or returns the type of the sales tax authority on which the tax rate of the current line is based. Field name: STAType. This is a foreign key to the SalesTaxAuthorities object.
- `Public Property STCCode() As String` [R] Sets or returns the code of the tax authority on which the the tax rate of the current line is based. Field name: STCCode. Length: 8 characters. This is a foreign key to the SalesTaxCodes object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# SBObob (Object)

The SBObob object is raw data access object that enables you to retrieve information quickly and easily. The returned data is usually a Recordset object that enables data manipulation. See SBObob samples.

## Methods (29)
- `Public Function ConvertEnumValueToValidValue(ByVal enumName As String, ByVal enumValue As Long) As String` Converts a specified enumeration value of an enumeration name to the valid value defined in the company database. See Conversion sample.
  - param `enumName`: Enumeration name
  - param `enumValue`: Enumeration value.
- `Public Function ConvertValidValueToEnumValue(ByVal enumName As String, ByVal ValidValue As String) As Long` Converts a specified valid value of an enumeration name to the enumeration value defined in the company database. See Conversion sample.
  - param `enumName`: Enumeration name.
  - param `ValidValue`: Valid value.
- `Public Function Format_DateToString(ByVal inDate As Date) As Recordset` Converts the system date to a string. See Formatting sample.
  - param `inDate`: System date.
- `Public Function Format_MoneyToString(ByVal inMoney As Double, ByVal inPrecision As BoMoneyPrecisionTypes) As Recordset` Converts a specified amount of money to a string according to a specified precision. See Formatting sample.
  - param `inMoney`: Amount of money.
  - param `inPrecision`: one of the enumeration's values (see the enum file)
  - enum: `BoMoneyPrecisionTypes` in `../enums/enums-01.md`
- `Public Function Format_StringToDate(ByVal inStr As String) As Recordset` Converts date string to a system date.
  - param `inStr`: Date as string.
- `Public Function GetAccountSegmentsByCode(ByVal AccountCode As String, ByVal AddSeperator As Boolean) As Recordset` Returns a Recordset object that contains the value of the FormatCode property for a specified AccountCode.
  - param `AccountCode`: Account code (Code) as assigned in SAP Business One when adding a G/L account with segments. For example, _SYS 00000000010.
  - param `AddSeperator`: Specifies whether or not to include a separator, such as - (dash), between the account segments. The separator is defined in SAP BUsiness One (Administration -->System Initialization --> General Settings --> Display tab).
- `Public Function GetBPList(ByVal CardType As BoCardTypes) As Recordset` Returns a Recordset object that contains a list of business partners keys that can be used as a parameter in many business objects. See Get Business Partners List sample.
  - param `CardType`: one of the enumeration's values (see the enum file)
  - returns: A Recordset object containing three fields : CardCode, CardName, and CardType.
  - enum: `BoCardTypes` in `../enums/enums-01.md`
- `Public Function GetContactEmployees(ByVal CardCode As String) As Recordset` Returns a Recordset object that contains a list of contact employees for a specified business partner. See Get Contact Employees sample.
  - param `CardCode`: Specifies the business partner code for which you want to obtain contact employees.
- `Public Function GetCurrencyRate(ByVal Currency As String, ByVal Date As Date) As Recordset` Returns a Recordset object that contains the currency rate for a specified date and currency code. See Currency sample. Source table: ORTT.
  - param `Currency`: Specifies the currency code.
  - param `Date`: Specifies the date for the currency exchange rate.
  - returns: A Recordset object that contains one field named CurrencyRate that holds the rate value. SAP Business One returns 0 if the system cannot find the exchange rate. Exceptions -2000 The connection with the database has been disconnected.
  - remarks: You can use this method to query the exchange rate between any currency and the local currency. For example, if the local currency is US dollars, and you need the currency rate for EUR on January 10, 2002. Use the following line code: vObj.GetCurrencyRate("eur", Date("10.01.2002")) A result of 0.98 from the returned Recordset object means that on January 10, 2002 the exchange rate was 1 EUR = 0.98 USD.
- `Public Function GetDueDate(ByVal CardCode As String, ByVal refDate As Date) As Recordset` Returns the due date for a specified business partner based on the business partner code and the reference date. See Get Due Date sample.
  - param `CardCode`: Specifies the business partner code.
  - param `refDate`: Specifies the reference date.
  - returns: A Recordset object that contains one field named DueDate that holds the due date value. Exceptions -2000 The connection with the database has been disconnected.
  - remarks: When you create a document, you can use this method to get the due date of that document using the business partner code and document date. The due date is defined in the customer payment terms, in the business partner master record. You can change the due date when you create the document.
- `Public Sub GetEwaParameters(ByVal bstrKey As String, ByRef pbstrRsltEwaUserName As String, ByRef pbstrRsltEwaPassword As String)` Returns a Recordset that defines the Early Watch Alert user parameters: - EWA Key - User Name - User PassWord
  - param `bstrKey`: Specifies the Early Warning Alert Key.
  - param `pbstrRsltEwaUserName`: Specifies the Early Warning Alert User name.
  - param `pbstrRsltEwaPassword`: Specifies the Early Warning Alert User Password.
- `Public Function GetFieldValidValues(ByVal TableName As String, ByVal FieldName As String) As Recordset` Returns a Recordset object that contains the valid values of a specified field and table in the database. Each valid value includes its name and description. For example, the valid values for CardType field in OCRD table are: C - Customer, S - Supplier, and L - Lead.
  - param `TableName`: Table name in the database.
  - param `FieldName`: Field name in the database.
  - remarks: The following is a returned recordset that is saved in XML format: <?xml version="1.0" encoding="UTF-16"?> <BOM> <BO> <AdmInfo> <Object>-1</Object> </AdmInfo> <GENREC> <row> <Value>C</Value> <Description>Customer</Description> </row> <row> <Value>S</Value> <Description>Vendor</Description> </row> <row> <Value>L</Value> <Description>Lead</Description> </row> </GENREC> </BO> </BOM>
- `Public Function GetIndexRate(ByVal Index As String, ByVal Date As Date) As Recordset` Returns a Recordset object that contains the index rate for a specified date and index code. See Get Index Rate sample.
  - param `Index`: Specifies the index code.
  - param `Date`: Specifies the reference date.
  - returns: A Recordset object that contains one field named IndexRate that holds the index rate value. If the index does not exists, the system returns 0. Exceptions -2000 The connection with database has been disconnected.
  - remarks: SAP Business One supports multiple index rates. You can use these indexes in reporting sheet to help users to analyze business data.
- `Public Function GetItemList() As Recordset` Returns a Recordset object that contains an item code and item name. To retrieve the items list, apply this method in a loop. See Get Items List sample.
  - returns: A Recordset object that contains two fields: ItemCode and ItemName. Exceptions -2000 The connection with database has been disconnected.
  - remarks: For more detailed information about the item, you can create a new instance for the Items object, and then use the GetByKey method.
- `Public Function GetItemPrice(ByVal CardCode As String, ByVal ItemCode As String, ByVal amount As Double, ByVal Date As Date) As Recordset` Returns a Recordset object that contains the item price for specified business partner and item, based on the amount and transaction date. See Get Item Price sample.
  - param `CardCode`: Specifies the business partner code.
  - param `ItemCode`: Specifies the item code.
  - param `amount`: Specifies transaction quantity (number of units).
  - param `Date`: Specifies transaction date.
  - returns: A Recordset object that contains two fields: Price and Currency. The system returns 0, if a price is not found for the specified business partner and item. Exceptions -2000 The connection with database has been disconnected.
  - remarks: The item price consists on the following four factors: business partner, item, transaction amount, and transaction date. If the currency of the returned price is not the same currency as you use, use the GetCurrencyRate method to convert between currencies.
- `Public Function GetLicenseStatus(ByVal UserName As String, ByVal FormID As String) As Long` You can get the information whether a user has a license to access a form.
  - param `UserName`: The use name.
  - param `FormID`: The form ID. You can get the from ID from View → System Information.
  - remarks: Note: If either of the input parameter UserName or FormID is not valid, the returned value will not be accurate. This function can be called by any user. A super user can check any user, while a regular user can check his/her own user only. If a regular user tries to check a different user name, an error occurs: "You are not permitted to perform this action".
  - C# example (from SAP's help):
    ```csharp
    static void GetLicenseStatusDemo(Company oCompany)
            {
                SAPbobsCOM.SBObob oSBObob = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoBridge);
                try
                {
                    int retValue1 = oSBObob.GetLicenseStatus("manager", "1320000000"); //2

                }
                catch (Exception ex)
                {
                    Console.Write(ex.ToString());
                    return;
                }

            }
    ```
- `Public Function GetLocalCurrency() As Recordset` Returns the local currency defined in the company database. See Currency sample.
  - returns: A Recordset object containing one field named LocalCurrency that holds the local currency code. Exceptions -2000 The connection with database has been disconnected.
- `Public Function GetObjectKeyBySingleValue(ByVal ObjNum As BoObjectTypes, ByVal PropName As String, ByVal Value As String, ByVal Condition As BoQueryConditions) As Recordset` Returns a Recordset object that contains the object key by single value. See Get Object Key By Single Value sample.
  - param `ObjNum`: one of the enumeration's values (see the enum file)
  - param `PropName`: Property name of the selected object.
  - param `Value`: Value for the specified property.
  - param `Condition`: one of the enumeration's values (see the enum file)
  - enum: `BoObjectTypes` in `../enums/enums-01.md`
- `Public Function GetObjectPermission(ByVal Object As BoObjectTypes) As Recordset` Returns a single record that contains the permission type (BoPermission) of a specified PermissionId and UserSignature.
  - param `Object`: one of the enumeration's values (see the enum file)
  - enum: `BoObjectTypes` in `../enums/enums-01.md`
- `Public Function GetSystemCurrency() As Recordset` Returns the system currency defined in the company database. See Currency sample.
  - returns: A Recordset object that contains one field: SystemCurrency that holds the system currency code. Exceptions -2000 The connection with database has been disconnected.
- `Public Function GetSystemPermission(ByVal UserName As String, ByVal PermissionID As String) As Recordset` Returns the permission for a type of permission for a specific user.
  - param `UserName`: A user code
  - param `PermissionID`: A permission ID A list of permissions is available at Permissions List.
  - returns: One of the following values: 1: Read/Write 2: Read only 3: Not authorized 4: Various authorizations 6: Not defined
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oSBObob As SAPbobsCOM.SBObob

    Dim oRecordSet As SAPbobsCOM.Recordset

    '// Get an initialized SBObob object

    oSBObob = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoBridge)

    '// return the General permission (142) for the manager

    oRecordSet = oSBObob.GetSystemPermission("manager", "142")

    '// Print permission value (Read/Write=1, ReadOnly=2, NoAuthorization=3,

    '// VariousAuthorization=4, NotDefined=6)

    Debug.WriteLine(oRecordSet.Fields.Item(0).Value())
    ```
- `Public Function GetTableFieldList(ByVal TableName As String) As Recordset` Returns a Recordset object that contains the fields list of a specified table in the database. Each field includes the following parameters (the examples in parenthesis relates to OCRD: CardCode): - Name (CardCode) - Type (nvarchar) -- a numeric value representing a BoFieldTypes enumeration value - Length (15) - Linked table name for foreign key (GroupCode) - Valid values indicator, which indicates whether or not this field uses valid values (no) - IsNullable -- specifies whether or not nulls are permitted
  - param `TableName`: Table name in the database.
  - remarks: The following is a returned recordset that is saved in XML format: <?xml version="1.0" encoding="UTF-16"?> <BOM> <BO> <AdmInfo> <Object>-1</Object> </AdmInfo> <GENREC> <row> <FieldName>CardCode</FieldName> <FieldLength>15</FieldLength> <FieldType>0</FieldType> <IsNullable>0</IsNullable> <IsValidValues>0</IsValidValues> <LinkedTo/> </row> <row> <FieldName>CardName</FieldName> <FieldLength>100</FieldLength> <FieldType>0</FieldType> <IsNullable>0</IsNullable> <IsValidValues>0</IsValidValues> <LinkedTo/> </row> </GENREC> </BO> </BOM>
- `Public Function GetTableList() As Recordset` Returns a Recordset object that contains a list of all the tables in the database. Each table includes its name and description (for example: OCRD, Business Partner.
  - remarks: The following is a returned recordset that is saved in XML format: <?xml version="1.0" encoding="UTF-16"?> <BOM> <BO> <AdmInfo> <Object>-1</Object> </AdmInfo> <GENREC> <row> <row> <Alias>ACRD</Alias> <Description>Business Partner - History</Description> </row> <row> <Alias>ADO1</Alias> <Description>A/R Invoice (Rows) - History</Description> </row> <row> . . . <row> <Alias>WTR9</Alias> <Description>Stock Transfer - Base Docs Details</Description> </row> </row> </GENREC> </BO> </BOM>
- `Public Function GetUserList() As Recordset` Returns a recordset that contains a list of user codes defined in the SAP Business One company database.
  - remarks: Exceptions -2000 The connection with database has been disconnected.
- `Public Function GetValidValueDescription(ByVal ObjNum As BoObjectTypes, ByVal ObjectName As String, ByVal PropertyName As String, ByVal enumValue As Long) As String` Returns a string that contains the valid value description of a valid value.
  - param `ObjNum`: one of the enumeration's values (see the enum file)
  - param `ObjectName`: Object name.
  - param `PropertyName`: Property name of the selected object.
  - param `enumValue`: Enumeration value.
  - enum: `BoObjectTypes` in `../enums/enums-01.md`
- `Public Function GetWareHouseList() As Recordset` Returns a Recordset object that contains the warehouse code and name defined the company database. To retrieve a list of warehouses, apply this method in a loop. See Get Warehouse List sample.
  - returns: A Recordset object that contains two fields: WareHouseCode and WareHouseName. Exceptions -2000 The connection with database has been disconnected.
- `Public Sub PutEwaParameters(ByVal bstrKey As String, ByVal bstrEwaUserName As String, ByVal bstrEwaPassword As String)` Sets a Recordset that contains the Early Watch Alert user parameters: - EWA Key - User Name - User PassWord
  - param `bstrKey`: Sets the Early Warning Alert Key.
  - param `bstrEwaUserName`: Sets the Early Warning Alert User name.
  - param `bstrEwaPassword`: Sets the Early Warning Alert User Password.
- `Public Sub SetCurrencyRate(ByVal Currency As String, ByVal Date As Date, ByVal Value As Double, Optional ByVal Update As Boolean = False)` Sets the exchange rate for a specified date and currency in the company database. See Currency sample.
  - param `Currency`: Specifies the target currency.
  - param `Date`: Specifies the date of the currency rate.
  - param `Value`: Specifies the rate of the target currency.
  - param `Update`: Specifies a value indicating whether or not to update the currency.
- `Public Sub SetSystemPermission(ByVal UserName As String, ByVal PermissionID As String, ByVal Permission As Long)` Sets the permission for a type of permission for a specific user.
  - param `UserName`: A user code
  - param `PermissionID`: A permission ID A list of permissions is available at Permissions List.
  - param `Permission`: A permission, which is one of the following: 1: Read/Write 2: Read only 3: Not authorized 4: Various authorizations 6: Not defined
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oSBObob As SAPbobsCOM.SBObob

    Dim oRecordSet As SAPbobsCOM.Recordset

    '// Get an initialized SBObob object

    oSBObob = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoBridge)

    '// Get an initialized Recordset object

    oRecordSet = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.BoRecordset)

    '//set the General permission to Read/Write(Read/Write=1 ,ReadOnly=2,NoAuthorization=3,

    '//VariousAuthorization=4,NotDefined=6)

    Call oSBObob.SetSystemPermission("manager", "142", 1)
    ```

# Section (Object)

Represents a section of the tax code that defines the type of business transaction subject to TDS (withholding tax). Source table: OSEC All properties are mandatory.

**Remarks:** For India only. Mandatory properties: Code, Description, ECode

## Properties (4)
- `Public Property AbsEntry() As Long` [R] The section key. Field name: AbsID
- `Public Property Code() As String` [R/W] The section code. Field name: Code
- `Public Property Description() As String` [R/W] A description for the section. Field name: Descr
- `Public Property ECode() As String` [R/W] The eCode for filing eTDS reports. Field name: eCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SectionParams (Object)

Holds the key and code to an existing section. This object is used to pass keys to and retrieve keys from SectionsService methods.

## Properties (3)
- `Public Property AbsEntry() As Long` [R/W] The section key. Field name: AbsID
- `Public Property Code() As String` [R] The section code. Field name: Code
- `Public Property Description() As String` [R] A description for the section. Field name: Descr

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SectionsParams (Collection)

A collection of SectionParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As SectionParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As SectionParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SectionsService (Object)

The SectionsService service enables you to add, look up and remove sections in the section master data table. Sections are used to specify a type of business transaction subject to TDS (withholding tax). Source table: OSEC

**Remarks:** For India only.

## Methods (8)
- `Public Function AddSection(ByVal pISection As Section) As SectionParams` Adds a section.
  - param `pISection`: The data for the new section.
  - returns: Contains the key (AbsId) of the new section.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Section oSec = (SAPbobsCOM.Section)oSectionSrv.GetDataInterface(SectionsServiceDataInterfaces.ssSection);

    oSec.Code = "192J";
    oSec.Description = "HUM";
    oSec.ECode = "92J";
    oSectionSrv.AddSection(oSec);
    ```
- `Public Sub DeleteSection(ByVal pISectionParams As SectionParams)` Deletes an existing section. The section is specified by its key (AbsId), which is contained in the SectionParams object passed to the method.
  - param `pISectionParams`: The key of the section to be deleted.
  - remarks: You cannot delete a section that is associated with a withholding tax code (WithholdingTaxCodes) or certificate series (CertificateSeries).
  - C# example (from SAP's help):
    ```csharp
    try
    {
         SAPbobsCOM.SectionParams oSecPara = (SAPbobsCOM.SectionParams)oSectionSrv.GetDataInterface(SectionsServiceDataInterfaces.ssSectionParams);
         oSecPara.AbsEntry = 10;
         oSectionSrv.DeleteSection(oSecPara);
    }
    catch (Exception ex)
    {
         Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SectionsServiceDataInterfaces) As Object` Creates an empty data structure for use with the SectionsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `SectionsServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetSection(ByVal pISectionParams As SectionParams) As Section` Retrieves a section. The section is specified by its key (AbsId), which is contained in the SectionParams object passed to the method.
  - param `pISectionParams`: The key of the section to retrieve.
  - returns: The section with the specified key.
- `Public Function GetSectionList() As SectionsParams` Retrieves the keys and codes of all the sections.
  - C# example (from SAP's help):
    ```csharp
    SectionsParams oSecList = oSectionSrv.GetSectionList();

    String result = "";
    foreach (SAPbobsCOM.SectionParams oItem in oSecList)
    {
        result += oItem.AbsEntry + " " + oItem.Code + " " + oItem.Description + "\n";
    }

    Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)0, null);
    ```
- `Public Sub UpdateSection(ByVal pISection As Section)` Updates an existing section. The data for the section, including the key of the section to be updated, is contained in the Section passed to the method. To update a section, you must first retrieve it using the GetSection method.
  - param `pISection`: The data for the section to be updated. The Section object must contain the key of the object to be updated.
  - remarks: If the section is associated with a withholding tax code (WithholdingTaxCodes) or certificate series (CertificateSeries), you cannot update the Code and ECode properties.
  - C# example (from SAP's help):
    ```csharp
    try
    {
        SAPbobsCOM.SectionParams oSecPara = (SAPbobsCOM.SectionParams)oSectionSrv.GetDataInterface(SectionsServiceDataInterfaces.ssSectionParams);

        oSecPara.AbsEntry = 10;
        SAPbobsCOM.Section oSec = oSectionSrv.GetSection(oSecPara);
        oSec.ECode = "09J";
        oSec.Description = "Human";
        oSectionSrv.UpdateSection(oSec);
    }
    catch (Exception ex)
    {
        Interaction.MsgBox(ex.Message, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    }
    ```

# SensitiveDataAccess (Object)

SensitiveDataAccess Class

## Properties (8)
- `Public Property Key1() As String` [R/W] property Key1
- `Public Property Key2() As String` [R/W] property Key2
- `Public Property Key3() As String` [R/W] property Key3
- `Public Property Key4() As String` [R/W] property Key4
- `Public Property PropertyID() As Long` [R/W] property PropertyID
- `Public Property PropertyName() As String` [R/W] property PropertyName
- `Public Property PropertyValue() As String` [R/W] property PropertyValue
- `Public Property Table() As String` [R/W] property Table

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# SensitiveDataAccessService (Object)

SensitiveDataAccessService Class

## Methods (5)
- `Public Function Access(ByVal pISensitiveDataAccess As SensitiveDataAccess) As SensitiveDataAccess` Access
  - param `pISensitiveDataAccess`: 
- `Public Function GetDataInterface(ByVal enumMSDI As SensitiveDataAccessServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `SensitiveDataAccessServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function IsDataSensitive(ByVal pISensitiveDataAccess As SensitiveDataAccess) As DataSensitiveStatus` IsDataSensitive
  - param `pISensitiveDataAccess`: 

# SerialNumberDetail (Object)

The serial number details for the item. Source table: OSRN, OITL, ITL1.

## Properties (15)
- `Public Property AdmissionDate() As Date` [R/W] The creation date of the serial number. Field name: InDate.
- `Public Property Details() As String` [R/W] Specify any free text regarding serial numbers. Field name: Notes. Length: 16 characters.
- `Public Property DocEntry() As Long` [R] The document entry key that identifies the serial number detail. Field name: DocEntry.
- `Public Property ExpirationDate() As Date` [R/W] The expiry date of the serial number. Field name: ExpDate.
- `Public Property ItemCode() As String` [R] The number of the item. Field name: ItemCode. Length: 20 characters.
- `Public Property ItemDescription() As String` [R] The description of the item.
- `Public Property Location() As String` [R/W] The location of the item in the warehouse. Field name: Location. Length: 100 characters.
- `Public Property LotNumber() As String` [R/W] The lot number, in case a serial number is a part of the lot. Field name: LotNumber. Length: 36 characters.
- `Public Property ManufacturingDate() As Date` [R/W] The date on which the item was manufactured. Field name: MnfDate.
- `Public Property MfrSerialNo() As String` [R/W] The manufacturer serial number. Field name: MnfSerial. Length: 36 characters.
- `Public Property MFrWarrantyEnd() As Date` [R/W] The end of the warranty dates for the serial numbers, if a manufacturer warranty exists. Field name: GrntExp.
- `Public Property MfrWarrantyStart() As Date` [R/W] The start of the warranty dates for the serial numbers, if a manufacturer warranty exists. Field name: GrntStart.
- `Public Property SerialNumber() As String` [R/W] The serial number.
- `Public Property SystemNumber() As Long` [R] The system number of the item. Field name: SysNumber.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SerialNumberDetailParams (Object)

Holds the key to the serial details for the item. This object is used to pass keys to and retrieve keys from SerialNumberDetailsService methods.

## Properties (1)
- `Public Property DocEntry() As Long` [R/W] The document entry key that identifies the serial number detail. Field name: DocEntry.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SerialNumberDetailsService (Object)

The SerialNumberDetailsService service enables you to look up and update serial number details for the item. Source table: OSRN, OITL, ITL1.

**Remarks:** To access the Serial Number Details window, from the SAP Business One Main Menu, choose Inventory --> Item Management --> Serial Numbers --> Serial Number Details.

## Methods (5)
- `Public Function Get(ByVal pISerialNumberDetailParams As SerialNumberDetailParams) As SerialNumberDetail` Retrieves the serial details for the item. The serial details is specified by its key, which is contained in the SerialNumberDetailParams object passed to the method.
  - param `pISerialNumberDetailParams`: The key of the serial details to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As SerialNumberDetailsServiceDataInterfaces) As Object` Creates an empty data structure for use with the SerialNumberDetailsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `SerialNumberDetailsServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Sub Update(ByVal pISerialNumberDetail As SerialNumberDetail)` Updates the serial details for the item.
  - param `pISerialNumberDetail`: The data for the serial details to be updated. The SerialNumberDetail object must contain the key of the object to be updated.

# SerialNumbers (Object)

SerialNumbers is a business object that represents the serial numbers and additional tracking information of items. This object is part of the Inventory and Production module. Source table: OSRN, OSRW, OSRQ, OITL, ITL1.

**Remarks:** This object helps you to track items using their serial number. A computer, for example, can be located by its serial number. The serial number can provide additional information regarding a specific item such as its manufacturing date, warranty data, location in warehouse, and so on. To display the form in the application: - Select Inventory --> Item Management --> Serial Number --> Serial Numbers Management. - Set your selection criteria and click OK. (The form will appear only if Serial Numbers are defined for the selected items.) To de-allocate batches without actually remove them from stock (based Delivery), update SO so that it has no batches defined - it works this way in the UI and should work in DI the same - if not it should be fixed. Please note that batches allocated by Reserve Invoice canNOT be deallocated this way since we do not support Reserve Invoice updating. Batches allocated by Reserve Invoice can only be drawn to the Delivery/Invoice.

## Properties (18)
- `Public Property BaseLineNumber() As Long` [R/W] Sets or returns the Row No. in thhDocument. Field name: BaseLinNum.
  - remarks: Sets or returns the row number in the current document.
- `Public Property BatchID() As String` [R/W] Sets or returns the unique batch number of an item. Field name: BatchId. Length: 32 characters. This is a foreign key to the SerialNumbers object.
- `Public Property Count() As Long` [R] Returns the total data rows in the SerialNumbers object.
  - remarks: When you add a data row, the Count value is incremented automatically.
- `Public Property ExpiryDate() As Date` [R/W] Sets or returns the expiration date for the item. Field name: ExpDate.
- `Public Property InternalSerialNumber() As String` [R/W] Sets or returns the internal serial number for the item. Field name: IntrSerial. Length: 32 characters. This is a foreign key to the SerialNumbers object.
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property Location() As String` [R/W] Sets or returns the location of the item, for example, in the warehouse. Field name: Located. Length: 100 characters.
- `Public Property ManufactureDate() As Date` [R/W] Sets or returns the manufacturing date for the batch. Field name: PrdDate.
- `Public Property ManufacturerSerialNumber() As String` [R/W] Sets or returns the manufacturer's serial number for the selected item. Field name: SuppSerial. Length: 32 characters. This is a foreign key to the SerialNumbers object.
- `Public Property Notes() As String` [R/W] Sets or returns a memo type string that specifies comments for the item. Field name: Notes. Length: 64,000 characters.
- `Public Property Quantity() As Double` [R/W] The total number of serial numbers for the item. Field name: Quantity.
- `Public Property ReceptionDate() As Date` [R/W] Sets or returns the reception date. Field name: InDate.
- `Public Property SystemSerialNumber() As Long` [R/W] Sets or returns the successive numerator starting from1 issued for each item with serial numbers management. This numerator progresses according to the creation of new units of the same sort (for the same item). This property is mandatory when using Serial Numbers for outgoing documents. Field name: SysSerial. This is a foreign key to the SerialNumbers object.
  - remarks: Using System Serial Number - This property is mandatory when using existing serial numbers through the DI API. - When you set this property it means that you want to use an existing serial number. If the system serial number does not exist, any action will fail. - When you do not set this properyt (empty) it means that you want to create a new serial number. You cannot provide a system number of your choice to create a new serial number.
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WarrantyEnd() As Date` [R/W] Sets or returns the warranty end date for the items. Field name: GrntExp.
- `Public Property WarrantyStart() As Date` [R/W] Sets or returns the warranty start date for the items. Field name: GrntStart.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Series (Object)

Series is a data structure related to the SeriesService. It represents the series object, a part of a document name. Source table: NNM1 (Documents Numbering - Series).

## Properties (27)
- `Public Property ATDocumentType() As String` [R/W] property ATDocumentType
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property CostAccountOnly() As BoYesNoEnum` [R/W] property CostAccountOnly
- `Public Property DigitNumber() As Long` [R/W] property DigitNumber
- `Public Property Document() As String` [R/W] Sets or returns Document name. Field name: ObjectCode. Length: 20 characters.
- `Public Property DocumentSubType() As String` [R/W] Sets or returns the document sub-type, part of the document name. Field name: DocSubType.
- `Public Property GroupCode() As BoSeriesGroupEnum` [R/W] Sets or returns a Group Code for current series. Field name: GroupCode.
- `Public Property InitialNumber() As Long` [R/W] Sets or returns Initial Number of current Series. Field name: InitialNum.
- `Public Property InvoiceType() As Long` [R/W] property InvoiceType
- `Public Property InvoiceTypeOfNegativeInvoice() As Long` [R/W] property InvoiceTypeOfNegativeInvoice
- `Public Property IsDigitalSeries() As BoYesNoEnum` [R/W] property IsDigitalSeries
- `Public Property IsElectronicCommEnabled() As BoYesNoEnum` [R/W] property IsElectronicCommEnabled
- `Public Property IsManual() As BoYesNoEnum` [R] property IsManual
- `Public Property LastNumber() As Long` [R/W] Sets or returns the last number allowed for current Series. Field name: LastNum.
- `Public Property Locked() As BoYesNoEnum` [R/W] Determines whether or not the current series is locked. Field name: Locked.
- `Public Property Name() As String` [R/W] Sets or returns current Series name. Field name: SeriesName. Length:8 characters.
- `Public Property NextNumber() As Long` [R/W] Sets or returns the next number to be used from current series. Field name: NextNumber.
- `Public Property PeriodIndicator() As String` [R/W] Sets or returns the period indicator. Field name: Indicator. This is a foreign key to the Period Indicators table OPID, which is not exposed through the DI API. Length: 10 characters.
- `Public Property PortugalSeriesAction() As String` [R/W] Field name: Action. Length: 1 Characters. R - Report C - Cancel F - Finalize
- `Public Property PortugalSeriesPhase() As String` [R] Field name: Phase. Length: 1 Characters. T - To Be Processed I - In Process O - OK E - Error
- `Public Property PortugalSeriesStatus() As String` [R] Field name: Status. Length: 1 Characters. R - Reported C - Canceled F - Finalized
- `Public Property Prefix() As String` [R/W] Sets or returns the folio prefix string of this series. Field name: BeginStr. Length: 2 Characters.
- `Public Property Remarks() As String` [R/W] Sets or returns remarks regarding current series. Field name: Remark. Length: 50 Characters.
- `Public Property Series() As Long` [R] Returns current Series value. Field name: Series.
- `Public Property SeriesType() As BoSeriesTypeEnum` [R/W] property SeriesType
- `Public Property Suffix() As String` [R/W] Sets or returns the suffix string of this series. Field name: EndStr. Length: 8 Characters.
- `Public Property UserFields() As Fields` [R] Get User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# SeriesCollection (Collection)

SeriesCollection is a data collection of Series data structures. Source table: NNM1 (Documents Numbering - Series).

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of Series data structures in the SeriesCollection.

## Methods (5)
- `Public Function Add() As Series` Adds a new Series to the SeriesCollection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As Series` Returns a Series data structures from the SeriesCollection.
  - param `vtIndex`: Specifies the index of the Series that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# SeriesLine (Object)

Contains the details of a certificate series. Source table: CSN1

**Remarks:** For India only. Mandatory properties: FirstNum

## Properties (5)
- `Public Property FirstNum() As Long` [R/W] First number in the series. Field name: InitialNum
  - remarks: Must be a number.
- `Public Property LastNum() As Long` [R/W] Last number in the series. Field name: LastNum
  - remarks: Must be a number no less than the FirstNum property.
- `Public Property NextNum() As Long` [R] Next number in the series. Field name: NextNum
  - remarks: Must be a number.
- `Public Property Prefix() As String` [R/W] A prefix for all document numbers from the series. Field name: BeginStr
- `Public Property Series() As Long` [R] The ID for the series.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SeriesLines (Collection)

A collection of SeriesLine objects. Currently, a certificate series can have only one series line in its SeriesLines property.

**Remarks:** For India only.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As SeriesLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As SeriesLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# SeriesParams (Object)

The SeriesParams specifies an identification key (Series) for which the SeriesService is related.

## Properties (1)
- `Public Property Series() As Long` [R/W] Sets or returns the Series object, part of the document name.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure. Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# SeriesService (Object)

SeriesService manages the Series object, a component of the document numbering system. Source table: NNM1 (Documents Numbering - Series).

**Remarks:** See the documentation for the SeriesService methods for more code samples. In general, to use a DI service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or - You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method.

## Methods (22)
- `Public Function AddElectronicSeries(ByVal pIElectronicSeries As ElectronicSeries) As ElectronicSeriesParams` AddElectronicSeries
  - param `pIElectronicSeries`: 
- `Public Function AddSeries(ByVal pISeries As Series) As SeriesParams` Adds a new Series to the series Service and returns the SeriesParams identification key.
  - param `pISeries`: Specifies the Series you want to add.
- `Public Sub AttachSeriesToDocument(ByVal pIDocumentSeriesParams As DocumentSeriesParams)` Attach a Series to a document, both defined by a DocumentSeriesParams.
  - param `pIDocumentSeriesParams`: The DocumentSeriesParams that identifies the Series and the document.
  - example note: The following is a VB.NET sample related to the the Belgium localization, which is different than other localizations. It shows how to add a series, attach it to a document and set it as the default series.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    Dim oDocSeriesParam As DocumentSeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'create a new series data structure

    oSeries = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeries)

    'set series name

    oSeries.Name = "Series1"

    'set the period indicator

    oSeries.PeriodIndicator = "Default"

    'set the group code

    '(enum BoSeriesGroupEnum has all Group Enum)

    oSeries.GroupCode = 1

    'set the first number

    oSeries.InitialNumber = 300

    'set last number

    oSeries.LastNumber = 350

    'add new series

    oSeriesParams = oSeriesService.AddSeries(oSeries)

    'create a new DocumentSeriesParams data structure

    oDocSeriesParam = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentSeriesParams)

    'set document type(e.g. Deliveries=15)

    oDocSeriesParam.Document = "15"

    'set the series code

    oDocSeriesParam.Series = oSeriesParams.Series

    'attach Series to document

    Call oSeriesService.AttachSeriesToDocument(oDocSeriesParam)

    'set the series to be the default series for the specify document

    Call oSeriesService.SetDefaultSeriesForCurrentUser(oDocSeriesParam)
    ```
- `Public Sub ChangeDocumentMenuName(ByVal pIDocumentChangeMenuName As DocumentChangeMenuName)` Modifies the menu name for a specific document type/document subtype.
  - param `pIDocumentChangeMenuName`: A document type/document subtype and its new menu name.
  - C# example (from SAP's help):
    ```csharp
    Company oCompany = new SAPbobsCOM.Company();

        // ... specify some parameters for the company object

    int iRetCode = oCompany.Connect();
    CompanyService companyService = oCompany.GetCompanyService();

    SeriesService seriesService = (SeriesService)companyService.GetBusinessService(ServiceTypes.SeriesService);

    DocumentTypeParams documentTypeParams = (DocumentTypeParams)seriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentTypeParams);
    documentTypeParams.Document = "10000105";
    documentTypeParams.DocumentSubType = "--";

    DocumentChangeMenuName documentChangeMenuName = seriesService.GetDocumentChangedMenuName(documentTypeParams);
    documentChangeMenuName.ChangedMenuName = "My New Name";

    seriesService.ChangeDocumentMenuName(documentChangeMenuName);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As SeriesServiceDataInterfaces) As Object` Creates an empty data structure.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `SeriesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - example note: Shows how to get a Series from an XML file.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    Dim oSeriesFromFile As Series

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 5

    'get the series

    oSeries = oSeriesService.GetSeries(oSeriesParams)

    'save series to file

    oSeries.ToXMLFile("c:\MySeries.xml")

    'create a new series data structure and fill it with the data from

    'the xml file

    oSeriesFromFile = oSeriesService.GetDataInterfaceFromXMLFile("c:\MySeries.xml")
    ```
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Get the data interface from an XML String.
  - param `bstrXMLString`: Specifies the XML string.
  - example note: Shows how to get a Series from an XML string.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    Dim oSeriesFromStr As Series

    Dim sSeriesXmlString As String

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 5

    'get the series

    oSeries = oSeriesService.GetSeries(oSeriesParams)

    'save series to string

    sSeriesXmlString = oSeries.ToXMLString()

    'create a new series data structure and fill it with the data from

    'the xml file

    oSeriesFromStr = oSeriesService.GetDataInterfaceFromXMLString(sSeriesXmlString)
    ```
- `Public Function GetDefaultElectronicSeries(ByVal pISeriesParams As SeriesParams) As ElectronicSeriesParams` GetDefaultElectronicSeries
  - param `pISeriesParams`: 
- `Public Function GetDefaultSeries(ByVal pIDocumentTypeParams As DocumentTypeParams) As Series` Return the default Series object for a document identified by its DocumentTypeParams.
  - param `pIDocumentTypeParams`: Specified by the DocumentTypeParams identification key.
  - example note: The following is a VB.NET sample that retrieves the default series of a specified document type.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oDocumentTypeParams As DocumentTypeParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get new series

    oSeries = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeries)

    'get DocumentTypeParams for filling the document type

    oDocumentTypeParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentTypeParams)

    'set the document type (e.g. A/R Invoice=13)

    oDocumentTypeParams.Document = 13

    'get the default series of the SaleOrder documentset the document type

    oSeries = oSeriesService.GetDefaultSeries(oDocumentTypeParams)

    'print the default series name

    Debug.WriteLine(oSeries.Name)

    'print the first number of the series

    Debug.WriteLine(oSeries.InitialNumber)
    ```
- `Public Function GetDocumentChangedMenuName(ByVal pIDocumentTypeParams As DocumentTypeParams) As DocumentChangeMenuName` Retrieves the DocumentChangeMenuName object for modifying the menu name for a specific document type/document subtype.
  - param `pIDocumentTypeParams`: The document type/document subtype for which you want to change the menu name
- `Public Function GetDocumentSeries(ByVal pIDocumentTypeParams As DocumentTypeParams) As SeriesCollection` Returns the SeriesCollection of all the Series that match a document identified by its DocumentTypeParams.
  - param `pIDocumentTypeParams`: Specified by the DocumentTypeParams identification key.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeriesCollection As SeriesCollection

    Dim oSeries As Series

    Dim oDocumentTypeParams As DocumentTypeParams

    Dim i As Integer

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series collection

    oSeriesCollection =     oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesCollection)

    'get Document Type Params

    oDocumentTypeParams =     oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentTypeParams)

    'set the document type

    '(e.g. SaleInvoice=13 , BoObjectTypes has all document types)

    oDocumentTypeParams.Document = 13

    'get series collection

    oSeriesCollection = oSeriesService.GetDocumentSeries(oDocumentTypeParams)

    For i = 0 To oSeriesCollection.Count - 1

        'print the series name

        Debug.WriteLine(oSeries.Name)

        'print the series first number

        Debug.WriteLine(oSeries.InitialNumber)

    Next
    ```
- `Public Function GetElectronicSeries(ByVal pElectronicSeriesParams As ElectronicSeriesParams) As ElectronicSeries` GetElectronicSeries
  - param `pElectronicSeriesParams`: 
- `Public Function GetSeries(ByVal pSeriesParams As SeriesParams) As Series` Returns a Series object identified by its SeriesParams.
  - param `pSeriesParams`: The SeriesParams identification key of the Series you want to get.
  - example note: The following is a VB.NET sample that retrieves the series by its parameters.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 84

    'get the series

    oSeries = oSeriesService.GetSeries(oSeriesParams)

    'print the series name

    Debug.WriteLine(oSeries.Name)
    ```
- `Public Sub RemoveElectronicSeries(ByVal pIElectronicSeriesParam As ElectronicSeriesParams)` RemoveElectronicSeries
  - param `pIElectronicSeriesParam`: 
- `Public Sub RemoveSeries(ByVal pISeriesParam As SeriesParams)` Removes a Series identified by its SeriesParams.
  - param `pISeriesParam`: The SeriesParams identification key of the Series that you want to remove.
  - example note: Remove a Series
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeriesParams As SeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 29

    'remove series

    oSeriesService.RemoveSeries(oSeriesParams)
    ```
- `Public Sub SetDefaultElectronicSeries(ByVal pIDefaultElectronicSeriesParams As DefaultElectronicSeriesParams)` SetDefaultElectronicSeries
  - param `pIDefaultElectronicSeriesParams`: 
- `Public Sub SetDefaultSeriesForAllUsers(ByVal pIDocumentSeriesParams As DocumentSeriesParams)` Set a Series, identified by its DocumentTypeParams, as a default Series for all users.
  - param `pIDocumentSeriesParams`: The DocumentSeriesParams that defines the document type and series number.
  - example note: Description: shows how to set a default Series for all the users.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oDocumentSeriesParams As DocumentSeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oDocumentSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentSeriesParams)

    ''set doument type(e.g. Deliveries=15)

    oDocumentSeriesParams.Document = 15

    'set the number of an existing series

    oDocumentSeriesParams.Series = 28

    'set default series

    oSeriesService.SetDefaultSeriesForAllUsers(oDocumentSeriesParams)
    ```
- `Public Sub SetDefaultSeriesForCurrentUser(ByVal pIDocumentSeriesParams As DocumentSeriesParams)` Set a Series, identified by its DocumentTypeParams, as a default Series for current user.
  - param `pIDocumentSeriesParams`: The DocumentSeriesParams that defines the document type and series number.
  - example note: Shows how to set a default Series for a current user.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oDocumentSeriesParams As DocumentSeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oDocumentSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentSeriesParams)

    'set doument type(e.g. Deliveries=15)

    oDocumentSeriesParams.Document = 15

    'set the number of an existing series

    oDocumentSeriesParams.Series = 28

    'set default series

    oSeriesService.SetDefaultSeriesForCurrentUser(oDocumentSeriesParams)
    ```
- `Public Sub SetDefaultSeriesForUser(ByVal pIDocumentSeriesUserParams As DocumentSeriesUserParams)` Set a default Series for a specific user where the user Id, Series number and the document type are defined by DocumentSeriesUserParams.
  - param `pIDocumentSeriesUserParams`: Specifies the DocumentSeriesUserParams identification key.
- `Public Sub UnattachSeriesFromDocument(ByVal pIDocumentSeriesParams As DocumentSeriesParams)` Disconnect a Series from a document where the Series and the document are identified by DocumentSeriesParams.
  - param `pIDocumentSeriesParams`: Specifies the DocumentSeriesParams identification key that defines both series and document that you want to separate.
  - example note: Shows how to unattach a Series from a document (related only to the the Belgium localization)
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oDocumentSeriesParams As DocumentSeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oDocumentSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiDocumentSeriesParams)

    'set the number of an existing series

    oDocumentSeriesParams.Series = 7

    'set doument type(e.g. Deliveries=15)

    oDocumentSeriesParams.Document = 15

    'unattach the series from the document

    oSeriesService.UnattachSeriesFromDocument(oDocumentSeriesParams)
    ```
- `Public Sub UpdateElectronicSeries(ByVal pIElectronicSeries As ElectronicSeries)` UpdateElectronicSeries
  - param `pIElectronicSeries`: 
- `Public Sub UpdateSeries(ByVal pISeries As Series)` Replace a Series by another Series.
  - param `pISeries`: Specifies the Series that will replace the current series.
  - example note: Description: shows how to update a Series.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oCmpSrv As SAPbobsCOM.CompanyService

    Dim oSeriesService As SAPbobsCOM.SeriesService

    Dim oSeries As Series

    Dim oSeriesParams As SeriesParams

    'get company service

    oCmpSrv = oCompany.GetCompanyService

    'get series service

    oSeriesService = oCmpSrv.GetBusinessService(ServiceTypes.SeriesService)

    'get series params

    oSeriesParams = oSeriesService.GetDataInterface(SeriesServiceDataInterfaces.ssdiSeriesParams)

    'set the number of an existing series

    oSeriesParams.Series = 28

    'get the series

    oSeries = oSeriesService.GetSeries(oSeriesParams)

    'set the series name

    oSeries.Name = "MySeries"

    'update series

    oSeriesService.UpdateSeries(oSeries)
    ```

# ServiceAppReport (Object)

ServiceAppReport Class

## Properties (4)
- `Public Property Code() As Long` [R] property Code
- `Public Property CustomizedReportName() As String` [R/W] property CustomizedReportName
- `Public Property ReportChoice() As MobileAppReportChoiceEnum` [R/W] property ReportChoice
- `Public Property SystemReportName() As String` [R/W] property SystemReportName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ServiceAppReportContent (Object)

ServiceAppReportContent Class

## Properties (1)
- `Public Property ReportContent() As String` [R/W] property ReportContent

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ServiceAppReportParams (Object)

ServiceAppReportParams Class

## Properties (2)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property ReportChoice() As MobileAppReportChoiceEnum` [R/W] property ReportChoice

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# ServiceCallActivities (Object)

ServiceCallActivities is a child object of the ServiceCalls object in the Service module. The service call activities are associated with the Activities with Business Partners table. Source table: SCL5.

**Remarks:** Mandatory field in SAP Business One: ActivityCode. To display the form in the application: - Select Service --> Service Call. - Select the Activities tab.

## Properties (4)
- `Public Property ActivityCode() As Long` [R/W] Sets or returns the activity code. Mandatory property. Field name: ClgID. This is a foreign key to the Contacts object.
- `Public Property Count() As Long` [R] Returns the total rows in the activities table.
- `Public Property LineNum() As Long` [R] Returns the current row number. Field name: Line.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - remarks: You cannot delete a line if the service call is closed.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.ServiceCalls oSrvCall;

    // Delete service call activity
    if(oSrvCall.GetByKey(1) == true)
    {
        oSrvCall.Activities.SetCurrentLine(1);
        oSrvCall.Activities.Delete();
        oSrvCall.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
