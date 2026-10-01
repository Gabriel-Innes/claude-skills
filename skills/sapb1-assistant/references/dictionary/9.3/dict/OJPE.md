<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OJPE - Local Era Calendar
Module: Administration | 3 columns | ObjType: 250
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code VarChar(1) Local Era Code
  EraName nVarChar(20) Local Era Name
  StartDate Date(8) Start Date
