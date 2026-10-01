<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DMW1 - Query List
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: QueryCode, PacCode
Fields (name type(len) description [values] ->parent table):
  PacCode Int(11) Package Code ->ODMW
  QueryCode Int(11) Query Code ->OUQR
  UserSign Int(6) User Signature ->OUSR
