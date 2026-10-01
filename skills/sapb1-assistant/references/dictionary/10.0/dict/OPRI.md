<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPRI - Browser Access Printers
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(250) Printer Name
  UserID Int(6) User ID
  Desc nVarChar(254) Description
  Server nVarChar(254) Server
  Selected VarChar(1) Select Printer default=N
  DPrinter VarChar(1) Default Printer default=N
