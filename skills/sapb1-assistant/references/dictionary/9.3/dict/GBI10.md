<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI10 - GBI Row 10 - Enterprise's Cash Flow Statement
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RowId, HistoryId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  LineTitle nVarChar(100) Line Title
  LineNum nVarChar(5) Line Number
  Amount Num(19,6) Amount
