<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSCP - Service Call Problem Types
Module: Service | 4 columns | ObjType: 169
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: prblmTypID
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  prblmTypID Int(6) Problem Type ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
