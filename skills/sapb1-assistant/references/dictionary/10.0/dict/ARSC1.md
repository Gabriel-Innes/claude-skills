<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ARSC1 - Resources - Warehouses - Log
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, WhsCode, LogInstanc
  WHS: WhsCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Locked VarChar(1) Locked default=N [N=No, Y=Yes]
  ObjType nVarChar(20) Object default=290
  LogInstanc Int(11) Log Instance default=0
