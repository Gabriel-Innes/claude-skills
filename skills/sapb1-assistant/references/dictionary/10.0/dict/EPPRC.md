<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EPPRC - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrcId
Fields (name type(len) description [values] ->parent table):
  PrcId nVarChar(60) Plugin processor id
  AsmName nVarChar(100) FK to EPASM table
  PrcType nVarChar(160) the type name of the processor
  OutSerName nVarChar(160) default service
  OutOprName nVarChar(60) default service operation
