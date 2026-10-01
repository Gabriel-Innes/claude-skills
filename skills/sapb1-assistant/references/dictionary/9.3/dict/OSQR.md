<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSQR - Standard Queries
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: IntrnalKey
  QNAME_K U: QName
Fields (name type(len) description [values] ->parent table):
  IntrnalKey Int(11) Internal Key
  QCategory Int(11) Query Group
  QName nVarChar(100) Query Name
  QString Text(16) Query
  QType VarChar(1) Query Type default=R [R=Regular, W=Wizard, G=Report Generator]
  ColumnSize nVarChar(100) Column Size
  DBType Int(11) DB Type
