<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFLR - Object Filter
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Key
  FilterName nVarChar(64) Filter Name
  UserSign Int(6) User Signature ->OUSR
  TableName nVarChar(5) Table Name
  VisOrder Int(6) Visible Order
  StatCol nVarChar(10) Statistics Column
  UnitCol nVarChar(10) Unit Column
