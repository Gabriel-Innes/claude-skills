<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PJT1 - Project Plan Steps
Module: Administration | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: StepCode, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  StepCode Int(11) Step Code
  Father Int(11) Father Step Code
  VisOrder Int(11) Visual Order
  Level Int(11) Node Level
  StepName nVarChar(254) Step Name
  StepInfo nVarChar(254) Step Info
  StepNotes nVarChar(254) Step Notes
  StepLink nVarChar(32) Step Link to Menu ID
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  IsComplete VarChar(1) Is Complete
  LogInstanc Int(11) Log Instance
  Owner nVarChar(254) Owner ->OUSR
  Status Int(11) Status default=0
  Duration Num(19,6) Duration
  PlanTime Num(19,6) Planned Time
  AtcEntry Int(11) Attachment Entry ->OATC
  TotalPTime Num(19,6) Total Planned Time
  QueryID Int(11) Step Link Query ID ->OUQR
