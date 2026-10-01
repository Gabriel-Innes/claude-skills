<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# TaxReportFilter (Object)

TaxReportFilter is a data structure related to the TaxReportsService. Source table: OVTR.

## Properties (35)
- `Public Property AppendixOorPSelection() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not this Appendix is O or P selection. Field name: ApndxOOrP.
- `Public Property Cancellation() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not cancelation is required for For EU Sales Report. Field name: ApndxOOrP.
- `Public Property Code() As Long` [R] Returns the Abs Entry (numerator) of this tax report. Field name: AbsEntry.
- `Public Property DeclarationType() As TaxReportFilterDeclarationType` [R/W] Sets or returns a valid value that determines whether this declaration type is original, substitute or complementary. Field name: Declration.
- `Public Property DiplayCreditMemosInSeparateColumn() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to display credit memos in separate column. Field name: CreditMemo.
- `Public Property DocumentType() As TaxReportFilterApArDocumentType` [R/W] Sets or returns a valid value that determines whether or not this document is an A/P Document or an A/R Document. Field name: DocType.
- `Public Property ExcludeWT() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to exclude withholding tax for this report. Field name: ExcludeWT.
- `Public Property FilterType() As TaxReportFilterType` [R/W] Sets or returns a valid value that determines the Selection Criteria Type to be used with this report. Field name: Selection Criteria Type.
- `Public Property FirstPrintedNumber() As Long` [R/W] Sets or returns the first printed number in this report. Field name: FirstPrint.
- `Public Property FirstRegisterNumber() As Long` [R/W] Sets or returns the first register number in this report. Field name: FirstReg.
- `Public Property FromDate() As Date` [R/W] Sets or returns this report period start date. Field name: FromDate.
- `Public Property FromSeries() As Long` [R/W] Sets or returns this report first Series. Field name: FromSeries.
- `Public Property HideTaxWithoutTransaction() As BoYesNoEnum` [R/W] Determines whether or not to hide tax without Transaction. Field name: HideNTrans.
- `Public Property IncludeCustomers() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines whether or not to include customers in this report. Field name: CustomerIn.
- `Public Property IncludeDocumentType() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include document type in report. Field name: DocTyp.
- `Public Property IncludeGLAccounts() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include GL Accounts in this report. Field name: AccountIn.
- `Public Property IncludeSeriesFilter() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include series filter in this report. Field name: SerieeIn.
- `Public Property IncludeVendors() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include vendors in this report . Field name: VendorIn.
- `Public Property Name() As String` [R/W] Sets or returns this report name. Field name: ReportName. Length: 50 characters.
- `Public Property OpeningAndClosingBalance() As BoYesNoEnum` [R/W] Sets or returns the opening and closing balance of this report. Field name: DispOBCB.
- `Public Property Period() As TaxReportFilterPeriod` [R/W] Sets or returns the tax report filter period of this report. Field name: Period.
- `Public Property Quarter() As Long` [R/W] Sets or returns the quarter number of this report . Field name: quarter.
- `Public Property QuarterOrDates() As TaxReportFilterQuarterOrDates` [R/W] Sets or returns a valid value that determines wether this report period is defined by quarters or by start / end dates. Field name: DateRBtn.
- `Public Property ReportLayout() As TaxReportFilterReportLayoutType` [R/W] Sets or returns a valid value that determines the report layout, register book, declaration or base layout. Field name: RptLayout.
- `Public Property RoundAmount() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to round this report amount. Field name: RoundSum.
- `Public Property ShowPaymentsWithDeferredTax() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not . Field name: DeferTaxIn.
- `Public Property TaxDate() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to include tax date. Field name: TaxDate.
- `Public Property TaxReportAccounts() As TaxReportAccounts` [R] Returns the TaxReportAccounts object, a Data Collection of TaxReportAccount data structures.
- `Public Property TaxReportBusinessPartners() As TaxReportBusinessPartners` [R] Returns the TaxReportBusinessPartners object, a Data Collection of TaxReportBusinessPartner data structures.
- `Public Property TaxReportDocuments() As TaxReportDocuments` [R] Returns the TaxReportDocuments object, a Data Collection of TaxReportDocument data structures.
- `Public Property TaxReportGroups() As TaxReportGroups` [R] Returns the TaxReportGroups object, a Data Collection of TaxReportGroup data structures.
- `Public Property TaxReportSeriesCollection() As TaxReportSeriesCollection` [R] Returns the TaxReportSeriesCollection object, a Data Collection of TaxReportSeries data structures.
- `Public Property ToDate() As Date` [R/W] Sets or returns the end date of this report period. Field name: ToDate.
- `Public Property ToSeries() As Long` [R/W] Sets or returns the last Series of this report . Field name: ToSeries.
- `Public Property Year() As Long` [R/W] Sets or returns the year field of this document date. Field name: Year.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportFilterParams (Object)

The TaxReportFilterParams specifies the identification key combination(Code, Filter-Type and Name) for which the TaxReportsService is related. Source table: OVTR.

## Properties (3)
- `Public Property Code() As Long` [R/W] Sets or returns the unique code of this tax report filter. Field name: AbsEntry.
- `Public Property FilterType() As TaxReportFilterType` [R/W] Sets or returns a valid value that determines selection criteria type for this report. Field name: FilterType.
- `Public Property Name() As String` [R] Returns this report name . Field name: ReportName. Length: 50 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the index of the item that you want to get.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Creates an XML string that represents the object data.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportFiltersParams (Collection)

TaxReportFiltersParams is a Data Collection of TaxReportFilterParams Identification key combination. Source table: OVTR.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportFilterParams identification keys in the TaxReportFiltersParams data collection.

## Methods (5)
- `Public Function Add() As TaxReportFilterParams` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportFilterParams` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportGroup (Object)

TaxReportGroup is a data structure related to the TaxReportsService. Source table: VTR1.

## Properties (2)
- `Public Property Code() As String` [R/W] Sets or returns this tax report grou[p code. Field name: ObjectCode.
- `Public Property Sum() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not sum this report group. Field name: Sum.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportGroups (Collection)

TaxReportGroups is a Data Collection of TaxReportGroupss. Source table: VTR1.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportGroups in the TaxReportGroups data collection.

## Methods (5)
- `Public Function Add() As TaxReportGroup` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportGroup` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportSeries (Object)

TaxReportSeries is a data structure related to the TaxReportsService. Source table: VTR3.

## Properties (2)
- `Public Property DocumentType() As TaxReportFilterDocumentType` [R/W] Sets or returns a valid value that determines DocumentType. Field name: ObjectCode.
- `Public Property SeriesCode() As Long` [R/W] Sets or returns this document series code. Field name: SeriesCode.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# TaxReportSeriesCollection (Collection)

TaxReportSeriesCollection is a Data Collection of TaxReportSeries. Source table: VTR3.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportSeries. in the TaxReportSeriesCollection data collection. Field name: .

## Methods (5)
- `Public Function Add() As TaxReportSeries` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportSeries` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates XML file that represents the object data.

# TaxWebSite (Object)

TaxWebSite Class

## Properties (4)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property Description() As String` [R/W] property Description
- `Public Property WebSiteName() As String` [R/W] property WebSiteName
- `Public Property WebSiteURL() As String` [R/W] property WebSiteURL

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxWebSiteParams (Object)

TaxWebSiteParams Class

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property WebSiteName() As String` [R] property WebSiteName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxWebSitesParams (Collection)

TaxWebSitesParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TaxWebSiteParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TaxWebSiteParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TaxWebSitesService (Object)

TaxWebSitesService Class

## Methods (10)
- `Public Function AddTaxWebSite(ByVal pITaxWebSite As TaxWebSite) As TaxWebSiteParams` AddTaxWebSite
  - param `pITaxWebSite`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TaxWebSitesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TaxWebSitesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetDefaultWebSite() As TaxWebSiteParams` GetDefaultWebSite
- `Public Function GetTaxWebSite(ByVal pITaxWebSiteParams As TaxWebSiteParams) As TaxWebSite` GetTaxWebSite
  - param `pITaxWebSiteParams`: 
- `Public Function GetTaxWebSiteList() As TaxWebSitesParams` GetTaxWebSiteList
- `Public Sub RemoveTaxWebSite(ByVal pITaxWebSiteParams As TaxWebSiteParams)` RemoveTaxWebSite
  - param `pITaxWebSiteParams`: 
- `Public Sub SetAsDefault(ByVal pITaxWebSiteParams As TaxWebSiteParams)` SetAsDefault
  - param `pITaxWebSiteParams`: 
- `Public Sub UpdateTaxWebSite(ByVal pITaxWebSite As TaxWebSite)` UpdateTaxWebSite
  - param `pITaxWebSite`: 

# TeamCounter (Object)

A group of counters' counting results of an item at a storage location add up to its total quantity. Source table: INC4.

## Properties (6)
- `Public Property CounterID() As Long` [R/W] The ID of the counter. Field name: CounterId.
- `Public Property CounterName() As String` [R] The name of the counter. Field name: CounteName.
- `Public Property CounterNumber() As Long` [R/W] The number of the counter. Field name: CounteNum.
- `Public Property CounterType() As CounterTypeEnum` [R/W] The type of the counter. Field name: CounteType.
- `Public Property CounterVisualOrder() As Long` [R] The visual order number of the counter. The value for the first row is null, and from the second row the number starts from 1. Field name: VisOrder.
- `Public Property DocumentEntry() As Long` [R] The internal key of the inventory counting. Field name: DocEntry.

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

# TeamCounters (Collection)

A collection of TeamCounter objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As TeamCounter` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As TeamCounter` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# TeamMembers (Object)

TeamMembers is a child object of the Teams object that represents the membership role in a team of an employee. An employee can be a Member or a Leader of more than one team. Source table: HTM1.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Membership tab.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total rows in the table.
  - remarks: When you add a data row, the value of this property is incremented automatically.
- `Public Property EmployeeID() As Long` [R/W] Sets or returns the employee ID as defined by EmployeesInfo object.
- `Public Property RoleInTeam() As BoRoleInTeam` [R/W] Sets or returns a valid value of BoRoleInTeam type that specifies whether the employee is a Member or a Leader of the team.
- `Public Property TeamID() As Long` [R] Returns the team identification key.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# Teams (Object)

Teams is a business object that represents the list of teams from which team memberships of an employee can be selected. An employee can be a Member or a Leader of more than one team. Source table: OHTM.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Membership tab. - From the Team list box, click Define New.

## Properties (6)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Description() As String` [R/W] Sets or returns a memo type string that specifies the description for the team name. Length: 64,000 characters.
- `Public Property TeamID() As Long` [R] Returns the identification key of the team.
  - remarks: This is a sequential number assigned by SAP Business One automatically, starting from 1, when adding a new team to the list. Property type Read-only property " -->
- `Public Property TeamMembers() As TeamMembers` [R] Returns the TeamMembers child object.
- `Public Property TeamName() As String` [R/W] Sets or returns the team name. Length: 20 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lTeamID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lTeamID`: Primary key: TeamID.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
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

# TechnicianSchedulings (Object)

TechnicianSchedulings Class

## Properties (5)
- `Public Property EndDate() As Date` [R] property EndDate
- `Public Property IsClosed() As BoYesNoEnum` [R] property IsClosed
- `Public Property SchedulingLineNum() As Long` [R] property SchedulingLineNum
- `Public Property ServiceCallID() As Long` [R] property ServiceCallID
- `Public Property StartDate() As Date` [R] property StartDate

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TechnicianSchedulingsCollection (Collection)

TechnicianSchedulingsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TechnicianSchedulings` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TechnicianSchedulings` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TechnicianSchedulingsParams (Object)

TechnicianSchedulingsParams Class

## Properties (3)
- `Public Property EndDate() As Date` [R/W] property EndDate
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property Technician() As Long` [R/W] property Technician

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TechnicianSettings (Object)

TechnicianSettings Class

## Properties (2)
- `Public Property GroupCode() As Long` [R/W] property GroupCode
- `Public Property Technician() As Long` [R/W] property Technician

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TechnicianSettingsGroup (Object)

TechnicianSettingsGroup Class

## Properties (11)
- `Public Property AdvancedDashBoard() As Long` [R/W] property AdvancedDashBoard
- `Public Property Code() As Long` [R] property Code
- `Public Property CustomizedGroup() As BoYesNoEnum` [R/W] property CustomizedGroup
- `Public Property EnableActualDuration() As BoYesNoEnum` [R/W] property EnableActualDuration
- `Public Property EnableEditTime() As BoYesNoEnum` [R/W] property EnableEditTime
- `Public Property EnableFollowup() As BoYesNoEnum` [R/W] property EnableFollowup
- `Public Property EnableReject() As BoYesNoEnum` [R/W] property EnableReject
- `Public Property EnableResign() As BoYesNoEnum` [R/W] property EnableResign
- `Public Property EnableSignature() As BoYesNoEnum` [R/W] property EnableSignature
- `Public Property EnableStarRating() As BoYesNoEnum` [R/W] property EnableStarRating
- `Public Property Name() As String` [R/W] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TechnicianSettingsGroupParams (Object)

TechnicianSettingsGroupParams Class

## Properties (2)
- `Public Property Code() As Long` [R/W] property Code
- `Public Property Name() As String` [R/W] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TechnicianSettingsParams (Object)

TechnicianSettingsParams Class

## Properties (1)
- `Public Property Technician() As Long` [R/W] property Technician

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TerminationReason (Object)

TerminationReason Class

## Properties (3)
- `Public Property Description() As String` [R/W] property Description
- `Public Property Name() As String` [R/W] property Name
- `Public Property ReasonID() As Long` [R] property ReasonID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TerminationReasonParams (Object)

TerminationReasonParams Class

## Properties (3)
- `Public Property Description() As String` [R] property Description
- `Public Property Name() As String` [R] property Name
- `Public Property ReasonID() As Long` [R/W] property ReasonID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TerminationReasonParamsCollection (Collection)

TerminationReasonParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TerminationReasonParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TerminationReasonParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TerminationReasonService (Object)

TerminationReasonService Class

## Methods (8)
- `Public Function Add(ByVal pITerminationReason As TerminationReason) As TerminationReasonParams` Add
  - param `pITerminationReason`: 
- `Public Sub Delete(ByVal pITerminationReasonParams As TerminationReasonParams)` Delete
  - param `pITerminationReasonParams`: 
- `Public Function Get(ByVal pITerminationReasonParams As TerminationReasonParams) As TerminationReason` Get
  - param `pITerminationReasonParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TerminationReasonServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TerminationReasonServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As TerminationReasonParamsCollection` GetList
- `Public Sub Update(ByVal pITerminationReason As TerminationReason)` Update
  - param `pITerminationReason`: 

# Territories (Object)

Territories is a business object that represents the territory segmentation. This object is part of the Business Partners module. Territories are segments of the market that are defined by attributes such as geographical locations, product lines, and so on. This object enables you to: - Add a territory segmentation. - Retrieve a territory segmentation by its key. - Update a territory segmentation. - Remove a territory segmentation. - Save the object in XML format. Source table: OTER.

**Remarks:** Mandatory fields in SAP Business One: Description, LocationIndex, and Parent (only in case of a child territory). To display the form in the application: - Select Administration --> Setup --> General --> Define Territories.

## Properties (7)
- `Public Property Browser() As DataBrowser` [R] Retrieves the DataBrowser object.
- `Public Property Description() As String` [R/W] Sets or returns the territory name. Mandatory property. Length: 200 characters.
- `Public Property Inactive() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the territory is inactive.
- `Public Property LocationIndex() As Long` [R/W] Sets or returns the territory location order in the hierarchal relationship (first, after specific territory, or last). Mandatory property.
- `Public Property Parent() As Long` [R/W] Sets or returns the parent territory (in case of a child territory). Mandatory field in SAP Business One only in case of a child territory.
- `Public Property TerritoryID() As Long` [R] Returns the ID number (key) of the territory. SAP Business One creates a sequential number for each territory that you add.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lID`: Territory ID number (TerritoryID).
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

# TrackingNote (Object)

TrackingNote Class

## Properties (8)
- `Public Property CCDNumber() As String` [R/W] property CCDNumber
- `Public Property CountryOfOrigin() As String` [R/W] property CountryOfOrigin
- `Public Property CustomsTerminal() As String` [R/W] property CustomsTerminal
- `Public Property Date() As Date` [R/W] property Date
- `Public Property IsDirectImport() As BoYesNoEnum` [R/W] property IsDirectImport
- `Public Property TrackingNoteBrokerCollection() As TrackingNoteBrokerCollection` [R] property TrackingNoteBrokerCollection
- `Public Property TrackingNoteItemCollection() As TrackingNoteItemCollection` [R] property TrackingNoteItemCollection
- `Public Property TrackingNoteNumber() As Long` [R] property TrackingNoteNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TrackingNoteBroker (Object)

TrackingNoteBroker Class

## Properties (4)
- `Public Property AgreementNumber() As Long` [R/W] property AgreementNumber
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property TrackingNoteLineNumber() As Long` [R] property TrackingNoteLineNumber
- `Public Property TrackingNoteNumber() As Long` [R] property TrackingNoteNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TrackingNoteBrokerCollection (Collection)

TrackingNoteBrokerCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TrackingNoteBroker` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TrackingNoteBroker` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TrackingNoteItem (Object)

TrackingNoteItem Class

## Properties (10)
- `Public Property AccumulatedAPQuantity() As Double` [R] property AccumulatedAPQuantity
- `Public Property AccumulatedARQuantity() As Double` [R] property AccumulatedARQuantity
- `Public Property AccumulatedRelocatedQuantity() As Double` [R] property AccumulatedRelocatedQuantity
- `Public Property CountryOfOrigin() As String` [R/W] property CountryOfOrigin
- `Public Property CustomsGroupCode() As Long` [R/W] property CustomsGroupCode
- `Public Property ItemCCDNumber() As String` [R/W] property ItemCCDNumber
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property Quantity() As Double` [R/W] property Quantity
- `Public Property TrackingNoteLineNumber() As Long` [R] property TrackingNoteLineNumber
- `Public Property TrackingNoteNumber() As Long` [R] property TrackingNoteNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TrackingNoteItemCollection (Collection)

TrackingNoteItemCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TrackingNoteItem` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TrackingNoteItem` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TrackingNoteParams (Object)

TrackingNoteParams Class

## Properties (2)
- `Public Property CCDNumber() As String` [R/W] property CCDNumber
- `Public Property TrackingNoteNumber() As Long` [R/W] property TrackingNoteNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TrackingNoteParamsCollection (Collection)

TrackingNoteParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TrackingNoteParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TrackingNoteParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TrackingNotesService (Object)

TrackingNotesService Class

## Methods (8)
- `Public Function Add(ByVal pITrackingNote As TrackingNote) As TrackingNoteParams` Add
  - param `pITrackingNote`: 
- `Public Sub Delete(ByVal pITrackingNoteParams As TrackingNoteParams)` Delete
  - param `pITrackingNoteParams`: 
- `Public Function Get(ByVal pITrackingNoteParams As TrackingNoteParams) As TrackingNote` Get
  - param `pITrackingNoteParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TrackingNotesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TrackingNotesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As TrackingNoteParamsCollection` GetList
- `Public Sub Update(ByVal pITrackingNote As TrackingNote)` Update
  - param `pITrackingNote`: 

# TransactionCode (Object)

TransactionCode Class

## Properties (2)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransactionCodeParams (Object)

TransactionCodeParams Class

## Properties (2)
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R] property Description

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransactionCodeParamsCollection (Collection)

TransactionCodeParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TransactionCodeParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TransactionCodeParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransactionCodesService (Object)

TransactionCodesService Class

## Methods (8)
- `Public Function Add(ByVal pITransactionCode As TransactionCode) As TransactionCodeParams` Add
  - param `pITransactionCode`: 
- `Public Sub Delete(ByVal pITransactionCodeParams As TransactionCodeParams)` Delete
  - param `pITransactionCodeParams`: 
- `Public Function Get(ByVal pITransactionCodeParams As TransactionCodeParams) As TransactionCode` Get
  - param `pITransactionCodeParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TransactionCodesServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TransactionCodesServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetList() As TransactionCodeParamsCollection` GetList
- `Public Sub Update(ByVal pITransactionCode As TransactionCode)` Update
  - param `pITransactionCode`: 

# TranslationsInUserLanguages (Object)

TranslationsInUserLanguages is a child object of the MultiLanguageTranslations object. It enables to set, in each row, a translated content in a specified user language. Source table: MLT1.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property KeyFromHeaderTable() As Long` [R] Returns the key of the translated field value. Field name: TranEntry.
- `Public Property LanguageCodeOfUserLanguage() As Long` [R/W] Sets or returns the user language code. This code must be one of the codes defined in the UserLanguages object. Field name: LangCode.
- `Public Property Translationscontent() As String` [R/W] Sets or returns the translated content for the specified field (KeyFromHeaderTable). Lentgh: 64,000 characters. Field name: Trans.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# TransportationDocumentCollection (Collection)

TransportationDocumentCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TransportationDocumentData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TransportationDocumentData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransportationDocumentData (Object)

TransportationDocumentData Class

## Properties (19)
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property Canceled() As BoYesNoEnum` [R/W] property Canceled
- `Public Property CarrierCode() As String` [R/W] property CarrierCode
- `Public Property ElDocExportFormat() As Long` [R/W] property ElDocExportFormat
- `Public Property ElDocGenType() As ElectronicDocGenTypeEnum` [R/W] property ElDocGenType
- `Public Property ExpirationDate() As Date` [R/W] property ExpirationDate
- `Public Property IssueGate() As Long` [R/W] property IssueGate
- `Public Property NextNumber() As Long` [R/W] property NextNumber
- `Public Property PostDate() As Date` [R/W] property PostDate
- `Public Property TrailerID() As String` [R/W] property TrailerID
- `Public Property TranspDocNumber() As Long` [R] property TranspDocNumber
- `Public Property TransportationDocumentLineDataCollection() As TransportationDocumentLineDataCollection` [R] property TransportationDocumentLineDataCollection
- `Public Property TransportationDocumentParamsCollection() As TransportationDocumentParamsCollection` [R] property TransportationDocumentParamsCollection
- `Public Property TransportationNumber() As String` [R/W] property TransportationNumber
- `Public Property TransportedTotalLC() As Double` [R] property TransportedTotalLC
- `Public Property VehicleID() As String` [R/W] property VehicleID
- `Public Property WarehouseCode() As String` [R/W] property WarehouseCode
- `Public Property Weight() As Double` [R] property Weight
- `Public Property WeightUnit() As Long` [R] property WeightUnit

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransportationDocumentLineData (Object)

TransportationDocumentLineData Class

## Properties (8)
- `Public Property DocLineNumber() As Long` [R/W] property DocLineNumber
- `Public Property DocNumber() As Long` [R/W] property DocNumber
- `Public Property DocOrderNum() As Long` [R/W] property DocOrderNum
- `Public Property DocType() As DocumentObjectTypeEnum` [R/W] property DocType
- `Public Property ItemCode() As String` [R] property ItemCode
- `Public Property LineId() As Long` [R] property LineID
- `Public Property TranspDocNumber() As Long` [R] property TranspDocNumber
- `Public Property TransportedQuantity() As Double` [R/W] property TransportedQuantity

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransportationDocumentLineDataCollection (Collection)

TransportationDocumentLineDataCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TransportationDocumentLineData` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TransportationDocumentLineData` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransportationDocumentParams (Object)

TransportationDocumentParams Class

## Properties (1)
- `Public Property TranspDocNumber() As Long` [R/W] property TranspDocNumber

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransportationDocumentParamsCollection (Collection)

TransportationDocumentParamsCollection Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As TransportationDocumentParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As TransportationDocumentParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# TransportationDocumentService (Object)

TransportationDocumentService Class

## Methods (7)
- `Public Function AddTransportationDocument(ByVal pITransportationDocumentData As TransportationDocumentData) As TransportationDocumentParams` AddTransportationDocument
  - param `pITransportationDocumentData`: 
- `Public Sub CancelTransportationDocument(ByVal pITransportationDocumentParams As TransportationDocumentParams)` CancelTransportationDocument
  - param `pITransportationDocumentParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As TransportationDocumentServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `TransportationDocumentServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetTransportationDocument(ByVal pITransportationDocumentParams As TransportationDocumentParams) As TransportationDocumentData` GetTransportationDocument
  - param `pITransportationDocumentParams`: 
- `Public Sub UpdateTransportationDocument(ByVal pITransportationDocumentData As TransportationDocumentData)` UpdateTransportationDocument
  - param `pITransportationDocumentData`: 

# UnitOfMeasurement (Object)

To manage inventory items by different UoMs (units of measurement) applicable to your business, you need to define the individual UoMs. These are the units in which the items will be purchased, sold, and stocked. You can later group associated ones together as a set of UoMs with a definition of its conversion rules. Source table: OUOM.

**Remarks:** To access the Units of Measurement - Setup window, choose Administration --> Setup --> Inventory --> Units of Measurement.

## Properties (28)
- `Public Property AbsEntry() As Long` [R] The internal key of a UoM. Field name: UomEntry.
- `Public Property Code() As String` [R/W] The unique code for the UoM. Field name: UomCode. Length: 20 characters.
- `Public Property EWBUnitEntry() As Long` [R/W] property EWBUnitEntry
- `Public Property Height1() As Double` [R/W] The height for the unit. Field name: Height1.
- `Public Property Height1Unit() As Long` [R/W] The height UoM. Field name: Hght1Unit.
- `Public Property Height2() As Double` [R/W] The height for the unit. Field name: Height2.
- `Public Property Height2Unit() As Long` [R/W] The height UoM. Field name: Hght2Unit.
- `Public Property InternationalSymbol() As String` [R/W] The international symbol for the UoM. Field name: IntSymbol. Length: 20 characters.
- `Public Property Length1() As Double` [R/W] The length for the unit. Field name: Length1.
- `Public Property Length1Unit() As Long` [R/W] The length UoM. Field name: Len1Unit.
- `Public Property Length2() As Double` [R/W] The length for the unit. Field name: Length2.
- `Public Property Length2Unit() As Long` [R/W] The length UoM. Field name: Len2Unit.
- `Public Property Name() As String` [R/W] The name for the UoM. Field name: UomName. Length: 100 characters.
- `Public Property PPWe1Unit() As Long` [R/W] Weight of plastic packaging, 1, unit. Number, default 0. Field name: PPWe1Unit.
  - remarks: For UK localization only.
  - C# example (from SAP's help):
    ```csharp
    UnitOfMeasurement uomAdd = service.GetDataInterface(UnitOfMeasurementsServiceDataInterfaces.uomsUnitOfMeasurement);
    uomAdd.Code = ""DI_API_TEST_CODE"";
    uomAdd.Name = ""DI_API_TEST_NAME"";
    uomAdd.PPWeight1 = 3;
    uomAdd.PPWe1Unit = 2;
    uomAdd.PPWeight2 = 3;
    uomAdd.PPWe2Unit = 1;
    service.Add(uomAdd);
    ```
- `Public Property PPWe2Unit() As Long` [R/W] Weight of plastic packaging, 2, unit. Number, default 0. Field name: PPWe2Unit.
  - remarks: For UK localization only.
- `Public Property PPWeight1() As Double` [R/W] Weight of plastic packaging, 1. Number, default 0. Field name: PPWeight1.
  - remarks: For UK localization only.
- `Public Property PPWeight2() As Double` [R/W] Weight of plastic packaging, 2. Number, default 0. Field name: PPWeight2.
  - remarks: For UK localization only.
- `Public Property UserFields() As Fields` [R] Get User Fields
- `Public Property Volume() As Double` [R/W] The volume for the unit. Field name: Volume.
  - remarks: The application automatically calculates the volume according to the length, width, and height you have defined, and displays the result in the grid. You can change it by manually entering a different value, but the values in the Length, Width and Height fields will be cleared immediately.
- `Public Property VolumeUnit() As Long` [R/W] The volume UoM. Field name: VolUnit.
  - remarks: The default volume UoM corresponds to the default length UoM specified on the Display tab of the General Settings window.
- `Public Property Weight1() As Double` [R/W] The weight for the unit. Field name: Weight1.
- `Public Property Weight1Unit() As Long` [R/W] The weight UoM. Field name: WghtUnit.
- `Public Property Weight2() As Double` [R/W] The weight for the unit. Field name: Weight2.
- `Public Property Weight2Unit() As Long` [R/W] The weight UoM. Field name: Wght2Unit.
- `Public Property Width1() As Double` [R/W] The width for the unit. Field name: Width1.
- `Public Property Width1Unit() As Long` [R/W] The width UoM. Field name: Wdth1Unit.
- `Public Property Width2() As Double` [R/W] The width for the unit. Field name: Width2.
- `Public Property Width2Unit() As Long` [R/W] The width UoM. Field name: Wdth2Unit.

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

# UnitOfMeasurementGroup (Object)

A UoM (Unit of Measurement) group is a set of UoMs that you want to use for a certain type of product. Each UoM group has a base UoM. All the other UoMs belonging to this group are related to this base UoM by conversion rules. You can assign a UoM group to an item. When you use different UoMs for the item in sales, purchasing, inventory, and production transactions, SAP Business One automatically processes the differences in UoMs according to their conversion rules. Source table: OUGP.

**Remarks:** From the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Unit of Measurement Groups. In the Unit of Measurement - Setup window, enter a group name and its description. Choose Group Definition to open the Unit of Measurement Groups – <Group> – Setup window.

## Properties (5)
- `Public Property AbsEntry() As Long` [R] The internal key of a unit of measurement group. Field name: UgpEntry.
- `Public Property BaseUoM() As Long` [R/W] The base UoM. Field name: BaseUom.
- `Public Property Code() As String` [R/W] The unique code for the UoM group. Field name: UgpCode. Length: 20 characters.
- `Public Property GroupDefinitions() As UoMGroupDefinitionCollection` [R] Defines the unit of measurement group.
- `Public Property Name() As String` [R/W] The name for the UoM group. Field name: UgpName. Length: 20 characters.

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

# UnitOfMeasurementGroupParams (Object)

Holds the key to an existing unit of measurement group. This object is used to pass keys to and retrieve keys from UnitOfMeasurementGroupsService methods.

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] The internal key of a unit of measurement group. Field name: UgpEntry.
- `Public Property Code() As String` [R/W] The unique code for the UoM group. Field name: UgpCode. Length: 20 characters.

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

# UnitOfMeasurementGroupParamsCollection (Collection)

A collection of UnitOfMeasurementGroupParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As UnitOfMeasurementGroupParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As UnitOfMeasurementGroupParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# UnitOfMeasurementGroupsService (Object)

The UnitOfMeasurementGroupsService service enables you to add, look up, update, and remove unit of measurement groups. Source table: OUGP.

**Remarks:** From the SAP Business One Main Menu, choose Administration --> Setup --> Inventory --> Unit of Measurement Groups. In the Unit of Measurement - Setup window, enter a group name and its description. Choose Group Definition to open the Unit of Measurement Groups – <Group> – Setup window.

## Methods (8)
- `Public Function Add(ByVal pIUnitOfMeasurementGroup As UnitOfMeasurementGroup) As UnitOfMeasurementGroupParams` Adds a UoM group.
  - param `pIUnitOfMeasurementGroup`: The data for the new UoM group.
- `Public Sub Delete(ByVal pIUnitOfMeasurementGroupParams As UnitOfMeasurementGroupParams)` Deletes an existing UoM group.
  - param `pIUnitOfMeasurementGroupParams`: The key of the UoM group to be deleted.
- `Public Function Get(ByVal pIUnitOfMeasurementGroupParams As UnitOfMeasurementGroupParams) As UnitOfMeasurementGroup` Retrieves a UoM group. The UoM group is specified by its key, which is contained in the UnitOfMeasurementGroupParams object passed to the method.
  - param `pIUnitOfMeasurementGroupParams`: The key of the UoM group to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As UnitOfMeasurementGroupsServiceDataInterfaces) As Object` Creates an empty data structure for use with the UnitOfMeasurementGroupsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `UnitOfMeasurementGroupsServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetList() As UnitOfMeasurementGroupParamsCollection` Returns the UnitOfMeasurementGroupParamsCollection data collection that identifies all UoM groups.
- `Public Sub Update(ByVal pIUnitOfMeasurementGroup As UnitOfMeasurementGroup)` Updates an existing UoM group.
  - param `pIUnitOfMeasurementGroup`: The data for the UoM group to be updated. The UnitOfMeasurementGroup object must contain the key of the object to be updated.

# UnitOfMeasurementParams (Object)

Holds the key to an existing unit of measurement. This object is used to pass keys to and retrieve keys from UnitOfMeasurementsService methods.

## Properties (2)
- `Public Property AbsEntry() As Long` [R/W] The internal key of a UoM. Field name: UomEntry.
- `Public Property Code() As String` [R/W] The unique code for the UoM. Field name: UomCode. Length: 20 characters.

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

# UnitOfMeasurementParamsCollection (Collection)

A collection of UnitOfMeasurement objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As UnitOfMeasurementParams` Adds an empty object to the collection.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As UnitOfMeasurementParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# UnitOfMeasurementsService (Object)

The UnitOfMeasurementsService service enables you to add, look up, update, and remove unit of measurements. Source table: OUOM.

**Remarks:** To access the Units of Measurement - Setup window, choose Administration --> Setup --> Inventory --> Units of Measurement.

## Methods (8)
- `Public Function Add(ByVal pIUnitOfMeasurement As UnitOfMeasurement) As UnitOfMeasurementParams` Adds a UoM.
  - param `pIUnitOfMeasurement`: The data for the new UoM.
- `Public Sub Delete(ByVal pIUnitOfMeasurementParams As UnitOfMeasurementParams)` Deletes an existing UoM.
  - param `pIUnitOfMeasurementParams`: The key of the UoM to be deleted.
- `Public Function Get(ByVal pIUnitOfMeasurementParams As UnitOfMeasurementParams) As UnitOfMeasurement` Retrieves a UoM. The UoM is specified by its key, which is contained in the UnitOfMeasurementParams object passed to the method.
  - param `pIUnitOfMeasurementParams`: The key of the UoM to retrieve.
- `Public Function GetDataInterface(ByVal enumMSDI As UnitOfMeasurementsServiceDataInterfaces) As Object` Creates an empty data structure for use with the UnitOfMeasurementsService.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `UnitOfMeasurementsServiceDataInterfaces` in `../enums/enums-03.md`
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
- `Public Function GetList() As UnitOfMeasurementParamsCollection` Returns the UnitOfMeasurementParamsCollection data collection that identifies all UoMs.
- `Public Sub Update(ByVal pIUnitOfMeasurement As UnitOfMeasurement)` Updates an existing UoM.
  - param `pIUnitOfMeasurement`: The data for the UoM to be updated. The UnitOfMeasurement object must contain the key of the object to be updated.

# UoMGroupDefinition (Object)

Defines the unit of measurement group. Source table: UGP1.

## Properties (6)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property AlternateQuantity() As Double` [R/W] The alternate quantity. Field name: AltQty.
- `Public Property AlternateUoM() As Long` [R/W] The alternate UoM. Field name: UomEntry.
- `Public Property BaseQuantity() As Double` [R/W] The base quantity. Field name: BaseQty.
- `Public Property UdfFactor() As Long` [R/W] property UdfFactor
- `Public Property WeightFactor() As Long` [R/W] property WeightFactor

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

# UoMGroupDefinitionCollection (Collection)

A collection of UoMGroupDefinition objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As UoMGroupDefinition` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As UoMGroupDefinition` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes the object at the specified index.
  - param `vtIndex`: The index of the object to be removed.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# UoMPrices (Object)

UoMPrices Class

## Properties (13)
- `Public Property AdditionalCurrency1() As String` [R/W] property AdditionalCurrency1
- `Public Property AdditionalCurrency2() As String` [R/W] property AdditionalCurrency2
- `Public Property AdditionalPrice1() As Double` [R/W] property AdditionalPrice1
- `Public Property AdditionalPrice2() As Double` [R/W] property AdditionalPrice2
- `Public Property AdditionalReduceBy1() As Double` [R/W] property AdditionalReduceBy1
- `Public Property AdditionalReduceBy2() As Double` [R/W] property AdditionalReduceBy2
- `Public Property Auto() As BoYesNoEnum` [R/W] property Auto
- `Public Property Count() As Long` [R] property Count
- `Public Property Currency() As String` [R/W] property Currency
- `Public Property Price() As Double` [R/W] property Price
- `Public Property PriceList() As Long` [R/W] property PriceList
- `Public Property ReduceBy() As Double` [R/W] property ReduceBy
- `Public Property UoMEntry() As Long` [R/W] property UoMEntry

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# UserActionRecord (Object)

Displays the access details and the actions of SAP Business One users who have logged on and logged off with the SAP Business One client or the DI API. Source table: USR5.

**Remarks:** In the SAP Business One application, to open the Access Log window, in the SAP Business One menu bar, choose Tools --> Access Log. To open the Access Log Details window, in the Access Log window, double-click the table row of a user whose access information you want to display.

**Example:**
- C# example (from SAP's help):
  ```csharp
  UserActionRecord oUserActionRecord = (UserActionRecord)oCompany.GetBusinessObject(BoObjectTypes.oUserActionRecord);
  Recordset rs = (Recordset)oCompany.GetBusinessObject(BoObjectTypes.BoRecordset);
  rs.DoQuery("select * from USR5 where UserID = 'manager' and Date > '2009-11-01'");

  oUserActionRecord.Browser.Recordset = rs;
  oUserActionRecord.Browser.MoveFirst();

  while (!oUserActionRecord.Browser.EoF)
  {
      Console.Write(oUserActionRecord.UserCode + "\t");
      Console.Write(oUserActionRecord.Action + "\t");
      Console.Write(oUserActionRecord.ActionBy + "\t");
      Console.Write(oUserActionRecord.ClientIP + "\t");
      Console.Write(oUserActionRecord.ClientName + "\t");
      Console.Write(oUserActionRecord.ActionDate + "\t");
      Console.Write(oUserActionRecord.ActionTime + "\t");
      Console.WriteLine();

      oUserActionRecord.Browser.MoveNext();
  }
  ```

## Properties (14)
- `Public Property Action() As UserActionTypeEnum` [R] The action that the user performed. Field name: Action.
- `Public Property ActionBy() As String` [R] The user ID of the user who performed the action. Field name: ActionBy. Length: 8 characters.
- `Public Property ActionDate() As Date` [R] The date of the action. Field name: Date.
- `Public Property ActionTime() As Date` [R] The time of the action. Field name: Time.
- `Public Property AliveDuration() As Long` [R] property AliveDuration
- `Public Property ClientIP() As String` [R] The IP addresses of the SAP Business One client computer in use by the user. Field name: ClientIP. Length: 200 characters.
- `Public Property ClientName() As String` [R] The name of the SAP Business One client computer in use by the user. Field name: ClientName. Length: 32 characters.
- `Public Property Count() As Long` [R] Returns the total number of records.
- `Public Property ProcessID() As Long` [R] The process ID of the SAP Business One application. Field name: ProcessID.
- `Public Property ProcessName() As String` [R] The process name of the logged-on application. Field name: ProcName. Length: 80 characters.
- `Public Property UserCode() As String` [R] Returns the user code. This is the foreign key to the Users object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WindowsSession() As Long` [R] The windows session ID. Field name: WinSessnID.
- `Public Property WindowsUser() As String` [R] The windows user name. Field name: WinUsrName. Length: 100 characters.

## Methods (1)
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# UserBranchAssignment (Object)

UserBranchAssignment Class

## Properties (3)
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Count() As Long` [R] property Count
- `Public Property UserCode() As String` [R] property UserCode

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# UserDefaultGroups (Object)

The UserDefaultGroups object enables to define default values (such as, default documents, default address in printed documents, windows color, and so on). These default values can be applied to specific user or group of users by setting the Defaults property of the Users object. Source table: OUDG.

**Remarks:** Mandatory field in SAP Business One: Code. If you set this object, the system uses these defaults instead of the company defaults. For example: - The Address setting is used instead of the Address setting of the AdminInfo object. - The BPforInvoicePayment setting is used instead of the InvoicePaymentBP setting of the PeriodCategory object. To display the form in the application: - Select Administration -->Setup -->General -->Users. - From the Defaults field, click the Choose From List button. - In the List of User Defaults, click the New button.

## Properties (36)
- `Public Property AdditionalIdNumber() As String` [R/W] Sets or returns the default additional ID number of the company. Field name: FreeZoneNo. Length: 32 characters.
  - remarks: If you set this property, the system uses its setting as default instead of the AdditionalIdNumber of the AdminInfo object.
- `Public Property Address() As String` [R/W] Sets or returns the default company address. Field name: Address. Length: 254 characters.
  - remarks: If you set this property, the system uses its setting as default instead of Address of the AdminInfo object.
- `Public Property AddressinForeignLanguage() As String` [R/W] Sets or returns the default company address in foreign language. Field name: FrgnAddr. Length: 254 characters.
  - remarks: If you set this property, the system uses its setting as default instead of the AddressinForeignLanguage of the AdminInfo object.
- `Public Property AssetInDoc() As BoYesNoEnum` [R/W] property AssetInDoc
- `Public Property BPforInvoicePayment() As String` [R/W] Sets or returns the default customer for A/R invoices and payments. This is a foreign key to CardCode (BusinessPartners. Field name: ICTCard. Length: 15 characters. This is a foreign key to the BusinessPartners object.
  - remarks: If you set this property, the system uses its setting as default instead of InvoicePaymentBP (PeriodCategory object).
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CashAccount() As String` [R/W] Sets or returns the default G/L account for cash receipt. Field name: CashAcct. Length: 15 characters.
  - remarks: If you set this property, the system uses its setting as default instead of AccountforCashReceipt (PeriodCategory object).
- `Public Property CheckingAcct() As String` [R/W] Sets or returns the default G/L account for incoming checks. Field name: CheckAcct. Length: 15 characters.
  - remarks: If you set this property, the system uses its setting as default instead of AccountforOutgoingchecks (PeriodCategory object).
- `Public Property Code() As String` [R/W] Sets or returns the code (primary key) of the user defaults group. Mandatory property. Field name: Code. Length: 8 characters.
- `Public Property Country() As String` [R/W] Sets or returns the default country code. Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: This a foreign key to the Countries table (OCRY - not exposed through the DI API). If you set this property, the system uses its setting as default instead of Country of the AdminInfo object.
- `Public Property DefaultCreditCards() As DefaultCreditCards` [R] Returns the DefaultCreditCards child object.
- `Public Property DefaultDocuments() As DefaultDocuments` [R] Returns the DefaultDocuments child object.
- `Public Property DefaultPTICode() As String` [R/W] property DefaultPTICode
- `Public Property DefaultPTICodes() As DefaultPTICodes` [R] property DefaultPTICodes
- `Public Property DefaultTaxCode() As String` [R/W] Sets or returns the default sales tax code. This is a foreign key to Code of the SalesTaxCodes object. Field name: DflTaxCode. Length: 8 charcters. This is a foreign key to the SalesTaxCodes object.
  - remarks: If you set this property, the system uses its setting as default instead of DefaultTaxCode of the AdminInfo object. Applicable for US and Canada only where the tax is calculated per card. The system displays this tax group code by default in a document row in case the following conditions are met: - The item is not an inventory one. - The item is a purchase item. - The item is taxable.
- `Public Property eMail() As String` [R/W] Sets or returns the default e-mail address. Field name: E_Mail. Length: 100 characters.
  - remarks: If you set this property, the system uses its setting as default instead of eMail of the AdminInfo object.
- `Public Property FaxNumber() As String` [R/W] Sets or returns the default fax number. Field name: Fax. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of FaxNumber of the AdminInfo object.
- `Public Property FaxNumberForeignLang() As String` [R/W] Sets or returns the default fax number in foreign language. Field name: FrgnFax. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of FaxNumberForeignLang of the AdminInfo object.
- `Public Property LanguageCode() As BoSuppLangs` [R/W] property LanguageCode
- `Public Property Name() As String` [R/W] Sets or returns the name of the user defaults group. Field name: Name. Length: 20 characters.
- `Public Property PhoneNumber1() As String` [R/W] Sets or returns the first default phone number. Field name: Phone1. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PhoneNumber1 of the AdminInfo object.
- `Public Property PhoneNumber1ForeignLang() As String` [R/W] Sets or returns the first default phone number in foreign language. Field name: FrgnPhone1. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PhoneNumber1ForeignLang of the AdminInfo object.
- `Public Property PhoneNumber2() As String` [R/W] Sets or returns the second default phone number. Field name: Phone2. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PhoneNumber2 of the AdminInfo object.
- `Public Property PhoneNumber2ForeignLang() As String` [R/W] Sets or returns the second default phone number in foreign language. Field name: FrgnPhone2. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PhoneNumber2ForeignLang of the AdminInfo object.
- `Public Property PrintingHeader() As String` [R/W] Sets or returns the default header to print in all documents (for example, the company name). Field name: PrintHeadr. Length: 100 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PrintingHeader of the AdminInfo object.
- `Public Property PrintingHeaderInForeignLangu() As String` [R/W] Sets or returns the default header in foreign language to print in all documents. Field name: FrnPrntHdr. Length: 100 characters.
  - remarks: If you set this property, the system uses its setting as default instead of LetterHeaderinForeignLangu of the AdminInfo object.
- `Public Property PrintInvoiceandPaymentinS() As BoYesNoEnum` [R/W] Determines the default for whether or not to print invoices and payments in succession. Field name: ShortRcpt.
  - remarks: If you set this property, the system uses its setting as default instead of the ShortRcpt field of the Print Preferences (OADP table, which is not exposed through the DI API).
- `Public Property PrintReceipt() As BoPrintReceiptEnum` [R/W] Sets or returns a valid value of BoPrintReceiptEnum that determines when to print payment with invoice. Field name: PrintRcpt.
  - remarks: If you set this property, the system uses its setting as default instead of the PrintRcpt field of the Print Preferences (OADP table, which is not exposed through the DI API).
- `Public Property SalesEmployee() As Long` [R/W] Sets or returns the default sales employee code that will be applied in documents, sales opportunities, and so on. Field name: SalePerson. This is a foreign key to SalesEmployeeCode.
  - remarks: If you set this property, the system uses its value as default instead of -1 (No sales employee).
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Sets or returns the key of the user who defines the UseDefaultGroups object. Field name: UserSign. This is a foreign key to Users object.
- `Public Property UseTax() As BoYesNoEnum` [R/W] Determines the default whether or not to enable Use Tax calculations. Country-specific for U.S. Field name: UseTax.
  - remarks: If you set this property, the system uses its setting as default instead of UseTax of the AdminInfo object.
- `Public Property UseWarehouseAddressinAPD() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to use the warehouse address in purchase documents. Field name: AdrsFromWh.
  - remarks: If you set this property, the system uses its setting as default instead of AdressFromWH of the AdminInfo object.
- `Public Property Warehouse() As String` [R/W] Sets or returns the default warehouse code that will be applied in documents. Length 8 characters. Field name: Warehouse. This is a foreign key to the Warehouses object.
  - remarks: If you set this property, the system uses its setting as default instead of DefaultWarehouse of the AdminInfo object.
- `Public Property WindowsColor() As Long` [R/W] Sets or returns the the default windows color. Field name: Color.
  - remarks: If you set this property, the system uses its setting as default instead of CompanyColor of the AdminInfo object. The valid values include: 0 - Combined 1 - Classic (default) 2 - Gray 3 - Violet 4 - Blue 5 - Green 6 - Yellow 7 - Orange 8 - Red 9 - Brown

## Methods (7)
- `Public Function Add() As Long` method Add
  - remarks: Adds a users group.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrCode`: Code.
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

# UserFields (Object)

The UserFields object is a collection of Fields objects, which are user defined fields.

## Properties (1)
- `Public Property Fields() As Fields` [R] Returns a Fields collection, which contains the fields of the result set.

# UserFieldsMD (Object)

UserFieldsMD is a business object that enables you to manage user-defined fields in user and system tables. This object enables you to: - Add a user-defined field. - Retrieve a user-defined field from the database by its key. - Remove a user-defined field. - Save the object in XML format. Source table: CUFD Mandatory properties: Name and TableName IMPORTANT: After creating a new user-defined field in .NET, you must release the object by executing the following line of code, where myObject is a reference to the UserFieldsMD object: System.Runtime.InteropServices.Marshal.ReleaseComObject(myObject);

**Remarks:** The DI API allows only one metadata object instance (with no other instances of any object type). This maintains data integrity by preventing any manipulation of a business object while modifying the object's properties. If you add a mandatory user-defined field, you must also define a default value; otherwise, the following message appears: "Invalid object name; cannot add field". Note: After adding a user-defined field, you can view it in the User-Defined Fields - Management window. To view the new user-defined field in the Settings window, you must restart the SAP Business One application. Before adding a user-defined field, check the application window and make sure there is an entry for the object to which you want to add a user-defined field. To display the form in the application: - From the main menu bar, select Tools --> Customization Tools --> User-Defined Fields - Management.

## Properties (15)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DefaultValue() As String` [R/W] Sets or returns the default value of the field. Field name: Dflt. Length: 254 characters.
  - remarks: Use the DefaultValue property in conjunction with the Value property of the ValidValuesMD object to determine the default value for the new field.
- `Public Property Description() As String` [R/W] Sets or returns the description of the field. Field name: Descr. Length: 80 characters.
- `Public Property EditSize() As Long` [R/W] Sets or returns the field maximum value entered by the user. This applies only when the Type property is set to db_Alpha or db_Numeric. Field name: EditSize.
- `Public Property FieldID() As Long` [R] Returns the unique identification key of the field in the meta data table. Field name: FieldID.
  - remarks: This value is also used with the GetByKey method.
- `Public Property LinkedSystemObject() As UDFLinkedSystemObjectTypesEnum` [R/W] Links to an existing system object of SAP Business One.
- `Public Property LinkedTable() As String` [R/W] Sets or returns a linked user table name, so that the user field will be used as a foreign key in the TableName. Field name: RTable. Length: 20 characters.
  - remarks: The values of the Size and Type properties must match the Size and Type values of the key field in the linked table. When using the LinkedTable property, do not set the DefaultValue and ValidValues properties. For the linked user tables do not use the @ sign in the LinkedTable name. This property is not supported by the Recordset object.
- `Public Property LinkedUDO() As String` [R/W] Links to a user-defined object (UDO) form of both Matrix style and Header Lines style. Field name: RelUDO. Length: 20 characters.
- `Public Property Mandatory() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not this User Field is mandatory in SAP Business One. Field name: Sys.
- `Public Property Name() As String` [R/W] Sets or returns the field name. Field name: AliasID. Length: 50 characters.
- `Public Property Size() As Long` [R/W] The actual size of the field. The value is automatically determined by the input of the EditSize property. Do not set any value in the Size property. Field name: SizeID.
  - remarks: Relevant when the Type property is set to db_Alpha or db_Numeric.
- `Public Property SubType() As BoFldSubTypes` [R/W] Returns or set the field sub-type, which specifies a specific format of the data type.
  - remarks: The following table describes the relations between the SAP Business One application data types and the DI API data types. Application DI API Type Structure Type SubType Alphanumeric Regular db_Alpha st_None Alphanumeric Address db_Alpha st_Address Alphanumeric Phone db_Alpha st_Phone Alphanumeric Text db_Memo st_None Numeric None db_Numeric st_None Date/Hour Date db_Date st_None Date/Hour Hour db_Date st_Time Units And Totals Rate db_Float st_Rate Units And Totals Sum db_Float st_Sum Units And Totals Price db_Float st_Price Units And Totals Quantity db_Float st_Quantity Units And Totals Percent db_Float st_Percentage Units And Totals Measure db_Float st_Measurement General Link db_Memo st_Link General Image db_Alpha st_Image
- `Public Property TableName() As String` [R/W] Sets or returns the name of the parent table that this field refers to. Length: 21 characters. Field name: TableID.
- `Public Property Type() As BoFieldTypes` [R/W] Sets or returns the data type, which describes the nature of the data, of the specified field . Field name: TypeID.
- `Public Property ValidValues() As ValidValuesMD` [R] Returns the ValidValuesMD object.
  - remarks: You can use this property to retrieve the valid values for the specified field.

## Methods (7)
- `Public Function Add() As Long` Adds a new user field to an exiting user table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal TableName As String, ByVal FieldID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `TableName`: Specifies the name of the user defined table. (use the symbol @ as a prefix to the name, see the TableName property of the UserTablesMD object).
  - param `FieldID`: Specifies the field identification key.
- `Public Function Remove() As Long` Removes a specified field from the table.
  - remarks: Warning: when removing a field, all it's content is lost.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.

# UserGroup (Object)

UserGroup Class

## Properties (7)
- `Public Property DueDate() As Date` [R/W] property DueDate
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property TPLId() As Long` [R/W] property TPLId
- `Public Property UserGroupDec() As String` [R/W] property UserGroupDec
- `Public Property UserGroupId() As Long` [R] property UserGroupId
- `Public Property UserGroupName() As String` [R/W] property UserGroupName
- `Public Property UserGroupType() As UserGroupCategoryEnum` [R/W] property UserGroupType

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# UserGroupByUser (Object)

UserGroupByUser Class

## Properties (4)
- `Public Property Count() As Long` [R] property USERId
- `Public Property DueDate() As Date` [R/W] property DueDate
- `Public Property GroupId() As Long` [R/W] property GroupId
- `Public Property StartDate() As Date` [R/W] property StartDate

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`: 

# UserGroupParams (Object)

UserGroupParams Class

## Properties (2)
- `Public Property UserGroupId() As Long` [R/W] property UserGroupId
- `Public Property UserGroupName() As String` [R/W] property UserGroupName

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# UserGroupService (Object)

UserGroupService Class

## Methods (8)
- `Public Function AddUserGroup(ByVal pIUserGroup As UserGroup) As UserGroupParams` AddUserGroup
  - param `pIUserGroup`: 
- `Public Sub DeleteUserGroup(ByVal pIUserGroupParams As UserGroupParams)` DeleteUserGroup
  - param `pIUserGroupParams`: 
- `Public Function GetDataInterface(ByVal enumMSDI As UserGroupServiceDataInterfaces) As Object` GetDataInterface
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `UserGroupServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` GetDataInterfaceFromXMLFile
  - param `bstrFileName`: 
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` GetDataInterfaceFromXMLString
  - param `bstrXMLString`: 
- `Public Function GetUserGroup(ByVal pIUserGroupParams As UserGroupParams) As UserGroup` GetUserGroup
  - param `pIUserGroupParams`: 
- `Public Function GetUserGroupList() As UserGroupsParams` GetUserGroupList
- `Public Sub UpdateUserGroup(ByVal pIUserGroup As UserGroup)` UpdateUserGroup
  - param `pIUserGroup`: 

# UserGroupsParams (Collection)

UserGroupsParams Class

## Properties (1)
- `Public Property Count() As Long` [R] Count

## Methods (5)
- `Public Function Add() As UserGroupParams` method Add
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Function Item(ByVal vtIndex As Variant) As UserGroupParams` DISPID_VALUE
  - param `vtIndex`: 
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# UserKeysMD (Object)

The UserKeysMD object enables to mange user defined keys of user tables. A user table contains a default primary key that consists of the Code and Name columns. Use the UserKeysMD object to add secondary keys to user tables. This object enables you to: - Add a user key (identifier) to a user table. - Retrieve the values of the object's properties by its KeyIndex and TableName. - Remove a user key. - Save the object in XML format. Source table: OUKD.

**Remarks:** DI API allows only one meta data object instance (with no other instances of any object type). This maintains data integrity by preventing any manipulation of a business object while modifying the object's properties. Furthermore, it is recommended to add user keys while the user table is still empty. To display the form in the application: - From the main menu bar, select Tools --> Manage User Fields. - Select a User Table. - Click Keys.

## Properties (6)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Elements() As UserKeysMD_Elements` [R] Returns the UserKeysMD_Elements child object that contains the list of fields in the database used for adding the key.
- `Public Property KeyIndex() As Long` [R] Returns the serial number that uniquely identifies the key in the user table. This serial number is automatically assigned by SAP Business One (starting from 0). Field name: KeyId.
- `Public Property KeyName() As String` [R/W] Sets or returns the unique key name used for identification. Field name: KeyName. Length: 10 characters.
- `Public Property TableName() As String` [R/W] Sets or returns the name of the required table in the database. Field name: TableName. Length: 20 characters.
- `Public Property Unique() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the key is unique. Unique keys prevents the end-user from adding new keys with the same key combination. Field name: UniqueKey.

## Methods (6)
- `Public Function Add() As Long` Adds a key to a row of a user defined table. See sample, Adding a Private Key.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal TableName As String, ByVal KeyIndex As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `TableName`: The name of the required table in the database.
  - param `KeyIndex`: A serial number (read only) that is automatically assigned by the system and uniquely identifies the key in the user table (starts from 0).
- `Public Function Remove() As Long` Deletes a key from an existing table.
  - remarks: Before using the Remove method, you must get the required table using the GetByKey method.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.

# UserKeysMD_Elements (Object)

UserKeysMD_Elements is a child object of the UserKeysMD object. UserKeysMD_Elements defines the fields that combine the key index. Source table: UKD1.

## Properties (3)
- `Public Property ColumnAlias() As String` [R/W] Sets or returns the field name in the database. Field name: ColAlias. Length: 18 characters.
- `Public Property Count() As Long` [R] Returns the total key indexes that exist in the collection.
- `Public Property SubKeyIndex() As Long` [R] Returns the internal key of the field. Used for reference only. Field name: SubKeyId.

## Methods (2)
- `Public Sub Add()` Adds a field to an existing key index.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# UserLanguages (Object)

The UserLanguages object represents the languages setup and enables to define new languages or modify the exisiting ones. Source table: OLNG.

**Remarks:** Mandatory properties: LanguageShortName, LanguageFullName, and RelatedSystemLanguage. To display the form in the application: - Select Administration --> System Initialization -->Company Details -->Basic Initialization tab. - Select the Multi-Language Support check box, then click the Update button. - Select Administration --> Setup -->General -->Languages.

## Properties (6)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As Long` [R] Returns the language code as assigned by the system (numerator). Field name: Code.
- `Public Property LanguageFullName() As String` [R/W] Sets or returns the language full name, for example, English (US). Field name: Name. Length: 30 characters.
- `Public Property LanguageShortName() As String` [R/W] Sets or returns the language short name, for example, EN for English. Field name: ShortName. Length: 3 characters.
- `Public Property RelatedSystemLanguage() As Long` [R/W] Sets or returns the key of the related language as defined in the system. For example, set the value 3 for English (US). Field name: SysLang.
  - remarks: For a list of related system languages, see the BoSuppLangs enumaration.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a new language definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: Code.
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

# UserLicenseParams (Object)

Contains the parameters for assigning licenses.

## Properties (3)
- `Public Property LicenseType() As LicenseTypeEnum` [R/W] Type of license to assign or remove.
- `Public Property LicenseUpdateType() As LicenseUpdateTypeEnum` [R/W] Indicates whether to assign or remove the license.
- `Public Property UserName() As String` [R/W] The user to whom to assign the license, or from whom to remove the license.

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

# UserMenuItem (Object)

UserMenuItem is a Data structure related to the UserMenuService. Source table: CUMI.

## Properties (9)
- `Public Property LinkedFormMenuID() As Long` [R/W] Sets or returns the id of the Form linked to this menu item. Field name: FormMenuId.
- `Public Property LinkedFormNum() As Long` [R/W] Sets or returns the Form number of the linked Form. Field name: FormNum.
- `Public Property LinkedObjKey() As String` [R/W] Sets or returns the key of the object linked to this menu item. Field name: Key_. Length: 50 characters.
- `Public Property LinkedObjType() As String` [R/W] Sets or returns the type of the object linked to this menu item. Field name: Type_.
- `Public Property Name() As String` [R/W] Sets or returns this menu item name. Field name: Name_. Length: 100 characters.
- `Public Property Position() As Long` [R/W] Sets or returns the position of this menu item within the menu. Field name: SortNum.
- `Public Property ReportPath() As String` [R/W] Sets or returns the path of the report attached to this menu Item. Field name: RepPath.
- `Public Property Type() As UserMenuItemTypeEnum` [R/W] Returns a valid value that defines this menu item type. Field name: Type_.
- `Public Property UserMenuItems() As UserMenuItems` [R/W] Sets or returns the UserMenuItems object, a data collection of UserMenuItem data structures.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# UserMenuItems (Collection)

UserMenuItems is a Data Collection of UserMenuItem data structures. Source table: CUMI.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of UserMenuItem data structures in the UserMenuItems data collection.

## Methods (6)
- `Public Function Add() As UserMenuItem` Adds a new UserMenuItem to the UserMenuItems data collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As UserMenuItem` Returns a reference to the UserMenuItem that you want to get.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes a specified UserMenuItem from the data collection.
  - param `vtIndex`: Specifies the index of the UserMenuItem you want to delete from the collection. Warning: when removing a field, all it's content is lost.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# UserMenuParams (Object)

The UserMenuParams specifies the identification key (UserID) for which the UserMenuService is related. Source table: CUMI.

## Properties (1)
- `Public Property UserID() As Long` [R/W] Returns the User Id. Field name: UserSign. This is a foreign key to the Users object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Specifies the path and file name of the XML data.
  - param `bstrXML`: Specifies the path and file name of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# UserMenuService (Object)

UserMenuService manages the user menu. Source table: CUMI. The service maintains a collection of user menus, each identified by a specific value of UserMenuParams. It enables the user to: - Get current user menu definition. - Get any user menu definition from the collection by it params identification key. - Update user menus in the collection. - Replace current user menu with user menu from the collection.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: - Select Main Menu--User Menu Tab

## Methods (7)
- `Public Function GetCurrentUserMenu() As UserMenuItems` Get the UserMenuItems data collection that represents current user menu.
  - example note: Get the current user menu
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oUserMenuItems As UserMenuItems

    Dim oUserMenuItem As UserMenuItem

    'get Current User Menu

    oUserMenuItems = oUserMenuService.GetCurrentUserMenu()

    'Get the first menu item

    oUserMenuItem = oUserMenuItems.Item(0)

    'print the menu name

    Debug.WriteLine(oUserMenuItem.Name())
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As UserMenuServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `UserMenuServiceDataInterfaces` in `../enums/enums-03.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Retrieves the Data Interface schema from XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Retrieves the Data Interface schema from XML string.
  - param `bstrXMLString`: Specifies the the XML string.
- `Public Function GetUserMenu(ByVal pIUserMenuParams As UserMenuParams) As UserMenuItems` Get a User's defined menu (UserMenuItems), by its UserMenuParams identification key.
  - param `pIUserMenuParams`: User menu UserMenuParams identification key.
- `Public Sub UpdateCurrentUserMenu(ByVal pIUserMenuItems As UserMenuItems)` Replace current User Menu with another User menu (UserMenuItems).
  - param `pIUserMenuItems`: The UserMenuItems data collection that defines the new user menu.
  - example note: Update Current User Menu
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oUserMenuItems As UserMenuItems

    Dim oUserMenuItem As UserMenuItem

    'get Current User Menu

    oUserMenuItems = oUserMenuService.GetCurrentUserMenu()

    'get the first menu item

    oUserMenuItem = oUserMenuItems.Item(0)

    'set the menu item name

    oUserMenuItem.Name = "My Forms"

    'update the User Menu

    oUserMenuService.UpdateCurrentUserMenu(oUserMenuItems)
    ```
- `Public Sub UpdateUserMenu(ByVal pIUserMenuParams As UserMenuParams, ByVal pIUserMenuItems As UserMenuItems)` Replace a User Menu definition (UserMenuItems), identified by it UserMenuParams with a new User menu definition (UserMenuItems).
  - param `pIUserMenuParams`: Identification key (UserMenuParams) of the new menu definition.
  - param `pIUserMenuItems`: The new UserMenuItems data collection that defines the new menu.
  - example note: Update the user menu of user 2(doris) with the menu of user 1 (manager)
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oUserMenuItems As UserMenuItems

    Dim oSourceUserMenuParams As UserMenuParams

    Dim oDestUserMenuParams As UserMenuParams

    'get new User Menu Params

    oSourceUserMenuParams = oUserMenuService.GetDataInterface(UserMenuServiceDataInterfaces.umsdiUserMenuParams)

    'set the user id(manager=1)

    oSourceUserMenuParams.UserID = 1

    'get User Menu Params

    oDestUserMenuParams = oUserMenuService.GetDataInterface(UserMenuServiceDataInterfaces.umsdiUserMenuParams)

    'set the user id(doris=2)

    oDestUserMenuParams.UserID = 2

    'get Menu Items of the user 1 (manager)

    oUserMenuItems = oUserMenuService.GetUserMenu(oSourceUserMenuParams)

    'update the user menu of user 2(doris) with the menu of user 1 (manager)

    oUserMenuService.UpdateUserMenu(oDestUserMenuParams, oUserMenuItems)
    ```

# UserObjectMD_ChildTables (Object)

UserObjectMD_ChildTables is child object of the UserObjectsMD object that represents child user tables and their related history log tables. Source table: UDO1.

## Properties (6)
- `Public Property Code() As String` [R] Returns the Child Object Unique ID., inherited from Parent Object. This Unique ID is the primary key of the user defined object and its Parent object. Field name: Code. Length: 20 characters (must include at least one alphabetical character).
- `Public Property Count() As Long` [R] Returns the number of child user tables in the object.
- `Public Property LogTableName() As String` [R/W] Sets or returns the history log table name. This table maintains a history log of all actions related to the child user table. Field name: LogName. Length: 19 characters.
  - remarks: If you select the History Log service, then set a history log table name starting with "A" followed by the object's Child User Table name. Notes: - If you unregister a user defined object that is registered to the history log service, the related history log table is deleted from the database. - If you unregister the history log service while updating a user defined object, the history log table is not deleted (only unregistered).
- `Public Property ObjectName() As String` [R/W] The name of child UDO object when specifying a child table for a UDO object. This name is used to specify the child table in the Child method of the GeneralData object.
- `Public Property SonNumber() As Long` [R] Returns the number of the child user table. SAP Business One creates a sequential number for each child user table that you add. Field name: SonNum.
- `Public Property TableName() As String` [R/W] Sets or returns the child table name to link to the user-defined object. Field name: TableName. Length: 19 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# UserObjectMD_EnhancedFormColumns (Object)

UserObjectMD_EnhancedFormColumns is a child object of the UserObjectsMD object that represents the default fields (columns) to display in the UDO enhanced default form (UDO form with the header-line style). Source table: UDO4.

**Remarks:** When adding fields to a default form, the first field must be as follows: - For Master data object type - Code. - For Document object type - DocEntry.

## Properties (8)
- `Public Property ChildNumber() As Long` [R/W] The number of the child user table to relate to the default user form. Field name: SonNum.
- `Public Property Code() As String` [R] Returns the Child Object Unique ID., inherited from Parent Object. This Unique ID is the primary key of the user defined object and its Parent object. Field name: Code. Length: 20 characters (must include at least one alphabetical character).
- `Public Property ColumnAlias() As String` [R/W] The alias name of the default field to display in the default form. Field name: ColAlias. Length: 20 characters.
- `Public Property ColumnDescription() As String` [R/W] The description of the default field to display in the default form. Field name: ColDesc. Length: 30 characters.
- `Public Property ColumnIsUsed() As BoYesNoEnum` [R/W] Indicates whether the form column is used or not. Field name: ColIsUsed.
- `Public Property ColumnNumber() As Long` [R/W] The number of the default field to display in the default form. SAP Business One creates a sequential number for each column that you add. Field name: ColumnNum.
- `Public Property Count() As Long` [R] Returns the number of columns in the default form.
- `Public Property Editable() As BoYesNoEnum` [R/W] Indicates whether the form column is editable (active) or not. Field name: ColEdit.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# UserObjectMD_FindColumns (Object)

UserObjectMD_FindColumns is a child object of the UserObjectsMD object that represents the fields (columns) to display in the Find Form (Choose From List form). Source table: UDO2.

## Properties (5)
- `Public Property Code() As String` [R] Returns the Child Object Unique ID., inherited from Parent Object. This Unique ID is the primary key of the user defined object and its Parent object. Field name: Code. Length: 20 characters (must include at least one alphabetical character).
- `Public Property ColumnAlias() As String` [R/W] Sets or returns the alias name of the field to display in the Find Form. Length: 10 characters. Field name: ColAlias.
- `Public Property ColumnDescription() As String` [R/W] Sets or returns the field description to display in the Find Form. Length: 30 characters. Field name: ColumnDesc.
- `Public Property ColumnNumber() As Long` [R] Returns the number of the field to display in the Find Form. SAP Business One creates a sequential number for each column that you add. Field name: ColumnNum.
- `Public Property Count() As Long` [R] Returns the number of columns in the Find Form (Choose From List form).

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.

# UserObjectMD_FormColumns (Object)

UserObjectMD_FormColumns is child object of the UserObjectsMD object that represents the default fields (columns) to display in the default form (UDO form with the matrix style). Source table: UDO3.

**Remarks:** If the user-defined object uses the default form service (CanCreateDefaultForm), then the mandatory field in SAP Business One is: SonNumber. When adding fields to a default form, the first field must be as follows: - For Master data object type - Code. - For Document object type - DocEntry.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  oUserObjectMD.FormColumns.FormColumnAlias = "Code"

  oUserObjectMD.FormColumns.FormColumnDescription = "Code"

  oUserObjectMD.FormColumns.Add

  'Add the remaining columns to the default form
  ```
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  oUserObjectMD.FormColumns.FormColumnAlias = "DocEntry"

  oUserObjectMD.FormColumns.FormColumnDescription = "DocEntry"

  oUserObjectMD.FormColumns.Add

  'add the remaining columns to the default form
  ```

## Properties (7)
- `Public Property Code() As String` [R] Returns the Child Object Unique ID., inherited from Parent Object. This Unique ID is the primary key of the user defined object and its Parent object. Field name: Code. Length: 20 characters (must include at least one alphabetical character).
- `Public Property Count() As Long` [R] Returns the number of columns in the default form.
- `Public Property Editable() As BoYesNoEnum` [R/W] Indicates whether the form column is editable (active) or not. Field name: ColEdit.
- `Public Property FormColumnAlias() As String` [R/W] Sets or returns the alias name of the default field to display in the default form. Field name: ColAlias. Length: 10 characters.
- `Public Property FormColumnDescription() As String` [R/W] Sets or returns the description of the default field to display in the default form. Field name: ColDesc. Length: 30 characters.
- `Public Property FormColumnNumber() As Long` [R] Returns the number of the default field to display in the default form. SAP Business One creates a sequential number for each column that you add. Field name: ColumnNum.
- `Public Property SonNumber() As Long` [R/W] Sets or returns the number of the child user table to relate to the default user form. Field name: SonNum.
  - remarks: Mandatory if the user defined object uses the default form service (CanCreateDefaultForm).

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
