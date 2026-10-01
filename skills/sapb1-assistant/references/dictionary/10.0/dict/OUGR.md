<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OUGR - Authorization Group
Module: Administration | 15 columns | ObjType: 231000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupId
  NAME_KEY U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupId Int(6) Authorization Group ID
  GroupName nVarChar(155) Group Name
  GroupDec nVarChar(155) Group Description
  Allowences Text(16) Allowances
  TPLId Int(6) Template ID ->UICU
  StartDate Date(8) Start Date
  DueDate Date(8) Due Date
  GroupType VarChar(1) Group Type default=A [A=Authorization, F=Form Settings, T=Alerts, U=UI Configuration Templates, L=All]
  CockpitId Int(6) Cockpit Template ID
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User - History ->OUSR
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  VersionNum nVarChar(13) Version Number
