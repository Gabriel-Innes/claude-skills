<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FTR2 - Transfer - Area Journal Transactions
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OFTR
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  JrnlMemo nVarChar(50) Journal Remarks
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
  TransNum Int(11) Transaction Number ->OJDT
  JrnlMemo1 nVarChar(50) Cancellation Journal Remarks
  TransNum1 Int(11) Cancellation Transaction No. ->OJDT
