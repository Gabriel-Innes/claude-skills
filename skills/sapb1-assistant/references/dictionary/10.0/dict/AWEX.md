<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWEX - Workflow Engine Execution Entity
Module: Administration | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id, logInst
Fields (name type(len) description [values] ->parent table):
  Id Int(11) ID
  IsActive Int(6) Is Active
  IsConCurr Int(6) Is Concurrent
  IsScope Int(6) Is Scope
  ProcInstId nVarChar(100) Process Instance ID
  BizKey nVarChar(250) Business Key
  ParentId Int(11) Parent ID
  ProcDefId Int(11) Process Definition ID
  ActId nVarChar(250) Activity ID
  DataContex Text(16) Data Context
  B1WFInstId Int(11) Workflow Instance ID
  logInst Int(11) Log Instance
  LastUpdate nVarChar(50) Last Update Date
