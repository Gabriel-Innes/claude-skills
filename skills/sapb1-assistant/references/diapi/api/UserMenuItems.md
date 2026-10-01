<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserMenuItems (Collection)

UserMenuItems is a Data Collection of UserMenuItem data structures. Source table: CUMI.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of UserMenuItem data structures in the UserMenuItems data collection.

## Methods (6)
- `Public Function Add() As UserMenuItem` Adds a new UserMenuItem to the UserMenuItems data collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As UserMenuItem` Returns a reference to the UserMenuItem that you want to get.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub Remove(ByVal vtIndex As Variant)` Removes a specified UserMenuItem from the data collection.
  - param `vtIndex`: Specifies the index of the UserMenuItem you want to delete from the collection. Warning: when removing a field, all it's content is lost.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
