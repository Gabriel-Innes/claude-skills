<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXROA - XLR Object Access
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectAcce
Fields (name type(len) description [values] ->parent table):
  ObjectAcce Identity(11) ObjectAccessId
  RoleId nVarChar(16) RoleId
  ObjId nVarChar(254) ObjId
  SubId nVarChar(50) SubId
  AccessLeve Int(11) AccessLevel
