<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWIN - Workflow Engine Information
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
