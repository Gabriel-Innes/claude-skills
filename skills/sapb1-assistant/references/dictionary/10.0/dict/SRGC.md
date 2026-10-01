<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SRGC - Registred companies
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: dbName, dbUser
Fields (name type(len) description [values] ->parent table):
  dbName nVarChar(100) DB Name
  cmpName nVarChar(100) Comp. Name
  versStr nVarChar(13) Version
  dbUser nVarChar(50) SQL User
  LOC nVarChar(100) localization
  cmpStatus VarChar(1) Comp. Status
