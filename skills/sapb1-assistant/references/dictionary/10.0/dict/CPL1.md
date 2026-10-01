<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CPL1 - Quick Copy - Instance Log
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Number ->OCPL
  LogId Int(11) Log ID
  ObjectID nVarChar(20) Object ID
  Instance nVarChar(254) Instance Key
  ErrCode nVarChar(20) Error Code
  MessageId nVarChar(20) Message ID
  MessageDes nVarChar(254) Message Description
  InstName nVarChar(254) Instance Name
