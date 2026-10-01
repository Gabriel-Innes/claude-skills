<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# APM2 - Project Management - Stages - Open Issues - History
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMG1
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
