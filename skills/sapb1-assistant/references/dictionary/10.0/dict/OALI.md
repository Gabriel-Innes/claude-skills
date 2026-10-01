<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OALI - Alternative Items 2
Module: Inventory and Production | 4 columns | ObjType: 107
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OrigItem, AltItem
Fields (name type(len) description [values] ->parent table):
  OrigItem nVarChar(50) Original Item No. ->OITM
  AltItem nVarChar(50) Alternative Item No. ->OITM
  Match Num(19,6) Match Factor
  Remarks nVarChar(50) Item Remarks
