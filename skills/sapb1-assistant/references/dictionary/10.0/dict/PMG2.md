<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PMG2 - Project Management - Stages - Open Issues
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  AREA Int(11) Area ->PMC3
  PRIORITY Int(11) Priority
  REMARKS Text(16) Remarks
  CLOSED VarChar(1) Closed default=N [Y=Yes, N=No]
  SOLUTIONID Int(11) Solution Code ->OSLT
  SOLUTION nVarChar(254) Solution Description
  RESPNSIBLE Int(11) Responsible ->OHEM
  ENTERED Int(11) Entered By ->OHEM
  DATE Date(8) Date Entered
  EFFORT Num(19,6) Effort Costs
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV
