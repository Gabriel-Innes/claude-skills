<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SINP - [SINP]
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SupplCode
Fields (name type(len) description [values] ->parent table):
  SupplCode nVarChar(128) Supplier code
  SubDate Date(8) Submission date
  SubTime Int(6) Submission time
  LogNum Int(11) ??' ?????
