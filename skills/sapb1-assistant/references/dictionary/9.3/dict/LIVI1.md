<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# LIVI1 - IVI Log Array File
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CalcNum, LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Internal Number ->LIVI
  CalcNum Int(11) Partial Sequence Number
  CreateDate Date(8) Create Date
  UserToDate Date(8) User To Date
  ActuToDate Date(8) Actual To Date
  LastMsgID Int(11) Last Calculated OILM Message
  Result VarChar(1) Result of Calculation default=F [F=Failure, S=Success, A=Archived]
  ResultStr nVarChar(254) Result String of Calculation
  UserSign Int(6) User Signature ->OUSR
  IgnFail VarChar(1) Ignore Previous Failure default=N [Y=Yes, N=No]
  ReorderFrm Date(8) Reorder 8.8 Messages: From Date
  ReorderTo Date(8) Reorder 8.8 Messages: To Date
  StopDate Date(8) Stop Date
  StopTime Int(6) Stop Time
