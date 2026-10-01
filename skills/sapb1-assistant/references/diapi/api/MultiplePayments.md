<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MultiplePayments (Collection)

A data collection of MultiplePayment objects related to the BankStatementService.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (6)
- `Public Function Add() As MultiplePayment` Adds an object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As MultiplePayment` Returns reference by index to existing multiple payment in the collection.
  - param `vtIndex`: Specifies the index of the multiple payment you want to get.
- `Public Sub Remove(ByVal vtIndex As Variant)` Deletes the specified record from the data collection.
  - param `vtIndex`: Specifies the index of the record. Specifies the index of the record.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.
