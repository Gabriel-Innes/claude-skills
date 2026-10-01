<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CFN1 - Default Common Functions
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ItemIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OCFN
  ItemIndex Int(11) Common Function Item Index
  UserMenu VarChar(1) User Menu Flag default=N [Y=, N=]
  MenuUID nVarChar(50) Menu UID
  Name nVarChar(100) Name
