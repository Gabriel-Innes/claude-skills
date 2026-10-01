<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# KPI3 - Key Performance Indicator Parameter or Filter
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  KPIEntry Int(11) KPI Number
  Type nVarChar(20) Type
  FldName nVarChar(250) Field Name
  FldMethod nVarChar(250) Field Method
  Operator nVarChar(250) Operator
  DbType nVarChar(250) Database Type
  SqlType Int(11) SQL Type
  FromValue nVarChar(250) From Value
  ToValue nVarChar(250) To Value
  DftValue nVarChar(250) Default Value
  ParamType nVarChar(20) Parameter Type
  UdqPh nVarChar(50) UDQ Parameter's Placeholder
  UdqOp nVarChar(20) UDQ Parameter's Operator
