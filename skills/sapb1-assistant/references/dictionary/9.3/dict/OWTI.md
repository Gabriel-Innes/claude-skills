<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWTI - Workflow Timer Definition
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  Name nVarChar(50) Name
  TemplateId Int(11) Workflow Template ID
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  RepeatCnt Int(11) Repeat Event Count
  Duration nVarChar(200) Duration
  LastUpdate nVarChar(50) Last Update Date and Time
  UnScheStDt Date(8) Start Date of Next Schedule
  UnScheStTi Int(11) Start Time of Next Schedule
  UnScheReCt Int(11) Unschedule Repeat Count
  IsComplete VarChar(1) Is This Timer Completed default=N [Y=Yes, N=No]
  JobHanType nVarChar(50) Job Handler Type
  JobHanConf Text(16) Job Handler Configuration
  IsActive VarChar(1) Is This an Active Timer
