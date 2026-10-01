<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CIGR - Approval Process Ignore List
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, FieldName
Fields (name type(len) description [values] ->parent table):
  Category VarChar(1) Category [D=Document, O=Inventory Opening Balance, P=Inventory Posting, C=Inventory Counting, V=Payment]
  TableName nVarChar(20) Table Name
  FieldName nVarChar(50) Field Name
