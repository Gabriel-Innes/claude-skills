<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEDT - EWB Document Type
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  DOC_TYPE U: TypeCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TypeCode nVarChar(3) EWB Document Type Code
  TypeName nVarChar(50) EWB Document Type Description
