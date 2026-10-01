<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EBUSR - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: B1Company
Fields (name type(len) description [values] ->parent table):
  B1Company nVarChar(100) B1 Company DB name
  B1User nVarChar(30) B1 user name (from OUSR)
  Pwd Text(16) encrypted password
  Pwd2 nVarChar(254) encrypted password (backup)
