<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MTH2V - Bank Statements of External Reconciliation
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MthAcctCod, IsInternal, MatchNum, Sequence
  SECONDARY U: BnkAcctCod, Sequence
Fields (name type(len) description [values] ->parent table):
  MthAcctCod nVarChar(15) Account Code
  IsInternal VarChar(1) Reconciliation Type default=E [I=Internal, E=External]
  MatchNum Int(11) Reconciliation No.
  BnkAcctCod nVarChar(15) Account Code
  Sequence Int(11) Sequence No.
  DueDate Date(8) Due Date
  Ref nVarChar(27) Reference
  DebAmount Num(19,6) Debit Amount
  Memo nVarChar(254) Details
