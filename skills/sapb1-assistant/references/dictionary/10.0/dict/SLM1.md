<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SLM1 - Special Ledger - Analytical Accounting Report Lines: Material
Module: Finance | 34 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocID, LineID
Fields (name type(len) description [values] ->parent table):
  DocID Int(11) Document Identification Number ->OSLM
  LineID Int(11) Line Identification
  RuleID Int(6) Rule Identification Number ->OSCM
  GoalNum Int(6) Rule Goal Number
  TransType Int(6) Transaction Type Number
  PrfCntVal nVarChar(8) Distribution Rule Code ->OOCR
  PrfCntOrig nVarChar(8) Orig. Distribution Rule Code ->OOCR
  Checked VarChar(1) Selected for Processing default=Y [N=No, Y=Yes]
  Status VarChar(1) Status
  Enabled VarChar(1) Enabled for Processing default=Y [N=No, Y=Yes]
  DebitAct nVarChar(15) Debit Account ->OACT
  CreditAct nVarChar(15) Credit Account ->OACT
  RevSides VarChar(1) Revert Debit/Credit Sides default=N [N=No, Y=Yes]
  Src Num(19,6) Source Amount
  SrcFC Num(19,6) Source Amount, Foreign Currency
  SrcSC Num(19,6) Source Amount, System Currency
  SrcCalc Num(19,6) Calculated Amount
  SrcCalcFC Num(19,6) Calculated Amount - Foreign
  SrcCalcSC Num(19,6) Calculated Amount - System
  FinalSum Num(19,6) Final Amount
  FinalSumFC Num(19,6) Final Amount (FC)
  FinalSumSC Num(19,6) Final Amount (SC)
  Currency nVarChar(3) Foreign Currency ->OCRN
  MainTable nVarChar(20) Main Source Table
  PKField0 nVarChar(50) Primary Key Field
  PKField1 nVarChar(50) Primary Key Field
  PKField2 nVarChar(50) Primary Key Field
  PKField3 nVarChar(50) Primary Key Field
  PKField4 nVarChar(50) Primary Key Field
  PKField5 nVarChar(50) Primary Key Field
  PKField6 nVarChar(50) Primary Key Field
  PKField7 nVarChar(50) Primary Key Field
  PKField8 nVarChar(50) Primary Key Field
  PKField9 nVarChar(50) Primary Key Field
