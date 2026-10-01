<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MIDX - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, idxName
  GUID U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36)
  fatherId nVarChar(36)
  idxName nVarChar(36)
  isUnique VarChar(1)
