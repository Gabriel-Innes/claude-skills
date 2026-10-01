<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CLC1 - Change Logs Cleanup Line
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ModObjKey
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ModObjKey nVarChar(8) Module or Object Key
  CurSize Num(19,6) Current Size (MB)
  Status Int(11) Status
