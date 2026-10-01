<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# APM5 - Project Management - Stages - Resources - History
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMG1
  LogInstanc Int(11) Log Instance default=0
