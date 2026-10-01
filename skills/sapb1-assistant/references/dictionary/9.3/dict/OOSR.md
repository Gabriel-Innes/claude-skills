<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OOSR - Information Source
Module: Inventory and Production | 4 columns | ObjType: 100
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Description
  SortOrder Int(6) Sort
  UserSign Int(6) User Signature ->OUSR
