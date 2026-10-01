<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserObjectMD_EnhancedFormColumns (Object)

UserObjectMD_EnhancedFormColumns is a child object of the UserObjectsMD object that represents the default fields (columns) to display in the UDO enhanced default form (UDO form with the header-line style). Source table: UDO4.

**Remarks:** When adding fields to a default form, the first field must be as follows: - For Master data object type - Code. - For Document object type - DocEntry.

## Properties (8)
- `Public Property ChildNumber() As Long` [R/W] The number of the child user table to relate to the default user form. Field name: SonNum.
- `Public Property Code() As String` [R] Returns the Child Object Unique ID., inherited from Parent Object. This Unique ID is the primary key of the user defined object and its Parent object. Field name: Code. Length: 20 characters (must include at least one alphabetical character).
- `Public Property ColumnAlias() As String` [R/W] The alias name of the default field to display in the default form. Field name: ColAlias. Length: 20 characters.
- `Public Property ColumnDescription() As String` [R/W] The description of the default field to display in the default form. Field name: ColDesc. Length: 30 characters.
- `Public Property ColumnIsUsed() As BoYesNoEnum` [R/W] Indicates whether the form column is used or not. Field name: ColIsUsed.
- `Public Property ColumnNumber() As Long` [R/W] The number of the default field to display in the default form. SAP Business One creates a sequential number for each column that you add. Field name: ColumnNum.
- `Public Property Count() As Long` [R] Returns the number of columns in the default form.
- `Public Property Editable() As BoYesNoEnum` [R/W] Indicates whether the form column is editable (active) or not. Field name: ColEdit.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
