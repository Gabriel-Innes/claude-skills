<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITT2 - BOM - Route Stages
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StageId, Father
  SEQUENCE U: SeqNum, Father
Fields (name type(len) description [values] ->parent table):
  Father nVarChar(50) Parent Item ->OITT
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  WaitDays Num(19,6) Waiting Days default=0
