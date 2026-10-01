<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ContractTemplates (Object)

ContractTemplates is a business object that represents the contract templates in the Service module. This object enables you to: - Add a contract template. - Retrieve a contract template by its key. - Update a contract template. - Remove a contract template. - Save the object in XML format. Source table: OCTT.

**Remarks:** Mandatory field in SAP Business One: TemplateName. To display the form in the application: - Select Administration --> Setup --> Service --> Contract Templates.

## Properties (42)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ContractType() As BoContractTypes` [R/W] Sets or returns a valid value of BoContractTypes that specifies the service contract types for the contract template. Field name: CntrctType.
- `Public Property Description() As String` [R/W] Sets or returns the description of the contract template. Field name: Remark. Length: 16 characters.
- `Public Property DurationOfCoverage() As Long` [R/W] Sets or returns the duration of the service contract coverage in the contract template. Field name: Duration.
- `Public Property FridayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Fridays to the contract template coverage. Field name: FriEnabled.
- `Public Property FridayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Fridays. Field name: FriEnd.
- `Public Property FridayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Fridays. Field name: FriStart.
- `Public Property IncludeHolidays() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include holidays to the contract template coverage. Field name: InclHldays.
- `Public Property IncludeLabor() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include technician's work to the contract template coverage. Field name: InclWork.
- `Public Property IncludeParts() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include replacement parts (items) to the contract template coverage. Field name: InclParts.
- `Public Property IncludeTravel() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include travel to the contract template coverage. Field name: InclTravel.
- `Public Property MondayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Mondays to the contract template coverage. Field name: MonEnabled.
- `Public Property MondayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Mondays. Field name: MonEnd.
- `Public Property MondayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Mondays. Field name: MonStart.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks for the contract template. Field name: Descriptio. Length: 64,000 characters.
- `Public Property RemindBeforeRenewal() As Long` [R/W] Sets or returns the number of days, weeks, or months for the alert to appear prior to the termination of the contract. To enable this reminder, set the TemplateIsRenewal property to tYES. Field name: Renewal.
- `Public Property RemindUnit() As BoRemindUnits` [R/W] Sets or returns a valid value of BoRemindUnits type that specifies the units (days, weeks, or months) for the RemindBeforeRenewal property. Field name: RemindUnit.
- `Public Property ResolutionTime() As Long` [R/W] Sets or returns the maximum time, in hours or days, to resolve the service call. Field name: ResponsVal.
- `Public Property ResolutionUnit() As BoResolutionUnits` [R/W] Sets or returns a valid value of BoResolutionUnits type that specifies the units, hours or days, for the ResolutionTime property. Field name: ResponsUnt.
- `Public Property ResponseUnit() As BoResponseUnit` [R/W] Sets or returns a valid value of BoResponseUnit type that specifies the units, hours or days, for the ResponseValue property. Field name: ResponseU.
- `Public Property ResponseValue() As Long` [R/W] Sets or returns the maximum time, in hours or days, to respond to a service call. Field name: ResponseV.
- `Public Property SaturdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Saturdays to the contract template coverage. Field name: SatEnabled.
- `Public Property SaturdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Saturdays. Field name: SatEnd.
- `Public Property SaturdayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Saturdays. Field name: SatStart.
- `Public Property SundayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Sundays to the contract template coverage. Field name: SunEnabled.
- `Public Property SundayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Sundays. Field name: SunEnd.
- `Public Property SundayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Sundays. Field name: SunStrart.
- `Public Property TemplateIsDeleted() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the contract template is expired. Field name: TmpltName.
- `Public Property TemplateIsRenewal() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to renew the service contract. Field name: Renewal.
- `Public Property TemplateName() As String` [R/W] Sets or returns the name for the contract template. Field name: TmpltName. Mandatory field in SAP Business One. Length: 20 characters.
- `Public Property ThursdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Thursdays to the contract template coverage. Field name: ThuEnabled.
- `Public Property ThursdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Thursdays. Field name: ThuEnd.
- `Public Property ThursdayStart() As Date` [R/W] Sets or returns the beginning working hour of the company on Thursdays. Field name: ThuStart.
- `Public Property TuesdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Tuesdays to the contract template coverage. Field name: ThuEnabled.
- `Public Property TuesdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Tuesdays. Field name: ThuEnd.
- `Public Property TuesdayStart() As Date` [R/W] Sets or returns the beginning working hour of the company on Tuesdays. Field name: ThuStart.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WednesdayEnabled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include Wednesdays to the contract template coverage. Field name: WedEnabled.
- `Public Property WednesdayEnd() As Date` [R/W] Sets or returns the ending working hour, for the service coverage, on Wednesdays. Field name: WedEnd.
- `Public Property WednesdayStart() As Date` [R/W] Sets or returns the beginning working hour, for the service coverage, on Wednesdays. Field name: WedStart.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal TemplateName As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `TemplateName`: Specifies the template name.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Not supported.
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
