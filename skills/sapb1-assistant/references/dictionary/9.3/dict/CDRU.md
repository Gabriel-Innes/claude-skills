<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CDRU - Drag & Relate User Settings
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PartOf, ObjectId, UserID
Fields (name type(len) description [values] ->parent table):
  UserID Int(11) User ID default=-1
  ObjectId nVarChar(4) ObjectId
  PartOf VarChar(1) PartOf default=C [C=Category, R=Report, F=Table]
  Disabled VarChar(1) Disabled default=N [Y=Yes, N=No]
