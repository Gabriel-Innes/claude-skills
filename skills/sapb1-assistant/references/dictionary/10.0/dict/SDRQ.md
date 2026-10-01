<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SDRQ - Drag&Relate - Queries
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjTo, ObjFrom, ServerType
Fields (name type(len) description [values] ->parent table):
  ObjTo nVarChar(4) ObjectTo
  ObjFrom nVarChar(4) ObjectFrom
  JoinStr nVarChar(254) Join String
  FilterStr nVarChar(128) Filter String
  ServerType Int(11) Server Type default=0
