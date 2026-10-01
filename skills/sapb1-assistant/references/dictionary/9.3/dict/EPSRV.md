<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EPSRV - EPSRV
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
  IX_SERVICE U: Namespace, SrvName
  IX_ADDRESS U: SrvAddress
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) auto generated id
  PkgName nVarChar(50) FK to EPPKG table
  SrvName nVarChar(60) thee name of the service
  Namespace nVarChar(100) namespace of service in code
  SrvAddress nVarChar(254) the prefix url of the service
  InOut nVarChar(10) Service direction
