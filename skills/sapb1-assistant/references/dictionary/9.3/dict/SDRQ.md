<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SDRQ - Drag&Relate - Queries
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ServerType, ObjFrom, ObjTo
Fields (name type(len) description [values] ->parent table):
  ObjTo nVarChar(4) ObjectTo
  ObjFrom nVarChar(4) ObjectFrom
  JoinStr nVarChar(254) Join String
  FilterStr nVarChar(128) Filter String
  ServerType Int(11) Server Type default=0
