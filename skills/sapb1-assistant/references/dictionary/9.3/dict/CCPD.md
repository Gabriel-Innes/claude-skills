<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CCPD - Period-End Closing
Module: Finance | 20 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line_ID, PerAbs
Fields (name type(len) description [values] ->parent table):
  PerAbs Int(11) Period Code
  Line_ID Int(11) Row Number default=0
  ProfitAct nVarChar(15) Account Code ->OACT
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  DueDate Date(8) Due Date
  RefDate Date(8) Posting Date
  TaxDate Date(8) Document Date
  Memo nVarChar(50) Row Details
  MarkLine VarChar(1) Select default=N [Y=Yes, N=No]
  ActKeyLine nVarChar(15) Account Code ->OACT
  LocBalLine Num(19,6) Current Balance
  FcBalLine Num(19,6) Balance (Account Currency)
  SysBalLine Num(19,6) Balance (SC)
  ToPerAbs Int(11) To Period Code
  CtrlAct nVarChar(15) Control Account ->OACT
  PL_ACCOUNT VarChar(1) P/L Account default=Y [Y=Yes, N=No]
  Ref1_l nVarChar(100) Reference 1 for line
  Ref2_l nVarChar(100) Reference 2 for line
  Ref3_l nVarChar(27) Reference 3 for line
