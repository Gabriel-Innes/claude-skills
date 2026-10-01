<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XSCMP - XApp Company Assignment
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: COMPANY, XID
Fields (name type(len) description [values] ->parent table):
  XID nVarChar(64) XID
  COMPANY nVarChar(128) COMPANY
  ACTIVATE Int(6) ACTIVATE
