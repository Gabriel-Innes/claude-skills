<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateStages (Collection)

ApprovalTemplateStages is a Data Collection of ApprovalTemplateStage data structures. Source table: WTM2.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateStage data structures in the ApprovalTemplateStages data collection.

## Methods (5)
- `Public Function Add() As ApprovalTemplateStage` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateStage` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.
