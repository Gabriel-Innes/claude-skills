<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SPRG - Application Start
Module: Administration | 8 columns | ObjType: 86
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, UserCode
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Row Number
  UserCode nVarChar(25) User Code default=-1
  Name nVarChar(128) Application Name
  FileName nVarChar(254) File Name
  Path Text(16) Application Route
  Params Text(16) Application Parameters
  OPRTION nVarChar(50) Operation Method default=open [open=Open, edit=Edit, explore=Find Folder, find=Find File, print=Print, properties=Properties]
  WIN_STYLE nVarChar(2) Windows Type default=1 [0=Hide, 1=Standard, 3=Enlarge, 5=Operate as Previous, 6=Reduce, 9=Restore]
