<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CPA1 - Periods Category - WIP Mapping
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OACP
  LineNum Int(11) Line Number
  LogInstanc Int(11) Log Instance
  AcctFrom nVarChar(15) Consolidate from Account ->OACT
  AcctTo nVarChar(15) Consolidate to Account ->OACT
