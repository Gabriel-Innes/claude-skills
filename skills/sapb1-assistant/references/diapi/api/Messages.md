<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Messages (Object)

Messages is a business object that represents the messages in the Administration module. This object enables you to send messages through SAP Business One messaging service. You can use the MessagesService, which enables more functions than the Messages object. Source table: OALR.

**Remarks:** To display the form in the application: - From the main menu bar, select File --> Send --> Send Message.

## Properties (6)
- `Public Property AttachmentEntry() As Long` [R/W] Sets or returns the identification key of the attachment file, as assigned by SAP Business One when adding an Attachment Entry to alert message. Field name: AtcEntry.
- `Public Property Attachments() As Attachments` [R] Returns the Attachments object.
- `Public Property MessageText() As String` [R/W] Sets or returns a memo type string that specifies the message text. Field name: MsgData. Length: 64,000 characters.
- `Public Property Priority() As BoMsgPriorities` [R/W] Sets or returns a valid value that determines the message priority. Field name: ).
- `Public Property Recipients() As Recipients` [R] Returns a Recipients object, which specifies the recipients of this message.
- `Public Property Subject() As String` [R/W] Sets or returns the message subject. Field name: Subject. Length: 50 characters.

## Methods (2)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Sub AddDataColumn(ByVal Title As String, ByVal Text As String, ByVal Object As BoObjectTypes, ByVal ObjectKey As String)` Links a business object to your message.
  - param `Title`: Specifies the column title.
  - param `Text`: Specifies column description.
  - param `Object`: one of the enumeration's values (see the enum file)
  - param `ObjectKey`: Specifies the object key.
  - enum: `../enums/BoObjectTypes.md`
