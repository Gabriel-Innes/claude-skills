<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCLA - Activity Status
Module: Business Partners | 4 columns | ObjType: 217
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: statusID
Fields (name type(len) description [values] ->parent table):
  statusID Int(11) Status ID
  name nVarChar(30) Status Name
  descriptio nVarChar(254) Status Description
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
