<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODGL - Deduction Group List
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupCode
Fields (name type(len) description [values] ->parent table):
  GroupCode nVarChar(2) Group Code
  GroupName nVarChar(100) Group Name
  UserSign Int(6) User Signature
