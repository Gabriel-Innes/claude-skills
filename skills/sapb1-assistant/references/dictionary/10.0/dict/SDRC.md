<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SDRC - Drag&Relate - Categories
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) ObjectId
  DescStr nVarChar(30) Description
  VisOrder Int(6) Visual order
  PartOf VarChar(1) PartOf default=D [D=Docs, R=Reports, T=Tools]
