<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSCS - Service Call Statuses
Module: Service | 5 columns | ObjType: 167
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: statusID
  NAME: Name
Fields (name type(len) description [values] ->parent table):
  statusID Int(6) Status ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Locked VarChar(1) Locked
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
