<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CSV16 - A/R Correction Invoice Reversal - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OCSV
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=166
  LogInstanc Int(11) Log Instance
