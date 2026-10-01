<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MKEY - MKEY
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: lineNum, fatherId
  GUID U: guid
  COLUMN U: columnId, fatherId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Unique Id
  fatherId nVarChar(36) Meta Object Guid
  columnId nVarChar(36) Column Id
  lineNum Int(11) Line Number
  fatheColId nVarChar(36) Father Column Id
