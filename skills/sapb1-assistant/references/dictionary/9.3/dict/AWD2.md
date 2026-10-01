<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWD2 - Value Ranges
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, SeqNum, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  EfctFrom Date(8) Effective From
  ValueFrom Num(19,6) Value From
  Rate Num(19,6) Rate
  WTCur nVarChar(3) Currency
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number
