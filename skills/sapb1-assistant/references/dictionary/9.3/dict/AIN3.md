<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIN3 - Inventory Count - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]
