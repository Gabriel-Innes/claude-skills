<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRO1 - Lines of Transportation Document
Module: Marketing Documents | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  DOC_LINK_U U: DocLineNum, DocEntry, DocObjType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OTRO
  LineNum Int(11) Line Number
  DocObjType Int(11) Document Object Type [13=A/R Invoice, 15=Delivery, 21=Goods Return, 67=Inventory Transfer]
  DocEntry Int(11) Internal Number
  DocLineNum Int(11) Document Line Number
  ItemCode nVarChar(50) Item No.
  TranspQty Num(19,6) Transported Quantity
  LogInstanc Int(11) Log Instance default=0
  DocOrdNum Int(11) Document Order Number
