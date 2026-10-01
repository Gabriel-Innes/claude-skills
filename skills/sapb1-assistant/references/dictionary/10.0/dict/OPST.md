<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPST - Service Call Problem Subtype
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ProSubTyId
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  ProSubTyId Int(6) Problem Subtype ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
