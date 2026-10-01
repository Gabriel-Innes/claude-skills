<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlertManagementRecipients (Collection)

AlertManagementRecipients is a Data Collection of AlertManagementRecipient data structures. Source table: ALT1.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of instances in the data collection.

## Methods (5)
- `Public Function Add() As AlertManagementRecipient` Adds new object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As AlertManagementRecipient` Returns reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.
