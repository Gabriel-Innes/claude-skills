<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GBI15 - GBI Row 15 - Enterprise's VAT Payable Detail Report
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  ItemName nVarChar(100) Item Name
  LineNum nVarChar(6) Line Number
  CurMonAmnt Num(19,6) Current Month Amount
  CurYrAmnt Num(19,6) Current Year Amount
