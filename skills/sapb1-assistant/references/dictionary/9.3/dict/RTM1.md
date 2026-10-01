<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RTM1 - Rate Differences - Rows
Module: Finance | 19 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: IsSysCurr, JdtLine, TransId, LineNum
  SYS_CURR: IsSysCurr
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Reconciliation Key
  TransId Int(11) Journal Key ->OJDT
  JdtLine Int(11) Journal Row default=0
  IsSysCurr VarChar(1) Is System Currency default=N [Y=Yes, N=No]
  AcctCode nVarChar(15) G/L Account/BP Code
  Balance Num(19,6) Balance
  FrnBlnc Num(19,6) Balance (FC)
  Valid VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  RevalRate Num(19,6) Revaluation Rate
  Delta Num(19,6) Difference in LC
  FCCurrency nVarChar(3) Foreign Currency
  JdtAcctCod nVarChar(15) Journal Account Code
  BaseRef nVarChar(11) Base Reference
  JdtType VarChar(1) Journal Entry Type default=U [P=Primary, G=Generated, W=Without Primary, U=Undefined Type]
  RefDate Date(8) Posting Date
  DueDate Date(8) Due Date
  TaxDate Date(8) Document Date
  BPLId Int(11) Branch ->OBPL
  CntBlnc Num(19,6) Converted Balance
