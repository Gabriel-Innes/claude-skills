<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VPM8 - Outgoing Payment - TDS Entries
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocNum
  INVOICE: DocLine, DocEntry, InvType
  PAYMENT: PaidLine, PaidEntry
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  LineNum Int(11) Row Number
  InvType nVarChar(20) Invoice Category default=-1 [-1=All Transactions, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 10000079=TDS Adjustment]
  DocEntry Int(11) Invoice Internal ID
  DocLine Int(11) Invoice Row Number
  ObjectType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  PaidEntry Int(11) Payment Internal ID ->OVPM
  PaidLine Int(11) Payment Row Number
