<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeEducationInfo (Object)

EmployeeEducationInfo is a child object of the EmployeesInfo object and represents the employee education information. Source table: HEM2.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data. - Select the Administration tab. - Click Education.

## Properties (10)
- `Public Property Count() As Long` [R] Returns the total data rows in the employee education information list.
- `Public Property Diploma() As String` [R/W] Sets or returns the diploma of the employee (such as, BA, MBA, and so on). Field name: diploma. Length: 50 characters.
- `Public Property EducationType() As Long` [R/W] Sets or returns the education type of the employee (such as, high-school, university, and so on). Field name: type. Length: 50 characters. This is a foreign key to the Education Types table (OHED - not exposed through the DI API).
- `Public Property EmployeeNo() As Long` [R/W] Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property FromDate() As Date` [R/W] Sets or returns the start date of the education period. Field name: fromDate.
- `Public Property Institute() As String` [R/W] Sets or returns the institute name. Field name: institute. Length: 100 characters.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee education list. Field name: line.
- `Public Property Major() As String` [R/W] Sets or returns the major study subject. Field name: major. Length: 50 characters.
- `Public Property ToDate() As Date` [R/W] Sets or returns the end date of the education period. Field name: toDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
