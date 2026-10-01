<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalStageApprovers (Collection)

ApprovalStageApprovers is a Data Collection of ApprovalStageApprover data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalStageApprover data structures, in the ApprovalStageApprovers data collection.

## Methods (5)
- `Public Function Add() As ApprovalStageApprover` Adds a new ApprovalStageApprover to the ApprovalStageApprovers Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the ApprovalStageApprover data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalStageApprover` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
