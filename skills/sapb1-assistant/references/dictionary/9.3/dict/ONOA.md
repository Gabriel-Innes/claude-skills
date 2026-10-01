<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ONOA - Nature of Assessee
Module: Administration | 4 columns | ObjType: 10000077
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(4) Code
  Descr nVarChar(100) Description
  AsseType VarChar(1) Assessee Type default=C [C=Company, P=Others]
