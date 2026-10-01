<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GBI5 - GBI Row 5 - Projects
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RowId, HistoryId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  PrjCode nVarChar(20) Project Code ->OPRJ
  PrjName nVarChar(100) Project Name
