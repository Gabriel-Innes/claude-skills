<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWST - Confirmation Level
Module: Administration | 6 columns | ObjType: 120
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WstCode
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  WstCode Int(11) Stage ->OWST
  Name nVarChar(20) Name
  Remarks nVarChar(100) Description
  MaxReqr Int(6) No. of Authorizers default=1
  UserSign Int(6) User Signature ->OUSR
  MaxRejReqr Int(6) No. of Rejects default=1
