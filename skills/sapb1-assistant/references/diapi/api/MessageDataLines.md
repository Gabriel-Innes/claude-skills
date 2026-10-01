<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MessageDataLines (Collection)

MessageDataLines is a collection of the MessageDataLine data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Retrurns the number of MessageDataLine data structures in the data column.

## Methods (5)
- `Public Function Add() As MessageDataLine` Adds a data structure (Item in the collection) and returns a reference to it (Index starting from 0).
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As MessageDataLine` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the location of the row in the data column (starts from 0).
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
