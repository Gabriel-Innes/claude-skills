<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWEX - Workflow Engine Execution Entity
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  IsActive Int(6) Is Active
  IsConCurr Int(6) Is Concurrent
  IsScope Int(6) Is Scope
  ProcInstId nVarChar(100) Process Instance ID
  ParentId Int(11) Parent ID
  ProcDefId Int(11) Process Definition ID
  ActId nVarChar(250) Activity ID
  DataContex Text(16) Data Context
  B1WFInstId Int(11) Workflow Instance ID
  LastUpdate nVarChar(50) Last Update Date and Time
