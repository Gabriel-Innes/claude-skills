<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PHA3 - Project Management - Stages - Attachments
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  PATH Text(16) Document Path
  FILE nVarChar(100) File Name
  DATE Date(8) Date
  LogInstanc Int(11) Log Instance default=0
