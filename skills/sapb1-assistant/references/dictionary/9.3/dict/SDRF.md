<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SDRF - Drag&Relate - Files
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) ObjectId
  DescStr nVarChar(30) Description
  FatherId nVarChar(4) FatherId
  VisLevel Int(6) Visual level [1=, 2=]
  VisOrder Int(6) Visual order
