<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DAB1 - Dashboard Queries
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DsbEntry, QryCtgry, QryName
Fields (name type(len) description [values] ->parent table):
  DsbEntry Int(11) Dashboard Entry ->ODAB
  QryCtgry Int(11) Query Category ->OQCN
  QryName nVarChar(100) Query Name
