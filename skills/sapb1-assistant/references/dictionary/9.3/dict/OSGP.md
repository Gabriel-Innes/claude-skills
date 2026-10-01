<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSGP - Service Group for Brazil
Module: Service | 6 columns | ObjType: 255
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: ServiceGrp
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Service Group ID
  ServiceGrp nVarChar(3) Service Group
  Descrip nVarChar(70) Description
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
