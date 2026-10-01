<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WST1 - Confirmation Level - Rows
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UserID, WstCode
Fields (name type(len) description [values] ->parent table):
  WstCode Int(11) Code ->OWST
  UserID Int(11) User Code default=-1 ->OUSR
