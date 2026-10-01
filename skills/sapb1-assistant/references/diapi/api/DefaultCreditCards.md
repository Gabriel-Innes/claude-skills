<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DefaultCreditCards (Object)

The DefaultCreditCards is a child object of the UserDefaultGroups object. It enables to link G/L accounts to credit card codes. Source table: UDG2.

**Remarks:** To display the form in the application: - Select Administration -->Setup -->General -->Users. - From the Defaults field, click the Choose From List button. - In the List of User Defaults, click the New button. - In the User Defaults form, select the Credit Cards tab.

## Properties (5)
- `Public Property Code() As String` [R] Returns the code (primary key) of the user defaults group. Field name: Code. Length: 8 characters.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property CreditAccountCode() As String` [R/W] Sets or returns the G/L account code that is linked to the default credit card. Field name: AcctCode. Length: 15 characters. This is a foreign key to the Code of the ChartOfAccounts object.
- `Public Property CreditCardCode() As Long` [R/W] Sets or returns the default credit card code. Field name: CreditCard. This is a foreign key to the CreditCardCode of the CreditCards object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
