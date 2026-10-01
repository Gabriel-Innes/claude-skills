<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSCT - Service Call Types
Module: Service | 4 columns | ObjType: 168
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: callTypeID
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  callTypeID Int(6) Call Type ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
