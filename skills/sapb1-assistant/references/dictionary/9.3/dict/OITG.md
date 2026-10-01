<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OITG - Item Properties
Module: Inventory and Production | 3 columns | ObjType: 8
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItmsTypCod
  GROUP_NAME U: ItmsGrpNam
Fields (name type(len) description [values] ->parent table):
  ItmsTypCod Int(6) Number
  ItmsGrpNam nVarChar(50) Property Name
  UserSign Int(6) User Signature ->OUSR
