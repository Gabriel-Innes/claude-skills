<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalStages (Collection)

The ApprovalStages is a Data Collection of ApprovalStage data structure. Source table: OWST.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalStage data structures in the ApprovalStages data collection.

## Methods (5)
- `Public Function Add() As ApprovalStage` Adds a new ApprovalStage data structure to the ApprovalStages Object.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalStage` Returns a reference to the ApprovalStage you want to get by its index.
  - param `vtIndex`: Specifies the index of the new item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
