<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GPA4 - Gross Profit Adjustment - JE Details Accounts
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  LineType VarChar(1) Line Type default=T [T=Total, A=Account]
  CurrCogs Num(19,6) Current COGS
  CalcCogs Num(19,6) Calculated COGS
  CogsDebit Num(19,6) COGS Debit
  CogsCredit Num(19,6) COGS Credit
  CogsAcct nVarChar(15) COGS Account
  PrDiffAcct nVarChar(15) Price Difference Account
  AutoPost VarChar(1) Automatic Posting default=Y [Y=Yes, N=No]
