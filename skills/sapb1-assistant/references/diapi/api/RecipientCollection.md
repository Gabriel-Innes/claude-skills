<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RecipientCollection (Collection)

RecipientCollection is a collection of Recipient data structures. It represents the list of receipients of a message (replaces the Recipients object - backward compatibilty is maintained).

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total number of Recipients of a message.

## Methods (5)
- `Public Function Add() As Recipient` Adds a receipient to a message.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As Recipient` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the recipient in the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
