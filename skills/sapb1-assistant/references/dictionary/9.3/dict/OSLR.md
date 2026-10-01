<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSLR - Special Ledger - Analytical Accounting Report: Revenues & Expenses
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocID
Fields (name type(len) description [values] ->parent table):
  DocID Int(11) Document Identification Number
  DocDate Date(8) Date of Report Generation
  Ref1 Int(11) Journal Entry Number ->OJDT
  Ref2 Int(11) Original JE Reference ->OJDT
  Status VarChar(1) Document Status
  DateFrom Date(8) Document Start Date
  DateTo Date(8) Document End Date
  TotDebit Num(19,6) Total Debit Amount
  TotCredit Num(19,6) Total Credit Amount
  RateType VarChar(1) Type of Exchange Rate default=O [O=Original document, E=Execution date, V=Other value]
  Comment nVarChar(250) Remarks
  UserSign Int(6) User Signature ->OUSR
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  CancelUser Int(6) Document Cancelled by ->OUSR
