<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DAB1 - Dashboard Queries
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: QryName, QryCtgry, DsbEntry
Fields (name type(len) description [values] ->parent table):
  DsbEntry Int(11) Dashboard Entry ->ODAB
  QryCtgry Int(11) Query Category ->OQCN
  QryName nVarChar(100) Query Name
