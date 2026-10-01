<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DMW1 - Query List
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: QueryCode, PacCode
Fields (name type(len) description [values] ->parent table):
  PacCode Int(11) Package Code ->ODMW
  QueryCode Int(11) Query Code ->OUQR
  UserSign Int(6) User Signature ->OUSR
