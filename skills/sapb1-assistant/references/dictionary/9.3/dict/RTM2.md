<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RTM2 - Rate Differences - SC Adjustment Rows
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AcctCode, CardCode, IsSysCurr, LineNum
  CARD_CODE: CardCode
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Reconciliation Key
  IsSysCurr VarChar(1) IS System Currency default=N [Y=Yes, N=No]
  CardCode nVarChar(15) BP Code ->OCRD
  AcctCode nVarChar(15) BP Control Account
  TransAmtSC Num(19,6) Total Transaction Amount (SC)
  BalDueSC Num(19,6) Total Balance Due (SC)
