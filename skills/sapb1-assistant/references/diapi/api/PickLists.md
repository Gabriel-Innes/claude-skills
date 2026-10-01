<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PickLists (Object)

The PickLists object supports the picking process of items from the warehouse. The picking process is applicable only for items that are already approved in sales orders. Source table: OPKL.

**Remarks:** To display the form in the application, select Inventory --> Pick and Pack --> Pick List.

## Properties (12)
- `Public Property AbsoluteEntry() As Long` [R] Returns the pick list number (sequential) as assigned by the system. Field name: AbsEntry.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Lines() As PickLists_Lines` [R] Returns the PickLists_Lines child object.
- `Public Property Name() As String` [R/W] Sets or returns the name of the employee who is responsible for the picking (picker). Field name: Name. Length: 30 characters.
- `Public Property ObjectType() As String` [R] Returns the type of the table (in this case OPKL). Field name: ObjType. Length: 20 characters.
- `Public Property OwnerCode() As Long` [R/W] Sets or returns the code of the user who prepares the pick list. This is a foreign key to the Users object (see InternalKey). Field name: OwnerCode. This is a foreign key to the Users object.
- `Public Property OwnerName() As String` [R] Returns the name of the user who prepares the pick list. Field name: OwnerName. Length: 30 characters.
- `Public Property PickDate() As Date` [R/W] Sets or returns the planned delivery date. Field name: PickDate.
- `Public Property Remarks() As String` [R/W] Sets or returns the remarks related to the pick list. Field name: Remarks. Length: 64,000 characters.
- `Public Property Status() As BoPickStatus` [R] Returns a valid value that specifies the status of the pick list. For example: released for picking, already picked, and so on. Field name: Status.
- `Public Property UseBaseUnits() As BoYesNoEnum` [R/W] property UseBaseUnits
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (9)
- `Public Function Add() As Long` method Add
  - remarks: Adds a pick list.
- `Public Function Close() As Long` Closes a record of the object in SAP Business One database.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal lAbsEntry As Long) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database. Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lAbsEntry`: AbsoluteEntry.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function GetReleasedAllocation(ByVal lAbsEntry As Long) As Boolean` GetReleasedAllocation
  - param `lAbsEntry`: 
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
- `Public Function UpdateReleasedAllocation() As Long` method UpdateReleasedAllocation
