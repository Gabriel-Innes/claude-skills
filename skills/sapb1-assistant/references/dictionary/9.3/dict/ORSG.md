<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORSG - Resource Properties
Module: General | 3 columns | ObjType: 291
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ResTypCod
  GROUP_NAME U: ResGrpNam
Fields (name type(len) description [values] ->parent table):
  ResTypCod Int(6) Number
  ResGrpNam nVarChar(50) Property Name
  UserSign nVarChar(6) User Signature ->OUSR
