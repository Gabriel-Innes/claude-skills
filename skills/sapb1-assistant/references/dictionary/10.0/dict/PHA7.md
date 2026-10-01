<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PHA7 - Project Management - Workorders
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry ->OWOR
  LogInstanc Int(11) Log Instance default=0
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  EncryptIV nVarChar(100) Encrypt IV
