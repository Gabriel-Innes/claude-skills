<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlertManagementDocuments (Collection)

AlertManagementDocuments is a Data Collection of AlertManagementDocument data structures. Source table: OALT.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of AlertManagementDocument in the AlertManagementDocuments data collection. Field name: NumOfDocs.

## Methods (5)
- `Public Function Add() As AlertManagementDocument` Adds new AlertManagementDocument to the data-collection object.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As AlertManagementDocument` Returns reference to existing AlertManagementDocument in the collection by its index.
  - param `vtIndex`: Specifies the index of the new AlertManagementDocument you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.
