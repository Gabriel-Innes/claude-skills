<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateQueries (Collection)

ApprovalTemplateQueries is a Data Collection of ApprovalTemplateQuery data structures. Source table: WTM5.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateQuery data structures. in the ApprovalTemplateQueries data collection. Field name: NumOfDocs.

## Methods (5)
- `Public Function Add() As ApprovalTemplateQuery` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateQuery` Returns reference to existing ApprovalTemplateQuery in the collection (by its index).
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
