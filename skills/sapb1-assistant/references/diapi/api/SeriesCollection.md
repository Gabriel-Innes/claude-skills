<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SeriesCollection (Collection)

SeriesCollection is a data collection of Series data structures. Source table: NNM1 (Documents Numbering - Series).

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of Series data structures in the SeriesCollection.

## Methods (5)
- `Public Function Add() As Series` Adds a new Series to the SeriesCollection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As Series` Returns a Series data structures from the SeriesCollection.
  - param `vtIndex`: Specifies the index of the Series that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
