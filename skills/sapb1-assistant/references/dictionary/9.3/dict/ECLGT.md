<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ECLGT - ECLGT
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CfgCol, TableId, TableName, Id
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(100) transaction id
  TableName nVarChar(50) db table name
  TableId nVarChar(100) id field within db table
  CfgCol nVarChar(50) column within db table
  OldValue nVarChar(254)
  NewValue nVarChar(254)
