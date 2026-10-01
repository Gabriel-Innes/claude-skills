<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PHA7 - Project Management - Workorders
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry ->OWOR
  LogInstanc Int(11) Log Instance default=0
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
