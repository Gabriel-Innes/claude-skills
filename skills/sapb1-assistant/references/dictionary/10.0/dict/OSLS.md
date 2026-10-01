<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSLS - Short Link Mapping
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) GUID for short link
  Origin nVarChar(128) The origin of source link
  SrcLink Text(16) The source link URL
  OwnerCode nVarChar(50) The creator user code
  CreateDate Date(8) Date
  CreateTime Int(11) Time default=0
