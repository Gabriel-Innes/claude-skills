<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Recipients (Object)

Recipients is a business object that represents the recipients' list of a message or alert. This object enables you to add recipient information to the recipients list for sending messages. You can use the RecipientCollection and the Recipient object instead of the Recipients object (backward compatibilty is maintained). Source table: AOB1.

**Remarks:** Mandatory fields in SAP Business One: UserCode and UserType. To display the form in the application: - From the main menu bar, select File --> Send --> Send Message. - Click Add Recipient.

## Properties (11)
- `Public Property CellularNumber() As String` [R/W] Sets or returns the cellular phone number of the recipient. Field name: PortNum. Length: 50 characters.
- `Public Property Count() As Long` [R] Returns the number of recipients in the collection.
  - remarks: After adding a new recipient, the value of this property increases automatically.
- `Public Property EmailAddress() As String` [R/W] Sets or returns the recipient email address. Field name: E_Mail. Length: 100 characters.
- `Public Property FaxNumber() As String` [R/W] Sets or returns the recipient fax number. Field name: Fax. Length: 20 characters.
- `Public Property NameTo() As String` [R/W] Sets or returns the recipient name. Field name: ObjName. Length: 100 characters.
- `Public Property SendEmail() As BoYesNoEnum` [R/W] Determines whether or not the message is sent to an email address. Field name: SendEMail.
- `Public Property SendFax() As BoYesNoEnum` [R/W] Determines whether or not the message is sent by fax. Field name: SendFax.
- `Public Property SendInternal() As BoYesNoEnum` [R/W] Determines whether or not the message is internal. That is, the message will be sent only to users (employees) that are defined in SAP Business One. Field name: SendIntrnl.
- `Public Property SendSMS() As BoYesNoEnum` [R/W] Determines whether or not the message is sent by SMS. Field name: SendSMS.
- `Public Property UserCode() As String` [R/W] Sets or returns the user code of the recipient. Mandatory property. Field name: ObjCode. Length: 50 characters.
  - remarks: The user code is a reference to a key in the database table.
- `Public Property UserType() As BoMsgRcpTypes` [R/W] Sets or returns a valid value that specifies the type of recipient for the message. Mandatory property. Field name: ObjType.

## Methods (2)
- `Public Sub Add()` Adds a new recipient to the collection.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
