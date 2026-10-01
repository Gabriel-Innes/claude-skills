<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWMG - Workflow Manager
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogIns, ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Workflow ID
  TemplateID Int(11) Template ID
  TmplateKey nVarChar(254) Template Key
  Name nVarChar(254) Name
  Version nVarChar(13) Version
  MAXIns Int(11) Maximum Number of Instances
  Status VarChar(1) Status default=I [I=Inactive, A=Active, E=Activation failed, M=Importing, P=Imported, F=Import failed, D=Deleted]
  XMLFile Text(16) XML File
  Desc Text(16) Description
  LogIns Int(11) Log Instance - History
  StartType VarChar(1) Start Type default=M [M=Manual Start, T=Timer Start, C=Conditional Start]
