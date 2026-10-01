<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPAccountReceivablePayble (Object)

BPAccountReceivablePayble is a child object of the BusinessPartners object and represents the Business Partner Account Receivable Payable table in the Business Partner module. This object enables you to add a business partner account. Source table: CRD3.

**Remarks:** To display the form in the application: - Select Business Partners --> Business Partner Master Data. - In the Accounting tab, click the button [...] next to Control Accounts.

## Properties (4)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code of the business partner as defined in Chart of Accounts. Field name: AcctCode. Length: 15 characters.
  - remarks: To set the AccountCode value when working with segmentation, use the FormatCode to find its key value (for example, _SYS00000000010) as follows: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010).
- `Public Property AccountType() As BoBpAccountTypes` [R/W] Sets or returns a valid value of BoBpAccountTypes that specifies the account type of the business partner. Field name: AcctType.
- `Public Property BPCode() As String` [R] The key to the current object's parent business partner.
- `Public Property Count() As Long` [R] Returns the number of records in the BPAccountReceivablePayble object. Field name: .

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
