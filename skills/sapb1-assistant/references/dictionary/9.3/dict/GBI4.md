<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI4 - GBI Row 4 - Business Partners
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RowId, HistoryId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  BPNo nVarChar(30) BP Number
  BPName nVarChar(60) BP Name
  CatNo Int(6) Category Number
  Loc nVarChar(103) Location Area
  Tel nVarChar(20) Telephone
  Address nVarChar(100) Street/PO Box
  CreditRank nVarChar(6) Credit Rank
