<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UKD1 - User Sub-Keys Description
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, KeyId, SubKeyId
  ALIAS: TableName, ColAlias
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(20) Table Name
  KeyId Int(6) Key Index
  SubKeyId Int(6) Sub-Key Index
  ColAlias nVarChar(18) Column Alias
