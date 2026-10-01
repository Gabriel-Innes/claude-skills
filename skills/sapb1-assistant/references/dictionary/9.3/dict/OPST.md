<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPST - Service Call Problem Subtype
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ProSubTyId
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  ProSubTyId Int(6) Problem Subtype ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
