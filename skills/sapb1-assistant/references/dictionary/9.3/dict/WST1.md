<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WST1 - Confirmation Level - Rows
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserID, WstCode
Fields (name type(len) description [values] ->parent table):
  WstCode Int(11) Code ->OWST
  UserID Int(11) User Code default=-1 ->OUSR
