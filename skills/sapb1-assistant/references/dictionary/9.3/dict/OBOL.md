<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBOL - Business Object Link
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ColumnName, TableName
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(30) Table Name
  ColumnName nVarChar(30) Column Name
  ItemUid Int(11) Form Item UID
