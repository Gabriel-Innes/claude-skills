<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SCSP - Stored Procs (Company)
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ServerType, SpName
Fields (name type(len) description [values] ->parent table):
  SpName nVarChar(50) SP Name
  SpString Text(16) SP String
  doBefore VarChar(1) Do before [Y=, N=]
  ForceCreat VarChar(1) Force Create [Y=Yes, N=No]
  ServerType Int(11) Server Type default=0
