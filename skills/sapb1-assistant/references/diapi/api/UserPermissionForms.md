<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserPermissionForms (Object)

UserPermissionForms is a child object of UserPermissionTree object and enables to add a user permission to a collection of forms. Source table: UPT1.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total forms in the collection (rows).
- `Public Property DisplayOrder() As Long` [R/W] Sets or returns the display order of the user permission form in the collection (starts from 1). Field name: VisOrder.
- `Public Property FormType() As String` [R/W] Sets or returns the form ID (primary key) linked to the user permission. Length: 20 characters. Field name: FormId.
  - remarks: To display the form ID in the application status bar: - From the main menu, select View --> System Information.
- `Public Property PermissionID() As String` [R] Returns the identification key of the user permission tree as defined in UserPermissionTree object. Length: 20 characters. Field name: PermId. This is a foreign key to the UserPermissionTree object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
