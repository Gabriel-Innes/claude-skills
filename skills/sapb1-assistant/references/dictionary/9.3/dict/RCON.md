<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RCON - Connection Map for CR Templates
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ConnID, DocCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Internal Template Key
  ConnID Int(11) Connection ID
  OldServer nVarChar(64) Old Server Name
  OldDbName nVarChar(64) Old Database Name
  NewServer nVarChar(64) Mapped Server Name
  NewDbName nVarChar(64) Mapped Database Name
  UserCode nVarChar(32) User Code
  SubIndex Int(6) Subreport Index
  SubName nVarChar(64) Subreport Name
