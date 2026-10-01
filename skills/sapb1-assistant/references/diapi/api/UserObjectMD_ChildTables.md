<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserObjectMD_ChildTables (Object)

UserObjectMD_ChildTables is child object of the UserObjectsMD object that represents child user tables and their related history log tables. Source table: UDO1.

## Properties (6)
- `Public Property Code() As String` [R] Returns the Child Object Unique ID., inherited from Parent Object. This Unique ID is the primary key of the user defined object and its Parent object. Field name: Code. Length: 20 characters (must include at least one alphabetical character).
- `Public Property Count() As Long` [R] Returns the number of child user tables in the object.
- `Public Property LogTableName() As String` [R/W] Sets or returns the history log table name. This table maintains a history log of all actions related to the child user table. Field name: LogName. Length: 19 characters.
  - remarks: If you select the History Log service, then set a history log table name starting with "A" followed by the object's Child User Table name. Notes: - If you unregister a user defined object that is registered to the history log service, the related history log table is deleted from the database. - If you unregister the history log service while updating a user defined object, the history log table is not deleted (only unregistered).
- `Public Property ObjectName() As String` [R/W] The name of child UDO object when specifying a child table for a UDO object. This name is used to specify the child table in the Child method of the GeneralData object.
- `Public Property SonNumber() As Long` [R] Returns the number of the child user table. SAP Business One creates a sequential number for each child user table that you add. Field name: SonNum.
- `Public Property TableName() As String` [R/W] Sets or returns the child table name to link to the user-defined object. Field name: TableName. Length: 19 characters.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
