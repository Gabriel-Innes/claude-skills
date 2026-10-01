<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBFI - Brazil Fuel Indexer
Module: General | 5 columns | ObjType: 540000067
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(10) Fuel Code
  FGroupCode Int(11) Fuel Group Code
  Descr nVarChar(254) Description
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) ID
