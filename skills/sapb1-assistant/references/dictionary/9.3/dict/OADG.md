<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OADG - Depreciation Groups
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  Group nVarChar(15) Depreciation Group
