<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SHQR - Upgrade queries history
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version, TableId, Instance, DoBefore, ServerType
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  TableId nVarChar(4) Metadata CAB
  Instance Int(6) Query instance
  DoBefore VarChar(1) Do Before default=Y [Y=Yes, N=No]
  QurString Text(16) Query String
  ServerType Int(11) Server Type default=0
