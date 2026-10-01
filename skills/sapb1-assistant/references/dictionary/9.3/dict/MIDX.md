<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MIDX - MIDX
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: idxName, fatherId
  GUID U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36)
  fatherId nVarChar(36)
  idxName nVarChar(36)
  isUnique VarChar(1)
