<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CHO2 - Checks for Payment - Print Status
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Index
  ChkNum Int(11) Check Number
  Status VarChar(1) Status default=N [D=Details, V=Void, N=Not Confirmed, T=Not Printed, O=Overflow]
  PrnBy Int(6) Printed By
  LineNum Int(11) Row Number
  LogInstanc Int(11) Log Instance default=0
