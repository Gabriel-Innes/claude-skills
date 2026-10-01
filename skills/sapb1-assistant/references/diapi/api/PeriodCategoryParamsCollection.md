<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PeriodCategoryParamsCollection (Collection)

PeriodCategoryParamsCollection is a collection of PeriodCategoryParams identification keys.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of PeriodCategoryParams identification keys in the PeriodCategoryParamsCollection.

## Methods (5)
- `Public Function Add() As PeriodCategoryParams` Adds a new record to the table.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As PeriodCategoryParams` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the PeriodCategoryParams in the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
