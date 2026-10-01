<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WOR4 - Production Order - Route Stages
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StageId, DocEntry
  SEQUENCE U: SeqNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  Status VarChar(1) Stage Status default=P [P=Planned, I=In Progress, C=Complete]
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  ReqDays Num(19,6) Required Days default=0
  WaitDays Num(19,6) Waiting Days default=0
