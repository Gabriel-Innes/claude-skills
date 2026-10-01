<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CountriesParams (Collection)

A data collection of CountryParams identification properties.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of instances in the collection.

## Methods (5)
- `Public Function Add() As CountryParams` Adds a new CountryParams instance.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As CountryParams` Returns a CountryParams instance by a specified index.
  - param `vtIndex`: Specifies the index of the CountryParams instance to retrieve.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
