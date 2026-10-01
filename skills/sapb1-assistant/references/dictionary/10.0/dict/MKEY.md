<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MKEY - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  COLUMN U: fatherId, columnId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Unique Id
  fatherId nVarChar(36) Meta Object Guid
  columnId nVarChar(36) Column Id
  lineNum Int(11) Line Number
  fatheColId nVarChar(36) Father Column Id
