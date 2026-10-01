<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OQWZ - Query Wizard
Module: Reports | 3 columns | ObjType: 141
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Query Code
  Name nVarChar(50) Query Name
  UserSign Int(6) User Signature ->OUSR
