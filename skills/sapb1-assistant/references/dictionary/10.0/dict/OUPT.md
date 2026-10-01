<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OUPT - User Autorization Tree
Module: Administration | 9 columns | ObjType: 214
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId nVarChar(20) Authorization ID
  Name nVarChar(64) Name
  Options Int(6) Options default=0 [0=Full/Read/None, 1=Full/None]
  FathId nVarChar(20) Parent ID ->OUPT
  VisOrder Int(6) Display Order
  Levels Int(6) Levels default=1
  IsItem VarChar(1) IS Item default=N [Y=Yes, N=No]
  Action Int(6) Action
  UserSign Int(6) User Signature ->OUSR
