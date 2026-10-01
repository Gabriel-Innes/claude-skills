<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateParams (Object)

The ApprovalTemplateParams specifies the identification key combination (Code and Name) for which the ApprovalTemplatesService is related. Source table: OWTM.

## Properties (2)
- `Public Property Code() As Long` [R/W] Sets or returns this approval template Code. Field name: WtmCode. This is a key to the ApprovalTemplate object.
- `Public Property Name() As String` [R] Returns this approval template Name. Field name: Name. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
