<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# KPI1 - Key Performance Indicator Field
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  KPIEntry Int(11) KPI Number
  Type Int(11) KPI Field Type
  FieldName nVarChar(250) KPI Field Name
  Method nVarChar(250) Aggregation Method
  DbType nVarChar(250) Database Type
  DefValue nVarChar(250) Default Value
