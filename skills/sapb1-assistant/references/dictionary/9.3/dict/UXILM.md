<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UXILM - IVI Irrelevant Message IDs
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID
  MinMsgID Int(11) MINMessage ID
  MaxMsgID Int(11) MaxMessage ID
  DocEntry Int(11) Doc Number
  DocLineNum Int(11) Doc Row Number
  TransType Int(11) Transaction Type default=-1
