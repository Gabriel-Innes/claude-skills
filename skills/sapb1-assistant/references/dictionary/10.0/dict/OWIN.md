<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWIN - Workflow Engine Information
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) ID
  WFInstId Int(11) Workflow Instance ID
  TaskId Int(11) Task ID
  ProcDefId nVarChar(250) Process Definition ID
  FlowElemId nVarChar(250) Flow Element ID
  InfoType nVarChar(2) Information Type [E=Error, W=Warning, I=Information, O=Other]
  InfoCode nVarChar(10) Predefined Information Code
  Desc Text(16) Description
  CreateDate Date(8) Create Date
  CreateTime Int(11) Create Time
  IsRead VarChar(1) Info. read by SAP Business One? [N=No, Y=Yes]
