<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RSDB - Resource DB List
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsKey
  SERVER_DB U: DbName, ServerName
Fields (name type(len) description [values] ->parent table):
  AbsKey Int(11) Abs Key
  ServerName nVarChar(254) Server Name
  DbName nVarChar(64) Resource DB Name
  Date Date(8) Creation date
  Time Date(8) Creation Time
  OrigDB Int(11) Original DB
  MBServer nVarChar(254) Master Base Server Name
  MBDbName nVarChar(64) Master Base DB Name
