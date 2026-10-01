<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeRolesInfo (Object)

A child object of the EmployeesInfo object that represents the employee roles, for example, technician, sales employee and purchasing. Source table: HEM6.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Membership tab. To modify the master data list of employees roles, use the EmployeeRolesSetupService service.

## Properties (5)
- `Public Property Count() As Long` [R] Returns the number of roles of the employee.
- `Public Property EmployeeID() As Long` [R/W] Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee roles list. Field name: line.
- `Public Property RoleID() As Long` [R/W] Sets or returns the role ID of the employee. Field name: roleID. This is a foreign key to OHTY table, which is not exposed through the DI API.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
