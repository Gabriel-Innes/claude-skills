<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Contacts (Object)

Contacts is a business object that represents the activities with customers and vendors in the Business Partners module. This object enables you to: - Add an activity. - Retrieve an activity by its key. - Update an activity. - Save the object in XML format. Source table: OCLG.

**Remarks:** Mandatory fields in SAP Business One: CardCode (only if the activity is not personal) and ContactPersonCode. To display the form in the application: - Select Business Partners --> Activities. Auto-complete of the Activity Schedule Properties (new for release 2005) The schedule of the activity must be specified at the database level, therefore the system completes automatically the values of the properties that are related to the activity schedule. These properties include: - Start time - combination of StartDate and StartTime. - Duration - combination of Duration and DurationType. - End time - combination of EndDuedate and EndTime. When adding or updating an activity, there are five scenarios for the auto-complete operation according to the specified values: 1. If no value is specified (when adding only), then the system sets the following default values: - Start time - the current time when adding the activity. - Duration - 15 minutes (0 minute when upgrading the system to release 2005). - End time - the system calculates the values as follows: End time = Start time + Duration. 2. If all three values are specified (when adding or updating), then the system checks their validity, and if there is an error the system issues an error message (-5002 - invalid object). 3. If two values are specified (or modified when updating), then the system calculates (or recalculates) the remaining value as follows: - Start time and End time are specified - the system calculates the Duration. - Start time and Duration are specified - the system calculates the End time. - Duration and End time are specified - when adding, the system sets Start time to default and recalculates the Duration. When updating, the Start time remains the same and the system recalculates the Duration. 4. If one value is specified (when adding only), then the system calculates the remaining values as follows: - Start time is specified - the system sets the Duration to default and calculates the End time. - Duration is specified - the system sets the Start time to default and calculates the End time. - End time is specified - the system sets the Start time to default and calculates the Duration. 5. If one value is modified (when updating only), then the system recalculates the remaining value as follows: - Start time is specified - the system recalculates the End time (for release 2005) or the Duration (for release 2004). - Duration is specified - the system recalculates the End time. - End time is specified - the system recalculates the Duration.

## Properties (48)
- `Public Property Activity() As BoActivities` [R/W] Sets or returns a valid value of BoActivities type that specifies activity with the business partner. Field name: Action.
- `Public Property ActivityType() As Long` [R/W] Sets or returns the type of the activity. Field name: CntctType. This is a foreign key to the ActivityTypes object.
  - remarks: You can add new activity types to the list using the ActivityTypes object.
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Mandatory field in SAP Business One only if the activity is not personal . Length: 15 characters. This is a foreign key to the BusinessPartners object.
  - remarks: Mandatory property. SAP Business One validates the CardCode, and if not valid, returns an error code.
- `Public Property City() As String` [R/W] Sets or returns the city where the Activity (Meeting type only) with the business partner takes place. Field name: city. Length: 100 characters.
- `Public Property Closed() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the activity is closed and no further processing is required. Field name: Closed.
  - remarks: You can use the CloseDate property to find out the closing date.
- `Public Property CloseDate() As Date` [R/W] Sets or returns the closing date of the activity. Field name: CloseDate.
  - remarks: In case the end-user does not enter a value, the system completes automatically the closing date.
- `Public Property ContactCode() As Long` [R] Returns the identification key of the activity. Field name: CntctCode.
- `Public Property ContactDate() As Date` [R/W] Sets or returns the contact date. Field name: CntctDate.
- `Public Property ContactPersonCode() As Long` [R/W] Sets or returns the internal code for the contact person. Field name: CntctCode. Mandatory property. This is a foreign key to the ContactEmployees object.
- `Public Property ContactTime() As Date` [R/W] Sets or returns the activity time. Field name: CntctTime.
  - remarks: In case the end-user does not enter a value, the system completes automatically the contact time.
- `Public Property Country() As String` [R/W] Sets or returns the country where the Activity (Meeting type only) with the business partner takes place. Field name: country. Length: 3 characters. This is a foreign key to the Countries table (OCRY).
- `Public Property Details() As String` [R/W] Sets or returns the details for the next action. Field name: Details. Length: 60 characters.
- `Public Property DocEntry() As String` [R/W] Sets or returns the document entry key. Field name: DocEntry. Length: 20 characters.
  - remarks: You can use this key to reference a document.
- `Public Property DocNum() As String` [R] Returns the number of the linked document. Field name: DocNum. Length: 20 characters.
- `Public Property DocType() As Long` [R/W] Sets or returns the type of the document, such as invoice or purchase order, that is linked to the activity. Field name: DocType.
- `Public Property DocTypeEx() As String` [R/W] The document type that is linked to the activity. This property replaces the DocType property (integer). Length: 20 characters. Field name: DocNum.
  - remarks: The valid values are: '13' - 'A/R Invoice' '14' - 'A/R Credit Memo' '15' - 'Delivery' '16' - 'Return' '17' - 'Sales Order' '18' - 'A/P Invoice' '19' - 'A/P Credit Memo' '20' - 'Goods Receipt PO' '21' - 'Goods Return' '22' - 'Purchase order' '23' - 'Sales Quotation' '24' - 'Incoming Payment' '25' - 'Deposit' '30' - 'Journal Entry' '46' - 'Outgoing Payment' '57' - 'Checks for Payment' '59' - 'Goods Receipt' '60' - 'Goods Issue' '1250000001' - 'Stock Transfer Request' '67' - 'Stock Transfer' '68' - 'Work Order' '69' - 'Landed Costs' '132' - 'Correction Invoice' '162' - 'Material Revaluation' '202' - 'Production Order' '203' - 'AR Down Payment' '204' - 'AP Down Payment' '140000009' - 'Outgoing Excise Invoice' '140000010' - 'Incoming Excise Invoice' '-1' - '' '0' - '' '4' - 'Items' '163' - 'AP Correction Invoice' '164' - 'AP Correction Invoice Reversal' '165' - 'AR Correction Invoice' '166' - 'AR Correction Invoice Reversal' '1320000012' - 'Campaign' '540000006' - 'Purchase Quotation' '1250000025' - 'Blanket Agreements' '1470000113' - 'Purchase Request' '112' - 'Document Drafts' '140' - 'Payment Drafts' '123' - 'Checks for Payment Drafts' '254000065' - 'Self Invoice' '254000066' - 'Self Credit Note' '234000031' - 'Return Request' '234000032' - 'Goods Return Request' '1250000026' - 'Sales Blanket Agreement' '1250000027' - 'Purchase Blanket Agreement'
- `Public Property Duration() As Double` [R/W] Sets or returns the amount of time scheduled for the activity. Field name: Duration.
  - remarks: The duration value specifies the number of minutes, hours, or days according to the DurationType. The duration value must be equal or greater than 0. In case the start time (days + hours) and end time (days + hours) are specified, then the system recalculates the duration time.
- `Public Property DurationType() As BoDurations` [R/W] Sets or returns a valid value of BoDurations type that specifies the duration type for the activity (minutes, hours, or days). Field name: DurType.
- `Public Property EndDuedate() As Date` [R/W] Sets or returns the due date for completing the activity. Field name: endDate.
  - remarks: The end date must be later than the start date.
- `Public Property EndTime() As Date` [R/W] Sets or returns the end time (hh:mm) of the activity. Field name: ENDTime.
  - remarks: The end time must be later than the start time.
- `Public Property Fax() As String` [R/W] Sets or returns the fax number of the contact person. Field name: Fax. Length: 50 characters.
- `Public Property HandledBy() As Long` [R/W] Sets or returns the name or title of the person who is responsible for entering the activity details. Field name: AttendUser. This is a foreign key to the Users object.
- `Public Property Inactiveflag() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the the activity is inactive. Field name: inactive.
- `Public Property Location() As Long` [R/W] Sets or returns the code for the activity location. Field name: Location. This is a foreign key to the ActivityLocations object.
  - remarks: You can add new locations to the list using the ActivityLocations object.
- `Public Property Notes() As String` [R/W] Sets or returns a memo type string that specifies remarks regarding the activity. Field name: Notes. Length: 16 characters.
- `Public Property ParentobjectId() As Long` [R] Returns the source object ID of the activity: - For Service Call object type: ServiceCallID. - For Sales Opportunity object type: SequentialNo. Field name: parentId.
- `Public Property Parentobjecttype() As String` [R] Returns the source object type of the activity: Sales Opportunity or Service Call. Field name: parentType. Length: 20 characters.
- `Public Property Personalflag() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether the the activity is personal or business. If business, you must set the business partner details (CardCode). Field name: personal.
- `Public Property Phone() As String` [R/W] Sets or returns the phone number of the contact person. Field name: Tel. Length: 50 characters.
- `Public Property PreviousActivity() As Long` [R/W] Sets or returns the previous activity number (ContactCode) related to the current activity. Field name: prevActvty.
- `Public Property Priority() As BoMsgPriorities` [R/W] Sets or returns a valid value of BoMsgPriorities type that specifies the priority of the activity (low, normal, or high). Field name: Priority.
- `Public Property Recontact() As Date` [R/W] Sets or returns the date for the next activity. Field name: Recontact.
- `Public Property Reminder() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not SAP Business One will send a reminder message to the user mailbox ('user' means the current SAP Business One user). Field name: Reminder.
- `Public Property ReminderPeriod() As Double` [R/W] Sets or returns the duration for sending the reminder message. Field name: RemTime.
- `Public Property ReminderType() As BoDurations` [R/W] Sets or returns a valid value of BoDurations type that specifies the duration types: minutes or hours. Field name: RemType.
- `Public Property Room() As String` [R/W] Sets or returns the room where the Activity (Meeting type only) with the business partner takes place. Field name: room. Length: 50 characters.
- `Public Property SalesEmployee() As Long` [R/W] Sets or returns the code of the sales employee who is responsible for the activity. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: The sales employees can be defined through the SalesPersons object (see SalesEmployeeCode).
- `Public Property StartDate() As Date` [R/W] Sets or returns the start date of the activity. Field name: Recontact.
- `Public Property StartTime() As Date` [R/W] Sets or returns the start time (hh:mm) of the activity. Field name: BeginTime.
- `Public Property State() As String` [R/W] Sets or returns the code of the state where the Activity (Meeting type only) with the business partner takes place. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST).
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property Status() As Long` [R/W] Sets or returns the status of the Activity (Task type only) as defined in ActivityStatus object. Field name: status. This is a foreign key to the ActivityStatus object.
- `Public Property Street() As String` [R/W] Sets or returns the street where the Activity (Meeting type only) with the business partner takes place. Field name: street. Length: 100 characters.
- `Public Property Subject() As String` [R/W] Sets or returns the subject of the activity. Field name: CntctSbjct.
- `Public Property Tentativeflag() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the activity is tentative. Field name: tentative.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (6)
- `Public Function Add() As Long` Adds a new activity with a business partner.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ContactCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ContactCode`: Specifies the identification key of the activity (see ContactCode property).
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
