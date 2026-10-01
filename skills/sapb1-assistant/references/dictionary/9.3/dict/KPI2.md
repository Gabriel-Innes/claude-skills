<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# KPI2 - Key Performance Indicator Scope
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  KPIEntry Int(11) KPI Number
  Type nVarChar(250) KPI Scope Type
  From Num(19,6) From Value
  To Num(19,6) To Value
  Color nVarChar(250) Color
