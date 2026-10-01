<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUPT - User Autorization Tree
Module: Administration | 9 columns | ObjType: 214
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
