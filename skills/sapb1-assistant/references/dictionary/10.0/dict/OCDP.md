<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCDP - Closing Date Procedure
Module: Administration | 6 columns | ObjType: 261
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ClsDateNum
  ABS_ENTRY U: ClsDtCode
Fields (name type(len) description [values] ->parent table):
  ClsDateNum Int(6) Closing Date Procedure Number
  ClsDtCode nVarChar(30) Closing Date Procedure Code
  BsLineDate VarChar(1) Base Row Date default=S [P=Posting Date, S=System Date]
  DueMonth VarChar(1) Start From default=N [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Extra Month
  ExtraDay Int(6) Extra Day
