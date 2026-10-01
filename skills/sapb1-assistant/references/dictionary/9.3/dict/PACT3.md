<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PACT3 - Pervasive's Insight to Action's Table Field
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ActItemEnt Int(11) Action Item Number
  TableName nVarChar(50) Table Name
  FieldName nVarChar(50) Field Name
  IsUDF VarChar(1) Is UDF or Not default=N [Y=Yes, N=No]
