<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SDRC - Drag&Relate - Categories
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) ObjectId
  DescStr nVarChar(30) Description
  VisOrder Int(6) Visual order
  PartOf VarChar(1) PartOf default=D [D=Docs, R=Reports, T=Tools]
