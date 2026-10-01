<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IMGDT - User Delete Group Log Time
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  Owner nVarChar(25) Message Owner
  GrpId Int(11) Group Id
  Time Date(8) Time
