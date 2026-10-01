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

# InventoryOpeningBalance (Object)

InventoryOpeningBalance Class

## Properties (17)
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BranchID() As Long` [R/W] property BranchID
- `Public Property DocObjectCodeEx() As String` [R] property DocObjectCodeEx
- `Public Property DocumentDate() As Date` [R/W] property DocumentDate
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property DocumentNumber() As Long` [R] property DocumentNumber
- `Public Property FinancialPeriod() As Long` [R] property FinancialPeriod
- `Public Property InventoryOpeningBalanceLines() As InventoryOpeningBalanceLines` [R] property InventoryOpeningBalanceLines
- `Public Property JournalRemark() As String` [R/W] property JournalRemark
- `Public Property PeriodIndicator() As String` [R] property PeriodIndicator
- `Public Property PostingDate() As Date` [R/W] property PostingDate
- `Public Property PriceList() As Long` [R/W] property PriceList
- `Public Property PriceSource() As InventoryOpeningBalancePriceSourceEnum` [R/W] property PriceSource
- `Public Property Reference2() As String` [R/W] property Reference2
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property Series() As Long` [R/W] property Series
- `Public Property UserFields() As Fields` [R] Get User Fields

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

# InventoryOpeningBalanceBatchNumber (Object)

InventoryOpeningBalanceBatchNumber Class

## Properties (13)
- `Public Property AddmisionDate() As Date` [R/W] property AddmisionDate
- `Public Property BaseLineNumber() As Long` [R/W] property BaseLineNumber
- `Public Property BatchNumber() As String` [R/W] property BatchNumber
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property ExpiryDate() As Date` [R/W] property ExpiryDate
- `Public Property InternalSerialNumber() As String` [R/W] property InternalSerialNumber
- `Public Property Location() As String` [R/W] property Location
- `Public Property ManufactureDate() As Date` [R/W] property ManufactureDate
- `Public Property ManufacturerSerialNumber() As String` [R/W] property ManufacturerSerialNumber
- `Public Property Notes() As String` [R/W] property Notes
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine

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

# InventoryOpeningBalanceBatchNumbers (Collection)

InventoryOpeningBalanceBatchNumbers Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryOpeningBalanceBatchNumber` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryOpeningBalanceBatchNumber` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryOpeningBalanceCCDNumber (Object)

InventoryOpeningBalanceCCDNumber Class

## Properties (9)
- `Public Property BaseLineNumber() As Long` [R/W] property BaseLineNumber
- `Public Property CCDNumber() As String` [R/W] property CCDNumber
- `Public Property ChildNumber() As Long` [R/W] property ChildNumber
- `Public Property CountryOfOrigin() As String` [R/W] property CountryOfOrigin
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property SubLineNumber() As Long` [R/W] property SubLineNumber
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InventoryOpeningBalanceCCDNumbers (Collection)

InventoryOpeningBalanceCCDNumbers Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As InventoryOpeningBalanceCCDNumber` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As InventoryOpeningBalanceCCDNumber` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InventoryOpeningBalanceLine (Object)

InventoryOpeningBalanceLine Class

## Properties (32)
- `Public Property ActualPrice() As Double` [R] property ActualPrice
- `Public Property AllowBinNegativeQuantity() As BoYesNoEnum` [R/W] property AllowBinNegativeQuantity
- `Public Property BarCode() As String` [R/W] property BarCode
- `Public Property BinEntry() As Long` [R/W] property BinEntry
- `Public Property CostingCode() As String` [R/W] property CostingCode
- `Public Property CostingCode2() As String` [R/W] property CostingCode2
- `Public Property CostingCode3() As String` [R/W] property CostingCode3
- `Public Property CostingCode4() As String` [R/W] property CostingCode4
- `Public Property CostingCode5() As String` [R/W] property CostingCode5
- `Public Property Currency() As String` [R/W] property Currency
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property InventoryOpeningBalanceBatchNumbers() As InventoryOpeningBalanceBatchNumbers` [R] property InventoryOpeningBalanceBatchNumbers
- `Public Property InventoryOpeningBalanceCCDNumbers() As InventoryOpeningBalanceCCDNumbers` [R] property InventoryOpeningBalanceCCDNumbers
- `Public Property InventoryOpeningBalanceSerialNumbers() As InventoryOpeningBalanceSerialNumbers` [R] property InventoryOpeningBalanceSerialNumbers
- `Public Property InWarehouseQuantity() As Double` [R] property InWarehouseQuantity
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property ItemDescription() As String` [R/W] property ItemDescription
- `Public Property LineNumber() As Long` [R/W] property LineNumber
- `Public Property Manufacturer() As Long` [R/W] property Manufacturer
- `Public Property OpeningBalance() As Double` [R/W] property OpeningBalance
- `Public Property OpenInventoryAccount() As String` [R/W] property OpenInventoryAccount
- `Public Property PostedValueLC() As Double` [R] property PostedValueLC
- `Public Property PostedValueSC() As Double` [R] property PostedValueSC
- `Public Property PreferredVendor() As String` [R/W] property PreferredVendor
- `Public Property Price() As Double` [R/W] property Price
- `Public Property ProjectCode() As String` [R/W] property ProjectCode
- `Public Property Remarks() As String` [R/W] property Remarks
- `Public Property SupplierCatalogNo() As String` [R/W] property SupplierCatalogNo
- `Public Property Total() As Double` [R] property Total
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property VisualOrder() As Long` [R] property VisualOrder
- `Public Property WarehouseCode() As String` [R/W] property WarehouseCode

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

# InventoryOpeningBalanceLines (Collection)

InventoryOpeningBalanceLines Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryOpeningBalanceLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryOpeningBalanceLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryOpeningBalanceParams (Object)

InventoryOpeningBalanceParams Class

## Properties (2)
- `Public Property DocumentEntry() As Long` [R/W] property DocumentEntry
- `Public Property DocumentNumber() As Long` [R] property DocumentNumber

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

# InventoryOpeningBalanceParamsCollection (Collection)

InventoryOpeningBalanceParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryOpeningBalanceParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryOpeningBalanceParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryOpeningBalanceSerialNumber (Object)

InventoryOpeningBalanceSerialNumber Class

## Properties (16)
- `Public Property BaseLineNumber() As Long` [R/W] property BaseLineNumber
- `Public Property BatchID() As String` [R/W] property BatchID
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property ExpiryDate() As Date` [R/W] property ExpiryDate
- `Public Property InternalSerialNumber() As String` [R/W] property InternalSerialNumber
- `Public Property Location() As String` [R/W] property Location
- `Public Property ManufactureDate() As Date` [R/W] property ManufactureDate
- `Public Property ManufacturerSerialNumber() As String` [R/W] property ManufacturerSerialNumber
- `Public Property Notes() As String` [R/W] property Notes
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property ReceptionDate() As Date` [R/W] property ReceptionDate
- `Public Property SystemSerialNumber() As Long` [R/W] property SystemSerialNumber
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine
- `Public Property WarrantyEnd() As Date` [R/W] property WarrantyEnd
- `Public Property WarrantyStart() As Date` [R/W] property WarrantyStart

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

# InventoryOpeningBalanceSerialNumbers (Collection)

InventoryOpeningBalanceSerialNumbers Class

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryOpeningBalanceSerialNumber` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryOpeningBalanceSerialNumber` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryOpeningBalancesService (Object)

InventoryOpeningBalancesService Class

## Methods (7)
- `Public Function Add(ByVal pIInventoryOpeningBalance As InventoryOpeningBalance) As InventoryOpeningBalanceParams` Add
  - param `pIInventoryOpeningBalance`: 
- `Public Function Get(ByVal pIInventoryOpeningBalanceParams As InventoryOpeningBalanceParams) As InventoryOpeningBalance` Get
  - param `pIInventoryOpeningBalanceParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As InventoryOpeningBalancesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `InventoryOpeningBalancesServiceDataInterfaces` in `../enums/enums-02.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As InventoryOpeningBalanceParamsCollection` GetList
- `Public Sub Update(ByVal pIInventoryOpeningBalance As InventoryOpeningBalance)` Update
  - param `pIInventoryOpeningBalance`: 

# InventoryPosting (Object)

If there are differences between the inventory counting results and the item quantities recorded in SAP Business One, you may need to reconcile the quantities so as not to distort your inventory valuation results. For this purpose, use the inventory posting function. Source table: OIQR.

## Properties (20)
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BranchID() As Long` [R/W] property BranchID
- `Public Property CountDate() As Date` [R/W] property CountDate
- `Public Property CountTime() As Date` [R/W] property CountTime
- `Public Property DocObjectCodeEx() As String` [R] property DocObjectCodeEx
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory posting. Field name: DocEntry.
- `Public Property DocumentNumber() As Long` [R] The document number of the inventory posting transaction. Field name: DocNum.
- `Public Property DocumentReferences() As InventoryPostingDocumentReferences` [R] property DocumentReferences
- `Public Property FinancialPeriod() As Long` [R] property FinancialPeriod
- `Public Property InventoryPostingLines() As InventoryPostingLines` [R] The line entries of an inventory posting transaction.
- `Public Property JournalRemark() As String` [R/W] The information to display in the Remarks field of the journal entry. By default, this field contains the text: Inventory Posting. Field name: JrnlMemo. Length: 50 characters.
- `Public Property PeriodIndicator() As String` [R] property PeriodIndicator
- `Public Property PostingDate() As Date` [R/W] The inventory posting date. If the inventory posting document is based on an inventory counting document, this field is not editable and is the count date of the inventory counting document. Field name: DocDate.
- `Public Property PriceList() As Long` [R/W] The price list of the item. Field name: PriceList.
- `Public Property PriceSource() As InventoryPostingPriceSourceEnum` [R/W] The price source that the application uses to fill the Price field. The prices will be used in journal entries and may affect the costs of the items. Field name: PriceSrc.
- `Public Property Reference2() As String` [R/W] The second reference code of the document. Field name: Reference2. Length: 11 characters.
- `Public Property Remarks() As String` [R/W] The remarks of the inventory posting document. Field name: Comments. Length: 254 characters.
- `Public Property Series() As Long` [R/W] property Series
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property YearEndDate() As Date` [R/W] property YearEndDate

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

# InventoryPostingBatchNumber (Object)

InventoryPostingBatchNumber is a child object of the IInventoryPostingLine object. If an item is counted by batch number, use this object to record the batch number information in inventory posting. Source table: BTNT.

## Properties (13)
- `Public Property AddmisionDate() As Date` [R/W] property AddmisionDate
- `Public Property BaseLineNumber() As Long` [R/W] property BaseLineNumber
- `Public Property BatchNumber() As String` [R/W] property BatchNumber
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory posting. Field name: DocEntry.
- `Public Property ExpiryDate() As Date` [R/W] property ExpiryDate
- `Public Property InternalSerialNumber() As String` [R/W] property InternalSerialNumber
- `Public Property Location() As String` [R/W] property Location
- `Public Property ManufactureDate() As Date` [R/W] property ManufactureDate
- `Public Property ManufacturerSerialNumber() As String` [R/W] property ManufacturerSerialNumber
- `Public Property Notes() As String` [R/W] property Notes
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine

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

# InventoryPostingBatchNumbers (Collection)

A collection of InventoryPostingBatchNumber objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryPostingBatchNumber` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryPostingBatchNumber` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryPostingCCDNumber (Object)

InventoryPostingCCDNumber Class

## Properties (9)
- `Public Property BaseLineNumber() As Long` [R/W] property BaseLineNumber
- `Public Property CCDNumber() As String` [R/W] property CCDNumber
- `Public Property ChildNumber() As Long` [R/W] property ChildNumber
- `Public Property CountryOfOrigin() As String` [R/W] property CountryOfOrigin
- `Public Property DocumentEntry() As Long` [R] property DocumentEntry
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property SubLineNumber() As Long` [R/W] property SubLineNumber
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InventoryPostingCCDNumbers (Collection)

InventoryPostingCCDNumbers Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As InventoryPostingCCDNumber` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As InventoryPostingCCDNumber` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InventoryPostingCopyOption (Object)

InventoryPostingCopyOption Class

## Properties (2)
- `Public Property BaseEntry() As Long` [R/W] property BaseEntry
- `Public Property CopyOption() As InventoryPostingCopyOptionEnum` [R/W] property CopyOption

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

# InventoryPostingDocumentReference (Object)

InventoryPostingDocumentReference Class

## Properties (8)
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExternalReferencedDocNumber
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ReferencedDocEntry() As Long` [R/W] property ReferencedDocEntry
- `Public Property ReferencedDocNumber() As Long` [R] property ReferencedDocNumber
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property ReferencedObjectType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InventoryPostingDocumentReferences (Collection)

InventoryPostingDocumentReferences Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (6)
- `Public Function Add() As InventoryPostingDocumentReference` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As InventoryPostingDocumentReference` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub Remove(ByVal vtIndex As Variant)` method Remove
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# InventoryPostingLine (Object)

InventoryPostingLine is a child object of the InventoryPosting object and represents the line entries of the inventory posting transaction. Source table: IQR1. INC1V table is a virtual table to store the line data for inventory counting transaction.

## Properties (45)
- `Public Property ActualPrice() As Double` [R] property ActualPrice
- `Public Property AllowBinNegativeQuantity() As BoYesNoEnum` [R/W] Indicates whether negative quantity in the bin is allowed. Field name: BinNegQty.
- `Public Property BarCode() As String` [R/W] property BarCode
- `Public Property BaseEntry() As Long` [R/W] The base document internal ID. Field name: BaseEntry.
- `Public Property BaseLine() As Long` [R/W] The base document line. Field name: BaseLine.
- `Public Property BaseReference() As String` [R/W] The base document reference. Field name: BaseRef.
- `Public Property BaseType() As Long` [R/W] The base document type. Field name: BaseType.
- `Public Property BinEntry() As Long` [R/W] property BinEntry
- `Public Property CostingCode() As String` [R/W] property CostingCode
- `Public Property CostingCode2() As String` [R/W] property CostingCode2
- `Public Property CostingCode3() As String` [R/W] property CostingCode3
- `Public Property CostingCode4() As String` [R/W] property CostingCode4
- `Public Property CostingCode5() As String` [R/W] property CostingCode5
- `Public Property CountDate() As Date` [R/W] property CountDate
- `Public Property CountedQuantity() As Double` [R/W] property CountedQuantity
- `Public Property CountTime() As Date` [R/W] property CountTime
- `Public Property Currency() As String` [R/W] The price currency. Field name: Currency. Length: 3 characters.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory posting. Field name: DocEntry.
- `Public Property InventoryOffsetDecreaseAccount() As String` [R/W] The accounts in which the inventory decreasing movements are recorded. Field name: DOffDecAcc. Length: 15 characters.
  - remarks: This property is valid only if you use perpetual inventory.
- `Public Property InventoryOffsetIncreaseAccount() As String` [R/W] The accounts in which the inventory increasing movements are recorded. Field name: IOffIncAcc. Length: 15 characters.
  - remarks: This property is valid only if you use perpetual inventory.
- `Public Property InventoryPostingBatchNumbers() As InventoryPostingBatchNumbers` [R] The sub object for you to record the batch number information in inventory posting.
- `Public Property InventoryPostingCCDNumbers() As InventoryPostingCCDNumbers` [R] property InventoryPostingCCDNumbers
- `Public Property InventoryPostingLineUoMs() As InventoryPostingLineUoMs` [R] The sub object for you to specify the unit of measure information for the items you want to post.
- `Public Property InventoryPostingSerialNumbers() As InventoryPostingSerialNumbers` [R] The sub object for you to record the serial number information in inventory posting.
- `Public Property InWarehouseQuantity() As Double` [R] The quantities of the item in warehouses recorded by the system on the selected count date and time. Field name: Quantity.
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property ItemDescription() As String` [R/W] property ItemDescription
- `Public Property ItemsPerUnit() As Double` [R] property ItemsPerUnit
- `Public Property LineNumber() As Long` [R/W] The line number of the inventory posting document. Field name: LineNum.
- `Public Property Manufacturer() As Long` [R/W] property Manufacturer
- `Public Property PostedValueLC() As Double` [R] property PostedValueLC
- `Public Property PostedValueSC() As Double` [R] property PostedValueSC
- `Public Property PreferredVendor() As String` [R/W] property PreferredVendor
- `Public Property Price() As Double` [R/W] The price per unit of the item according to the price type you specified in the Price Source for Whse Inventory Posting field. Field name: Price.
- `Public Property ProjectCode() As String` [R/W] property ProjectCode
- `Public Property Remarks() As String` [R/W] The remarks of the inventory posting document line. Field name: Remark. Length: 254 characters.
- `Public Property SupplierCatalogNo() As String` [R/W] property SupplierCatalogNo
- `Public Property Total() As Double` [R] Total = Price × Variance The total value is displayed in local currency. Field name: DocTotal.
- `Public Property UoMCode() As String` [R/W] property UoMCode
- `Public Property UoMCountedQuantity() As Double` [R/W] property UoMCountedQuantity
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property Variance() As Double` [R/W] property Variance
- `Public Property VariancePercentage() As Double` [R] property VariancePercentage
- `Public Property VisualOrder() As Long` [R] property VisualOrder
- `Public Property WarehouseCode() As String` [R/W] property WarehouseCode

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

# InventoryPostingLines (Collection)

A collection of InventoryPostingLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryPostingLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryPostingLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryPostingLineUoM (Object)

InventoryPostingLineUoM is a child object of the InventoryPostingLine object and enables you to specify the unit of measure (UoM) information for the items you want to post. Source table: IQR2.

## Properties (9)
- `Public Property BarCode() As String` [R/W] property BarCode
- `Public Property ChildNumber() As Long` [R] property ChildNumber
- `Public Property CountedQuantity() As Double` [R/W] property CountedQuantity
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory posting. Field name: DocEntry.
- `Public Property ItemsPerUnit() As Double` [R] property ItemsPerUnit
- `Public Property LineNumber() As Long` [R] The line number of the inventory posting document. Field name: LineNum.
- `Public Property UoMCode() As String` [R/W] property UoMCode
- `Public Property UoMCountedQuantity() As Double` [R/W] property UoMCountedQuantity
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

# InventoryPostingLineUoMs (Collection)

A collection of InventoryPostingLineUoM objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryPostingLineUoM` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryPostingLineUoM` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryPostingParams (Object)

Holds the key to an existing inventory posting transaction. This object is used to pass keys to and retrieve keys from InventoryPostingsService methods.

## Properties (2)
- `Public Property DocumentEntry() As Long` [R/W] The internal key of the inventory posting. Field name: DocEntry.
- `Public Property DocumentNumber() As Long` [R] The document number of the inventory posting transaction. Field name: DocNum.

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

# InventoryPostingParamsCollection (Collection)

A collection of InventoryPostingParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryPostingParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryPostingParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryPostingSerialNumber (Object)

InventoryPostingSerialNumber is a child object of the IInventoryPostingLine object. If an item is counted by serial number, use this object to record the serial number information in inventory posting. Source table: SRNT.

## Properties (16)
- `Public Property BaseLineNumber() As Long` [R/W] property BaseLineNumber
- `Public Property BatchID() As String` [R/W] property BatchID
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory posting. Field name: DocEntry.
- `Public Property ExpiryDate() As Date` [R/W] property ExpiryDate
- `Public Property InternalSerialNumber() As String` [R/W] property InternalSerialNumber
- `Public Property Location() As String` [R/W] property Location
- `Public Property ManufactureDate() As Date` [R/W] property ManufactureDate
- `Public Property ManufacturerSerialNumber() As String` [R/W] property ManufacturerSerialNumber
- `Public Property Notes() As String` [R/W] property Notes
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property ReceptionDate() As Date` [R/W] property ReceptionDate
- `Public Property SystemSerialNumber() As Long` [R/W] property SystemSerialNumber
- `Public Property TrackingNote() As Long` [R/W] property TrackingNote
- `Public Property TrackingNoteLine() As Long` [R/W] property TrackingNoteLine
- `Public Property WarrantyEnd() As Date` [R/W] property WarrantyEnd
- `Public Property WarrantyStart() As Date` [R/W] property WarrantyStart

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

# InventoryPostingSerialNumbers (Collection)

A collection of InventoryPostingSerialNumber objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As InventoryPostingSerialNumber` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As InventoryPostingSerialNumber` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# InventoryPostingsService (Object)

The InventoryPostingsService service enables you to add, look up, and update inventory posting transactions. Source table: OIQR.

**Remarks:** To open the Inventory Posting window, from the SAP Business One Main Menu, choose Inventory --> Inventory Transactions --> Inventory Counting Transactions --> Inventory Posting.

## Methods (8)
- `Public Function Add(ByVal pIInventoryPosting As InventoryPosting) As InventoryPostingParams` Adds an inventory posting transaction.
  - param `pIInventoryPosting`: The data for the new inventory posting transaction.
- `Public Function Get(ByVal pIInventoryPostingParams As InventoryPostingParams) As InventoryPosting` Retrieves an inventory posting transaction. The inventory posting transaction is specified by its key, which is contained in the InventoryPostingParams object passed to the method.
  - param `pIInventoryPostingParams`: The key of the inventory posting transaction to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As InventoryPostingsServiceDataInterfaces) As Object` Creates an empty data structure for use with the InventoryPostingsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `InventoryPostingsServiceDataInterfaces` in `../enums/enums-02.md`
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
- `Public Function GetList() As InventoryPostingParamsCollection` Returns the InventoryPostingParamsCollection data collection that identifies all inventory posting transactions.
- `Public Sub SetCopyOption(ByVal pIInventoryPostingCopyOption As InventoryPostingCopyOption)` SetCopyOption
  - param `pIInventoryPostingCopyOption`: 
- `Public Sub Update(ByVal pIInventoryPosting As InventoryPosting)` Updates an existing inventory posting transaction.
  - param `pIInventoryPosting`: The data for the inventory posting transaction to be updated. The InventoryPosting object must contain the key of the object to be updated.

# InvokeParams (Object)

Holds a single string value. This object is used to pass a parameter to or receive a return value from the InvokeMethod method of the GeneralService service.

## Properties (1)
- `Public Property Value() As String` [R/W] A value to pass to the InvokeMethod method of the GeneralService service, or a value received from the method.

# ItemBarCodes (Object)

ItemBarCodes Class

## Properties (5)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property BarCode() As String` [R/W] property Barcode
- `Public Property Count() As Long` [R] property Count
- `Public Property FreeText() As String` [R/W] property FreeText
- `Public Property UoMEntry() As Long` [R/W] property UoMEntry

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# ItemCycleCount (Object)

ItemCycleCount object hold the information when an item will go through cycle counting. Each Item has a few Warehouses and each Warehouse has one ItemCycleCount. Source table: ITW1

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  Dim oItem As Items

  Dim oWhareHouse As ItemWarehouseInfo

  oItem = oCompany.GetBusinessObject(BoObjectTypes.oItems)

  'get item

  oItem.GetByKey("X0003")

  'get warehouse

  oWhareHouse = oItem.WhsInfo

  'set an existind cycle count (e.g CycleCode=1 : CycleName:"Weekly on Tuesday" ,OCYC table)

  oWhareHouse.ItemCycleCount.CycleCode = 1

  'set alert

  oWhareHouse.ItemCycleCount.Alert = BoYesNoEnum.tYES

  'set user

  oWhareHouse.ItemCycleCount.DestinationUser = 1

  'update item with new Cycle Count

  oItem.Update()
  ```

## Properties (8)
- `Public Property Alert() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to activate alert. Field name: Alert.
- `Public Property AlertTime() As Date` [R/W] Sets or returns the Alert Time. Field name: Time.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
- `Public Property CycleCode() As Long` [R/W] Sets or returns the Cycle Code. Field name: CycleCode. This is a foreign key to the OCYC object.
- `Public Property DestinationUser() As Long` [R/W] Sets or returns the alert destination user. Field name: DestUser. This is a foreign key to the Users object.
- `Public Property NextCountingDate() As Date` [R/W] Returns the next counting date for this item. Field name: NextDate.
- `Public Property UserFields() As UserFields` [R] Returns the user signature. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property WarehouseCode() As String` [R/W] Returns the warehouse code. Field name: WhsCode. This is a foreign key to the Warehouses object.

# ItemGroups (Object)

ItemGroups is a business object that represents the item groups definition in the Inventory and Production module. This object enables you to: - Add an item group. - Retrieve an item group by its key. - Update an item group details. - Remove an item group. - Save the object in XML format. Source table: OITB

**Remarks:** Mandatory field in SAP Business One: GroupName. To display the form in the application: - Select Administration --> Setup --> Inventory --> Item Groups. The item group definition includes: - General information about the group of items. - G/L accounts, which are defined in ChartOfAccounts, used in Item Master Data - Inventory Data in case GLMethod property is set to Item Group (Item Class).

## Properties (66)
- `Public Property Alert() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to activate an alert notification when the inventory count for the item group is due.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ComponentWarehouse() As BoMRPComponentWarehouse` [R/W] property ComponentWarehouse
- `Public Property CostAccount() As String` [R/W] Sets or returns the G/L account associated with Costs. Length: 15 characters.
- `Public Property CostInflationAccount() As String` [R/W] Sets or returns the G/L account associated with Cost Inflation. Field name: CostRvlAct. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property CostInflationOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Cost Inflation Offset. Field name: CstOffsAct. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property CycleCode() As Long` [R/W] Sets or returns the inventory cycle code as defined in SAP BUsiness One (OCYC table, which is not exposed through the DI API).
  - remarks: The inventory cycle schedules inventory counts and activates an alert when the inventory count is due.
- `Public Property DecreaseGLAccount() As String` [R/W] Sets or returns the G/L account associated with Decrease G/L Account. Field name: DecresGlAc. Length: 15 characters.
- `Public Property DecreasingAccount() As String` [R/W] Sets or returns the G/L account associated with decreased stock transactions (inventory offset). Field name: DecreasAc. Length: 15 characters.
- `Public Property DefaultInventoryUoM() As Long` [R/W] The default inventory UoM for the item group. Field name: IUomEntry.
- `Public Property DefaultUoMGroup() As Long` [R/W] The default UoM (Unit of Measurement) group for the item group. Field name: UgpEntry.
- `Public Property EUExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with EU Expenses Account. Field name: EUExpensAc. Field name: ExpensesAc. Length: 15 characters.
- `Public Property EUPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with EU Purchase Credit Account. Field name: APCMEUAct). Length: 15 characters.
- `Public Property EURevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with EU Revenues. Field name: EURevenuAc. Length: 15 characters.
- `Public Property ExchangeRateDifferencesAccount() As String` [R/W] Sets or returns the G/L account associated with Exchange Rate Differences between purchase delivery notes and A/P invoices. Field name: ExchangeAc. Length: 15 characters.
- `Public Property ExemptedCredits() As String` [R/W] Sets or returns the G/L account associated to the Exempted Credits. Field name: ARCMExpAct. Length: 15 characters.
- `Public Property ExemptRevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Exempted Revenues. Field name: ExmptIncom). Length: 15 characters.
- `Public Property ExpenseClearingAct() As String` [R/W] Sets or returns the G/L account associated with Expenses clearing Account. Field name: ExpClrAct. Length: 15 characters.
  - remarks: This is a foreign key to the ChartOfAccounts Object.
- `Public Property ExpenseOffsetAccount() As String` [R/W] Sets or returns the G/L account associated to the Expense Offset Account. Field name: ExpOfstAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
- `Public Property ExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with Expense Account. Field name: ExpensesAc. Length: 15 characters.
- `Public Property ForeignExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with Foreign Expenses account. Field name: FrExpensAc. Length: 15 characters.
- `Public Property ForeignPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with Foreign Purchase Credit Account. Field name: APCMFrnAct. Length: 15 characters.
- `Public Property ForeignRevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Sales Revenue - Foreign Account. Field name: FrRevenuAc. Length: 15 characters.
- `Public Property GoodsClearingAccount() As String` [R/W] Sets or returns the G/L account associated with closing a purchase delivery note. Field name: BalanceAcc. Length: 15 characters.
- `Public Property GroupName() As String` [R/W] Sets or returns the item group name. Mandatory property. Length: 20 characters.
- `Public Property IncreaseGLAccount() As String` [R/W] Sets or returns the G/L account associated to Increase G/L Account. Field name: IncresGlAc. Length: 15 characters.
- `Public Property IncreasingAccount() As String` [R/W] Sets or returns the G/L account associated to increased stock transactions (inventory offset). Field name: IncresGlAc. Length: 15 characters.
- `Public Property InventoryAccount() As String` [R/W] Sets or returns the G/L account associated to the inventory. Length: 15 characters.
- `Public Property InventoryOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to an inventory account used within production transactions and for change of value of the inventory account during the production process. Field name: StockOffst. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property InventorySystem() As BoInventorySystem` [R/W] Sets or returns a valid value of BoInventorySystem type that specifies the inventory evaluation method.
- `Public Property ItemClass() As ItemClassEnum` [R/W] property ItemClass
- `Public Property LeadTime() As Long` [R/W] Sets or returns the lead time in days for ordering items.
- `Public Property MinimumOrderQuantity() As Double` [R/W] Sets or returns the minimum quantity of items in a single order.
- `Public Property NegativeInventoryAdjustmentAccount() As String` [R/W] Sets or returns this item groups's Negative Inventory Adjustment Account. Field name: NegStckAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
- `Public Property Number() As Long` [R] Returns the item group code as assigned by SAP Business One.
- `Public Property OrderInterval() As Long` [R/W] Sets or returns the inventory cycle such as, every week on Monday, or every first day of the month. The inventory cycles are defined in SAP Business One (OCYC table, which is not exposed through the DI API).
- `Public Property OrderMultiple() As Double` [R/W] Sets or returns the multiple quantity in addition to the minimum quantity of items in a single order.
  - remarks: For example: If the minimum order quantity is 1000 items and multiple quantity is 500 items, then the allowed quantity in a single order can be: 1000, 1500, 2000, and so on.
- `Public Property PAReturnAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Returning account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property PlanningSystem() As BoPlanningSystem` [R/W] Sets or returns a valid value of BoPlanningSystem type that specifies the inventory planning system: MRP or None.
- `Public Property PriceDifferencesAccount() As String` [R/W] Sets or returns the G/L account associated with Price Differences Account. Field name: PriceDifAc. Length: 15 characters.
- `Public Property ProcurementMethod() As BoProcurementMethod` [R/W] Sets or returns a valid value of BoProcurementMethod type that specifies the procurement method of items: Buy or Make.
- `Public Property PurchaseAccount() As String` [R/W] Sets or returns the G/L account associated with Purchases. Field name: PurchaseAc. Length: 15 characters.
- `Public Property PurchaseBalanceAccount() As String` [R/W] property PurchaseBalanceAccount
- `Public Property PurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated to the Purchase Credit Account. Field name: APCMAct. Length: 15 characters.
- `Public Property PurchaseOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Offsetting. Field name: PurchOfsAc. Length: 15 characters.
- `Public Property RawMaterial() As BoYesNoEnum` [R/W] property RawMaterial
- `Public Property ReturningAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Returning Account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property RevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Revenues Account. Field name: RevenuesAc. Length: 15 characters.
- `Public Property SalesCreditAcc() As String` [R/W] Sets or returns the the G/L account associated to the Sales Credit Account. Field name: ARCMAct. Length: 15 characters.
- `Public Property SalesCreditEUAcc() As String` [R/W] Sets or returns the the G/L account associated to the Sales Credit EU Account. Field name: ARCMEUAct. Length: 15 characters.
- `Public Property SalesCreditForeignAcc() As String` [R/W] Sets or returns the the G/L account associated to the Sales Credit Foreign Account. Field name: ARCMFrnAct. Length: 15 characters.
- `Public Property ShippedGoodsAccount() As String` [R/W] Sets or returns the G/L account associated with shipped goods. Length: 15 characters.
- `Public Property StockInflationAdjustAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Inflation Adjust. Length: 15 characters. Field name: IncreasAc.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property StockInflationOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Inflation Offset. Field name: DecreasAc. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property StockInTransitAccount() As String` [R/W] The stock in transit G/L account for this item group. Field name: StkInTnAct
- `Public Property ToleranceDays() As Long` [R/W] property ToleranceDays
- `Public Property TransfersAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Transfers. Field name: TransferAc. Length: 15 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VarianceAccount() As String` [R/W] Sets or returns the G/L account associated with Variance Account. Field name: VarianceAc. Length: 15 characters.
- `Public Property VATInRevenueAccount() As String` [R/W] Sets or returns the G/L account associated with VAT in Revenues. Field name: VatRevAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
- `Public Property WarehouseInfo() As ItemGroups_WarehouseInfo` [R] property WarehouseInfo
- `Public Property WHIncomingCenvatAccount() As String` [R/W] Sets or returns the Incoming CENVAT Account (WH) for Account Setting in Item Group Definition. Applicable for cluster B only (country-specific for India). Field name: WhICenAct.
- `Public Property WHOutgoingCenvatAccount() As String` [R/W] Sets or returns the Outgoing CENVAT Account (WH) for Account Setting in Item Groups Definition. Applicable for cluster B only (country-specific for India). Field name: WhOCenAct.
- `Public Property WIPMaterialAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP). Field name: WipAcct. Length: 15 characters.
  - remarks: Work In Prog account is used for posting transactions such as, transferring row material from the warehouse to the production floor.
- `Public Property WIPMaterialVarianceAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP) differences. That is, the account for posting differences between the value of the row material (before production) and the value of the complete product (after production). Field name: WipVarAcct. Length: 15 characters.
- `Public Property WipOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to a WIP (work in progress) account used within production transactions and for change of value of the WIP account during the production process. Field name: WipOffset. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal GroupCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `GroupCode`: Item group code (Number).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
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

# ItemGroups_WarehouseInfo (Object)

ItemGroups_WarehouseInfo is a child object of the ItemGroups object that represents the items in the warehouse. Source table: OIGW.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property DefaultBin() As Long` [R/W] The default bin location in the warehouse for receiving items. Field name: DftBinAbs.
- `Public Property DefaultBinEnforced() As BoYesNoEnum` [R/W] Indicates whether to enforce the use of the default bin location during receipt of items to the warehouse. That is, when you receive an item to the warehouse, you must place it in the default bin location. Field name: DftBinEnfd.
- `Public Property ItemGroupCode() As Long` [R] The item group code. Field name: ItmsGrpCod.
- `Public Property WarehouseCode() As String` [R/W] The warehouse code. Field name: WhsCode. Length: 8 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# ItemIntrastatExtension (Object)

ItemIntrastatExtension Class

## Properties (20)
- `Public Property CommodityCode() As Long` [R/W] property CommodityCode
- `Public Property CountryOfOrigin() As String` [R/W] property CountryOfOrigin
- `Public Property ExportNatureOfTransaction() As Long` [R/W] property ExportNatureOfTransaction
- `Public Property ExportRegionCountry() As String` [R/W] property ExportRegionCountry
- `Public Property ExportRegionState() As Long` [R/W] property ExportRegionState
- `Public Property ExportStatisticalProcedure() As Long` [R/W] property ExportStatisticalProcedure
- `Public Property FactorOfSupplementaryUnit() As Double` [R/W] property FactorOfSupplementaryUnit
- `Public Property ImportNatureOfTransaction() As Long` [R/W] property ImportNatureOfTransaction
- `Public Property ImportRegionCountry() As String` [R/W] property ImportRegionCountry
- `Public Property ImportRegionState() As Long` [R/W] property ImportRegionState
- `Public Property ImportStatisticalProcedure() As Long` [R/W] property ImportStatisticalProcedure
- `Public Property IntrastatRelevant() As BoYesNoEnum` [R/W] property IntrastatRelevant
- `Public Property ItemCode() As String` [R] property ItemCode
- `Public Property ServiceCode() As Long` [R/W] property ServiceCode
- `Public Property ServicePaymentMethod() As BoServicePaymentMethods` [R/W] property ServicePaymentMethod
- `Public Property ServiceSupplyMethod() As BoServiceSupplyMethods` [R/W] property ServiceSupplyMethod
- `Public Property StatisticalCode() As String` [R] property StatisticalCode
- `Public Property SupplementaryUnit() As Long` [R/W] property SupplementaryUnit
- `Public Property Type() As BoDocumentTypes` [R/W] property Type
- `Public Property UseWeightInCalculation() As BoYesNoEnum` [R/W] property UseWeightInCalculation

# ItemLocalizationInfos (Object)

ItemLocalizationInfos Class

## Properties (3)
- `Public Property Count() As Long` [R] property Count
- `Public Property IncomeNature() As String` [R/W] property IncomeNature
- `Public Property ItemCode() As String` [R] property ItemCode

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNumber As Long)` method SetCurrentLine
  - param `LineNumber`: 

# ItemPriceParams (Object)

The item

## Properties (10)
- `Public Property BlanketAgreementLine() As Long` [R/W] The line number of the blanket agreement.
- `Public Property BlanketAgreementNumber() As Long` [R/W] The number of the blanket agreement.
- `Public Property CardCode() As String` [R/W] The business partner code.
- `Public Property Currency() As String` [R/W] The currency of the item price.
- `Public Property Date() As Date` [R/W] The date.
- `Public Property InventoryQuantity() As Double` [R/W] The inventory quantity.
- `Public Property ItemCode() As String` [R/W] The item code.
- `Public Property PriceList() As Long` [R/W] The price list.
- `Public Property UoMEntry() As Long` [R/W] The UoM code.
- `Public Property UoMQuantity() As Double` [R/W] The UoM quantity.

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

# ItemPriceReturnParams (Object)

Returns the item price.

## Properties (3)
- `Public Property Currency() As String` [R] Returns the currency of the item price.
- `Public Property Discount() As Double` [R] Returns the discount of the item price.
- `Public Property Price() As Double` [R] Returns the item price.

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

# ItemProperties (Object)

The ItemProperties object enables to update the property names that can be used for sorting or grouping items in reports. Source table: OITG

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Inventory --> Item Properties.

## Properties (4)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Number() As Long` [R] Returns the code (1 to 64) of the item property.
- `Public Property PropertyName() As String` [R/W] Sets or returns the property name, which can be used for sorting and grouping items in reports. Length: 50 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (5)
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lGroupCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lGroupCode`: Item property code (Number).
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

# Items (Object)

Items is a business object that represents the items master data in the Inventory and Production module. This object enables you to: - Add an item details. - Retrieve an item by its key. - Update item details. - Save the object in XML format. Source table: OITM.

**Remarks:** Mandatory fields in SAP Business One: ItemCode and Manufacturer. To display the Item Master Data window, from the SAP Business One Main Menu, choose Inventory --> Item Master Data. SAP Business One also lets you manage all fixed assets in the asset master data. To access the Asset Master Data window, from the SAP Business One Main Menu, choose Financials --> Fixed Assets --> Asset Master Data.

## Properties (223)
- `Public Property ApTaxCode() As String` [R/W] Sets or returns the Tax Code (AP) for purchase documents. Field name: TaxCodeAP. This is a foreign key to the SalesTaxCodes Object. Length: 8 characters.
  - remarks: Country-specific property for Mexico and Chile.
- `Public Property ArTaxCode() As String` [R/W] Sets or returns the Tax Code (AR) for sales documents. Field name: TaxCodeAR. This is a foreign key to the SalesTaxCodes Object Length: 8 characters.
  - remarks: Country-specific property for Mexico and Chile.
- `Public Property AssessableValue() As Double` [R/W] property AssessableValue
- `Public Property AssetClass() As String` [R/W] The asset class to which the asset belongs. Field name: AssetClass. Length: 20 characters.
  - remarks: After you assign an asset class to the asset, the following depreciation parameters of the asset class are copied to the asset as the defaults: Depreciation area Depreciation type Useful life
- `Public Property AssetGroup() As String` [R/W] The asset group to which the asset belongs. Field name: AssetGroup. Length: 15 characters.
- `Public Property AssetItem() As BoYesNoEnum` [R/W] Determines whether or not this item is a Fixed Assets. Field name: AssetItem.
- `Public Property AssetSerialNumber() As String` [R/W] The serial number of the asset. Field name: AssetSerNo. Length: 30 characters.
- `Public Property AssetStatus() As AssetStatusEnum` [R] The asset's status. Field name: AsstStatus.
- `Public Property AssVal4WTR() As Double` [R/W] property AssVal4WTR
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property AttributeGroups() As ItemsAttributeGroups` [R] Returns the ItemsAttributeGroups child object.
- `Public Property AutoCreateSerialNumbersOnRelease() As BoYesNoEnum` [R/W] Determines whether or not to create automatically a serial number when releasing the item. Applicable for cluster B only.
- `Public Property AvgStdPrice() As Double` [R/W] Sets or returns the Item Cost. Field name: AvgPrice.
- `Public Property BarCode() As String` [R/W] Sets or returns the Bar Code (EAN code) for this item. Field name: CodeBars. Length: 16 characters.
- `Public Property BarCodes() As ItemBarCodes` [R] property BarCodes
- `Public Property BaseUnitName() As String` [R/W] Sets or returns the inventory Unit Name. Field name: BaseUnit. Length: 20 characters.
- `Public Property BeverageCommercialBrandCode() As Long` [R/W] property BeverageCommercialBrandCode
- `Public Property BeverageGroupCode() As String` [R/W] property BeverageGroupCode
- `Public Property BeverageTableCode() As String` [R/W] property BeverageTableCode
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CapitalGoodsOnHoldLimit() As Double` [R/W] property CapitalGoodsOnHoldLimit
- `Public Property CapitalGoodsOnHoldPercent() As Double` [R/W] property CapitalGoodsOnHoldPercent
- `Public Property CapitalizationDate() As Date` [R/W] The date on which the asset is capitalized. Field name: CapDate.
- `Public Property Cession() As BoYesNoEnum` [R/W] Indicates whether the asset is owned by your company but financed by a bank mortgage. Field name: Cession.
- `Public Property CESTCode() As Long` [R/W] CEST Code. Field name: CESTCode.
- `Public Property ChapterID() As Long` [R/W] property ChapterID
- `Public Property CommissionGroup() As Long` [R/W] Sets or returns the Commission Group code. Field name: CommisGrp.
- `Public Property CommissionPercent() As Double` [R/W] Sets or returns the commission percentage for the specified Business Partner. Field name: CommisPcnt.
- `Public Property CommissionSum() As Double` [R/W] Sets or returns the Total Commission for Item. Field name: CommisSum.
- `Public Property CommodityClassification() As Long` [R/W] Commodity classification. Field name: CommClass.
- `Public Property ComponentWarehouse() As BoMRPComponentWarehouse` [R/W] property ComponentWarehouse
- `Public Property CostAccountingMethod() As BoInventorySystem` [R/W] Sets or returns the Valuation Method used to evaluate inventory. Field name: EvalSystem.
- `Public Property CountingItemsPerUnit() As Double` [R] The number of items per counting unit. Field name: NumInCnt.
- `Public Property CreateDate() As Date` [R] The date when the item master data created. Field name: CreateDate.
- `Public Property CreateQRCodeFrom() As String` [R/W] Provide data source that is used to create a QR Code. Field name: QRCodeSrc.
- `Public Property CreateTime() As Date` [R] The timestamp of the item master data created is recorded in the hhmmss format. Field name: CreateTS.
- `Public Property CtrSealQty() As Double` [R/W] Specify the Control Seal Quantity for Item Master Data. Field name: CtrSealQty.
- `Public Property CustomsGroupCode() As Long` [R/W] Sets or returns the Customs Group code. Customs groups determine the customs duty for an item purchased abroad. Field name: CstGrpCode.
- `Public Property DataExportCode() As String` [R/W] Sets or returns the Data Export Code. Field name: ExportCode. Length: 20 characters.
- `Public Property DeactivateAfterUsefulLife() As BoYesNoEnum` [R/W] Deactivate a low value asset when the asset's useful life ends. Field name: DeacAftUL.
  - remarks: The field is available only in the Germany localization when the following conditions are met: The asset is a low value asset. That is, the asset class of the asset has the Low Value Asset type. The asset's main depreciation area uses a depreciation type that has the After End of Useful Life retirement convention.
- `Public Property DefaultCountingUnit() As String` [R] The name of the default inventory counting unit. Field name: CntUnitMsr. Length: 100 characters.
- `Public Property DefaultCountingUoMEntry() As Long` [R/W] Specify a UoM to be used as the default inventory counting UoM. Field name: INUoMEntry.
  - remarks: Available only when the UoM group is not Manual.
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    Dim item As SAPbobsCOM.Items
    item = oCompany.GetBusinessObject(BoObjectTypes.oItems)
    Dim ret As Long

    ret = item.GetByKey("I001")
    item.DefaultCountingUoMEntry = 1 -- "SmallBox"

    ret = item.Update()
    ```
- `Public Property DefaultPurchasingUoMEntry() As Long` [R/W] The internal key of the default purchasing UoM. Field name: PUoMEntry.
- `Public Property DefaultSalesUoMEntry() As Long` [R/W] The internal key of the default sales UoM. Field name: SUoMEntry.
- `Public Property DefaultWarehouse() As String` [R/W] Sets or returns the Default Warehouse. Field name: DfltWH. Length: 8 characters.
- `Public Property DepreciationGroup() As String` [R/W] The depreciation areas you have specified in the asset class. Field name: DeprGroup. Length: 15 characters.
- `Public Property DepreciationParameters() As ItemsDepreciationParameters` [R] Returns the ItemsDepreciationParameters child object.
- `Public Property DesiredInventory() As Double` [R/W] Sets or returns the Preferred Quantity in Purchase Units. Field name: ReorderQty.
- `Public Property DistributionRules() As ItemsDistributionRules` [R] Returns the ItemsDistributionRules child object.
- `Public Property DNFEntry() As Long` [R/W] The DNF code for this item. Field name: DNFEntry This is a foreign key to the DNFCodeSetup object.
  - remarks: For Brazil only.
- `Public Property ECExpensesAccount() As String` [R/W] Sets or returns the EU Expense Account. Field name: ECExpAcc. Length: 15 characters.
  - remarks: Not relevant to DI API from version 6.2 and up.
- `Public Property ECRevenuesAccount() As String` [R/W] Sets or returns the EU revenues account. Field name: ECInAcct. Length: 15 characters.
  - remarks: Not relevant to DI API from version 6.2 and up.
- `Public Property Employee() As Long` [R/W] The employee to whom the asset is physically assigned. Field name: Technician.
- `Public Property EnforceAssetSerialNumbers() As BoYesNoEnum` [R/W] property EnforceAssetSerialNumbers
- `Public Property Excisable() As BoYesNoEnum` [R/W] property Excisable
- `Public Property ExemptIncomeAccount() As String` [R/W] Not used from DI API version 6.2 and up.
- `Public Property ExpanseAccount() As String` [R/W] Not used from DI API version 6.2 and up.
- `Public Property ForceSelectionOfSerialNumber() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to force selection of serial numbers for documents. Field name: BlockOut.
  - remarks: - This property, if set to Yes, blocks the generation of release documents, containing items with serial numbers management, for which serial numbers were not chosen.
- `Public Property ForeignExpensesAccount() As String` [R/W] Sets or returns the foreign expenses account. Length: 15 characters.
  - remarks: Not relevant to DI API from version 6.2 and up.
- `Public Property ForeignName() As String` [R/W] Sets or returns the item name or a description in foreign language. Field name: FrgnName. Length: 200 characters.
- `Public Property ForeignRevenuesAccount() As String` [R/W] Sets or returns the foreign revenues account. Length: 15 characters.
  - remarks: Not relevant to DI API from version 6.2 and up.
- `Public Property Frozen() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is on hold.
  - remarks: For items set to on hold, the end-user can specify the period when the item is on hold (FrozenFrom and FrozenTo), and also add remarks (FrozenRemarks).
- `Public Property FrozenFrom() As Date` [R/W] Sets or returns the start date for keeping the item on hold.
- `Public Property FrozenRemarks() As String` [R/W] Sets or returns the remarks regarding the on hold period. Length: 30 characters.
- `Public Property FrozenTo() As Date` [R/W] Sets or returns the end date for keeping the item on hold.
- `Public Property FuelID() As Long` [R/W] property FuelID
- `Public Property GLMethod() As BoGLMethods` [R/W] Sets or returns a valid value of BoGLMethods type that specifies the default G/L accounts for posting transactions related to the item. source: Warehouses, ItemGroups, or specified in the item level.
- `Public Property GSTRelevnt() As BoYesNoEnum` [R/W] property GSTRelevnt
- `Public Property GSTTaxCategory() As GSTTaxCategoryEnum` [R/W] property GSTTaxCategory
- `Public Property GTSItemSpec() As String` [R/W] property GTSItemSpec
- `Public Property GTSItemTaxCategory() As String` [R/W] property GTSItemTaxCategory
- `Public Property ImportedItem() As BoYesNoEnum` [R/W] property ImportedItem
- `Public Property IncomeAccount() As String` [R/W] Not used from DI API version 6.2 and up.
- `Public Property IncomingServiceCode() As Long` [R/W] Sets or returns the Item's incoming service code. Field name: ISvcCode. This is a foreign key to the Service Code table (OSCD), not exposed through the DI API.
  - remarks: The IncomingServiceCode Property is applicable for cluster B only (country-specific for Brazil only).
- `Public Property InCostRollup() As BoYesNoEnum` [R/W] property InCostRollup
- `Public Property IndirectTax() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to apply indirect tax.
  - remarks: Country-specific property for Mexico and Chile.
- `Public Property IntrastatExtension() As ItemIntrastatExtension` [R] Returns the ItemIntrastatExtension child object.
- `Public Property InventoryItem() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is a warehouse item (not a service).
- `Public Property InventoryNumber() As String` [R/W] The inventory number of the asset. Field name: InventoryNo. Length: 12 characters.
  - remarks: You can use the inventory number as an alternative to the asset number. This enables you to retain previously used numbers when transferring legacy fixed asset data, for example, from the Fixed Assets add-on.
- `Public Property InventoryUOM() As String` [R/W] Sets or returns the Unit of Measurement for the item (for example, box, case, piece.) Length: 5 characters.
- `Public Property InventoryUoMEntry() As Long` [R/W] The internal key of an inventory UoM. Field name: IUoMEntry.
- `Public Property InventoryWeight() As Double` [R/W] property InventoryWeight
- `Public Property InventoryWeight1() As Double` [R/W] property InventoryWeight1
- `Public Property InventoryWeightUnit() As Long` [R/W] property InventoryWeightUnit
- `Public Property InventoryWeightUnit1() As Long` [R/W] property InventoryWeightUnit1
- `Public Property IsPhantom() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the item is a phantom item.
  - remarks: Phantom items are considered as non-real items and are not part of the inventory (and therefore not managed). The purpose of defining an item as phantom is to facilitate the bill of material for manufacturing a product. For example, to manufacture a car, the bill of material can include a phantom item called electrical system. This item does not really exist in the inventory, but the items that are parts of the electrical system do exist.
- `Public Property IssueMethod() As BoIssueMethod` [R/W] Sets or returns a valid value that specifies the method for issuing the item from the inventory: Backflash (automatic) or Manual.
  - remarks: When one of the properties ManageBatchNumbers and ManageSerialNumbers is set to 1, you must set the IssueMethod property to Manual.
- `Public Property IssuePrimarilyBy() As IssuePrimarilyByEnum` [R/W] Specify whether you want to pick the serial or batch items for issuing according to their bin locations or their serial or batch information. Field name: IssuePriBy.
  - remarks: The field is available only if you have done the following: You have enabled bin locations for at least one warehouse. You have selected Serial Numbers or Batches in the Manage Item by field.
- `Public Property ItemClass() As ItemClassEnum` [R/W] Sets or returns a valid value of ItemClassEnum that determines wether or not current Item is a Service or Material. Field name: ItemClass.
  - remarks: The ItemClass property is applicable for cluster B (country-specific for Brazil only).
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. The item code must be unique. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property ItemCountryOrg() As String` [R/W] Sets or returns the origin country of the item. Length: 3 characters.
- `Public Property ItemName() As String` [R/W] Sets or returns the item name/description. Length: 200 characters.
- `Public Property ItemsGroupCode() As Long` [R/W] Sets or returns the items group code. The user can classify items by groups. Each item can be assigned to one group only. The items group is used for reports and evaluations.
- `Public Property ItemType() As ItemTypeEnum` [R/W] Sets or returns a valid value of this Item Type. Field name: ItemType.
  - remarks: To display the form in the application: - Select Inventory --> Item Master Data--> Item Type.
- `Public Property LeadTime() As Long` [R/W] Sets or returns the lead time in days for ordering the item. Property type Read-write property " -->
- `Public Property LegalText() As String` [R/W] Legal text. Field name: LegalText. Length: 250 characters.
- `Public Property LinkedResource() As String` [R] property LinkedResource
- `Public Property LocalizationInfos() As ItemLocalizationInfos` [R] Returns the ItemLocalizationInfos child object.
- `Public Property Location() As Long` [R/W] The location of the asset. Field name: Location.
- `Public Property Mainsupplier() As String` [R/W] Sets or returns the card code of the main supplier of this item. Length: 15 characters.
- `Public Property ManageBatchNumbers() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is managed by batch numbers.
  - remarks: ManageBatchNumbers cannot be set to 1 when ManageSerialNumbers is set to 1.
- `Public Property ManageByQuantity() As BoYesNoEnum` [R] Indicates whether the asset is managed by quantity. Field name: MgrByQty.
- `Public Property ManageSerialNumbers() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is managed by serial numbers.
  - remarks: ManageSerialNumbers cannot be set to 1 when ManageBatchNumbers is set to 1.
- `Public Property ManageSerialNumbersOnReleaseOnly() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that determines whether or not to create automatic serial numbers upon reception. Field name: ManOutOnly.
  - remarks: When this property is set to Yes, SAP Business One creates successive serial numbers (according to a successive numerator) and allows the end-user to select these numbers. - This method does not determine the management method. This is done by the SRIAndBatchManageMethod property. The property is relevant only when: - The item is managed by Serial Numbers (by setting ManageSerialNumbers to Yes). - The management method is On Release only (by setting the SRIAndBatchManageMethod to bomm_OnReleaseOnly). The property is set by the Automatic Serial Number Creation On Receipt check box.
- `Public Property ManageStockByWarehouse() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the inventory is managed by the warehouse quantity levels.
  - remarks: This property determines how the system calculates minimal and maximal stock quantities. When set to Yes, the system refers to the values of the MinInventoy, DesiredInventory, and MaxInventory in the warehouse.
- `Public Property Manufacturer() As Long` [R/W] Sets or returns the manufacturer code of the item (foreign key of the Manufacturers object). Mandatory property.
- `Public Property MaterialGroup() As Long` [R/W] Sets or returns the Item's Material Group. Field name: MatGrp. This is a foreign key to the Material Group OMGP object, not exposed through the DI API.
  - remarks: For Brazil only.
- `Public Property MaterialType() As BoMaterialTypes` [R/W] Sets or returns a valid value of BoMaterialTypes that determines current material state from Raw Material to Finished Goods. Field name: MatType.
  - remarks: For Brazil only.
- `Public Property MaxInventory() As Double` [R/W] Sets or returns the maximum inventory quantity for this item.
  - remarks: The maximum inventory quantity can be used as a threshold to provide an alert message.
- `Public Property MinInventory() As Double` [R/W] Sets or returns the minimum inventory quantity for this item.
  - remarks: The minimum inventory quantity can be used as a threshold to provide an alert message or a recommendation for purchasing.
- `Public Property MinOrderQuantity() As Double` [R/W] Sets or returns this Item Minimum Order Quantity limitation . Field name: MinOrdrQty.
  - remarks: To display the form in the application: - Select Inventory --> Item Master Data --> Planning Data --> Minimum Order Qty .
- `Public Property MovingAveragePrice() As Double` [R] Returns the average price of an item calculated according to quantities and prices.
  - remarks: SAP Business One evaluates inventories with the moving average price on an ongoing basis. This means a valuation takes place based on the corresponding quantities and prices for each goods receipt and issue, and the moving average price is updated accordingly. The valuation price is calculated as the quantity multiplied by the average price. Assuming prices will increase over time, the items in stock will be overvalue. This gain is not as high as under the FIFO method, but greater than under the LIFO method.
- `Public Property NCMCode() As Long` [R/W] Returns the item classification issued by the Brazilian government and used to determine the IPI tax rate. NCM stands for Nomenclatura Commun do Mercosul. Field name: NCMCode This is a foreign key to the NCM Code table (ONCM), which is exposed via the NCMCodesSetupService object.
  - remarks: Relevant for Brazil only.
- `Public Property NoDiscounts() As BoYesNoEnum` [R/W] property NoDiscounts
- `Public Property NVECode() As String` [R/W] Enter the NVE code. Field name: NVECode. Length: 6 characters.
- `Public Property OrderIntervals() As String` [R/W] Sets or returns the inventory cycle such as, every week on Monday, or every first day of the month. The inventory cycles are defined in SAP Business One (OCYC table, which is not exposed through the DI API).
- `Public Property OrderMultiple() As Double` [R/W] Sets or returns the multiple quantity in addition to the minimum quantity of items in a single order.
  - remarks: For example: If the minimum order quantity is 1000 items and multiple quantity is 500 items, then the allowed quantity in a single order can be: 1000, 1500, 2000, and so on.
- `Public Property OutgoingServiceCode() As Long` [R/W] Sets or returns the Outgoing Service Code. Field name: OSvcCode. This is a foreign key to the Service Code Table (OSCD), not exposed through the DI API.
  - remarks: The OutgoingServiceCode Property is applicable for cluster B only (country-specific for Brazil only).
- `Public Property PeriodControls() As ItemsPeriodControls` [R] Returns the ItemsPeriodControls child object.
- `Public Property Picture() As String` [R/W] Sets or returns the picture file name to attach to an item. Field name: PicturName. Length: 200 characters.
  - remarks: Do not include the full path , only the file name. You can use BitMapPath property to read or change the path.
- `Public Property PlanningSystem() As BoPlanningSystem` [R/W] Sets or returns a valid value of BoPlanningSystem type that specifies the inventory planning system: MRP or None.
- `Public Property PreferredVendors() As Items_PreferredVendors` [R] Returns the Items_PreferredVendors child object.
- `Public Property PriceList() As Items_Prices` [R] Returns the Items_Prices child object.
- `Public Property PricingUnit() As Long` [R/W] property PricingUnit
- `Public Property ProcurementMethod() As BoProcurementMethod` [R/W] Sets or returns a valid value of BoProcurementMethod type that specifies the procurement method of items: Buy or Make.
- `Public Property ProdStdCost() As Double` [R/W] property ProdStdCost
- `Public Property ProductSource() As Long` [R/W] Sets or returns a valid value of BoProductSources that determines the product source. Field name: ProductSrc.
  - remarks: The ProductSource Property applicable for cluster B only (country-specific for Brazil only).
- `Public Property Projects() As ItemsProjects` [R] Returns the ItemsProjects child object.
- `Public Property Properties(ByVal GroupNum As Long) As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item belongs to one or more query groups.
  - remarks: In SAP Business One, there are 64 properties users can assign to an item. These properties are typically used for creating cross-section reports. Additionally, each item can be assigned to a group describing the different characteristic of the item. By grouping items, users can create reports based on these groups.
- `Public Property PurchaseFactor1() As Double` [R/W] Sets or returns the factor #1 by which the base price list is multiplied to calculate the purchase prices.
  - remarks: The price calculation takes into account all purchase factors 1-4. Therefore, the default factor must be 1.
- `Public Property PurchaseFactor2() As Double` [R/W] Sets or returns the factor #2 by which the base price list is multiplied to calculate the purchase prices.
  - remarks: The price calculation takes into account all purchase factors 1-4. Therefore, the default factor must be 1.
- `Public Property PurchaseFactor3() As Double` [R/W] Sets or returns the factor #3 by which the base price list is multiplied to calculate the purchase prices.
  - remarks: The price calculation takes into account all purchase factors 1-4. Therefore, the default factor must be 1.
- `Public Property PurchaseFactor4() As Double` [R/W] Sets or returns the factor #4 by which the base price list is multiplied to calculate the purchase prices.
  - remarks: The price calculation takes into account all purchase factors 1-4. Therefore, the default factor must be 1.
- `Public Property PurchaseHeightUnit() As Long` [R/W] Sets or returns the units for the purchase unit width (cm, inch, etc.). Length: 6 characters.
- `Public Property PurchaseHeightUnit1() As Long` [R/W] Sets or returns the secondary units for the purchase unit width (cm, inch, etc.).
- `Public Property PurchaseItem() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is for purchase (for example, an item can be defined as an asset).
- `Public Property PurchaseItemsPerUnit() As Double` [R/W] Sets or returns the number of items per purchasing unit.
  - remarks: For example, an item, which is sold in bottles, is purchased in crates of 12 bottles. The items per purchasing unit is, in this case, 12.
- `Public Property PurchaseLengthUnit() As Long` [R/W] Sets or returns the units for the purchase unit length (cm, inches, etc.).
- `Public Property PurchaseLengthUnit1() As Long` [R/W] Sets or returns the secondary units for the purchase unit length (cm, inches, etc.).
- `Public Property PurchasePackagingUnit() As String` [R/W] Sets or returns the purchase packaging unit. Length: 8 characters.
- `Public Property PurchaseQtyPerPackUnit() As Double` [R/W] Sets or returns the number of items per purchase packaging unit.
- `Public Property PurchaseUnit() As String` [R/W] Sets or returns the purchasing unit. For example, an item, which is sold in bottles, is purchased in crates of 12 bottles. The purchasing unit is, in this case, a crate. Length: 5 characters.
- `Public Property PurchaseUnitHeight() As Double` [R/W] Sets or returns the height of the purchase unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property PurchaseUnitHeight1() As Double` [R/W] Sets or returns the secondary height of the purchase unit.
- `Public Property PurchaseUnitLength() As Double` [R/W] Sets or returns the length of the purchase unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property PurchaseUnitLength1() As Double` [R/W] Sets or returns the secondary length of the purchase unit.
- `Public Property PurchaseUnitVolume() As Double` [R/W] Sets or returns the volume of the purchase unit.
  - remarks: The system calculates the item's volume automatically if the HxWxL dimensions are set.
- `Public Property PurchaseUnitWeight() As Double` [R/W] Sets or returns the weight of the purchase unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property PurchaseUnitWeight1() As Double` [R/W] Sets or returns the secondary weight of the purchase unit.
- `Public Property PurchaseUnitWidth() As Double` [R/W] Sets or returns the width of the purchase unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property PurchaseUnitWidth1() As Double` [R/W] Sets or returns the secondary width of the purchase unit.
- `Public Property PurchaseVATGroup() As String` [R/W] Sets or returns the VAT group for a purchase item. Length: 8 characters.
  - remarks: This property is mandatory only for countries that calculate VAT per line/item.
- `Public Property PurchaseVolumeUnit() As Long` [R/W] Sets or returns the units for the purchase unit volume (m3, ft3, litter, gallon, etc.).
- `Public Property PurchaseWeightUnit() As Long` [R/W] Sets or returns the units for the purchase unit weight (kg, lb, etc.).
- `Public Property PurchaseWeightUnit1() As Long` [R/W] Sets or returns the secondary units for the purchase unit weight (kg, lb, etc.).
- `Public Property PurchaseWidthUnit() As Long` [R/W] Sets or returns the units for the purchase unit width (cm, inch, etc.).
- `Public Property PurchaseWidthUnit1() As Long` [R/W] Sets or returns the secondary units for the purchase unit width (cm, inch, etc.).
- `Public Property QuantityOnStock() As Double` [R] Sets or returns the total quantity of the item in the warehouse.
  - remarks: In these fields, the system displays the physical stock levels actually in the warehouse, the quantities that have been ordered from vendors, and the quantities promised to customers.On the basis of this information, the system calculates the actual quantity that is available in stock.
- `Public Property QuantityOrderedByCustomers() As Double` [R] Sets or returns the total quantity of the items ordered by customers.
- `Public Property QuantityOrderedFromVendors() As Double` [R] Sets or returns the total quantity of the items ordered from vendors.
- `Public Property SACEntry() As Long` [R/W] property SACEntry
- `Public Property SalesFactor1() As Double` [R/W] Sets or returns the factor #1 by which the base price list is multiplied to calculate the sale prices.
  - remarks: The price calculation takes into account all sales factors 1-4. Therefore, the default factor must be 1.
- `Public Property SalesFactor2() As Double` [R/W] Sets or returns the factor #2 by which the base price list is multiplied to calculate the sale prices.
  - remarks: The price calculation takes into account all sales factors 1-4. Therefore, the default factor must be 1.
- `Public Property SalesFactor3() As Double` [R/W] Sets or returns the factor #3 by which the base price list is multiplied to calculate the sale prices.
  - remarks: The price calculation takes into account all sales factors 1-4. Therefore, the default factor must be 1.
- `Public Property SalesFactor4() As Double` [R/W] Sets or returns the factor #4 by which the base price list is multiplied to calculate the sale prices.
  - remarks: The price calculation takes into account all sales factors 1-4. Therefore, the default factor must be 1.
- `Public Property SalesHeightUnit() As Long` [R/W] Sets or returns the units for the sales unit height (cm, inch, etc.).
- `Public Property SalesHeightUnit1() As Long` [R/W] Sets or returns the secondary units for the sales unit height (cm, inch, etc.).
- `Public Property SalesItem() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is a sales item.
- `Public Property SalesItemsPerUnit() As Double` [R/W] Sets or returns the number of items per sales unit.
- `Public Property SalesLengthUnit() As Long` [R/W] Sets or returns the units for the sales unit length (cm, inch, etc.).
- `Public Property SalesLengthUnit1() As Long` [R/W] Sets or returns the secondary units for the sales unit length (cm, inch, etc.).
- `Public Property SalesPackagingUnit() As String` [R/W] Sets or returns the sales packaging unit. Length: 8 characters.
- `Public Property SalesQtyPerPackUnit() As Double` [R/W] Sets or returns the number of items per sales packaging unit.
- `Public Property SalesUnit() As String` [R/W] Sets or returns the sales unit. Length: 5 characters.
  - remarks: In SAP Business One, users can distinguish between sales unit and purchasing using. For example, an item that is purchased in creates of 12 bottles is sold in packages of 6 bottles. The purchasing unit is "crate with 12 bottles", and the sales unit "package with 6 bottles". One sales unit contains half a unit of the purchasing unit. All sales transactions, including the associated documents, are performed with the sales unit. However, the warehouse stock is managed on the basis of the smallest unit, which, in this example, is a bottle.
- `Public Property SalesUnitHeight() As Double` [R/W] Sets or returns the height of the sales unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitHeight1() As Double` [R/W] Sets or returns the secondary height of the sales unit.
- `Public Property SalesUnitLength() As Double` [R/W] Sets or returns the length of the sales unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitLength1() As Double` [R/W] Sets or returns the secondary length of the sales unit.
- `Public Property SalesUnitVolume() As Double` [R/W] Sets or returns the volume of the sales unit.
  - remarks: The system calculates the item's volume automatically if the HxWxL dimensions are set. If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitWeight() As Double` [R/W] Sets or returns the weight of the sales unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitWeight1() As Double` [R/W] Sets or returns the secondary weight of the sales unit.
- `Public Property SalesUnitWidth() As Double` [R/W] Sets or returns the width of the sales unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitWidth1() As Double` [R/W] Sets or returns the secondary width of the sales unit.
- `Public Property SalesVATGroup() As String` [R/W] Sets or returns the VAT group for a sales item. Length: 8 characters.
  - remarks: This property is mandatory only for countries that calculate VAT per line/item.
- `Public Property SalesVolumeUnit() As Long` [R/W] Sets or returns the units for the sales unit volume (m3, ft3, litter, gallon, etc.).
- `Public Property SalesWeightUnit() As Long` [R/W] Sets or returns the units for the sales unit weight (kg, lb, etc.).
- `Public Property SalesWeightUnit1() As Long` [R/W] Sets or returns the secondary units for the sales unit weight (kg, lb, etc.). Length: 6 characters.
- `Public Property SalesWidthUnit() As Long` [R/W] Sets or returns the units for the sales unit width (cm, inch, etc.). Length: 6 characters.
- `Public Property SalesWidthUnit1() As Long` [R/W] Sets or returns the secondary units for the sales unit width (cm, inch, etc.).
- `Public Property ScsCode() As String` [R/W] property ScsCode
- `Public Property SerialNum() As String` [R/W] Sets or returns the serial number of the item. Length: 17 characters.
  - remarks: In SAP Business One, users can manage items by serial numbers so that providing additional information such as, items location in the warehouse, manufacturing date, warranty data, and so on. The work method is to enter serial numbers during stock entries for items that have a definition of serial numbers management, and to choose relevant serial numbers during sales or release documents.
- `Public Property Series() As Long` [R/W] property Series
- `Public Property ServiceCategoryEntry() As Long` [R/W] property ServiceCategoryEntry
- `Public Property ServiceGroup() As Long` [R/W] Sets or returns the Item's Service Group. Field name: ServiceGrp. This is a foreign key to the OSGP object, not exposed through the DI API.
  - remarks: The ServiceGroup Property is applicable for cluster B only (country-specific for Brazil only).
- `Public Property ShipType() As Long` [R/W] Sets or returns the shipping type of the item (air cargo, courier, etc.).
- `Public Property SOIExcisable() As SOIExcisableTypeEnum` [R/W] property SOIExcisable
- `Public Property SpProdType() As SpecialProductTypeEnum` [R/W] property SpProdType
- `Public Property SRIAndBatchManageMethod() As BoManageMethod` [R/W] Sets or returns a valid value that specifies the method for managing serial numbers and batch numbers.
  - remarks: Relevant only when one of the properties ManageBatchNumbers and ManageSerialNumbers is set to 1.
- `Public Property StatisticalAsset() As BoYesNoEnum` [R/W] Indicates whether the asset is only a statistical asset that is not owned by your company. Field name: StatAsset.
- `Public Property SupplierCatalogNo() As String` [R/W] Sets or returns the item catalog number as provided by the main supplier. Length: 17 characters.
- `Public Property SWW() As String` [R/W] Sets or returns an additional identifier of the item. Length: 16 characters.
- `Public Property TaxType() As BoTaxTypes` [R/W] Sets or returns a valid value of BoTaxTypes type that specifies the sales tax system for the item.
  - remarks: Country-specific property for USA and Canada.
- `Public Property Technician() As Long` [R/W] Assign an employee for maintenance of the asset. Field name: Technician.
- `Public Property TNVED() As String` [R/W] property TNVED
- `Public Property ToleranceDays() As Long` [R/W] property ToleranceDays
- `Public Property TraceableItem() As BoYesNoEnum` [R/W] Indicate whether the item is traceable. Field name: Traceable.
- `Public Property TreeType() As BoItemTreeTypes` [R] Returns a valid value of BoItemTreeTypes type that specifies the product tree type of the item (also known as bill of material type).
- `Public Property TypeOfAdvancedRules() As TypeOfAdvancedRulesEnum` [R/W] Indicates whether the advanced rule type assigned to an item is General, Warehouse, or Item Group. You can change the advanced rule type if required. Field name: GLPickMeth.
  - remarks: For additional information about advanced rule type assignment, see the How To Setup and Work with Advanced G/L Account Determination guide in the documentation resource center.
- `Public Property UnitOfMeasurements() As ItemUnitOfMeasurements` [R] Returns the ItemUnitOfMeasurements child object.
- `Public Property UoMGroupEntry() As Long` [R/W] The internal key of a unit of measurement group. Field name: UgpEntry.
- `Public Property UpdateDate() As Date` [R] The date when the item master data updated. Field name: UpdateDate.
- `Public Property UpdateTime() As Date` [R] The timestamp of the item master data updated is recorded in the hhmmss format. Field name: UpdateTS.
- `Public Property User_Text() As String` [R/W] Sets or returns a free text string for this item. Length: 10 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Valid() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is valid.
  - remarks: For items set to not valid, the end-user can specify the period when the item is valid (ValidFrom and ValidTo), and also add remarks (ValidRemarks).
- `Public Property ValidFrom() As Date` [R/W] Sets or returns the start date of the item's validity.
- `Public Property ValidRemarks() As String` [R/W] Sets or returns the remarks regarding the validity period. Length: 30 characters.
- `Public Property ValidTo() As Date` [R/W] Sets or returns the end date of the item's validity.
- `Public Property VatLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is subject to VAT.
  - remarks: Set to to Yes, if business transactions with this item are liable to VAT.
- `Public Property VirtualAssetItem() As BoYesNoEnum` [R/W] property VirtualAssetItem
- `Public Property WarrantyTemplate() As String` [R/W] Sets or returns the template for service warranty. Length: 20 characters.
- `Public Property WhsInfo() As ItemWarehouseInfo` [R] Returns the ItemWarehouseInfo object.
- `Public Property WTLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is subject to Withholding tax.
  - remarks: Set to to Yes, if business transactions with this item are liable to the Withholding tax.

## Methods (10)
- `Public Function Add() As Long` Adds a new record to the OITM table. Adds a record to the object table in SAP Business One company database.
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ItemCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ItemCode`: Specifies the identification key of the item (see ItemCode property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
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
- `Public Function UpdateFromXML(ByVal FileName As String) As Long` Receives and processes the XML content. You can remove sub-object lines from the Items object via the XML file.
  - param `FileName`: 
  - C# example (from SAP's help):
    ```csharp
    vComp.XmlExportType = BoXmlExportTypes.xet_ExportImportMode;
    Items myitems = (Items)vComp.GetBusinessObject(BoObjectTypes.oItems);
    //save an item to XML
    myitems.GetByKey("item0");
    myitems.SaveXML(@"C:\Test\mytest1.xml");

    //Delete sub line directly from C:\Test\mytest1.xml by manual

    //Update the item
    myitems.UpdateFromXML(@"C:\Test\mytest1.xml");
    ```

# Items_PreferredVendors (Object)

Items_PreferredVendors is a child object of the Items object that represents the preferred vendor for the item. Source table: ITM2

## Properties (3)
- `Public Property BPCode() As String` [R/W] The code of the vendor. Field name: VendorCode. Length: 15 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property UserFields() As UserFields` [R] Get User Fields

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Items_Prices (Object)

Items_Prices is a child object of the Items object that represents the items' prices in the Inventory and Production module. This object enables you to specify prices for various price lists. Source table: ITM1

**Remarks:** Mandatory fields in SAP Business One: Price and PriceList. To display the form in the application: - Select Inventory --> Item Master Data. - Select a Price List, and set a price.

**Example:**
- example note: The sample prints the pricelist of the Item and updates the price of the Item in the current price list.
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
         Dim lErrCode As Long

          Dim sErrMsg As String

          Dim bRetVal As Boolean

          Dim oItems As SAPbobsCOM.Items

          Dim oItemPrice As SAPbobsCOM.Items_Prices

          Dim i As Integer

          'Retrieve Items object

          oItems = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oItems)

          'Retrieve specific item

          bRetVal = oItems.GetByKey("X0004")

          'Check errors

          If Not bRetVal Then

              oCompany.GetLastError(lErrCode, sErrMsg)

              MsgBox("Failed to Retrieve the record " & lErrCode & " " & sErrMsg)

              Exit Sub

          End If

          'get item price object

          oItemPrice = oItems.PriceList

          'print price lists names and prices

          For i = 0 To oItemPrice.Count - 1

              oItemPrice.SetCurrentLine(i)

              'print price list name

              Debug.WriteLine(oItemPrice.PriceListName())

              'print the items price

              Debug.WriteLine(oItemPrice.Price())

          Next

          'change the price of the item in the last price list

          oItemPrice.Price = 600

          'save changes

          oItems.Update()
  ```

## Properties (13)
- `Public Property AdditionalCurrency1() As String` [R/W] property AdditionalCurrency1
- `Public Property AdditionalCurrency2() As String` [R/W] property AdditionalCurrency2
- `Public Property AdditionalPrice1() As Double` [R/W] property AdditionalPrice1
- `Public Property AdditionalPrice2() As Double` [R/W] property AdditionalPrice2
- `Public Property BasePriceList() As Long` [R/W] property BasePriceList
- `Public Property Count() As Long` [R] Returns the number of prices for the current item.
  - remarks: When you add a new price, the value is increased automatically.
- `Public Property Currency() As String` [R/W] Sets or returns the price currency used in the document row. Field name: Currency. Length: 3 characters.
  - remarks: You must define the currency strings before using this property. One business transaction may include more than one currency. In multiple currencies transaction, first call the GetCurrencyRate method to unify the total amount in different currencies into one currency. The value for multiple currencies is ##.
- `Public Property Factor() As Double` [R/W] property Factor
- `Public Property Price() As Double` [R/W] Sets or returns the item price before taxation. Mandatory property.
- `Public Property PriceList() As Long` [R] Returns the price list index for the item.
- `Public Property PriceListName() As String` [R] Returns the price list name. Length: 32 characters.
- `Public Property UoMPrices() As UoMPrices` [R] property UoMPrices
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
