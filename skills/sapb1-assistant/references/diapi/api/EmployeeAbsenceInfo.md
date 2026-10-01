<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeAbsenceInfo (Object)

EmployeeAbsenceInfo is a child object of the EmployeesInfo object and represents the employee absence information. Source table: HEM1.

**Remarks:** To display the form in the application: - Select Human Resources --> Employee Master Data - Select the Administration tab. - Click Absence.

## Properties (9)
- `Public Property ApprovedBy() As String` [R/W] Sets or returns the person name that approves the absence. Field name: approvedBy. Length: 20 characters.
- `Public Property ConfirmerNumber() As Long` [R/W] Sets or returns the employee's Confirmer Number. Field name: cnfrmrNum). This is a foreign key to the EmployeesInfo object.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property EmployeeID() As Long` [R/W] Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object. Sets or returns the employee ID, which SAP Business One generates automatically when adding a new employee. Field name: empID. This is a foreign key to the EmployeesInfo object.
- `Public Property FromDate() As Date` [R/W] Sets or returns the start date of the employee absence period. Field name: fromDate.
- `Public Property LineNum() As Long` [R] Returns the current row number in the employee absence information list. Field name: line.
- `Public Property Reason() As String` [R/W] Sets or returns the reason for employee absence. Field name: reason. Length: 20 characters.
- `Public Property ToDate() As Date` [R/W] Sets or returns the end date of the employee absence period. Field name: toDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the line number. The count starts from 0. Specifies the row number. The count starts from 0.
