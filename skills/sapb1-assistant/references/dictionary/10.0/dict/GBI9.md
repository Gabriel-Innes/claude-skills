<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GBI9 - GBI Row 9 - Enterprise's Profit and Loss Statement
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  RepItm nVarChar(60) Report Item
  RepItmNo nVarChar(3) Report Item Number
  PeriodAmt Num(19,6) Period Amount
  YearAmt Num(19,6) Year Accumulated Amount
