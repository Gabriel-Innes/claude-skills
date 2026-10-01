<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# PACT - Pervasive's Insight to Action
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(250) Insight to Action Name
  Type nVarChar(50) Insight to Action Type
  TgtObjId nVarChar(250) Target Object Number
  SrcObjId nVarChar(250) Source Object Number
  SrcType nVarChar(50) Source Object Type
