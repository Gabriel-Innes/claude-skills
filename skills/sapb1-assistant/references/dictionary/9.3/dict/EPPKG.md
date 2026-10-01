<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EPPKG - EPPKG
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PkgName
Fields (name type(len) description [values] ->parent table):
  PkgName nVarChar(50) Name of the plugin package
  PartnerId nVarChar(50) Id of the plugin's partner
  PkgVersion nVarChar(30) version of package installed
