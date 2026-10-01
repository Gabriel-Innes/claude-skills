<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# JournalVouchers (Object)

JournalVouchers is a business object that represents the journal vouchers in the Finance module. Use the JournalVouchers object as a draft for journal entries. That is, no values are created in the general ledger. The properties of the journal voucher are similar to the properties of JournalEntries and JournalEntries_Lines objects. Source table: OBTD. To display the form in the application: - Select Financials --> Journal Vouchers.

**Remarks:** BtfLine field in OBTF table - Journal Voucher Entry is no longer in use.

## Properties (1)
- `Public Property JournalEntries() As JournalEntries` [R] Returns the JournalEntries object.

## Methods (3)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
- `Public Sub LoadFromXML(ByVal FileName As String)` method LoadFromXML
  - param `FileName`: 
- `Public Sub SaveToXMLHierarchy(ByVal FileName As String)` method SaveToXMLHierarchy
  - param `FileName`:
