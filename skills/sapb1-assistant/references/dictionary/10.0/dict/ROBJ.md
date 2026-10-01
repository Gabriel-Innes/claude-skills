<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ROBJ - TM Import/Export Obj
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsKey
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsKey Int(11) Absolute Key
  Name nVarChar(100) Name
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time default=0
  SentDate Date(8) Date Sent For Trans
  SentTime Int(6) Time Sent For Trans default=0
  Localztion nVarChar(2) Localization relevance of obj default=XX
  SntStrCont Int(11) Send Strings Count
