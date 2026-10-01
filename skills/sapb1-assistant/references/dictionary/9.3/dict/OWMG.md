<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWMG - Workflow Manager
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Identity(11) Workflow ID
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
