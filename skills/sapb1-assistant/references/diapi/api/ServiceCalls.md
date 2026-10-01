<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ServiceCalls (Object)

ServiceCalls is a business object that represents the service calls table in the Service module. This object enables you to: - Add a service call. - Retrieve a service call by its key. - Update a service call. - Remove a service call. - Save the object in XML format. Source table: OSCL.

**Remarks:** Mandatory field in SAP Business One: CustomerCode and Subject. To display the form in the application: - Select Service --> Service Call.

## Properties (90)
- `Public Property Activities() As ServiceCallActivities` [R] Returns the ServiceCallActivities child object.
- `Public Property AddressName() As String` [R/W] property AddressName
- `Public Property AddressType() As BoAddressType` [R/W] property AddressType
- `Public Property AssignedDate() As Date` [R] Returns the assigned date for resolving the service call. Field name: AssignDate.
- `Public Property AssignedTime() As Long` [R] Returns the assigned time for resolving the service call. Field name: AssignTime.
- `Public Property AssigneeCode() As Long` [R/W] Sets or returns the code of the user who is responsible for the service call. Field name: assignee. This is a foreign key to the Users object.
  - remarks: In SAP Business One, the default assignee is the current user that is logged on the system. The list of users is defined in the ASHP table, which is not exposed by the DI API. To apply a service call to an assigned user, first the BelongsToAQueue property to tNO.
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property BelongsToAQueue() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether he service call belongs to a queue or to an assigned user. Field name: isQueue.
- `Public Property BPAddressComponents() As ServiceCallBPAddressComponents` [R] property BPAddressComponents
- `Public Property BPBillToAddress() As String` [R/W] property BPBillToAddress
- `Public Property BPBillToCode() As String` [R/W] property BPBillToCode
- `Public Property BPCellular() As String` [R/W] property BPCellular
- `Public Property BPContactPerson() As String` [R/W] property BPContactPerson
- `Public Property BPeMail() As String` [R/W] property BPeMail
- `Public Property BPFax() As String` [R/W] property BPFax
- `Public Property BPPhone1() As String` [R/W] property BPPhone1
- `Public Property BPPhone2() As String` [R/W] property BPPhone2
- `Public Property BPProjectCode() As String` [R/W] property BPProjectCode
- `Public Property BPShipToAddress() As String` [R/W] property BPShipToAddress
- `Public Property BPShipToCode() As String` [R/W] property BPShipToCode
- `Public Property BPTerritory() As Long` [R/W] property BPTerritory
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CallType() As Long` [R/W] Sets or returns the service call type. Field name: callType. This is a foreign key to the Service Call Types table (OCST), not exposed through the DI API.
- `Public Property City() As String` [R/W] property City
- `Public Property ClosingDate() As Date` [R/W] The date when the service call status is changed to Closed. Field name: closeDate.
- `Public Property ClosingTime() As Long` [R/W] The date when the service call status is changed to Closed. Field name: closeTime.
- `Public Property ClosingTimeEx() As Date` [R/W] property ClosingTimeEx
- `Public Property ContactCode() As Long` [R/W] Sets or returns the code of the contact person from the business partner master data. Field name: contctCode. This is a foreign key to the ContactEmployees object.
- `Public Property ContractEndDate() As Date` [R] Returns the expiration date of the service contract. Field name: cntrctDate. This is a foreign key to the ServiceContracts object.
- `Public Property ContractID() As Long` [R/W] Returns the ID of the service contract. Field name: contractID. This is a foreign key to the ServiceContracts object.
- `Public Property Country() As String` [R/W] property Country
- `Public Property CreationDate() As Date` [R/W] The date when the service call was first opened. Field name: createDate.
- `Public Property CreationTime() As Date` [R/W] The time when the service call was first opened. Field name: createTime.
- `Public Property CustomerCode() As String` [R/W] Sets or returns the customer code, which is the card code in the business partner master data. Mandatory property. Field name: customer. Length: 15 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CustomerName() As String` [R/W] Sets or returns the customer name from the business partner master data. Field name: custmrName. Length: 100 characters. This is a foreign key to the BusinessPartners object.
- `Public Property CustomerRefNo() As String` [R/W] property CustomerRefNo
- `Public Property Description() As String` [R/W] Sets or returns a memo type string that specifies the remarks for the service call. Field name: descrption. Length: 64,000 characters.
- `Public Property DisplayInCalendar() As BoYesNoEnum` [R/W] property DisplayInCalendar
- `Public Property DocNum() As Long` [R/W] property DocNum
- `Public Property Duration() As Double` [R/W] property Duration
- `Public Property DurationType() As BoDurations` [R/W] property DurationType
- `Public Property EndDuedate() As Date` [R/W] property EndDueDate
- `Public Property EndTime() As Date` [R/W] property EndTime
- `Public Property EntitledforService() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the business partner is entitled for a service based on the existence of a valid contract. Field name: isEntitled.
- `Public Property Expenses() As ServiceCallInventoryExpenses` [R] Returns the ServiceCallInventoryExpenses child object.
- `Public Property HandWritten() As BoYesNoEnum` [R/W] property HandWritten
- `Public Property InternalSerialNum() As String` [R/W] Sets or returns the unique internal serial number of the item. Field name: internalSN. Length: 32 characters.
  - remarks: In SAP Business One, if you set the value of ManufacturerSerialNum, the value of the internal serial number is set automatically, and vice versa.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code. Field name: itemCode. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property ItemDescription() As String` [R/W] Sets or returns the item description. Field name: itemName. Length: 100 characters.
- `Public Property ItemGroupCode() As Long` [R] Returns the code of the item group. Field name: itemGroup.
- `Public Property Location() As Long` [R/W] property Location
- `Public Property ManufacturerSerialNum() As String` [R/W] Sets or returns the unique manufacturer serial number of the item. Field name: internalSN. Length: 32 characters.
  - remarks: In SAP Business One, if you set the value of InternalSerialNum, the value of the manufacturer serial number is set automatically, and vice versa.
- `Public Property Origin() As Long` [R/W] Sets or returns the means whereby the complaint was received (such as, e-mail, phone, and so on). Field name: origin. This is a foreign key to the Service Call Origins table (OCSO) - not exposed through the DI API.
- `Public Property PeriodIndicator() As String` [R] property PeriodIndicator
- `Public Property Priority() As BoSvcCallPriorities` [R/W] Sets or returns a valid value of BoSvcCallPriorities type that specifies priority of the complaint (low, medium, or high). Field name: priority.
- `Public Property ProblemSubType() As Long` [R/W] property ProblemSubType
- `Public Property ProblemType() As Long` [R/W] Sets or returns the type of the problem as defined in the SAP Business One application. Field name: problemTyp. This is a foreign key to the Service Call Problem Types table (OSCP) - exposed to DI API using the ServiceCallProblemType object.
- `Public Property Queue() As String` [R/W] Sets or returns the queue ID assigned to the service call. Field name: Queue. Length: 20 characters. This is a foreign key to the Queue table (OQUE), not exposed through the DI API).
  - remarks: To assign a queue to a service call, first set the BelongsToAQueue property to tYES.
- `Public Property Reminder() As BoYesNoEnum` [R/W] property Reminder
- `Public Property ReminderPeriod() As Double` [R/W] property ReminderPeriod
- `Public Property ReminderType() As BoDurations` [R/W] property ReminderType
- `Public Property Resolution() As String` [R/W] Sets or returns a memo type string that specifies the description of the resolution. Field name: resolution. Length: 64,000 characters.
- `Public Property ResolutionDate() As Date` [R/W] Sets or returns the maximum date for resolving a service call. SAP Business One calculates the resolution date based on the the service contract ResolutionTime. Field name: resolution.
  - remarks: In SAP Business One the type of ResolutionDate is Read Only, but to maintain DI API backward compatibility the property type of ResolutionDatee is Read Write.
- `Public Property ResolutionOnDate() As Date` [R] Field name: resolution.
  - remarks: SAP Business One can update this date more than once according to the number of required solutions until the service call is closed.
- `Public Property ResolutionOnTime() As Long` [R] Returns the actual resolution time based on setting details in Resolution property or Solutions property. Field name: resolOnTim.
  - remarks: SAP Business One can update this time more than once according to the number of required solutions until the service call is closed.
- `Public Property ResolutionTime() As Date` [R/W] Sets or returns the maximum time for resolving a service call. SAP Business One calculates the resolution time based on the the service contract ResolutionTime. Field name: resolOnTim.
  - remarks: In SAP Business One the type of ResolutionTime is Read Only, but to maintain DI API backward compatibility the property type of ResolutionTime is Read-Write.
- `Public Property Responder() As Long` [R] Returns the user code of the assignee who responded the service call. Field name: responder.
  - remarks: In case the service call was respond with an activity, then the responder is the user assigned for the activity (HandledBy), else the responder is the AssigneeCode.
- `Public Property ResponseAssignee() As Long` [R] Returns the user code of the assignee who was responsible for the service call when it was actually responded by the Responder. Field name: respAssign.
- `Public Property ResponseByDate() As Date` [R] Returns the maximum date for responding to a service call. SAP Business One calculates the response date based on the service contract ResponseTime. Field name: respByDate.
- `Public Property ResponseByTime() As Long` [R] Returns the maximum time for responding to a service call. SAP Business One calculates the response time based on the the service contract ResponseTime. Field name: respByTime.
- `Public Property ResponseOnDate() As Date` [R] Returns the actual response date. Field name: respOnDate.
  - remarks: SAP Business One sets the ResponseOnDate when one of the following events first occurs: - A meeting or a phone call was added and closed. - A resolution or a solution is set.
- `Public Property ResponseOnTime() As Long` [R] Returns the actual response time. Field name: respOnTime.
- `Public Property Room() As String` [R/W] property Room
- `Public Property Schedulings() As ServiceCallSchedulings` [R] property Schedulings
- `Public Property Series() As Long` [R/W] property Series
- `Public Property ServiceBPType() As ServiceTypeEnum` [R/W] property ServiceBPType
- `Public Property ServiceCallID() As Long` [R] Returns the service call identification number. Field name: callID.
  - remarks: When you add a service call, this property is incremented automatically.
- `Public Property Solutions() As ServiceCallSolutions` [R] Returns the ServiceCallSolutions child object.
- `Public Property StartDate() As Date` [R/W] property StartDate
- `Public Property StartTime() As Date` [R/W] property StartTime
- `Public Property State() As String` [R/W] property State
- `Public Property Status() As Long` [R/W] Sets or returns the status of the service call, such as open, pending, or closed as defined in the SAP Business One application. Field name: status. This is a foreign key to the Service Call Statuses table (OSCS), not exposed through the DI API.
- `Public Property Street() As String` [R/W] property Street
- `Public Property Subject() As String` [R/W] Sets or returns a short description of the problem. Mandatory property. Field name: subject. Length: 254 characters.
- `Public Property SupplementaryCode() As String` [R] property SupplementaryCode
- `Public Property TechnicianCode() As Long` [R/W] Sets or returns the technician code as defined in the employee master data. Field name: technician. This is a foreign key to the EmployeesInfo object.
- `Public Property Telephone() As String` [R/W] property Telephone
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdatedTime() As Long` [R] Returns the update time of the service call, which is used for the history log. Field name: UpdateTime.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (8)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ServiceCallID As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ServiceCallID`: Specifies the service call ID in the database.
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
