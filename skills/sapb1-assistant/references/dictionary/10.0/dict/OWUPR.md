<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWUPR - User Preference
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  TableName nVarChar(10) Table Name
  ColName nVarChar(10) Column Name
  DefaultVal nVarChar(254) Default Value
