<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# USR7 - Group User Association
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserId, GroupId
Fields (name type(len) description [values] ->parent table):
  UserId Int(6) User ID ->OUSR
  GroupId Int(6) Group ID ->OUGR
  Category nVarChar(155) Group Category
  StartDate Date(8) Start Date
  DueDate Date(8) Due Date
