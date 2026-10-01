<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI6 - GBI Row 6 - G/L Account Balance
Module: Finance | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RowId, HistoryId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  AcctCode nVarChar(15) Account Code
  Currency nVarChar(3) Account Currency
  EvalGrp nVarChar(254) Group for Calculating
  PerBBal Num(19,6) Period Begin Balance
  PerBQty Num(19,6) Period Begin Quantity
  PerBFCBal Num(19,6) Period Begin FC Balance
  CPDAmt Num(19,6) Current Period Debit Amount
  CPDQty Num(19,6) Current Period Debit Quantity
  CPDFCAmt Num(19,6) Current Period Debit FC Amount
  CPCAmt Num(19,6) Current Period Credit Amount
  CPCQty Num(19,6) Current Period Credit Quantity
  CPCFCAmt Num(19,6) Current Period Credit FC Amnt
  PerEBal Num(19,6) Period End Balance
  PerEQty Num(19,6) Period End Quantity
  PerEFCBal Num(19,6) Period End FC Balance
  AcctPeriod nVarChar(2) Fiscal Month
