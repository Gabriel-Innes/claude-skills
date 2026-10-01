<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCUL - Customer Usage Statistics Log
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Identity(11) Internal Number
  StartRef Int(11) Session Start Reference
  EventType Int(11) Event Type
  DateTime nVarChar(20) Date Time
