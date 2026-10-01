<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PACT - Pervasive's Insight to Action
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(250) Insight to Action Name
  Type nVarChar(50) Insight to Action Type
  TgtObjId nVarChar(250) Target Object Number
  SrcObjId nVarChar(250) Source Object Number
  SrcType nVarChar(50) Source Object Type
