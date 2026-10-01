<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MTH3V - Filter for Query MTH
Module: Banking | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MthAcctCod, IsInternal, MatchNum
Fields (name type(len) description [values] ->parent table):
  absEntry Int(11) Internal Number
  AcctCdeFrm nVarChar(15) Account Code From
  AcctCdeTo nVarChar(15) Account Code To
  IsInternal VarChar(1) Reconciliation Type default=E [I=Internal, E=External]
  IsCard VarChar(1) Select BP or Account default=A [A=G/L Account, C=BP]
  MatchNumFr Int(11) Reconciliation No. From
  MatchNumTo Int(11) Reconciliation No. To
  MthDateFrm Date(8) Reconciliation Date From
  MthDateTo Date(8) Reconciliation Date To
  MthAcctCod nVarChar(15) Account Code
  MatchNum Int(11) Reconciliation No.
