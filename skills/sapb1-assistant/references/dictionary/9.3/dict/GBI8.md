<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI8 - GBI Row 8 - Enterprise's Balance Sheet
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RowId, HistoryId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  AcctName nVarChar(100) Account Name
  LineNum nVarChar(6) Line Number
  YearBAmt Num(19,6) Year Begin Amount
  PerEAmt Num(19,6) Period End Amount
  RepDate nVarChar(8) Report Date
