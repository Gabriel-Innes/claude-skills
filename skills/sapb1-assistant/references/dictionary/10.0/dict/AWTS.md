<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWTS - Workflow Engine Task Table
Module: Administration | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id, LogInst
Fields (name type(len) description [values] ->parent table):
  Id Int(11) ID
  Owner nVarChar(254) Owner
  OutputPar Text(16) Output Parameter
  EndTime nVarChar(50) End Time
  StartTime nVarChar(50) Start Time
  ProcDefId Int(11) Process Definition ID
  Name nVarChar(254) Name
  ExeId Int(11) Execution ID
  ProcInsId Int(11) Process Instance ID
  Desc nVarChar(254) Description
  InputPar Text(16) Input Parameter
  DelReason nVarChar(254) Delete Reason
  Assignee nVarChar(254) Assignee
  LogInst Int(11) Log Instance
  LastUpdate nVarChar(50) Last Update Date
  Key nVarChar(254) Task ID in XML
  B1Task Int(11) B1 Task ID
