<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RTM2 - Rate Differences - SC Adjustment Rows
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, IsSysCurr, CardCode, AcctCode
  CARD_CODE: CardCode
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Reconciliation Key
  IsSysCurr VarChar(1) IS System Currency default=N [Y=Yes, N=No]
  CardCode nVarChar(15) BP Code ->OCRD
  AcctCode nVarChar(15) BP Control Account
  TransAmtSC Num(19,6) Total Transaction Amount (SC)
  BalDueSC Num(19,6) Total Balance Due (SC)
