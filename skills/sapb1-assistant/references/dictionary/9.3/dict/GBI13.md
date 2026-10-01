<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI13 - GBI Row 13 - Enterprise's Profit Distribution Report
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RowId, HistoryId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History ID ->OGBI
  RowId Int(11) Row Number
  ItemName nVarChar(100) Item Name
  LineNum nVarChar(6) Line Number
  CurAmount Num(19,6) Current Period Amount
  PreAmount Num(19,6) Previous Period Amount
