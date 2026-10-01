<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCLA - Activity Status
Module: Business Partners | 4 columns | ObjType: 217
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: statusID
Fields (name type(len) description [values] ->parent table):
  statusID Int(11) Status ID
  name nVarChar(30) Status Name
  descriptio nVarChar(254) Status Description
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
