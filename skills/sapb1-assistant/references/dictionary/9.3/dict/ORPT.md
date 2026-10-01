<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORPT - Response Type
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RspType
Fields (name type(len) description [values] ->parent table):
  Dscrptn nVarChar(100) Response Description
  RspType nVarChar(20) Response Type
  IsActived VarChar(1) Active default=Y [Y=Yes, N=No]
