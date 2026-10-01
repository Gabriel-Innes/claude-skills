<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IMPLG - Private Message Log
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  Owner nVarChar(25) Message Owner
  From nVarChar(25) Message Sender
  To nVarChar(25) Message Receiver
  Msg Text(16) Message Content
  Time Date(8) Time
