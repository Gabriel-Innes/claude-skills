<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplates (Collection)

ApprovalTemplates is a Data Collection of ApprovalTemplate data structures. Source table: OWTM.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplate data structures in the ApprovalTemplates data collection. Field name: NumOfDocs.

## Methods (5)
- `Public Function Add() As ApprovalTemplate` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplate` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the new item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
