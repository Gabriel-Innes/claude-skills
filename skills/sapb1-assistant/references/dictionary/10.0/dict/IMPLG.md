<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IMPLG - Private Message Log
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  Owner nVarChar(25) Message Owner
  From nVarChar(25) Message Sender
  To nVarChar(25) Message Receiver
  Msg Text(16) Message Content
  Time Date(8) Time
