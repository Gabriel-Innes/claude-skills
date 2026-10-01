<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMGP - Material Group
Module: Inventory and Production | 6 columns | ObjType: 256
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: MatGrp
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  MatGrp nVarChar(3) Material Group
  Descrip nVarChar(70) Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
