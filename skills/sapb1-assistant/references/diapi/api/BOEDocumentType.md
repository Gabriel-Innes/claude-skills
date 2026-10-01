<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BOEDocumentType (Object)

A data structure object holding properties for the BOEDocumentTypesService. Source table: ODTY.

## Properties (3)
- `Public Property DocDescription() As String` [R/W] Sets or returns a string specifying the document description. Field name: DocDespt.
- `Public Property DocEntry() As Long` [R] Returns a string specifying the document entry. Field name: AbsEntry.
- `Public Property DocType() As String` [R/W] Sets or returns a string specifying the document type. Field name: DocType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
