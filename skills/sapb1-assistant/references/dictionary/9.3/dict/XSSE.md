<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XSSE - XS Session
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: XKEY, SID
Fields (name type(len) description [values] ->parent table):
  SID nVarChar(32) SID
  XKEY nVarChar(50) XKEY
  VALUE Text(16) VALUE
  UPDATETIME Date(8) UPDATETIME
