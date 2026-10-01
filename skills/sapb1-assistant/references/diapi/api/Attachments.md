<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Attachments (Collection)

Attachments is a collection of one or more Attachment objects. From DI API version 2005, use the Attachments2 object.

**Remarks:** To remove an Attachment item, set its FileName property to NULL ("") and call the Update method of the calling object.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of Attachment items in the collection.

## Methods (3)
- `Public Sub Add()` Adds a new Attachment item to the Attachments collection.
- `Public Function Item(ByVal Index As Variant) As Attachment` Retrieves an existing attachment item from the Attachments object.
  - param `Index`: specifies the index value of the item (starts from 0).
  - returns: The Item method returns an Attachment object, or nothing if failed.
  - remarks: You can use the Add method to add a new Attachment object to the Attachments collection, and then use the Item method to reference the attachment object by its index value.
- `Public Sub Refresh()` Refreshen the attachments collection.
  - remarks: Call this method after using the GetBusinessObjectFromXML method.
