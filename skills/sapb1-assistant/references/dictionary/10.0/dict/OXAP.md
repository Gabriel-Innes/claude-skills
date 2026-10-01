<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OXAP - XAPP Master Data
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of XAPP
  Name nVarChar(250) Name of XAPP
  Default VarChar(1) Is default default=N
