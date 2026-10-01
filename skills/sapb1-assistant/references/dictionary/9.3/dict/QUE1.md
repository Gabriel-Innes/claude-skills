<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# QUE1 - Queue Members
Module: Service | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: member, queueID
Fields (name type(len) description [values] ->parent table):
  queueID nVarChar(20) Queue ID ->OQUE
  member Int(11) Member Name ->OUSR
