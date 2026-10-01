<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateDocument (Object)

ApprovalTemplateDocument is a data structure related to the ApprovalTemplatesService. Source table: WTM3.

## Properties (1)
- `Public Property DocumentType() As ApprovalTemplatesDocumentTypeEnum` [R/W] Sets or returns a valid value that defines this document type. Field name: TransType. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
