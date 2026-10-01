<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ADO16 - Draft - SnB properties
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SnBIndex, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Number ->ADOC
  LineNum Int(11) Row Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) SnB Object No.
  DrfWObjAbs Int(11) SnBW Draft Object No. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
