<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlertManagementRecipient (Object)

AlertManagementRecipient is a data structure related to the AlertManagementService and defines the properties of the AlertManagementService's recipient. Source table: ALT1.

## Properties (6)
- `Public Property Code() As Long` [R] Returns the Internal Number of this alert's Recipient. Field name: Code.
- `Public Property SendEmail() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not to alert the recipient by sending an email. Field name: SendEMail.
- `Public Property SendFax() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not to alert the recipient by sending a FAX. Field name: SendFax.
- `Public Property SendInternal() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not to alert the recipient by sending Internal message. Field name: SendIntrnl.
- `Public Property SendSMS() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not to alert the recipient by sending an SMS message. Field name: SendSMS.
- `Public Property UserCode() As Long` [R/W] Sets or returns the User Signature. Field name: UserSign. This is foreign key to the Users object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object's data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object's data.
