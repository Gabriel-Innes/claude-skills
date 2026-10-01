<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWJB - Workflow Job Entity
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) ID
  HandlerTyp nVarChar(50) Handler Type
  ExecId Int(11) Execution ID
  Rev Int(11) Revision
  DueDate Date(8) Due Date
  ProcInstId Int(11) Process Instance ID
  Type nVarChar(250) Type
  HandlerCfg nVarChar(250) Handler Configuration
