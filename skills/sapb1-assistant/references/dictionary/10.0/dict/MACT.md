<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MACT - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  ACTION U: fatherId, actName
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Unique Id
  fatherId nVarChar(36) MOBJ id
  lineNum Int(11) Line Number
  actName nVarChar(50) Action Name
  noteSid Int(11) Action Name String Index
  note nVarChar(254) Note
  actType VarChar(1) Action Type
