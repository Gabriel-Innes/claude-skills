<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTNC - Transaction Category
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  TRANS U: TransCat
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  TransCat nVarChar(100) Transaction Category
  Locked VarChar(1) Locked default=N
