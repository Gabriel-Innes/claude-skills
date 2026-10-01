<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GBI11 - GBI Row 11 - Devalue Provision of Enterprise Assets
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History ID ->OGBI
  RowId Int(11) Row Number
  ItemName nVarChar(100) Item Name
  BOPBalance Num(19,6) Balance at Beginning of Period
  CurDebit Num(19,6) Current Period in Debit
  CurCredit Num(19,6) Current Period in Credit
  EOPBalance Num(19,6) Balance at End of Period
