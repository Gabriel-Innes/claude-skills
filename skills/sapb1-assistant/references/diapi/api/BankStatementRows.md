<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BankStatementRows (Collection)

A data collection of BankStatementRow objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As BankStatementRow` Adds a new BankStatementRow object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As BankStatementRow` Returns reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub Remove(ByVal vtIndex As Variant)` Deletes the specified record from the data collection.
  - param `vtIndex`: Specifies the index of the record. Specifies the index of the record.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.
