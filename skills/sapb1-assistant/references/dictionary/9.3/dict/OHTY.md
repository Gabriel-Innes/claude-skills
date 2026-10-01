<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OHTY - Employee Types
Module: Human Resources | 4 columns | ObjType: 172
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: typeID
  NAME_KEY: name
Fields (name type(len) description [values] ->parent table):
  typeID Int(11) Employee Type ID
  name nVarChar(20) Name
  descriptio Text(16) Description
  locked VarChar(1) Locked default=N [Y=Yes, N=No]
