<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateDocuments (Collection)

ApprovalTemplateDocuments is a Data Collection of ApprovalTemplateDocument data structures. Source table: WTM3.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateDocument data structures in the ApprovalTemplateDocuments data collection. Field name: NumOfDocs).

## Methods (5)
- `Public Function Add() As ApprovalTemplateDocument` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateDocument` Returns reference to existing ApprovalTemplateDocument in the collection by its index.
  - param `vtIndex`: Specifies the index of the ApprovalTemplateDocument you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
