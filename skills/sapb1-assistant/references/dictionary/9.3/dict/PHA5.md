<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PHA5 - Project Management - Stages - Resources
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  LogInstanc Int(11) Log Instance default=0
