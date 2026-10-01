<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OALI - Alternative Items 2
Module: Inventory and Production | 4 columns | ObjType: 107
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AltItem, OrigItem
Fields (name type(len) description [values] ->parent table):
  OrigItem nVarChar(50) Original Item No. ->OITM
  AltItem nVarChar(50) Alternative Item No. ->OITM
  Match Num(19,6) Match Factor
  Remarks nVarChar(50) Item Remarks
