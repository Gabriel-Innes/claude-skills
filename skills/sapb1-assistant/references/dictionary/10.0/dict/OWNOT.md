<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWNOT - Notifications
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  Date Date(8) Activity Date
  Read VarChar(1) Read/Unread status
  Dismissed VarChar(1) Dismissed or not
  NotiType Int(11) Notification Type
