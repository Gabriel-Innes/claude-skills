<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWO4 - Production Order - Route Stages - History
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, StageId, DocEntry
  SEQUENCE U: LogInstanc, SeqNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->AWOR
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  Status VarChar(1) Stage Status default=O [O=Open, C=Closed]
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  ReqDays Num(19,6) Required Days default=0
  WaitDays Num(19,6) Waiting Days default=0
