<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EESUB - EESUB
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SenderId, ReceiverId, ReturnAddr, Processor, EventType
Fields (name type(len) description [values] ->parent table):
  EventType nVarChar(30)
  Processor nVarChar(60)
  ReceiverId nVarChar(50)
  ReturnAddr nVarChar(254)
  SenderId nVarChar(50)
  FilterName nVarChar(60)
  FilterVal nVarChar(60)
