<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# LIVI1 - IVI Log Array File
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogEntry, CalcNum
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
