<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MACT - MACT
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: lineNum, fatherId
  GUID U: guid
  ACTION U: actName, fatherId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Unique Id
  fatherId nVarChar(36) MOBJ id
  lineNum Int(11) Line Number
  actName nVarChar(50) Action Name
  noteSid Int(11) Action Name String Index
  note nVarChar(254) Note
  actType VarChar(1) Action Type
