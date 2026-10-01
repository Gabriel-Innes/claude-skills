<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ONFT - Nota Fiscal Tax Category (Brazil)
Module: Administration | 4 columns | ObjType: 264
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(20) Tax Category
  Locked VarChar(1) Locked default=N [N=, Y=]
  GPCId Int(11) Government Payment Code default=-1 ->OGPC
