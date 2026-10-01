<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalTemplateTerms (Collection)

ApprovalTemplateTerms is a Data Collection of ApprovalTemplateTerm data structures. Source table: WTM4.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalTemplateTerm data structures in the ApprovalTemplateTerms data collection. Field name: NumOfDocs).

## Methods (5)
- `Public Function Add() As ApprovalTemplateTerm` Adds a new ApprovalTemplateterm data structure to the ApprovalTemplateTerms Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the ApprovalTemplateTerm data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalTemplateTerm` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.
