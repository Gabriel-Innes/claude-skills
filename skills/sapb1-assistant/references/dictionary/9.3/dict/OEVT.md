<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEVT - EWB Vehicle Type
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  VEHIC_TYPE U: TypeCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TypeCode VarChar(1) EWB Vehicle Type Code
  TypeName nVarChar(50) EWB Vehicle Type Description
