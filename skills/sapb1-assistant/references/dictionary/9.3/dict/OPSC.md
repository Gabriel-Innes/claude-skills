<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPSC - Product Source Code
Module: Inventory and Production | 3 columns | ObjType: 1320000039
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Source Code
  Desc nVarChar(100) Description
  GroupCode Int(6) Group Code ->OPSG
