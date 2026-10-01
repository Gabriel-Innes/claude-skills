<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDAB - UDAB
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  name nVarChar(50) Dashboard Name
  type VarChar(1) Dashboard Type
  scriptId nVarChar(36) Script Id
