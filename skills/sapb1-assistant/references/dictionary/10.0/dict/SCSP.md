<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SCSP - Stored Procs (Company)
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SpName, ServerType
Fields (name type(len) description [values] ->parent table):
  SpName nVarChar(50) SP Name
  SpString Text(16) SP String
  doBefore VarChar(1) Do before [Y=, N=]
  ForceCreat VarChar(1) Force Create [Y=Yes, N=No]
  ServerType Int(11) Server Type default=0
