<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeePrevEmpoymentInfo (Object)

EmployeePrevEmploymentInfo is a child object of the EmployeesInfo object and represents the employee previous employment information. Source table: HEM4.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Administration tab. - Click Previous Employment.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the number of lines in the employee previous employment list.
- `Public Property EmployeeNo() As Long` [R/W] P>Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property Employer() As String` [R/W] Sets or returns the name of the previous employer. Field name: employer. Length: 50 characters.
- `Public Property FromDtae() As Date` [R/W] Sets or returns the start date of the previous employment period. Field name: fromDate.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee reviews list. Field name: line.
- `Public Property Position() As String` [R/W] Sets or returns the employee position in the previous employment. Field name: position. Length: 50 characters.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks of the previous employment. Field name: remarks. Length: 64,000 characters.
- `Public Property ToDate() As Date` [R/W] Sets or returns the end date of the previous employment period. Field name: toDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
