<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPCodes (Collection)

BPCodes is a collection of BPCode data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of BPCode data structures in the BPCodes data collection.

## Methods (5)
- `Public Function Add() As BPCode` Add a new BPCode data structure to the to the BPCodes collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As BPCode` Returns a reference to the BPCode that you want to get.
  - param `vtIndex`: Specifies the number of the BPCode in the collection (starts from 0).
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
