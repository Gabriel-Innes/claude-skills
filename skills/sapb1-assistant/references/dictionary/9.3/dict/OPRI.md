<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPRI - Browser Access Printers
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(250) Printer Name
  UserID Int(6) User ID
  Desc nVarChar(254) Description
  Server nVarChar(254) Server
  Selected VarChar(1) Select Printer default=N
  DPrinter VarChar(1) Default Printer default=N
