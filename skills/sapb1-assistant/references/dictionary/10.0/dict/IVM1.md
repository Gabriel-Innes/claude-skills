<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IVM1 - Invoice Mapping Object Details
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OIVM
  LineNum Int(11) Line Number
  DocType nVarChar(20) Document Type
  DocEntry Int(11) Document Entry
  GtsStatus VarChar(1) GTS Status
