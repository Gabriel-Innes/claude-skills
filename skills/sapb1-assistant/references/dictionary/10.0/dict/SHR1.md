<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SHR1 - Shareholder's Rights and Interests Report History - Rows
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ShrId, RowId
Fields (name type(len) description [values] ->parent table):
  ShrId Int(11) SHR Identity ->OSHR
  RowId Int(11) Row Number
  CatId Int(6) Category Identity
  LineNum nVarChar(6) Line Number
  ItemName nVarChar(254) Item Name
  Level Int(6) Level Number
  IndentChar nVarChar(6) Number of Characters to Indent
  Formula VarChar(1) Formula?
  CurAmount Num(19,6) Current Period Amount
  PreAmount Num(19,6) Previous Period Amount
