<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SCR3 - Special Ledger - Analytical Accounting Configuration Rule Additional Calculations: Revenues & Expenses
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FldNum, RuleID
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCR
  FldNum Int(6) Result Field Number
  SrcTable nVarChar(20) Main Source Table
  SrcField nVarChar(20) Main Source Table Field
  CalcCase nVarChar(200) Additional Calcul. Expression
  CalcTable nVarChar(200) Main Calculation Expression
  CondCase nVarChar(200) Additional Calcul. Condition
  CondTable nVarChar(200) Main Calculation Condition
  Grouping nVarChar(100) Group by Clause
  CallProc nVarChar(50) Recalculation Stored Procedure Name
  ExtCond nVarChar(200) Extended Special Data
