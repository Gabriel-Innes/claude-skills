<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OHPS - Employee Position
Module: Human Resources | 4 columns | ObjType: 210
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: posID
  NAME U: name
Fields (name type(len) description [values] ->parent table):
  posID Int(11) Item ID
  name nVarChar(20) Position Name
  descriptio Text(16) Description
  LocFields VarChar(1) Activate Localization Fields default=N [Y=, N=]
