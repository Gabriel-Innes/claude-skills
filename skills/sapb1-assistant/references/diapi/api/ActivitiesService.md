<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ActivitiesService (Object)

The ActivitiesService service enables you to add, look up, remove, and update single activities and recurring activities. Source table: OCLG.

**Remarks:** To display the form in the application, choose Business Partners --> Activities.

## Methods (13)
- `Public Function AddActivity(ByVal pIActivity As Activity) As ActivityParams` Adds a new activity.
  - param `pIActivity`: The data for the new activity.
  - C# example (from SAP's help):
    ```csharp
    ActivitiesService oActSrv = (ActivitiesService)oCmpSrv.GetBusinessService(ServiceTypes.ActivitiesService);
    Activity oAct = (Activity)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivity);
    ActivityParams oParams;
    oAct.CardCode = "C001";
    oAct.ContactDate = DateTime.Parse("15/01/2010");
    oAct.Activity = BoActivities.cn_Conversation;
    oAct.Notes = "Discuss next year's financial plan";
    oParams = oActSrv.AddActivity(oAct);
    long singleActCode = oParams.ActivityCode;
    ```
  - C# example (from SAP's help):
    ```csharp
    oAct = (Activity)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivity);
    oAct.CardCode = "C002";
    oAct.ContactDate = DateTime.Parse("16/01/2010");
    oAct.Activity = BoActivities.cn_Meeting;
    oAct.Notes = "Monthly team meeting";
    oAct.StartDate = DateTime.Parse("18/02/2010");
    oAct.StartTime = DateTime.Parse("16:30:00");
    oAct.EndDate = DateTime.Parse("18/12/2010");
    oAct.EndTime = DateTime.Parse("17:30:00");
    oAct.RecurrencePattern = RecurrencePatternEnum.rpMonthly;
    oAct.EndType = EndTypeEnum.etByCounter;
    oAct.MaxOccurrence = 10;
    oAct.Interval = 1;
    oAct.RepeatOption = RepeatOptionEnum.roByDate;
    oParams = oActSrv.AddActivity(oAct);
    long seriesActCode = oParams.ActivityCode;
    ```
- `Public Sub DeleteActivity(ByVal pIActivityParams As ActivityParams)` Deletes an existing activity.
  - param `pIActivityParams`: The key of the activity to be deleted.
- `Public Sub DeleteSingleInstanceFromSeries(ByVal pIActivityInstanceParams As ActivityInstanceParams)` Deletes a single instance from an existing recurring activity series.
  - param `pIActivityInstanceParams`: The key of the activity instance to be deleted.
  - C# example (from SAP's help):
    ```csharp
    oInstanceParams.ActivityCode = seriesActCode;
    oInstanceParams.InstanceDate = DateTime.Parse("18/04/2010");
    oActSrv.DeleteSingleInstanceFromSeries(oParams);
    ```
- `Public Function GetActivity(ByVal pIActivityParams As ActivityParams) As Activity` Retrieves an activity. The activity is specified by its key, which is contained in the ActivityParams object passed to the method.
  - param `pIActivityParams`: The key of the activity to retrieve.
- `Public Function GetActivityList() As ActivitiesParams` Returns the ActivitiesParams data collection that identify all activities.
- `Public Function GetDataInterface(ByVal enumMSDI As ActivitiesServiceDataInterfaces) As Object` Creates an empty data structure for use with the ActivitiesService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/ActivitiesServiceDataInterfaces.md`
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
- `Public Function GetListByAttendUser(ByVal pIActivity As Activity) As ActivitiesParams` GetListByAttendUser
  - param `pIActivity`: 
- `Public Function GetSingleInstanceFromSeries(ByVal pIActivityInstanceParams As ActivityInstanceParams) As Activity` Retrieves a single instance from a recurring activity series. The activity instance is specified by its key, which is contained in the ActivityInstanceParams object passed to the method.
  - param `pIActivityInstanceParams`: The key of the activity instance to retrieve.
- `Public Function GetTopNActivityInstances(ByVal pActivityInstancesListParams As ActivityInstancesListParams) As ActivityInstancesParams` Retrieves the top N activity instances.
  - param `pActivityInstancesListParams`: The key of the activity instance list to retrieve.
- `Public Sub UpdateActivity(ByVal pIActivity As Activity)` Updates an existing activity. The data for the activity, including the key of the activity to be updated, is contained in the Activity object passed to the method. To update an activity, you must first retrieve it using the GetActivity method.
  - param `pIActivity`: The data for the activity to be updated. The Activity object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    //Get a single activity or a modified activity from a series
    oParams = (ActivityParams)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivityParams);
    oParams.ActivityCode = singleActCode;
    Activity oGet = oActSrv.GetActivity(oParams);
    oGet.Notes = "Discuss next year's financial plan and training plan";

    //update a single activity, or an already modified activity from a series
    oActSrv.UpdateActivity(oGet);
    ```
  - C# example (from SAP's help):
    ```csharp
    //Get an activity series
    oParams = (ActivityParams)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivityParams);
    oParams.ActivityCode = seriesActCode;
    oGet = oActSrv.GetActivity(oParams);
    oGet.StartTime = DateTime.Parse("16:00:00");

    //Update the whole series
    oActSrv.UpdateActivity(oGet);
    ```
- `Public Function UpdateSingleInstanceInSeries(ByVal pIActivity As Activity) As ActivityParams` Updates an existing single instance from a recurring activity series. The data for the activity, including the key of the activity to be updated, is contained in the Activity object passed to the method. To update an activity instance, you must first retrieve it using the GetSingleInstanceFromSeries method.
  - param `pIActivity`: The data for the single activity instance to be updated. The Activity object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    //Get a single instance from a series
    ActivityInstancesParams oInstanceParams = (ActivityInstancesParams)oActSrv.GetDataInterface(ActivitiesServiceDataInterfaces.asActivityInstancesParams);
    oInstanceParams.ActivityCode = seriesActCode;
    oInstanceParams.InstanceDate = DateTime.Parse("18/03/2010");
    oGet = oActSrv.GetSingleInstanceFromSeries(oParams);
    oGet.StartTime = DateTime.Parse("15:30:00");

    //Update a single activity from a series
    oActSrv.UpdateSingleInstanceInSeries(oGet);
    ```
