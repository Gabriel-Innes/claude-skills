<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DLN16 - Delivery - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnBIndex, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->ODLN
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=15
  LogInstanc Int(11) Log Instance
