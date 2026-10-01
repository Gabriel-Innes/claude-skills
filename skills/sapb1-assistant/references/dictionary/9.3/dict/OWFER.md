<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWFER - Workflow Error Message
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) Internal Number
  MsgID nVarChar(64) Message ID
  MsgDetails Text(16) Message Details
  CreateDate Date(8) Create Date - History
  UserSign Int(6) Updating User - History ->OUSR
  CreateTime Int(11) Create Time
  MsgTaskID nVarChar(6) Message Task ID
  MsgErrSrc nVarChar(20) Message Source
  Remark Text(16) Remarks
  MsgType VarChar(1) Message Type [I=Information, E=Error, W=Warning]
  MsgInstID Int(11) Message Instance ID
  TemplateID Int(11) Template ID
