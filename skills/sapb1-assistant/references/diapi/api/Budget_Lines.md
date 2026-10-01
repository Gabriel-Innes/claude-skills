<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Budget_Lines (Object)

Budget_Lines is a child object of Budget object and represents the budget item details of an account. Source table: BGT1.

**Remarks:** The budget item details of an account contains 12 lines, one for each monthly budget. The monthly budget percentage (PrecentOfAnnualBudgetAmount) depends on the budget distribution method (DivisionCode). To initialize the budget management: - Select Administration --> System Initialization --> General Settings. - In the Budget tab, select Budget Initialization. - Set the budget initialization parameters and click OK. To display the form in the application: - Select Financials --> Budget --> Define Budget. - In the Define Budget dialog box, select a scenario and click OK. The budget management window opens. - Click the number of a budget entry in the budget management table. The budget item details window opens.

## Properties (23)
- `Public Property AccountCode() As String` [R] Returns the G/L account code as defined in Chart of Accounts. Field name: AcctCode. Length: 15 characters.
- `Public Property BalSysTotCredit() As Double` [R] Returns the line budget balance in system currency of the revenue account (credit side), based on the journal transactions. Field name: CredSTotal.
- `Public Property BalSysTotDebit() As Double` [R] Returns the line budget balance in system currency of the account (debit side), based on the journal transactions. Field name: DebSTotal.
- `Public Property BalTotCredit() As Double` [R] Returns the line budget balance in local currency of the revenue account (credit side), based on the journal transactions. Field name: CredLTotal.
- `Public Property BalTotDebit() As Double` [R] Returns the line budget balance in local currency of the account (debit side), based on the journal transactions. Field name: DebLTotal.
- `Public Property BudgetKey() As Long` [R] Returns the identification key of the budget as assigned by SAP Business One. Field name: BudgId. This is a foreign key to the Budget object.
- `Public Property BudgetSysTotCredit() As Double` [R/W] Returns the budget in the line in system currency of the revenue account (credit side). Field name: CredSTotal.
- `Public Property BudgetSysTotDebit() As Double` [R/W] Returns the budget in the line in system currency of the account (debit side). Field name: DebSTotal.
- `Public Property BudgetTotCredit() As Double` [R/W] Returns the budget in the line in local currency of the revenue account (credit side). Field name: CrdRLTotal.
- `Public Property BudgetTotDebit() As Double` [R/W] Returns the budget in the line in local currency of the account (debit side). Field name: DebRLTotal.
- `Public Property Count() As Long` [R] Returns the total budget rows.
- `Public Property FutExpenCredit() As Double` [R] Returns the expense amount in the line (in local currency) of open purchase orders and purchase delivery notes related to the revenue account (credit side). Field name: FtrOCRLSum.
- `Public Property FutExpenDebit() As Double` [R] Returns the expense amount in the line (in local currency) of open purchase orders and purchase delivery notes related to the account (debit side). Field name: FtrODRLSum.
- `Public Property FutExpenSysCredit() As Double` [R] Returns the expense amount in the line (in system currency) of open purchase orders and purchase delivery notes related to the revenue account (credit side). Field name: FtrOCRSSum.
- `Public Property FutExpenSysDebit() As Double` [R] Returns the expense amount in the line (in system currency) of open purchase orders and purchase delivery notes related to the account (debit side). Field name: FtrODRSSum.
- `Public Property FutIncomesCredit() As Double` [R] Returns the future income in the line (in local currency) related to the revenue account (credit side). Field name: FtrICRLSum.
- `Public Property FutIncomesSysCredit() As Double` [R] Returns the future income in the line (in system currency) related to the revenue account (credit side). Field name: FtrICRSSum.
- `Public Property FutIncomesSysDebit() As Double` [R] Returns the future revenue in the line (in system currency) related to the account (debit side). Field name: FtrIDRSSum.
- `Public Property FutureIncomeDeb() As Double` [R] Returns the future revenue in the line (in local currency) related to the account (debit side). Field name: FtrIDRLSum.
- `Public Property PrecentOfAnnualBudgetAmount() As Double` [R] Returns the percentage of the annual budget amount for calculating the monthly budget. The value of this property depends on the budget distribution method (DivisionCode). Field name: MonthPrcnt.
- `Public Property RowDetails() As String` [R/W] Sets or returns a description about the monthly budget. Length: 50 characters. Field name: LineMemo.
- `Public Property RowNumber() As Long` [R] Returns the current available row number (month). Field name: Line_ID.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
