<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DAB1 - Dashboard Queries
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: QryName, QryCtgry, DsbEntry
Fields (name type(len) description [values] ->parent table):
  DsbEntry Int(11) Dashboard Entry ->ODAB
  QryCtgry Int(11) Query Category ->OQCN
  QryName nVarChar(100) Query Name
