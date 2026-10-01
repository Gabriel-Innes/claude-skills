<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AFA2 - Asset Document - Area Journal Transactions
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->AFAD
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  JrnlMemo nVarChar(254) Journal Remarks
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
  TransNum Int(11) Transaction Number ->OJDT
  JrnlMemo1 nVarChar(254) Cancellation Journal Remarks
  TransNum1 Int(11) Cancellation Transaction No. ->OJDT
