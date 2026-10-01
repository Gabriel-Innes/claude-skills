<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRDF - XLR Definition
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DimFilterI
  second U: DimId, RoleId
Fields (name type(len) description [values] ->parent table):
  DimFilterI Identity(11) DimFilterId
  RoleId nVarChar(16) RoleId
  DimId nVarChar(20) DimId
  ModuleId nVarChar(20) ModuleId
  AccessType Int(11) AccessType default=0
  ReadInclud Text(16) ReadIncludeExpr
