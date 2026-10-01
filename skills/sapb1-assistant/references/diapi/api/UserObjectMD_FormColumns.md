<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserObjectMD_FormColumns (Object)

UserObjectMD_FormColumns is child object of the UserObjectsMD object that represents the default fields (columns) to display in the default form (UDO form with the matrix style). Source table: UDO3.

**Remarks:** If the user-defined object uses the default form service (CanCreateDefaultForm), then the mandatory field in SAP Business One is: SonNumber. When adding fields to a default form, the first field must be as follows: - For Master data object type - Code. - For Document object type - DocEntry.

**Example:**
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  oUserObjectMD.FormColumns.FormColumnAlias = "Code"

  oUserObjectMD.FormColumns.FormColumnDescription = "Code"

  oUserObjectMD.FormColumns.Add

  'Add the remaining columns to the default form
  ```
- VB example (SAP provides no C# sample for this - translate, don't paste):
  ```vb
  oUserObjectMD.FormColumns.FormColumnAlias = "DocEntry"

  oUserObjectMD.FormColumns.FormColumnDescription = "DocEntry"

  oUserObjectMD.FormColumns.Add

  'add the remaining columns to the default form
  ```

## Properties (7)
- `Public Property Code() As String` [R] Returns the Child Object Unique ID., inherited from Parent Object. This Unique ID is the primary key of the user defined object and its Parent object. Field name: Code. Length: 20 characters (must include at least one alphabetical character).
- `Public Property Count() As Long` [R] Returns the number of columns in the default form.
- `Public Property Editable() As BoYesNoEnum` [R/W] Indicates whether the form column is editable (active) or not. Field name: ColEdit.
- `Public Property FormColumnAlias() As String` [R/W] Sets or returns the alias name of the default field to display in the default form. Field name: ColAlias. Length: 10 characters.
- `Public Property FormColumnDescription() As String` [R/W] Sets or returns the description of the default field to display in the default form. Field name: ColDesc. Length: 30 characters.
- `Public Property FormColumnNumber() As Long` [R] Returns the number of the default field to display in the default form. SAP Business One creates a sequential number for each column that you add. Field name: ColumnNum.
- `Public Property SonNumber() As Long` [R/W] Sets or returns the number of the child user table to relate to the default user form. Field name: SonNum.
  - remarks: Mandatory if the user defined object uses the default form service (CanCreateDefaultForm).

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
