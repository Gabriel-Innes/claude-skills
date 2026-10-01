<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateUsers (Collection)

ApprovalTemplateUsers is a Data Collection of ApprovalTemplateUser data structures. Source table: WTM1.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateUser data structures in the ApprovalTemplateUsers data collection. Field name: NumOfDocs.

## Methods (5)
- `Public Function Add() As ApprovalTemplateUser` Adds a new ApprovalTemplateUser to the ApprovalTemplateUsers Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the ApprovalTemplateUser data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateUser` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
