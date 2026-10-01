<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserObjectMD_FindColumns (Object)

UserObjectMD_FindColumns is a child object of the UserObjectsMD object that represents the fields (columns) to display in the Find Form (Choose From List form). Source table: UDO2.

## Properties (5)
- `Public Property Code() As String` [R] Returns the Child Object Unique ID., inherited from Parent Object. This Unique ID is the primary key of the user defined object and its Parent object. Field name: Code. Length: 20 characters (must include at least one alphabetical character).
- `Public Property ColumnAlias() As String` [R/W] Sets or returns the alias name of the field to display in the Find Form. Length: 10 characters. Field name: ColAlias.
- `Public Property ColumnDescription() As String` [R/W] Sets or returns the field description to display in the Find Form. Length: 30 characters. Field name: ColumnDesc.
- `Public Property ColumnNumber() As Long` [R] Returns the number of the field to display in the Find Form. SAP Business One creates a sequential number for each column that you add. Field name: ColumnNum.
- `Public Property Count() As Long` [R] Returns the number of columns in the Find Form (Choose From List form).

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
