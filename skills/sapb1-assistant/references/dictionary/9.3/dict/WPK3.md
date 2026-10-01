<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WPK3 - Dashboard Legend Color
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DsbrdEntry Int(11) Dashboard Entry
  FldName nVarChar(250) Field Name
  FldMethod nVarChar(250) Field Method
  DbType nVarChar(250) Database Type
  SqlType Int(11) SQL Type
