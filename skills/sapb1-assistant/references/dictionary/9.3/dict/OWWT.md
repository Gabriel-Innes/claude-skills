<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWWT - Workbench
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ID
  CATEGORY U: Category
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Workbench Template ID
  Category nVarChar(40) Workbench Category
  Layout Text(16) Workbench Layout
  Action Text(16) Workbench Actions
