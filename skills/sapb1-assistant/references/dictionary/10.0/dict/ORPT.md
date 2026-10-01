<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ORPT - Response Type
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RspType
Fields (name type(len) description [values] ->parent table):
  Dscrptn nVarChar(100) Response Description
  RspType nVarChar(20) Response Type
  IsActived VarChar(1) Active default=Y [Y=Yes, N=No]
