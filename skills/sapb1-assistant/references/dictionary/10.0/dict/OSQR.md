<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSQR - Standard Queries
Module: Reports | 7 columns
Indexes (name: columns; first = primary key; U = unique):
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
