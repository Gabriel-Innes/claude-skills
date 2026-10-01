<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SPAR - SPAR
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Name, Owner
Fields (name type(len) description [values] ->parent table):
  Owner nVarChar(40) Owner
  Name nVarChar(254) Name
  Value Text(16) Value
