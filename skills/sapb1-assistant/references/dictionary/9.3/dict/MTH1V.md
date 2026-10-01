<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MTH1V - Journal Entries of External Reconciliation
Module: Banking | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line_ID, TransID, MatchNum, IsInternal, MthAcctCod
Fields (name type(len) description [values] ->parent table):
  MthAcctCod nVarChar(15) Account Code
  IsInternal VarChar(1) Reconciliation Type default=E [I=Internal, E=External]
  MatchNum Int(11) Reconciliation No.
  TransID Int(11) Transaction No.
  Line_ID Int(11) Row Number
  RefDate Date(8) Posting Date
  DueDate Date(8) Due Date
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  Ref3Line nVarChar(27) Reference 3
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  SYSDeb Num(19,6) System Debit Amount
  SYSCred Num(19,6) System Credit Amount
  FCDebit Num(19,6) Foreign Debit Amount
  FCCredit Num(19,6) Foreign Credit Amount
  Currency nVarChar(3) Currency
  LineMemo nVarChar(254) Row Details
