<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlertManagementParamsCollection (Collection)

AlertManagementParamsCollection is a Data Collection of AlertManagementParams Identification Keys. Source table: ALT1.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of AlertManagementParams in the AlertManagementRecipients data collection.

## Methods (5)
- `Public Function Add() As AlertManagementParams` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As AlertManagementParams` Returns a reference to the item that you want to get.
  - param `vtIndex`: Specifies the index of the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
