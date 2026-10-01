<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SCM2 - Special Ledger - Analytical Accounting Configuration Rule Goals: Material
Module: Finance | 22 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GoalNum, RuleID
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCM
  GoalNum nVarChar(6) Rule Goal Number
  TransTpVal Int(6) Transaction Type Number
  TransTpFld nVarChar(20) Transaction Type Table Field
  PrfCntVal nVarChar(8) Distribution Rule Code ->OOCR
  PrfCntFld nVarChar(20) Distribution Rule Table Field
  DebitAct nVarChar(15) Debit Account ->OACT
  CreditAct nVarChar(15) Credit Account ->OACT
  RevSides VarChar(1) Revert Debit/Credit Sides default=N [N=No, Y=Yes]
  SrcTable nVarChar(10) Main Source Table
  SrcField nVarChar(20) Main Source Table Field
  SrcFieldFC nVarChar(20) Source Field, Foreign Currency
  SrcFieldSC nVarChar(20) Source Field, System Currency
  Calc nVarChar(200) Calculation Expression
  CalcFC nVarChar(200) Expression for Foreign Calculation
  CalcSC nVarChar(200) Expression for System Calculation
  CalcCond nVarChar(200) Calculation Condition
  CalcCondFC nVarChar(200) Condition for Foreign Calculation
  CalcCondSC nVarChar(200) Condition for System Calculation
  CurrFld nVarChar(20) Table Field with Currency
  CallProc nVarChar(50) Recalculation Stored Procedure Name
  ExtCond nVarChar(200) Extended Special Data
