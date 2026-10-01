<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeReviewsInfo (Object)

EmployeeReviewsInfo is a child object of the EmployeesInfo object and represents the employee reviews information. Source table: HEM3.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Administration tab. - Click Reviews.

## Properties (9)
- `Public Property Count() As Long` [R] Returns the total data rows in the employee reviews list.
- `Public Property Date() As Date` [R/W] Sets or returns the date of the review. Field name: date.
- `Public Property EmployeeNo() As Long` [R/W] Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property Grade() As String` [R/W] Sets or returns the grade of the employee. Field name: grade. Length: 50 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee reviews list. Field name: line.
- `Public Property Manager() As Long` [R/W] Sets or returns the manager's employee-ID of the employee. Field name: manager. This is a foreign key to the EmployeesInfo object.
- `Public Property Remarks() As String` [R/W] Sets or returns a memo type string that specifies remarks of the employee review. Field name: remarks. Length: 64,000 characters.
- `Public Property ReviewDescription() As String` [R/W] Sets or returns a description of the employee review. Field name: reviewDesc. Length: 100 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
