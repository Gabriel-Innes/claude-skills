<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SEWAD - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  DBNAME: DbName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry
  DbName nVarChar(100) DB Name (common/company)
  AddonId Int(11) Addon ID
  AddonName nVarChar(128) Addon Name
  AddonVer nVarChar(12) Addon Version
  NameSpace nVarChar(20) Partner Name Space
  PartName nVarChar(40) Partner Name
