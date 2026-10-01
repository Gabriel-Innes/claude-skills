<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IMLTM - Departure Time
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  UsrCode nVarChar(25) User Code
  Peer nVarChar(25) Peer
  GrpId Int(11) Group Id
  DptTime Date(8) Departure Time
