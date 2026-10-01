<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWUAC - Recent user activities
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  AppId Text(16) App Id
  AppType nVarChar(20) App Type
  Count Int(11) Count
  Timestamp nVarChar(20) Timestamp
  Title nVarChar(100) Title
  Url Text(16) Url
  UsageArray nVarChar(100) Usage Array
  UserId Int(11) User Id
  RecentDay nVarChar(20) Recent Day
