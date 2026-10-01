<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWDQ - SEWDQ
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CompDbNam, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry
  CompDbNam nVarChar(100) Company Db Name
  QueryStr Text(16) The query processed string
  NumCol Int(11) Number of column in answer
  NumRow Int(11) Number of rows in answer
  ResStr Text(16) The format restult string
