<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IMGLG - Group Message Log
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  From nVarChar(25) Message Sender
  GrpId Int(11) Group Id
  Msg Text(16) Message Content
  Time Date(8) Time
  Nty VarChar(1) Is Notification default=N [Y=Yes, N=No]
