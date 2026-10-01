<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ColumnsPreferences (Collection)

ColumnsPreferences is a collection of ColumnPreferences data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the total items in the collection.

## Methods (5)
- `Public Function Add() As ColumnPreferences` Adds a column preferences data structure to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ColumnPreferences` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the new item, which was added to the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
