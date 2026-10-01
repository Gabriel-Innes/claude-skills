<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EPPRC - EPPRC
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrcId
Fields (name type(len) description [values] ->parent table):
  PrcId nVarChar(60) Plugin processor id
  AsmName nVarChar(100) FK to EPASM table
  PrcType nVarChar(160) the type name of the processor
  OutSerName nVarChar(160) default service
  OutOprName nVarChar(60) default service operation
