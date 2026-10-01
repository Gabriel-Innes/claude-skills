<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPDT - Predefined Text
Module: Marketing Documents | 3 columns | ObjType: 215
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: TextCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TextCode nVarChar(20) Text Code
  Text Text(16) TEXT
