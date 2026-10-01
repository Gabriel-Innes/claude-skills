<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# USR8 - Point of Issue User Association
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserId, PTICode
Fields (name type(len) description [values] ->parent table):
  UserId Int(6) User ID ->OUSR
  PTICode nVarChar(5) POI Code ->OPTI
