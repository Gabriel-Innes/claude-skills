<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSAC - India SAC Code
Module: Inventory and Production | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SERVCODE U: ServCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  ServName nVarChar(254) Service Name
  ServCode nVarChar(8) Service Code
