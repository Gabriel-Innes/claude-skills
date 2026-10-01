<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRRO - XLR Relations
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RoleId
  second U: Name, DatabaseId, AppId
Fields (name type(len) description [values] ->parent table):
  RoleId nVarChar(16) RoleId
  AppId nVarChar(225) AppId
  DatabaseId nVarChar(225) DatabaseId
  Name nVarChar(50) Name
  Descriptio nVarChar(254) Description
