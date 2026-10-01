<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MessageHeader (Object)

MessageHeader is a data structure related to the MessagesService. The data is stored temporarily in the memory in a virtual table (at a later stage, the data is stored in the OAOB and OAIB tables). Source tables: - OAOB (Message Sent). - OAIB (Received Alerts).

## Properties (7)
- `Public Property Code() As Long` [R/W] Sets or returns the message key. Field name: AlertCode.
- `Public Property Read() As BoYesNoEnum` [R] Determines whether or not the message was read by the recipient (see OAIB table). Field name: WasRead.
- `Public Property Received() As BoYesNoEnum` [R] Determines whether or not the message was opened by the recipient (see OAIB table). Field name: Opened.
- `Public Property ReceivedDate() As Date` [R] Returns the received date (see OAIB table). Field name: RecDate.
- `Public Property ReceivedTime() As Date` [R] Returns the received time (see OAIB table). Field name: RecTime.
- `Public Property SentDate() As Date` [R] Returns the sent date (see OAOB table). Field name: SendDate.
- `Public Property SentTime() As Date` [R] Returns the sent time (see OAOB table). Field name: SendTime.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
