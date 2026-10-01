<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CHO2 - Checks for Payment - Print Status
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Index
  ChkNum Int(11) Check Number
  Status VarChar(1) Status default=N [D=Details, V=Void, N=Not Confirmed, T=Not Printed, O=Overflow]
  PrnBy Int(6) Printed By
  LineNum Int(11) Row Number
