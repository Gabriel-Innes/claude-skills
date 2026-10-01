<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserKeysMD (Object)

The UserKeysMD object enables to mange user defined keys of user tables. A user table contains a default primary key that consists of the Code and Name columns. Use the UserKeysMD object to add secondary keys to user tables. This object enables you to: - Add a user key (identifier) to a user table. - Retrieve the values of the object's properties by its KeyIndex and TableName. - Remove a user key. - Save the object in XML format. Source table: OUKD.

**Remarks:** DI API allows only one meta data object instance (with no other instances of any object type). This maintains data integrity by preventing any manipulation of a business object while modifying the object's properties. Furthermore, it is recommended to add user keys while the user table is still empty. To display the form in the application: - From the main menu bar, select Tools --> Manage User Fields. - Select a User Table. - Click Keys.

## Properties (6)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Elements() As UserKeysMD_Elements` [R] Returns the UserKeysMD_Elements child object that contains the list of fields in the database used for adding the key.
- `Public Property KeyIndex() As Long` [R] Returns the serial number that uniquely identifies the key in the user table. This serial number is automatically assigned by SAP Business One (starting from 0). Field name: KeyId.
- `Public Property KeyName() As String` [R/W] Sets or returns the unique key name used for identification. Field name: KeyName. Length: 10 characters.
- `Public Property TableName() As String` [R/W] Sets or returns the name of the required table in the database. Field name: TableName. Length: 20 characters.
- `Public Property Unique() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the key is unique. Unique keys prevents the end-user from adding new keys with the same key combination. Field name: UniqueKey.

## Methods (6)
- `Public Function Add() As Long` Adds a key to a row of a user defined table. See sample, Adding a Private Key.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal TableName As String, ByVal KeyIndex As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `TableName`: The name of the required table in the database.
  - param `KeyIndex`: A serial number (read only) that is automatically assigned by the system and uniquely identifies the key in the user table (starts from 0).
- `Public Function Remove() As Long` Deletes a key from an existing table.
  - remarks: Before using the Remove method, you must get the required table using the GetByKey method.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
