<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFLR - Object Filter
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Key
  FilterName nVarChar(64) Filter Name
  UserSign Int(6) User Signature ->OUSR
  TableName nVarChar(5) Table Name
  VisOrder Int(6) Visible Order
  StatCol nVarChar(10) Statistics Column
  UnitCol nVarChar(10) Unit Column
