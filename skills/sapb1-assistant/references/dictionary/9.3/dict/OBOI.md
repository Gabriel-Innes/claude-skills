<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBOI - Count Widget
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
