<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OOFR - Defect Cause
Module: Inventory and Production | 4 columns | ObjType: 102
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Num
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Description
  SortOrder Int(6) Sort default=100
  UserSign Int(6) User Signature ->OUSR
