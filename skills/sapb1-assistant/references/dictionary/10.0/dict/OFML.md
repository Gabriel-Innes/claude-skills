<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFML - Tax Formula Master Table
Module: Administration | 10 columns | ObjType: 276
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: FmlType, Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(20) Code
  Descr nVarChar(100) Description
  SttId Int(11) Tax Type ID ->OSTT
  FmlLang Text(16) Formula Language Free Text
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  FmlType VarChar(1) Formula Type default=T [T=Tax, W=WTax]
  IsOrigFml VarChar(1) Original/Edited Formula default=Y [Y=Yes, N=No]
