<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EPOPR - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrvId, OprName
Fields (name type(len) description [values] ->parent table):
  SrvId Int(11) FK to EPSRV table
  OprName nVarChar(60) name of service operation
  SyncMode nVarChar(20) synch or a-sync mode of opr
  PrmMsgType nVarChar(60) operation parameter type
  PrcId nVarChar(60) FK to EPPRC table
  RetMsgType nVarChar(60) operation returned type
  ParamName nVarChar(60) Parameter name
