<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BOEPortfoliosParams (Collection)

This object is a collection of BOEPortfolioParams.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total objects in the collection.

## Methods (5)
- `Public Function Add() As BOEPortfolioParams` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retreives the XML schema of the data structrue.
- `Public Function Item(ByVal vtIndex As Variant) As BOEPortfolioParams` Returns a reference to a specified object in the collection.
  - param `vtIndex`: Specifies the index of the object.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
