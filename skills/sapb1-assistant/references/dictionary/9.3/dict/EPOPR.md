<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EPOPR - EPOPR
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OprName, SrvId
Fields (name type(len) description [values] ->parent table):
  SrvId Int(11) FK to EPSRV table
  OprName nVarChar(60) name of service operation
  SyncMode nVarChar(20) synch or a-sync mode of opr
  PrmMsgType nVarChar(60) operation parameter type
  PrcId nVarChar(60) FK to EPPRC table
  RetMsgType nVarChar(60) operation returned type
  ParamName nVarChar(60) Parameter name
