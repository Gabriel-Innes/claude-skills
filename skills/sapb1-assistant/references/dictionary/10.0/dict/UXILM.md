<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UXILM - IVI Irrelevant Message IDs
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID
  MinMsgID Int(11) MINMessage ID
  MaxMsgID Int(11) MaxMessage ID
  DocEntry Int(11) Doc Number
  DocLineNum Int(11) Doc Row Number
  TransType Int(11) Transaction Type default=-1
