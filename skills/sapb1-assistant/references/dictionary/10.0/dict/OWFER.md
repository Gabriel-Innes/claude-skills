<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWFER - Workflow Error Message
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
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
