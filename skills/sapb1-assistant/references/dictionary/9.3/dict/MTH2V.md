<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MTH2V - Bank Statements of External Reconciliation
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Sequence, MatchNum, IsInternal, MthAcctCod
  SECONDARY U: Sequence, BnkAcctCod
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
