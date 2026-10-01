<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SSEN - SSEN
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(128) Session ID
  ServerName nVarChar(254) Server Name
  Port Int(11) Port Number
  ReqEnter Int(11) Request Enter Time
  ReqLeave Int(11) Request Leave Time
  DBServer nVarChar(254) DB Server Name
  DBName nVarChar(254) Company DB Name
  UserCode nVarChar(64) Company User Code
  UserPwd nVarChar(254) Company User
  Language Int(11) Language Code
