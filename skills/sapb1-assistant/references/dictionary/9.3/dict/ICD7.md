<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ICD7 - Inventory Counting Draft - Team Counter - Row SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
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
  CounterNum Int(11) Counter Number
