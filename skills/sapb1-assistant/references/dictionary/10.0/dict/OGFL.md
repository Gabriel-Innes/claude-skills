<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OGFL - Grid Filter
Module: Administration | 5 columns | ObjType: 222
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormID, GridID, UserCode
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  GridID nVarChar(11) Grid ID
  UserCode Int(6) User Code
  DefFilter Int(11) Default Filter
  NextFltID Int(11) Next Filter ID default=1
