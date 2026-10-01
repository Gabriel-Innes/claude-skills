<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTOF - Tax Offices
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TOFCode
Fields (name type(len) description [values] ->parent table):
  TOFCode Int(11) Tax Office Code
  TOFName nVarChar(100) Tax Office Name
