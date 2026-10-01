<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CallMessage (Object)

This object represents the response message to the request call. Source table: REQ1.

## Properties (8)
- `Public Property CallMessageArguments() As CallMessageArguments` [R] Returns the arguments of a single response message.
- `Public Property CreationDate() As Date` [R/W] Sets or returns the date when the message is created.
- `Public Property CreationTime() As Long` [R/W] Sets or returns the time when the message is created.
- `Public Property ErrorCode() As String` [R/W] Sets or returns an error type of a message (agreed between the request sender and receiver).
- `Public Property ID() As Long` [R] Returns the unique ID of a call message.
- `Public Property MessageBody() As String` [R/W] Sets or returns the content of the message.
- `Public Property Status() As CallMessageStatusEnum` [R] Returns the status of the response message: Read or Unread.
- `Public Property Type() As CallMessageTypeEnum` [R/W] Returns the type of the call message.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object's data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object's data.
