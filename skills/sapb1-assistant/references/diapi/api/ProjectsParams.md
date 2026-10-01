<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProjectsParams (Collection)

A data collection of ProjectParams identification properties.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ProjectParams instances in the collection.

## Methods (5)
- `Public Function Add() As ProjectParams` Adds a new ProjectParams to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ProjectParams` Returns a ProjectParams instance by a specified index.
  - param `vtIndex`: Specifies the index of the ProjectParams instance you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
