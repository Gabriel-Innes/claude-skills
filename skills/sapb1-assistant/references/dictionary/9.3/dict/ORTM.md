<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORTM - Rate Differences
Module: Finance | 20 columns | ObjType: 9
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IsSysCurr, LineNum
  SYS_CURR: IsSysCurr
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Reconciliation Key
  Rtmdate Date(8) Posting Date
  AcctCode nVarChar(15) G/L Account/BP Code
  IsCard VarChar(1) Card default=N [Y=Yes, N=No]
  ActCurrncy nVarChar(3) Document Valuation Currency
  ActRate Num(19,6) Document Revaluation Rate
  Balance Num(19,6) Balance
  FrnBlnc Num(19,6) FC Balance
  TransNum Int(11) Transaction Number default=0
  Valid VarChar(1) Confirmed default=N [Y=Yes, N=No]
  Delta Num(19,6) Difference in LC
  IsSysCurr VarChar(1) In System Currency default=N [Y=Yes, N=No]
  StornoDate Date(8) Reversal Date
  RevalRate Num(19,6) Revaluation Rate
  UserSign Int(6) User Signature ->OUSR
  BPLId Int(11) Branch ->OBPL
  CntBlnc Num(19,6) Converted Balance
  TransAmtSC Num(19,6) Transaction Amount Total
  BalDueSC Num(19,6) Balance Due Total
  SCAdjust VarChar(1) SC Adjustment default=N [Y=Yes, N=No]
