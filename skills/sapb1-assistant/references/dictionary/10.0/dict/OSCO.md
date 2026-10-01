<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSCO - Service Call Origins
Module: Service | 5 columns | ObjType: 192
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: originID
Fields (name type(len) description [values] ->parent table):
  originID Int(6) Origin ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Locked VarChar(1) Locked
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
