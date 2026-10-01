<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# InventoryCycles (Object)

The InventoryCycles object enables to setup cycles of inventory counts and order intervals. Inventory cycles setup enables to track inventory counts by issuing an alert each time a count is due. It also is used for planning the order intervals. Source table: OCYC.

**Remarks:** To display the form in the application: - Select Administration -->Setup -->Inventory -->Inventory Cycles. To display the Inventory Cycles Setup for order interval: - Select Inventory -->Item Master Data -->Planning Data tab. - From the Order Interval field, select Define New.

**Example:**
- C# example (from SAP's help):
  ```csharp
  AddInventoryCycleEnhancedIn90(oCompany, "CycleAnnualEnhancedIn90", BoFrequency.bof_Annually);
  AddInventoryCycle(oCompany, "CycleAnnual", BoFrequency.bof_Monthly, DateTime.Today);

  static void AddInventoryCycleEnhancedIn90(SAPbobsCOM.Company oCompany, string cycleName, BoFrequency frequecy)
  {
      InventoryCycles oCycle = (InventoryCycles)oCompany.GetBusinessObject(BoObjectTypes.oInventoryCycles);
      oCycle.CycleName       = cycleName;
      oCycle.Frequency       = frequecy;
      oCycle.RepeatOption    = RepeatOptionEnum.roByDate;
      oCycle.Interval        = 1;
      oCycle.Hour            = DateTime.Now;
      oCycle.endType         = EndTypeEnum.etByDate;
      oCycle.SeriesEndDate   = Convert.ToDateTime("2015-10-30");
      oCycle.RecurrenceMonth = 8;        // 1 ~ 12
      oCycle.RecurrenceDayInMonth = 20;  // 1 ~ 31
      oCycle.Add();
  }

  static void AddInventoryCycle(SAPbobsCOM.Company oCompany, string cycleName, BoFrequency frequecy, DateTime nextCountingDate)
  {
      InventoryCycles oCycle = (InventoryCycles)oCompany.GetBusinessObject(BoObjectTypes.oInventoryCycles);
      oCycle.CycleName = cycleName;
      oCycle.Frequency = frequecy;
      oCycle.Day       = 20;  // 1 ~ 31
      oCycle.Hour      = DateTime.Now;
      oCycle.Add();
  }
  ```

## Properties (24)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CycleCode() As Long` [R] Sets or returns the cycle code. Field name: Code.
- `Public Property CycleName() As String` [R/W] Sets or returns the inventory cycle name. Field name: Name. Length: 20 characters.
- `Public Property Day() As Long` [R/W] Sets or returns one of the following according to the valid value of the Frequency property: - Day of the week for weekly cycles (bof_Weekly). - Day of the month for monthly cycles (bof_Monthly). - Number of days for regular intervals, for example, every two days (bof_EveryXDays). Field name: Day.
  - remarks: To customize inventory cycles on a flexible and regular basis, use the new properties rather than the Day property in SAP Business One 9.0 and later versions.
- `Public Property endType() As EndTypeEnum` [R/W] Specifies how to stop the inventory cycle. Field name: EndType.
- `Public Property Frequency() As BoFrequency` [R/W] Sets or returns a valid value of the cycle interval. Field name: Frequency.
  - remarks: In the case of the bof_Weekly or bof_Every4Weeks valid values, you must set also the day of the week (RecurrenceDayOfWeek). In the case of the bof_Monthly valid value, you must set also the day of the month (RecurrenceDayInMonth). In the case of the bof_Quarterly, bof_HalfYearly, bof_Annually, or bof_OneTime valid values, you must set also the upcoming counting date (NextCountingDate).
- `Public Property Friday() As BoYesNoEnum` [R/W] Sets inventory cycle recurrence for Friday. Field name: Friday.
- `Public Property Hour() As Date` [R/W] Sets or returns the time for issuing an alert. Field name: Hour.
- `Public Property Interval() As Long` [R/W] The interval period. Field name: Interval.
- `Public Property MaxOccurrence() As Long` [R/W] The maximum number of times inventory cycles can occur. Field name: MaxOccur.
- `Public Property Monday() As BoYesNoEnum` [R/W] Sets inventory cycle recurrence for Monday. Field name: Monday.
- `Public Property NextCountingDate() As Date` [R/W] Sets or returns the date of the upcoming inventory cycle. Field name: NextDate.
  - remarks: Applicable in case the Frequency property is set to one of the following valid values: bof_Quarterly, bof_HalfYearly, bof_Annually, or bof_OneTime.
- `Public Property RecurrenceDayInMonth() As Long` [R/W] Schedules inventory cycles that run on a specific date each month. Field name: DayInMonth.
- `Public Property RecurrenceDayOfWeek() As RecurrenceDayOfWeekEnum` [R/W] Schedules inventory cycles that run on a specific day each week. Field name: DayOfWeek.
- `Public Property RecurrenceMonth() As Long` [R/W] Sets inventory cycle recurrence on a monthly basis. Field name: Month.
- `Public Property RecurrenceSequenceSpecifier() As RecurrenceSequenceSpecifierEnum` [R/W] Sets inventory cycle recurrence on a weekly basis. Field name: Week.
- `Public Property RepeatOption() As RepeatOptionEnum` [R/W] Determines how inventory cycles repeat at regular intervals. Field name: SubOption.
- `Public Property Saturday() As BoYesNoEnum` [R/W] Sets inventory cycle recurrence for Saturday. Field name: Saturday.
- `Public Property SeriesEndDate() As Date` [R/W] The end date of an inventory cycle series. Field name: SeEndDat.
- `Public Property Sunday() As BoYesNoEnum` [R/W] Sets inventory cycle recurrence for Sunday. Field name: Sunday.
- `Public Property Thursday() As BoYesNoEnum` [R/W] Sets inventory cycle recurrence for Thursday. Field name: Thursday.
- `Public Property Tuesday() As BoYesNoEnum` [R/W] Sets inventory cycle recurrence for Tuesday. Field name: Tuesday.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Wednesday() As BoYesNoEnum` [R/W] Sets inventory cycle recurrence for Wednesday. Field name: Wednesday.

## Methods (7)
- `Public Function Add() As Long` Adds a new inventory cycle.
  - remarks: Adds an inventory cycle.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: IndicatorCode.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Remove a inventory cycle .
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the inventory cycle to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates an existing inventory cycle .
