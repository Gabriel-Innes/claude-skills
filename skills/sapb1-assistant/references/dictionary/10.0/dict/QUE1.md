<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# QUE1 - Queue Members
Module: Service | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: queueID, member
Fields (name type(len) description [values] ->parent table):
  queueID nVarChar(20) Queue ID ->OQUE
  member Int(11) Member Name ->OUSR
