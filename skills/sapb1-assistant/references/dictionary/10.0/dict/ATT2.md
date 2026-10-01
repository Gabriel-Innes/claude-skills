<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ATT2 - BOM - Route Stages - History
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Father, StageId, LogInstanc
  SEQUENCE U: Father, SeqNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Father nVarChar(50) Parent Item ->OITT
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  WaitDays Num(19,6) Waiting Days default=0
