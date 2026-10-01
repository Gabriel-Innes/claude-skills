<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSST - Service Call Solution Statuses
Module: Service | 4 columns | ObjType: 188
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Number
  NAME: Name
Fields (name type(len) description [values] ->parent table):
  Number Int(11) Number
  Name nVarChar(20) Name
  Descriptio nVarChar(254) Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
