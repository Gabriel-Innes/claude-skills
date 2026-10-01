<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XRUDF - XLR company UDF
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UDFID
Fields (name type(len) description [values] ->parent table):
  UDFID Int(11) UDFID
  ColumnId nVarChar(254) ColumnId
  Module nVarChar(254) Module
  AttributeT Int(11) AttributeType
  Descriptio nVarChar(254) Description
  MetaName nVarChar(254) MetaName
