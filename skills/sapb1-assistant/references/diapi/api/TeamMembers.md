<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TeamMembers (Object)

TeamMembers is a child object of the Teams object that represents the membership role in a team of an employee. An employee can be a Member or a Leader of more than one team. Source table: HTM1.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Membership tab.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the total rows in the table.
  - remarks: When you add a data row, the value of this property is incremented automatically.
- `Public Property EmployeeID() As Long` [R/W] Sets or returns the employee ID as defined by EmployeesInfo object.
- `Public Property RoleInTeam() As BoRoleInTeam` [R/W] Sets or returns a valid value of BoRoleInTeam type that specifies whether the employee is a Member or a Leader of the team.
- `Public Property TeamID() As Long` [R] Returns the team identification key.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
