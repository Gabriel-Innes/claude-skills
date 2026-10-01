<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OOIN - Interest
Module: Inventory and Production | 4 columns | ObjType: 98
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Description
  SortOrder Int(6) Sort default=100
  UserSign Int(6) User Signature ->OUSR
