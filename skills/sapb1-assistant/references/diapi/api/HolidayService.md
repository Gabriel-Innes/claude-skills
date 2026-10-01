<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# HolidayService (Object)

The HolidayService service enables you to add, look up, remove, and update holidays. Source table: OHLD.

## Methods (8)
- `Public Function AddHoliday(ByVal pIHoliday As Holiday) As HolidayParams` Adds a new holiday.
  - param `pIHoliday`: The data for the new holiday.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Holiday hd1 = holidayService.GetDataInterface(SAPbobsCOM.HolidayServiceDataInterfaces.hsHoliday);
    hd1.HolidayCode = "holiday1";
    hd1.WeekendFrom = SAPbobsCOM.BoWeekEnum.Sunday;
    hd1.WeekendTO = SAPbobsCOM.BoWeekEnum.Monday;
    hd1.ValidForOneYearOnly = SAPbobsCOM.BoYesNoEnum.tNO;
    hd1.SetWeekendsAsWorkDays = "Y";
    hd1.WeekNoRule = SAPbobsCOM.BoWeekNoRuleEnum.fromFirstFourDayWeek;

    SAPbobsCOM.HolidayDate hdDate = hd1.HolidayDates.Add();
    hdDate.StartDate = new DateTime(2020, 10, 1);
    hdDate.EndDate = new DateTime(2020, 10, 6);
    hdDate.Remarks = "holiday1";
    try
    {
        SAPbobsCOM.HolidayParams hdParams1 = holidayService.AddHoliday(hd1);
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
    ```
- `Public Sub DeleteHoliday(ByVal pIHolidayParams As HolidayParams)` Deletes an existing holiday.
  - param `pIHolidayParams`: The key of the holiday to be deleted.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.HolidayParams hdParams2 = holidayService.GetDataInterface(HolidayServiceDataInterfaces.hsHolidayParams);
    hdParams2.HolidayCode = "holiday1";

    try
    {
        holidayService.DeleteHoliday(hdParams2);
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As HolidayServiceDataInterfaces) As Object` Creates an empty data structure for use with the HolidayService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `../enums/HolidayServiceDataInterfaces.md`
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
- `Public Function GetHoliday(ByVal pIHolidayParams As HolidayParams) As Holiday` Retrieves a holiday. The holiday is specified by its key, which is contained in the HolidayParams object passed to the method.
  - param `pIHolidayParams`: The key of the holiday to retrieve.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.HolidayParams hdParam = holidayService.GetDataInterface(SAPbobsCOM.HolidayServiceDataInterfaces.hsHolidayParams);
    hdParam.HolidayCode = "2007 Feiertage";
    SAPbobsCOM.Holiday hd = holidayService.GetHoliday(hdParam);
    Console.WriteLine(hd.HolidayCode);
    Console.WriteLine(hd.WeekendFrom);
    Console.WriteLine(hd.WeekendTO);
    Console.WriteLine(hd.ValidForOneYearOnly);
    Console.WriteLine(hd.SetWeekendsAsWorkDays);
    Console.WriteLine(hd.WeekNoRule);
    for (int i = 0; i < hd.HolidayDates.Count; i++)
    {
        Console.WriteLine(" " + hd.HolidayDates.Item(i).StartDate);
        Console.WriteLine(" " + hd.HolidayDates.Item(i).EndDate);
        Console.WriteLine(" " + hd.HolidayDates.Item(i).Remarks);
    }
    ```
- `Public Function GetHolidayList() As HolidaysParams` Returns the HolidaysParams data collection that identify all holidays.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CompanyService oCmpSrv = oCompany.GetCompanyService();
    SAPbobsCOM.HolidayService holidayService = oCmpSrv.GetBusinessService(SAPbobsCOM.ServiceTypes.HolidayService);
    SAPbobsCOM.HolidaysParams hdList = holidayService.GetHolidayList();
    for (int i = 0; i < hdList.Count; i++)
    {
        Console.WriteLine(hdList.Item(i).HolidayCode);
    }
    ```
- `Public Sub UpdateHoliday(ByVal pIHoliday As Holiday)` Updates an existing holiday. The data for the holiday, including the key of the holiday to be updated, is contained in the Holiday object passed to the method. To update a holiday, you must first retrieve it using the GetHoliday method.
  - param `pIHoliday`: The data for the holiday to be updated. The Holiday object must contain the key of the object to be updated.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.HolidayParams hdParams = holidayService.GetDataInterface(HolidayServiceDataInterfaces.hsHolidayParams);
    hdParams.HolidayCode = "holiday1";
    SAPbobsCOM.Holiday hd2 = holidayService.GetHoliday(hdParams);

    hd2.WeekNoRule = BoWeekNoRuleEnum.fromFirstFullWeek;

    int count = hd2.HolidayDates.Count;
    SAPbobsCOM.HolidayDate hdDate1 = hd2.HolidayDates.Item(0);
    hdDate1.Remarks = "new remarks";

    try
    {
        holidayService.UpdateHoliday(hd2);
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
    ```
