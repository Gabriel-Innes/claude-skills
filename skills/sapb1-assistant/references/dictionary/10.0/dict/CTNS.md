<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CTNS - Transaction Notification Setting
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  OBJECT_ID U: ObjectId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal No.
  ObjectId nVarChar(30) Business Object ID
  EnableAsyN VarChar(1) Enable async notification default=N [Y=Yes, N=No]
  EnableTn VarChar(1) Transaction Notification default=Y [Y=Yes, N=No]
  EnablePTn VarChar(1) Post Transaction Notification default=Y [Y=Yes, N=No]
