<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SRGC - Registred companies
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: dbUser, dbName
Fields (name type(len) description [values] ->parent table):
  dbName nVarChar(100) DB Name
  cmpName nVarChar(100) Comp. Name
  versStr nVarChar(10) Version
  dbUser nVarChar(50) SQL User
  LOC nVarChar(100) localization
  cmpStatus VarChar(1) Comp. Status
