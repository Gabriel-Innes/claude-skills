<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OHED - Education Types
Module: Human Resources | 4 columns | ObjType: 175
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: edType
  NAME_KEY U: name
Fields (name type(len) description [values] ->parent table):
  edType Int(11) Education Type
  name nVarChar(20) Name
  descriptio Text(16) Description
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
