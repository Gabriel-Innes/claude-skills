<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SDRF - Drag&Relate - Files
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) ObjectId
  DescStr nVarChar(30) Description
  FatherId nVarChar(4) FatherId
  VisLevel Int(6) Visual level [1=, 2=]
  VisOrder Int(6) Visual order
