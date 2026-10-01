<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GBI13 - GBI Row 13 - Enterprise's Profit Distribution Report
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History ID ->OGBI
  RowId Int(11) Row Number
  ItemName nVarChar(100) Item Name
  LineNum nVarChar(6) Line Number
  CurAmount Num(19,6) Current Period Amount
  PreAmount Num(19,6) Previous Period Amount
