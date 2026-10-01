<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBOI - Count Widget
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(15) Count Widget Code
  Name nVarChar(100) Name
  QueryId Int(11) Link Query ID ->OUQR
  QCategory Int(11) Link Query Category ->OQCN
  Desc nVarChar(200) Description
  MenuId Int(11) Menu ID default=0
