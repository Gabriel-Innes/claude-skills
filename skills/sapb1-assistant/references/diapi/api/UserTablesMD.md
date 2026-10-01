<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserTablesMD (Object)

The UserTablesMD object enables to manage user defined tables as follows: - Add a user table. - Retrieve a user table from the database by its TableName. - Remove a user table. - Save the object in XML format. Source table: OUTB. IMPORTANT: After creating a new user-defined table in .NET, you must release the object by executing the following line of code, where myObject is a reference to the UserTablesMD object: System.Runtime.InteropServices.Marshal.ReleaseComObject(myObject);

**Remarks:** DI API allows only one metadata object instance (with no other instances of any object type). This maintains data integrity by preventing any manipulation of a business object while modifying the object's properties. To display the form in the application: - From the main menu bar, select Tools --> Manage User Fields. - Click User Tables.

## Properties (7)
- `Public Property Archivable() As BoYesNoEnum` [R/W] property Archivable
- `Public Property ArchiveDateField() As String` [R/W] property ArchiveDateField
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property DisplayMenu() As BoYesNoEnum` [R/W] Determines whether to display the user-defined table as a submenu in the SAP Business One client, or a tile in the Web Client. Field name: DisplyMenu.
- `Public Property TableDescription() As String` [R/W] A string that describes the name and functionality of the table. Field name: Descr. Length: 30 characters.
- `Public Property TableName() As String` [R/W] Sets or returns the name for the user defined table. Field name: TableName. Length: 19 characters.
  - remarks: When adding a user table, SAP Business One automatically adds the symbol @ as a prefix to the table name. For example, if you add a table named ABC, the resulting table name is @ABC. When referring to a user-defined table, you must use the name including the prefix @. When adding a user table and assigning it a TableName, the DI API creates the table with an upper case name. By default, Microsoft SQL Server is not case sensitive. If it is configured to be case sensitive, make sure to specify the table name in upper-case when using the DoQuery method of the Recordset object.
- `Public Property TableType() As BoUTBTableType` [R/W] Sets or returns a valid value of BoUTBTableType type that specifies the type of the user table. Field name: ObjectType.
  - remarks: For each user table type, SAP Business One provides a default table. You can add user fields to the default user fields but not remove them. For a user defined object, do not use the table type 'No object'.

## Methods (7)
- `Public Function Add() As Long` Adds a new table to the User-Defined Tables collection. The new table includes two columns by default: Code and Name, where the Code column is the primary key of the specific user table.
  - remarks: When adding a user table, SAP Business One automatically adds the symbol @ as a prefix to the table name. For example, if you add a table named ABC, the resulting table name is @ABC. When referring to a user-defined table, you must use the name including the prefix @. When adding a user table and assigning it a TableName, the DI API creates the table with an upper case name. By default, Microsoft SQL Server is not case sensitive. If it is configured to be case sensitive, make sure to specify the table name in upper-case when using the DoQuery method of the Recordset object.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal TableName As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `TableName`: Specifies the name of the user defined table (use the symbol @ as a prefix to the name, see the TableName property of the UserTablesMD object).
- `Public Function Remove() As Long` Deletes a specified table.
  - remarks: Before using the Remove method, you must get the required table using the GetByKey method. Warning: Removing a table deletes all its content.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
- `Public Function Update() As Long` Updates the object data in the company database.
