<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AQAG - Query Authorization Groups - Log
Module: Reports | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AUTHGRPID
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
