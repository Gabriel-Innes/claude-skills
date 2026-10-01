<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WDBD1 - Dashboard Cards
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  Content Text(16) Content
  Sys VarChar(1) Sys default=Y [Y=Yes, N=No]
  Version nVarChar(40) Version
