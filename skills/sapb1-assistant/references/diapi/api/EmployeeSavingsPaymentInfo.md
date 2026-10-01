<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EmployeeSavingsPaymentInfo (Object)

A child object of the EmployeesInfo object that represents the employee's capital formation savings payments. Source table: HEM7.

**Remarks:** To display the form in the SAP Business One application: Choose Human Resources --> Employee Master Data, and select the Finance tab.

## Properties (14)
- `Public Property AG() As String` [R/W] The company part of the capital formation savings payments contract. Field name: AG. Length: 20 characters.
- `Public Property AGcurrency() As String` [R/W] The currency for the company part of the capital formation savings payments contract. Field name: AGCurrency.
- `Public Property AN() As String` [R/W] The employee part of the capital formation savings payments contract. Field name: AN. Length: 20 characters.
- `Public Property ANcurrency() As String` [R/W] The currency for the employee part of the capital formation savings payments contract. Field name: ANCurrency.
- `Public Property BankAccount() As String` [R/W] The bank account recipient of the capital formation savings payments contract. Field name: BankAcct. Length: 20 characters.
- `Public Property BankCode() As String` [R/W] The bank code recipient of the capital formation savings payments contract. Field name: BankCode. Length: 20 characters.
- `Public Property BankName() As String` [R/W] The bank name recipient of the capital formation savings payments contract. Field name: BankName. Length: 50 characters.
- `Public Property ContractName() As String` [R/W] The name of the capital formation savings payments contract. Field name: ConName. Length: 50 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
- `Public Property EmployeeID() As Long` [R/W] The foreign key to the EmployeesInfo object. Field name: empID.
- `Public Property LineNum() As Long` [R] Returns the current row number.
- `Public Property PaymentNotes() As String` [R/W] The payment notes of the capital formation savings payments contract. Field name: PmntNotes. Length: 50 characters.
- `Public Property Sequence() As ContractSequenceEnum` [R/W] The contract sequence. Field name: Sequence.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
