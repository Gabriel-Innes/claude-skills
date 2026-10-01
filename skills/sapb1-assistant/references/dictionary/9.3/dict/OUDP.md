<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUDP - Departments
Module: Banking | 5 columns | ObjType: 119
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(20) Departments Name
  Remarks nVarChar(100) Description
  UserSign Int(6) User Signature ->OUSR
  Father nVarChar(20) Parent Department
