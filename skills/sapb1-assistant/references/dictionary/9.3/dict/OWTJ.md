<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWTJ - Workflow Timer Job
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  IsASync VarChar(1) Is Asychronized [Y=Yes, N=No]
  Status nVarChar(10) Status
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  TimerEtyId Int(11) Timer Entity ID
  JobHanConf Text(16) Job Handler Configuration
  JobHanType nVarChar(50) Job Handler Type
  LastUpdate nVarChar(50) Last Update Date and Time
