<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DPO10 - A/P Down Payment - Row Structure
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineSeq
  SECONDARY U: DocEntry, AftLineNum, OrderNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODPO
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=204 ->ADP1
