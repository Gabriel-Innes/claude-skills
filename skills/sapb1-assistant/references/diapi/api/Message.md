<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Message (Object)

Message is a data structure related to the MessagesService. It includes properties related to the message content, such as subject, text, attached file, and attached data. Source table: OALR.

**Remarks:** The Message object replaces the Messages object. However, add-on that use the Messages object are valid. The major modification is in the way of attaching data to a message. That is, using the MessageDataColumn and MessageDataLine instead of AddDataColumn (Messages. To display the form in the application: - From the main menu bar, click the Message/Alert Overview icon.

## Properties (7)
- `Public Property Attachment() As Long` [R/W] Sets or returns the key of the attachment as assigned by SAP Business One when adding an attached file. Field name: Attachment.
- `Public Property MessageDataColumns() As MessageDataColumns` [R/W] Sets or returns the MessageDataColumns collection, which represents the data attached to a message.
- `Public Property Priority() As BoMsgPriorities` [R/W] Determines the priority flag of the message: Low, Normal, or High. Field name: Priority.
- `Public Property RecipientCollection() As RecipientCollection` [R/W] Sets or returns the RecipientCollection.
- `Public Property Subject() As String` [R/W] Sets or returns the message subject. Field name: Subject. Length: 50 characters.
- `Public Property Text() As String` [R/W] Sets or returns the message text. Field name: UserText. Length: 64,000 characters.
- `Public Property User() As Long` [R/W] Sets or returns the ID of the user that creates the message. Field name: UserSign. This is a foreign key to the Users object (InternalKey).

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
