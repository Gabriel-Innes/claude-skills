<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IDX1 - IDX1
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: lineNum, fatherId
  GUID U: guid
  COLUMN U: columnId, fatherId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36)
  fatherId nVarChar(36)
  columnId nVarChar(36)
  lineNum Int(11)
