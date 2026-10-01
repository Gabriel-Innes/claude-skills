<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TMP8 - Incoming Payment - TDS Entries
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocNum, LineNum
  INVOICE: InvType, DocEntry, DocLine
  PAYMENT: PaidEntry, PaidLine
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineNum Int(11) Row Number
  InvType nVarChar(20) Invoice Category
  DocEntry Int(11) Invoice Internal ID
  DocLine Int(11) Invoice Row Number
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  PaidEntry Int(11) Payment Internal ID
  PaidLine Int(11) Payment Row Number
