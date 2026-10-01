<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Recipient (Object)

Recipient is a data structure related to the MessagesService. It represents the data of a single recipient of a message or alert. Source table: AOB1.

## Properties (10)
- `Public Property CellularNumber() As String` [R/W] Sets or returns the cellular phone number of the recipient. Field name: PortNum. Length: 50 characters.
- `Public Property EmailAddress() As String` [R/W] Sets or returns the recipient email address. Field name: E_Mail. Length: 100 characters.
- `Public Property FaxNumber() As String` [R/W] Sets or returns the recipient fax number. Field name: Fax. Length: 20 characters.
- `Public Property NameTo() As String` [R/W] Sets or returns the recipient name. Field name: ObjName. Length: 100 characters.
- `Public Property SendEmail() As BoYesNoEnum` [R/W] Determines whether or not the message is sent to an email address. Field name: SendEMail.
- `Public Property SendFax() As BoYesNoEnum` [R/W] Determines whether or not the message is sent by fax. Field name: SendFax.
- `Public Property SendInternal() As BoYesNoEnum` [R/W] Determines whether or not the message is internal. That is, the message will be sent only to users (employees) that are defined in SAP Business One. Field name: SendIntrnl.
- `Public Property SendSMS() As BoYesNoEnum` [R/W] Determines whether or not the message is sent by SMS. Field name: SendSMS.
- `Public Property UserCode() As String` [R/W] Sets or returns the user code of the recipient. Mandatory property. Field name: ObjCode. Length: 50 characters.
- `Public Property UserType() As BoMsgRcpTypes` [R/W] Sets or returns a valid value that specifies the type of recipient for the message. Mandatory property. Field name: ObjType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: P>Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
