<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODAL - Link between dashboard and form
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  DashEntry Int(11) Dashboard Entry
  FormID nVarChar(250) Form ID
  MobDesc nVarChar(250) Mobile Description
