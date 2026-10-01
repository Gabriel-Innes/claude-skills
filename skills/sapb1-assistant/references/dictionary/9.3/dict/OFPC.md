<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFPC - Fixed Assets Fiscal Year Change
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PeriodCat nVarChar(10) Period Category
  NextPeriod nVarChar(10) Change to Period
