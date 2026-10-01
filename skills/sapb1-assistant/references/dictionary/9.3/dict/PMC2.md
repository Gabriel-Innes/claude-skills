<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PMC2 - Project Management Configuration - Stages Setup
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StageID
Fields (name type(len) description [values] ->parent table):
  StageID Int(11) Stage No.
  Name nVarChar(100) Stage Name
  Dscription nVarChar(254) Stage Description
