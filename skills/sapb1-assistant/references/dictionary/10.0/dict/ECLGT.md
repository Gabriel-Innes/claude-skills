<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ECLGT - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id, TableName, TableId, CfgCol
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(100) transaction id
  TableName nVarChar(50) db table name
  TableId nVarChar(100) id field within db table
  CfgCol nVarChar(50) column within db table
  OldValue nVarChar(254)
  NewValue nVarChar(254)
