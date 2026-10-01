<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# USR8 - Point of Issue User Association
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PTICode, UserId
Fields (name type(len) description [values] ->parent table):
  UserId Int(6) User ID ->OUSR
  PTICode nVarChar(5) POI Code ->OPTI
