<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFML - Tax Formula Master Table
Module: Administration | 10 columns | ObjType: 276
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  CODE U: Code, FmlType
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
