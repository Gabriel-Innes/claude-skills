<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OITG - Item Properties
Module: Inventory and Production | 3 columns | ObjType: 8
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItmsTypCod
  GROUP_NAME U: ItmsGrpNam
Fields (name type(len) description [values] ->parent table):
  ItmsTypCod Int(6) Number
  ItmsGrpNam nVarChar(50) Property Name
  UserSign Int(6) User Signature ->OUSR
