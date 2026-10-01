<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OHMM - SAP HANA Model Management
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ModelAuth nVarChar(100) Model Author
  ModelName nVarChar(100) Model Name
  ModelVer nVarChar(100) Model Version
  Desc Text(16) Description
  Status VarChar(1) Status [I=Imported, D=Deployed, T=In Task]
  InfoFile Text(16) Info File
  UpdateBy Int(11) Last Updated User's Code
  ChangeBy nVarChar(100) Last Changed SAP HANA User
  CreateDate nVarChar(100) Created at Date
  CreateTime Int(11) Created at Time
  ChangeDate nVarChar(100) Changed at Date
  ChangeTime Int(11) Changed at Time
  TaskId Int(11) Task ID
  DeployDate Date(8) Deployment Date
  DeployTime Int(11) Deployment Time
  Language nVarChar(8) Deployment Language
