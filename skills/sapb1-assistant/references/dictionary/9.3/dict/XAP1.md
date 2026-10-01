<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XAP1 - Page of XAPP
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of page
  XAPEntry Int(11) Foreign key of XAPP
  Name nVarChar(250) Page name
  Default VarChar(1) Is default or not default=N
