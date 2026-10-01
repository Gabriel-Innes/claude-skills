<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# NCP2 - New Cockpit Tile
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PageEntry, ObjectType, ObjectKey
Fields (name type(len) description [values] ->parent table):
  PageEntry Int(11) Page Number ->ONCP
  Type nVarChar(20) Type ->NCP1
  ObjectType Int(11) Object Type ->CDPM
  ObjectKey nVarChar(50) Object ID ->CDPM
