<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# APM6 - Project Management - Stages - Activities - History
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  ACTIVITYID Int(11) Activity Number ->OCLG
  LogInstanc Int(11) Log Instance default=0
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV
