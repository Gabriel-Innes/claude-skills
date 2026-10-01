<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UKD1 - User Sub-Keys Description
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SubKeyId, KeyId, TableName
  ALIAS: ColAlias, TableName
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(20) Table Name
  KeyId Int(6) Key Index
  SubKeyId Int(6) Sub-Key Index
  ColAlias nVarChar(18) Column Alias
