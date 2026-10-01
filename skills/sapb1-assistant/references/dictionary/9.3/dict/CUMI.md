<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CUMI - My Menu Items
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id_, UserSign
  DETAIL: SortNum, FatherId, Levels, Name_, UserSign
Fields (name type(len) description [values] ->parent table):
  Id_ Int(11) Folder Key default=0
  Name_ nVarChar(100) Menu Item Name
  UserSign Int(6) User Signature ->OUSR
  FatherId Int(11) Parent Key default=-1
  SortNum Int(11) Sort Number
  Type_ VarChar(1) Menu Item Type default=- [F=Form, Q=Query, R=Report, L=Link, -=Folder]
  ObjType nVarChar(20) Object Type ->ADP1
  Key_ nVarChar(50) Internal ID
  FormMenuId Int(11) Form Menu ID
  FormNum Int(11) Form No.
  RepPath Text(16) Report Path
  Levels Int(6) Item Level default=1
