<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserPermission (Object)

UserPermission is a business object that enables to set the authorization of a specified user to a UserPermissionTree. Source table: USR3.

**Remarks:** To display the form in the application: - Select Administration --> System Initialization --> Authorization --> General Authorization. See example of Authorizations Tree.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total rows in the table.
- `Public Property Permission() As BoPermission` [R/W] Sets or returns a valid value of BoPermission type that specifies the permission type assigned to the user. The available options are according to the setting of Options property. Field name: Permission.
- `Public Property PermissionID() As String` [R/W] Sets or returns the identification key of the user permission in the tree, for which the permission is set. Length: 20 characters. Field name: PermId. This is a foreign key to the UserPermissionTree object, not exposed through the DI API).
- `Public Property UserCode() As Long` [R] Returns the user code.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
