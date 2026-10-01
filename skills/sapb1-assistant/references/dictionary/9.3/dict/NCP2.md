<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NCP2 - New Cockpit Tile
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectKey, ObjectType, PageEntry
Fields (name type(len) description [values] ->parent table):
  PageEntry Int(11) Page Number ->ONCP
  Type nVarChar(20) Type ->NCP1
  ObjectType Int(11) Object Type ->CDPM
  ObjectKey nVarChar(50) Object ID ->CDPM
