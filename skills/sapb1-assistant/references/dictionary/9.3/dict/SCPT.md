<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SCPT - SCPT
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: guid
  NAME U: scriptName
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  scriptName nVarChar(50) Script Name
  script Text(16) Script Details
