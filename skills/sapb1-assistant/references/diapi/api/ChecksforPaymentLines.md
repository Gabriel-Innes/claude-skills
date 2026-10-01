<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ChecksforPaymentLines (Object)

ChecksforPaymentLines is a child object of the ChecksforPayment object that represents the appendix of the check. Source table: CHO1.

**Remarks:** Mandatory field in SAP Business One: RowTotal. To display the form in the application: - Select Banking --> Outgoing Payments --> Checks for Payment.

## Properties (10)
- `Public Property Count() As Long` [R] Returns the total data rows of the ChecksforPaymentLines object.
- `Public Property CreditedAccount() As String` [R/W] Sets or returns the G/L account to debit. Field name: CredAcct. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property LineTotal() As Double` [R] Returns the total amount (including tax) per row. Field name: LinesSum.
  - remarks: SAP Business One calculates the total amount per row using the RowTotal and TaxPercent properties.
- `Public Property RowCurrency() As String` [R/W] Sets or returns the currency for the row. Field name: LineCurr. Length: 3 characters.
- `Public Property RowDetails() As String` [R/W] Sets or returns the row details. Field name: LineDitail. Length: 40 characters.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (starts from 1). Field name: Line_ID.
- `Public Property RowTotal() As Double` [R/W] Sets or returns the total amount in the row. Field name: LineMoney. Mandatory property.
- `Public Property TaxDefinition() As String` [R/W] Sets or returns the tax group for the row. Field name: Code. Length: 8 characters. This is a foreign key to the VatGroups object.
- `Public Property TaxPercent() As Double` [R] Returns the tax percentage according to the tax group (TaxDefinition). Field name: VatPercent.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
