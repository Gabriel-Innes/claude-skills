<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IDX1 - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  COLUMN U: fatherId, columnId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36)
  fatherId nVarChar(36)
  columnId nVarChar(36)
  lineNum Int(11)
