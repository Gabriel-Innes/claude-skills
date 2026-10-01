<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GBI14 - GBI Row 14 - Small Enterprise's Cash Flow Statement
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  LineTitle nVarChar(100) Line Title
  LineNum nVarChar(5) Line Number
  PreAmount Num(19,6) Previous Year Amount
  CurAmount Num(19,6) Current Year Amount
