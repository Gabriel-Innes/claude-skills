<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# APH1 - Project Management - Stages - History
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OPHA
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMC2
  POS Int(11) Position
  START Date(8) Start Date
  CLOSE Date(8) Closing Date
  FINISHDATE Date(8) Finished Date
  Task Int(11) Task Type
  DSCRIPTION Text(16) Description
  EXPCOSTS Num(19,6) Planned Cost
  InvAmtAR Num(19,6) Invoiced Amount (A/R)
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvAmtAP Num(19,6) Invoiced Amount (A/P)
  OpenAmtAP Num(19,6) Open Amount (A/P)
  PERCENT Num(19,6) Contribution Rate - Percentage
  FINISH VarChar(1) Finished default=N [Y=Yes, N=No]
  OWNER Int(11) Owner ->OHEM
  StageDep1 Int(11) Stage Dependence (1)
  StageDep2 Int(11) Stage Dependence (2)
  StageDep3 Int(11) Stage Dependence (3)
  StageDep4 Int(11) Stage Dependence (4)
  StDp1Type VarChar(1) Stage Dependence (1) project type default=P [P=Project, S=Subproject]
  StDp2Type VarChar(1) Stage Dependence (2) project type default=P [P=Project, S=Subproject]
  StDp3Type VarChar(1) Stage Dependence (3) project type default=P [P=Project, S=Subproject]
  StDp4Type VarChar(1) Stage Dependence (4) project type default=P [P=Project, S=Subproject]
  StDp1Abs Int(11) Stage Dependence (1) project key
  StDp2Abs Int(11) Stage Dependence (2) project key
  StDp3Abs Int(11) Stage Dependence (3) project key
  StDp4Abs Int(11) Stage Dependence (4) project key
  LogInstanc Int(11) Log Instance default=0
  AtcEntry Int(11) Attachment Entry ->OATC
  UniqueID nVarChar(50) Unique ID
  EncryptIV nVarChar(100) Encrypt IV
