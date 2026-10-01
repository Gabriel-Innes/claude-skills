<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACPA1 - Periods Category - WIP Mapping - Log
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OACP
  LineNum Int(11) Line Number
  LogInstanc Int(11) Log Instance
  AcctFrom nVarChar(15) Consolidate from Account ->OACT
  AcctTo nVarChar(15) Consolidate to Account ->OACT
