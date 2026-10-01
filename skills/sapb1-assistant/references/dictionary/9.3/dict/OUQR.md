<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUQR - Queries
Module: Reports | 10 columns | ObjType: 160
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: QCategory, IntrnalKey
  QNAME_K U: QCategory, QName
Fields (name type(len) description [values] ->parent table):
  IntrnalKey Int(11) Internal Key
  QCategory Int(11) Query Category ->OQCN
  QName nVarChar(100) Query Description
  QString Text(16) Query
  QType VarChar(1) Query Type default=W [R=Regular, W=Wizard, G=Report Generator, S=Stored Procedure]
  ColumnSize nVarChar(100) Column Size
  DBType Int(11) DB Type
  QLastDate Date(8) Last Upload Date
  QLastTime Int(6) Last Upload Time
  Xslt Text(16) XSLT Transformation
