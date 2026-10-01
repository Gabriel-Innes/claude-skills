<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GBI12 - GBI Row 12 - Shareholder's Rights and Interests Changing Report
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  ShrId Int(11) SHR Report History ID
  RowNum Int(11) Row Number in Saved Report
  ItemName nVarChar(254) Item Name
  LineNum nVarChar(6) Line number
  CurAmount Num(19,6) Amount for Current Period
  PreAmount Num(19,6) Amount for Previous Period
