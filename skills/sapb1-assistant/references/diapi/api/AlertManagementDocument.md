<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlertManagementDocument (Object)

AlertManagementDocument is a data structure related to the AlertManagementService. Source table: OALT.

## Properties (2)
- `Public Property Active() As BoYesNoEnum` [R/W] Determines whether or not the Alert Template Document is Active. Field name: Active.
- `Public Property Document() As AlertManagementDocumentEnum` [R/W] Sets or returns valid value of the Alert Template Document type. Field name: Document.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
