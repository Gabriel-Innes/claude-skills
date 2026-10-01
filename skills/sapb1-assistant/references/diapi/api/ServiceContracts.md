<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceContracts (Object)

ServiceContracts is a business object that represents the service contracts table in the Service module of SAP Business One application. This object enables you to: - Add a service contract. - Retrieve a service contract by its key. - Update a service contract. - Remove a service contract. - Save the object in XML format. Source table: OCTR.

**Remarks:** Mandatory fields in SAP Business One: CustomerCode, EndDate, and ResolutionTime. To display the form in the application: - Select Service --> Service Contract.

## Properties (54)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ContactCode() As Long` [R/W] Sets or returns the code of the contact person (from the business partner master data). Field name: CntctCode. This is a foreign key to the ContactEmployees object.
- `Public Property ContractID() As Long` [R] Returns the ID of the service contract. Field name: ContractID.
- `Public Property ContractTemplate() As String` [R/W] Sets or returns the name of the contract template. Field name: CntrcTmplt. Length: 20 characters. This is a foreign key to the ContractTemplates object.
- `Public Property ContractType() As BoContractTypes` [R/W] Sets or returns a valid value of BoContractTypes type that specifies the contract type: Customer, Item Group, or Serial Number. Field name: CntrcType.
- `Public Property CustomerCode() As String` [R/W] Sets or returns the customer code, which is the business partner code. Mandatory field in SAP Business One. Field name: CstmrCode. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CustomerName() As String` [R/W] Sets or returns the customer name, which is the business partner name. Field name: CstmrName. Length: 100 characters. This is a foreign key to the BusinessPartners object.
- `Public Property Description() As String` [R/W] Sets or returns a string that describes the service contract. Field name: Descriptio. Length: 254 characters.
- `Public Property DurationOfCoverage() As Long` [R] Sets or returns the duration of the service contract coverage. Field name: duration.
- `Public Property EndDate() As Date` [R/W] Sets or returns the end date of the service contract. Mandatory field in SAP Business One. Field name: EndDate.
  - remarks: SAP Business One calculates the EndDate using the values of the StartDate and DurationOfCovarge properties.
- `Public Property FridayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Fridays to the contract coverage. Field name: FriEnabled.
- `Public Property FridayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Fridays. Field name: FriEnd.
- `Public Property FridayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Fridays. Field name: FriStart.
- `Public Property IncludeHolidays() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include holidays to the service contract coverage. Field name: InclHldays.
- `Public Property IncludeLabor() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include technician's work to the service contract coverage. Field name: InclWork.
- `Public Property IncludeParts() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include replacement parts (items) to the service contract coverage. Field name: InclParts.
- `Public Property IncludeTravel() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include travel to the service contract coverage. Field name: InclTravel.
- `Public Property Lines() As ServiceContract_Lines` [R] Returns the ServiceContract_Lines child object.
- `Public Property MondayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Mondays to the service contract coverage. Field name: WedEnabled.
- `Public Property MondayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Monday. Field name: MonEnd. Sets or returns the ending working hour, for the service coverage, on Mondays. Field name: MonEnd.
- `Public Property MondayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Monday. Field name: MonStart. Sets or returns the beginning working hour, for the service coverage, on Mondays. Field name: MonStart.
- `Public Property Owner() As Long` [R/W] Sets or returns the name or title of the employee that is responsible for the service contract. Field name: Owner. This is a foreign key to the Users Object.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks for the service contract (in addition to the remarks from the contract template). Length: 64,000 characters. Field name: Remarks1.
- `Public Property ReminderTime() As Long` [R/W] Sets or returns the number of days, weeks, or months for the alert to appear prior to the termination of the contract. To enable this reminder, set the Renewal property to tYES. Field name: RemindVal.
- `Public Property RemindUnit() As BoRemindUnits` [R/W] Sets or returns a valid value of BoRemindUnits type that specifies the units (days, weeks, or months) for the ReminderTime property. Field name: RemindUnit.
- `Public Property Renewal() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to renew the service contract. Field name: Renewal.
- `Public Property ResolutionTime() As Long` [R/W] Sets or returns the maximum time, in days or hours, to resolve a service call. Field name: ResponsVal.
- `Public Property ResolutionUnit() As BoResolutionUnits` [R/W] Sets or returns a valid value of BoResolutionUnits type that specifies the units, hours or days, for the ResolutionTime property. Field name: ResponsUnt.
- `Public Property ResponseTime() As Long` [R/W] Sets or returns the maximum time, in hours or days, to respond to a service call. Field name: ResponseV.
- `Public Property ResponseUnit() As BoResponseUnit` [R/W] Sets or returns a valid value of BoResponseUnit type that specifies the units, hours or days, for the ResponseTime property. Field name: ResponseU.
- `Public Property SaturdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Saturdays to the service contract coverage. Field name: SatEnabled.
- `Public Property SaturdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Saturday. Field name: SatEnd. Sets or returns the ending working hour, for the service coverage, on Saturdays. Field name: SatEnd.
- `Public Property SaturdayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Saturday. Field name: SatStart. Sets or returns the beginning working hour, for the service coverage, on Saturdays. Field name: SatStart.
- `Public Property ServiceBPType() As ServiceTypeEnum` [R/W] property ServiceBPType
- `Public Property ServiceType() As BoServiceTypes` [R/W] Sets or returns a valid value of BoServiceTypes type that specifies the service type of the contract: Regular or Warranty. Field name: SrvcType.
- `Public Property StartDate() As Date` [R/W] Sets or returns the start date of the service contract. Field name: StartDate.
- `Public Property Status() As BoSvcContractStatus` [R/W] Sets or returns a valid value of BoSvcContractStatus type that specifies the status of the service contract (approved, on-hold, or draft). Field name: Status.
- `Public Property SundayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Sundays to the service contract coverage. Field name: SunEnabled.
- `Public Property SundayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Sunday. Field name: SunEnd. Sets or returns the ending working hour, for the service coverage, on Sundays. Field name: SunEnd.
- `Public Property SundayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Sunday. Field name: SunStrart. Sets or returns the beginning working hour, for the service coverage, on Sundays. Field name: SunStrart.
- `Public Property TemplateRemarks() As String` [R] Returns a memo type string that specifies remarks for the contract template as defined in the Remarks property of the ContractTemplates object. Field name: Remarks1. Length: 64,000 characters.
- `Public Property TerminationDate() As Date` [R/W] Sets or returns the termination date of the service contract. Field name: TermDate.
- `Public Property ThursdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Thursdays to the service contract coverage. Field name: ThuEnabled.
- `Public Property ThursdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Thursdays. Field name: ThuEnd. Sets or returns the ending working hour, for the service coverage, on Thursdays. Field name: ThuEnd.
- `Public Property ThursdayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Thursdays. Field name: ThuStart. Sets or returns the beginning working hour of the company on Thursdays. Field name: ThuStart.
- `Public Property TuesdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Tuesdays to the service contract coverage. Field name: TueEnabled.
- `Public Property TuesdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Tuesdays. Field name: TueEnd. Sets or returns the ending working hour, for the service coverage, on Tuesdays. Field name: ThuEnd.
- `Public Property TuesdayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Tuesdays. Field name: TueStart. Sets or returns the beginning working hour of the company on Tuesdays. Field name: ThuStart.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WednesdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Wednesdays to the service contract coverage. Field name: WedEnabled.
- `Public Property WednesdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Wednesdays. Field name: WedEnd. Sets or returns the ending working hour, for the service coverage, on Wednesdays. Field name: WedEnd.
- `Public Property WednesdayStart() As Date` [R/W] Sets or returns the starting working hour, for the service coverage, on Wednesdays. Field name: WedStart. Sets or returns the beginning working hour, for the service coverage, on Wednesdays. Field name: WedStart.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ContractID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ContractID`: Specifies the service contract identification key.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported. Field name: .
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
