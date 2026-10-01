<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CFN1 - Default Common Functions
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemIndex, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OCFN
  ItemIndex Int(11) Common Function Item Index
  UserMenu VarChar(1) User Menu Flag default=N [Y=, N=]
  MenuUID nVarChar(50) Menu UID
  Name nVarChar(100) Name
