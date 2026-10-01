<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# POR10 - Purchase Order - Row structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineSeq, DocEntry
  SECONDARY U: OrderNum, AftLineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OPOR
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=22 ->ADP1
