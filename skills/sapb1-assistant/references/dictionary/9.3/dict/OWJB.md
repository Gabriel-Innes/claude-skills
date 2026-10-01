<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWJB - Workflow Job Entity
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
