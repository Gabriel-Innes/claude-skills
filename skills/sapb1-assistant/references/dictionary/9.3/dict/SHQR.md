<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SHQR - Upgrade queries history
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ServerType, DoBefore, Instance, TableId, Version
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  TableId nVarChar(4) Metadata CAB
  Instance Int(6) Query instance
  DoBefore VarChar(1) Do Before default=Y [Y=Yes, N=No]
  QurString Text(16) Query String
  ServerType Int(11) Server Type default=0
