<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AQAG - Query Authorization Groups - Log
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AUTHGRPID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AUTHGRPID Int(11) Query Authorization Group ID
  AUTHGRPCD nVarChar(50) Group Code
  AUTHGRPN nVarChar(254) Group Description
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) Item Created By ->OUSR
  UserSign2 Int(6) Item Updated By ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Date of Create
  Deleted VarChar(1) Deleted Field default=N
  SnapShotID Int(11) Snapshot ID default=0
