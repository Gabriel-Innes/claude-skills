<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EESUB - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EventType, Processor, ReturnAddr, ReceiverId, SenderId
Fields (name type(len) description [values] ->parent table):
  EventType nVarChar(30)
  Processor nVarChar(60)
  ReceiverId nVarChar(50)
  ReturnAddr nVarChar(254)
  SenderId nVarChar(50)
  FilterName nVarChar(60)
  FilterVal nVarChar(60)
