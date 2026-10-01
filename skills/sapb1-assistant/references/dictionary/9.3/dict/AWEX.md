<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWEX - Workflow Engine Execution Entity
Module: Administration | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: logInst, Id
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
